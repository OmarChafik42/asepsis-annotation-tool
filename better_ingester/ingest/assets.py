"""
ingest/assets.py — figures and tables: detection, crops, and reachability.

An asset is not just found, it is *attached*: the paper's reachability
measure asks whether a figure is reachable from the section that refers to
it, because that is what decides whether a retriever can ever surface it.
So this module produces three things per asset — the caption, a
self-contained crop, and the set of sections whose prose cites it.
"""

from __future__ import annotations

import re
from pathlib import Path

from bench.tree import Node, normalise_title
from ingest.ocr import Block
from ingest.order import SECTION_TITLE, reading_order
from ingest.text import PageText

# A subfigure panel label ("(a) …", "(b) …") is not a top-level float caption.
_SUBCAPTION = re.compile(r"^\s*\(?[a-zA-Z]\)\s")

# "Figure 3", "Fig. 3", "Table 1", "Tab 2" — an asset mention in prose.
_REF_MENTION = re.compile(r"\b(fig(?:ure)?|tab(?:le)?)s?\.?\s*(\d+)", re.I)

# Layout labels holding an asset's *content*, as opposed to its caption.
_ASSET_CONTENT = {"image", "chart", "table"}


def _caption_type(text: str) -> str:
    """figure | table, from the rendered caption label."""
    return "table" if text.strip().lower().startswith(("table", "tab.")) else "figure"


def caption_blocks(blocks: list[Block]) -> list[Block]:
    """Float captions in reading order, panel labels excluded."""
    return [b for b in reading_order(blocks)
            if b.label == "figure_title" and b.text.strip()
            and not _SUBCAPTION.match(b.text)]


def recovered_assets(blocks: list[Block]) -> list[Node]:
    """Detected assets as scoreable nodes, typed from the rendered label."""
    return [Node(title=b.text.strip(), kind="asset",
                 asset_type=_caption_type(b.text))
            for b in caption_blocks(blocks)]


def recovered_reachability(blocks: list[Block], pdf_path,
                           ocr_scale: float = 2.0) -> set[tuple[str, str, int]]:
    """{(normalised section heading, asset_type, number)}.

    A section is linked to an asset iff its body text mentions it by rendered
    number ("Figure 3"). Section = the most recent heading in reading order.
    The recovered side can only cite assets by their rendered number, which
    is why the ground-truth side reduces its \\label/\\ref graph to the same
    key before the two are compared.
    """
    pages = PageText(pdf_path, ocr_scale)
    out: set[tuple[str, str, int]] = set()
    current = ""
    for b in reading_order(blocks):
        if b.label == SECTION_TITLE:
            current = normalise_title(b.text)
        elif b.label == "text" and current:
            for m in _REF_MENTION.finditer(pages.of(b)):
                atype = "figure" if m.group(1).lower().startswith("fig") else "table"
                out.add((current, atype, int(m.group(2))))
    return out


def save_asset_crops(blocks: list[Block], pdf_path, out_dir,
                     ocr_scale: float = 2.0) -> list[dict]:
    """Crop each detected asset to a PNG and return a manifest.

    Each caption is paired with the nearest content block (image/chart/table)
    in its own column — horizontal overlap required, smallest vertical gap
    wins, search capped at a third of a page — and the saved crop is the
    union of the two, so it is self-contained. A caption with no content
    block near it (a table rendered as text, say) saves the caption region
    alone rather than inventing a region.
    """
    import pypdfium2 as pdfium  # type: ignore[import-untyped]

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    captions = caption_blocks(blocks)
    content = [b for b in blocks if b.label in _ASSET_CONTENT]

    doc = pdfium.PdfDocument(str(pdf_path))
    rendered: dict[int, object] = {}

    def page_img(p: int):
        if p not in rendered:
            rendered[p] = doc[p].render(scale=ocr_scale).to_pil()
        return rendered[p]

    manifest: list[dict] = []
    used: set[int] = set()
    count = {"figure": 0, "table": 0}
    for cap in captions:
        atype = _caption_type(cap.text)
        cx0, cy0, cx1, cy1 = cap.bbox
        page_height = page_img(cap.page).height
        best, best_gap = None, page_height * 0.30
        for i, cb in enumerate(content):
            if i in used or cb.page != cap.page:
                continue
            bx0, by0, bx1, by1 = cb.bbox
            if min(cx1, bx1) - max(cx0, bx0) <= 0:      # same column required
                continue
            gap = max(by0 - cy1, cy0 - by1, 0.0)        # vertical gap either way
            if gap < best_gap:
                best, best_gap = i, gap

        boxes = [cap.bbox]
        if best is not None:
            used.add(best)
            boxes.append(content[best].bbox)
        x0 = min(b[0] for b in boxes); y0 = min(b[1] for b in boxes)
        x1 = max(b[2] for b in boxes); y1 = max(b[3] for b in boxes)

        count[atype] += 1
        fname = f"{atype}_{count[atype]}.png"
        page_img(cap.page).crop((int(x0), int(y0), int(x1), int(y1))).save(out_dir / fname)
        num = re.search(r"\d+", cap.text)               # rendered "Figure 3" → 3
        manifest.append({
            "type": atype, "caption": cap.text.strip(),
            "number": int(num.group()) if num else count[atype],
            "image": str(out_dir / fname), "page": cap.page,
            "has_content": best is not None,
        })
    return manifest
