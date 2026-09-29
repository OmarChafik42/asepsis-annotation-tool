"""
ingest/betteringest.py — THE deliverable: a single ingestion class that slots
BetterIngest in front of PageIndex.

    from ingest.betteringest import BetterIngest

    bi  = BetterIngest(out_dir="out")
    doc = bi.ingest("guideline.pdf")          # deterministic: OCR → ladder → md
    doc.markdown                              #   structure-faithful markdown
    doc.assets                                #   figures/tables: crop PNG, page,
                                              #   bbox, caption, citing sections
    bi.describe_assets(doc, model="gemma-4-31b-it")   # optional: multimodal
                                              #   descriptions via the cached,
                                              #   rate-limited transport
    tree = doc.to_pageindex()                 # PageIndex's own {title, node_id,
                                              #   nodes} JSON via the vendored
                                              #   md_to_tree, enriched with page
                                              #   anchors, per-node paragraph
                                              #   indexes, and asset attachments
    tree = doc.to_pageindex(model=..., add_summaries=True)   # + PageIndex's own
                                              #   LLM node summaries

Everything up to `describe_assets`/`add_summaries` is deterministic and
LLM-free; the two LLM steps go through bench.transport's cached transport, so
re-runs are free and reproducible.
"""
from __future__ import annotations

import base64
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from bench.tree import Node, normalise_title
from ingest.assets import recovered_reachability, save_asset_crops
from ingest.document import build_content_tree, to_markdown
from ingest.ladder import build_ladder_tree
from ingest.levels import assign_levels, font_sizes_for_headings
from ingest.ocr import Block, OcrConfig, run_ocr
from ingest.order import doc_title as detect_doc_title, heading_blocks


@dataclass
class Asset:
    asset_id: str          # "figure_1", "table_2" — stable direct reference
    type: str              # "figure" | "table"
    number: int            # rendered number ("Figure 3" → 3)
    caption: str
    page: int              # 1-based physical page (PageIndex convention)
    image: str             # saved crop PNG path
    sections: list[str] = field(default_factory=list)   # normalised citing headings
    description: str = ""  # multimodal description (describe_assets)

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}


@dataclass
class IngestedDoc:
    doc_name: str
    title: str
    pdf_path: str
    md_path: str
    markdown: str
    assets: list[Asset]
    tree: Node                    # content-at-leaves tree (ladder hierarchy)
    blocks: list[Block]
    ladder_diag: dict
    ocr_scale: float

    def to_pageindex(self, *, model: str | None = None,
                     add_summaries: bool = False) -> dict:
        """PageIndex's own JSON tree (vendored md_to_tree — deliverable 3),
        enriched with:
          · physical_index page anchors (from our layout blocks),
          · per-node `paragraphs` [{paragraph_index, local_index, page, text}]
            so body passages are directly addressable under their heading,
          · per-node `assets` (the Asset records whose captions this section
            cites) + top-level `assets`/`unplaced_assets`.
        Deterministic unless add_summaries (PageIndex's own summary prompts,
        through the cached transport)."""
        from ingest.order import reading_order
        from ingest.pageindex_vendor import (
            attach_page_anchors, heading_pages_from_blocks,
            md_to_pageindex_structure)

        res = md_to_pageindex_structure(
            self.md_path, model=model, add_summaries=add_summaries,
            add_node_text="yes")
        structure = res["structure"]
        attach_page_anchors(structure,
                            heading_pages_from_blocks(reading_order(self.blocks)))
        self._attach_paragraphs(structure)
        placed = self._attach_assets(structure)
        res["assets"] = [a.to_dict() for a in self.assets]
        res["unplaced_assets"] = [a.asset_id for a in self.assets
                                  if a.asset_id not in placed]
        return res

    # ── enrichment ────────────────────────────────────────────────────────────

    def _attach_paragraphs(self, structure: list[dict]) -> None:
        skip_re = re.compile(r"^!\[|^#")           # image links / headings
        counter = [0]
        # page lookup: markdown text has no pages; approximate from the node's
        # own anchor (start page) — exact per-paragraph pages would need the
        # block partition, which the tree also carries via physical_index.
        def walk(nodes: list[dict]) -> None:
            for d in nodes:
                text = d.get("text") or ""
                paras = []
                for j, chunk in enumerate(p for p in
                                          (s.strip() for s in text.split("\n\n"))
                                          if p and not skip_re.match(p)):
                    paras.append({"paragraph_index": counter[0],
                                  "local_index": j,
                                  "page": d.get("physical_index"),
                                  "text": chunk})
                    counter[0] += 1
                if paras:
                    d["paragraphs"] = paras
                walk(d.get("nodes") or [])
        walk(structure)

    def _attach_assets(self, structure: list[dict]) -> set[str]:
        by_section: dict[str, list[Asset]] = {}
        for a in self.assets:
            for h in a.sections:
                by_section.setdefault(h, []).append(a)
        placed: set[str] = set()

        def walk(nodes: list[dict]) -> None:
            for d in nodes:
                key = normalise_title(str(d.get("title", "")))
                if key in by_section:
                    d["assets"] = [a.to_dict() for a in by_section[key]]
                    placed.update(a.asset_id for a in by_section[key])
                walk(d.get("nodes") or [])
        walk(structure)
        return placed


def _asset_links(assets: list[Asset], out: Path) -> dict[str, list[str]]:
    """Markdown image links keyed by the normalised heading that cites them.
    Assets no section cites go under the "\x00unplaced" key, which
    `to_markdown` renders as a trailing Figures and Tables section rather
    than dropping them."""
    at: dict[str, list[str]] = {}
    for a in assets:
        link = f"![{a.type} {a.number}]({Path(a.image).relative_to(out)})"
        for h in a.sections:
            at.setdefault(h, []).append(link)
        if not a.sections:
            at.setdefault("\x00unplaced", []).append(link)
    return at


def heading_skeleton(tree: Node, root_title: str = "") -> Node:
    """Heading-only view of a content tree for structure scoring, mirroring
    to_markdown's convention: a content leaf counts as a heading iff its title
    differs from its parent's (artificial partition leaves don't).  The bench
    convention roots every column at the GT title, so `root_title` overrides
    the recovered one when scoring."""
    def conv(src: Node) -> Node:
        out = Node(title=src.title)
        for c in src.children:
            if (c.kind == "content"
                    and normalise_title(c.title) == normalise_title(src.title)):
                continue
            out.children.append(conv(c))
        return out
    s = conv(tree)
    if root_title:
        s.title = root_title
    return s


def _ladder_levels(diag: dict,
                   head_titles: list[str]) -> list[int | None] | None:
    """Map the ladder's final leveling onto the detected headings, one entry
    per heading in reading order.  Unmapped headings get None (caller fills
    them from the legacy assigner); a fully unusable diag returns None.

    Rungs 1-5: diag['headings'] IS the detected-heading list (positional).
    Rung 0: diag['headings'] holds validated OUTLINE entries, which may omit
    some detected headings (references/acknowledgements are common) — match
    by normalised title in order (queue-consuming, so duplicate titles
    resolve by position), None where the outline is silent."""
    heads = diag.get("headings") or []
    if not heads or not head_titles:
        return None
    if diag.get("rung") not in (0,) and len(heads) == len(head_titles):
        return [h[1] for h in heads]
    queue = [(normalise_title(t), lv) for t, lv, *_ in heads]
    levels: list[int | None] = []
    for title in head_titles:
        key = normalise_title(title)
        for i, (qt, lv) in enumerate(queue):
            if qt == key:
                levels.append(lv)
                del queue[:i + 1]
                break
        else:
            levels.append(None)
    return levels if any(lv is not None for lv in levels) else None


class BetterIngest:
    """Deterministic PDF → structure-faithful markdown + managed assets,
    interfaced to PageIndex.  One instance is reusable across documents."""

    def __init__(self, out_dir: str | Path = "out", ocr_scale: float = 2.0,
                 outline_demotes: bool = False):
        self.out_dir = Path(out_dir)
        self.ocr_scale = ocr_scale
        # What happens to headings a validated outline does not name:
        # False (default) levels them via rung 0b, True drops them to
        # body text. See _levels_for.
        self.outline_demotes = outline_demotes

    def ingest(self, pdf_path: str | Path) -> IngestedDoc:
        pdf = Path(pdf_path)
        name = pdf.stem
        out = self.out_dir / name
        out.mkdir(parents=True, exist_ok=True)

        blocks = run_ocr(pdf, OcrConfig(ocr_scale=self.ocr_scale))
        title = detect_doc_title(blocks, name)

        _, diag = build_ladder_tree(blocks, title, pdf_path=pdf,
                                    ocr_scale=self.ocr_scale)
        heads = heading_blocks(blocks)
        levels = self._levels_for(diag, heads, pdf)
        tree = build_content_tree(blocks, title, pdf, self.ocr_scale,
                                  levels=levels)
        assets = self._collect_assets(blocks, pdf, out)
        markdown = to_markdown(tree, _asset_links(assets, out))
        md_path = out / f"{name}.md"
        md_path.write_text(markdown, encoding="utf-8")

        return IngestedDoc(doc_name=name, title=title, pdf_path=str(pdf),
                           md_path=str(md_path), markdown=markdown,
                           assets=assets, tree=tree, blocks=blocks,
                           ladder_diag=diag, ocr_scale=self.ocr_scale)

    # ── levelling ─────────────────────────────────────────────────────────────

    def _levels_for(self, diag: dict, heads: list[Block],
                    pdf: Path) -> list[int | None]:
        """One level per detected heading, in reading order.

        The ladder's own leveling covers every heading except when rung 0
        accepted an outline that stays silent about some of them. Those gaps
        go to rung 0b, the outline gap fill (ingest/levels.assign_levels),
        which fires on 24 of the 60 corpus documents and is worth +0.015
        detection F1 over dropping them. `outline_demotes` drops them
        instead, which is the stricter reading of the outline and measurably
        worse — see the ladder ablation in the report card.
        """
        mapped = _ladder_levels(diag, [b.text for b in heads])
        if mapped is not None and not any(lv is None for lv in mapped):
            return mapped
        if mapped is not None and self.outline_demotes and diag.get("rung") == 0:
            return mapped                      # None entries → demoted to body
        sizes = font_sizes_for_headings(heads, pdf, self.ocr_scale)
        filled = assign_levels([b.text for b in heads], sizes)
        if mapped is None:                     # ladder produced no usable levels
            return list(filled)
        return [m if m is not None else f for m, f in zip(mapped, filled)]

    # ── assets ────────────────────────────────────────────────────────────────

    def _collect_assets(self, blocks: list[Block], pdf: Path,
                        out: Path) -> list[Asset]:
        """Crops plus reachability: which sections cite which asset."""
        manifest = save_asset_crops(blocks, pdf, out / "assets", self.ocr_scale)
        cites: dict[tuple[str, int], list[str]] = {}
        for heading, atype, num in recovered_reachability(blocks, pdf,
                                                          self.ocr_scale):
            cites.setdefault((atype, num), []).append(heading)

        assets: list[Asset] = []
        seen: dict[str, int] = {}
        for m in manifest:
            aid = f"{m['type']}_{m['number']}"
            if aid in seen:                          # duplicate rendered numbers
                seen[aid] += 1
                aid = f"{aid}_{seen[aid]}"
            else:
                seen[aid] = 1
            assets.append(Asset(
                asset_id=aid, type=m["type"], number=m["number"],
                caption=m["caption"], page=int(m["page"]) + 1,
                image=m["image"],
                sections=sorted(cites.get((m["type"], m["number"]), []))))
        return assets

    # ── optional multimodal step ───────────────────────────────────────────────

    def describe_assets(self, doc: IngestedDoc, model: str,
                        chat=None, max_chars: int = 600) -> IngestedDoc:
        """Give every asset a retrieval-oriented description via a multimodal
        model (crop PNG + caption).  Goes through bench.transport.api_chat by
        default: cached by (model, messages), rate-limited, quota-aborting.
        Assets whose call fails keep description="" (retry = rerun)."""
        if chat is None:
            from bench.transport import api_chat as _api_chat

            def chat(messages):
                return _api_chat(model, messages, bucket=model)

        for a in doc.assets:
            if a.description:
                continue
            b64 = base64.b64encode(Path(a.image).read_bytes()).decode()
            messages = [{"role": "user", "content": [
                {"type": "text", "text":
                    f"This is a {a.type} from a document (caption: "
                    f"{a.caption!r}). Describe factually what it shows in 2-3 "
                    "sentences for a retrieval index: variables/axes or "
                    "columns, trends or key values, and what a reader could "
                    "look up in it. No preamble."},
                {"type": "image_url",
                 "image_url": {"url": f"data:image/png;base64,{b64}"}},
            ]}]
            r = chat(messages)
            if r is not None:
                text = re.sub(r"<thought>.*?(</thought>|$)", "", r[0],
                              flags=re.S)
                a.description = " ".join(text.split())[:max_chars]
        return doc
