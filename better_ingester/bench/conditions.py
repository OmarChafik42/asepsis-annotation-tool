"""
bench/conditions.py — the conditions of the intrinsic evaluation.

Every condition turns one PDF into a recovered heading tree, which the caller
scores against the same LaTeX ruler. They differ in exactly one respect —
where the hierarchy comes from — so a difference between two rows is
attributable to that and nothing else.

  OURS        the deployable class itself (ingest.betteringest.BetterIngest),
              not a reimplementation of it, so the benchmark scores the
              artifact that ships
  LADDER-0/1/2  the same hierarchy logic with its stages switched on one at a
              time: outline only, + marker induction, + typography. Detection
              is identical across all three by construction, which is the
              check that each row differs from the one above by one stage
  CEILING     not a competitor: the representation bound on content fidelity
  BASE-small  markitdown + a model asked to rebuild the hierarchy — the
  BASE-big    ecosystem default, at two model tiers
  REFINE      our own output handed back to a model for correction, which
              exists to settle whether a model earns a place in a
              deterministic pipeline

Conditions are grouped by COST TIER, which is what the executor schedules on:
tier 0 costs nothing and runs unattended; tier 1 needs one model call per
document, supplied offline (bench/offline.py).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from bench.offline import ReplyMissing, clean_llm_json, read_reply, write_prompt
from bench.tree import Node, build_tree
from ingest.ocr import OcrConfig, run_ocr
from ingest.order import reading_order
from ingest.text import PageText

OCR_SCALE = 2.0
REFINE_TEXT_CHARS = 6000


# ── model reply parsing (tolerant of schema drift between models) ──────────

_LIST_KEYS = ("headings", "sections", "outline", "structure", "toc", "items",
              "subsections", "children")
_TITLE_KEYS = ("title", "name", "heading", "section", "text")


def _collect(items, level: int, out: list[tuple[str, int]]) -> None:
    for it in items:
        if isinstance(it, str):
            if it.strip():
                out.append((it.strip(), level))
            continue
        if not isinstance(it, dict):
            continue
        title = next((str(it[k]).strip() for k in _TITLE_KEYS
                      if isinstance(it.get(k), str) and it[k].strip()), "")
        if title:
            out.append((title, int(it.get("level", it.get("depth", level)) or level)))
        for ck in ("children", "subsections", "sections"):
            if isinstance(it.get(ck), list):
                _collect(it[ck], level + (1 if title else 0), out)


def parse_headings(raw: str) -> tuple[list[str], list[int]]:
    """Headings and levels from a model reply.

    Deliberately permissive: different models return {"headings"}, a bare
    list, nested children, or the title under any of several keys. Being
    strict here would score the baseline's JSON formatting rather than its
    structure recovery, which is not the comparison we are making.
    """
    try:
        data = json.loads(raw)
    except Exception:
        return [], []
    items = None
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        for k in _LIST_KEYS:
            if isinstance(data.get(k), list):
                items = data[k]
                break
        if items is None:
            items = next((v for v in data.values() if isinstance(v, list)), None)
    if not items:
        return [], []
    out: list[tuple[str, int]] = []
    _collect(items, 1, out)
    return [t for t, _ in out], [max(1, lv) for _, lv in out]


# ── prompts ────────────────────────────────────────────────────────────────

_JSON_CONTRACT = (
    'Output ONLY a JSON object of the form\n'
    '  {"headings": [{"title": "...", "level": 1}, ...]}\n'
    "in reading order, with no commentary before or after it.\n")


def baseline_prompt(md: str) -> str:
    """The ecosystem default: flat markdown in, heading hierarchy out.

    This is the task markitdown-based stacks hand to a model, so the prompt
    asks for exactly that and nothing more. It does not describe the document
    genre, does not name the metric, and does not hint at how many headings to
    expect — any of which would make the baseline easier than the one a real
    deployment runs.
    """
    return (
        "Below is a document converted to flat markdown. Its heading "
        "hierarchy was lost in conversion.\n\n"
        "TASK: recover the section headings and their nesting depth. Use only "
        "headings that literally appear in the text — do not invent, and do "
        "not include running heads or figure captions. Drop any leading "
        "numbering from the title itself. Level 1 is a top-level section.\n\n"
        + _JSON_CONTRACT +
        "\n---- DOCUMENT ----\n" + md + "\n---- END DOCUMENT ----\n")


def refine_prompt(draft: list[tuple[str, int]], clean: str) -> str:
    """Our own output, handed back for correction.

    The condition asks one question: on input this clean, does a correction
    pass add more than it removes? So the draft is presented as a tool's
    output without vouching for it, and the model is told it may add, delete
    or relevel — a prompt that only invited deletions would decide the answer
    in advance.
    """
    listing = "\n".join(f"L{lv}  {t}" for t, lv in draft)
    return (
        "An automatic tool extracted the heading hierarchy below from a "
        "document (level, then title). It may contain mistakes of three "
        "kinds: entries that are not real section headings (running heads, "
        "figure or table captions, front matter such as Abstract or "
        "Keywords), entries at the wrong nesting level, and real section "
        "headings it missed entirely.\n\n"
        "TASK: return the corrected hierarchy. Fix all three kinds of "
        "mistake and leave correct entries unchanged.\n\n"
        + _JSON_CONTRACT +
        f"\n---- TOOL OUTPUT ----\n{listing}\n"
        f"\n---- DOCUMENT TEXT ----\n{clean[:REFINE_TEXT_CHARS]}\n"
        "---- END ----\n")


def flatten(root: Node) -> list[tuple[str, int]]:
    """(title, depth) for every node under the root, in pre-order."""
    out: list[tuple[str, int]] = []

    def walk(n: Node, d: int) -> None:
        for c in n.children:
            out.append((c.title, d))
            walk(c, d + 1)
    walk(root, 1)
    return out


def markitdown_text(pdf_path: Path) -> str:
    """PDF -> flat markdown via markitdown: text-layer extraction with no
    structure recovery at all. This is the input the ecosystem default hands
    to a model, and reproducing it exactly is what makes BASE a fair stand-in
    for that stack rather than a strawman."""
    from markitdown import MarkItDown  # type: ignore[import-untyped]
    return MarkItDown(enable_plugins=False).convert(str(pdf_path)).text_content


def clean_text(blocks, pdf: Path) -> str:
    """Body text in reading order, from the PDF text layer."""
    pages = PageText(pdf, OCR_SCALE)
    return " ".join(pages.of(b) for b in reading_order(blocks)
                    if b.label == "text")


# ── the document context, built once and shared by every condition ─────────

@dataclass
class DocCtx:
    name: str
    pdf: Path
    tex: Path
    truth: Node          # ground-truth heading tree (root = ground-truth title)
    gt: object           # DocGT: tree, assets, reach_keys()
    blocks: list
    _pdf_text: str | None = None
    _markdown: str | None = None

    @property
    def title(self) -> str:
        return self.truth.title

    def pdf_text(self) -> str:
        if self._pdf_text is None:
            self._pdf_text = PageText(self.pdf).whole_document()
        return self._pdf_text

    def markitdown(self) -> str:
        if self._markdown is None:
            self._markdown = markitdown_text(self.pdf)
        return self._markdown


def load_ctx(name: str, tex: Path, pdf: Path) -> DocCtx:
    from bench.latex import parse_doc, parse_latex
    return DocCtx(name=name, pdf=pdf, tex=tex,
                  truth=parse_latex(tex), gt=parse_doc(tex),
                  blocks=run_ocr(pdf, OcrConfig(ocr_scale=OCR_SCALE)))


# ── conditions ─────────────────────────────────────────────────────────────

def run_ours(ctx: DocCtx, out_dir: Path) -> dict:
    """The deployable pipeline, scored as itself."""
    from ingest.betteringest import BetterIngest, heading_skeleton
    doc = BetterIngest(out_dir=out_dir).ingest(ctx.pdf)
    return {"skeleton": heading_skeleton(doc.tree, ctx.title),
            "content_tree": doc.tree, "markdown": doc.markdown,
            "assets": doc.assets, "diag": doc.ladder_diag}


def run_ladder(ctx: DocCtx, max_rung: int | None) -> dict:
    """The ladder capped at one rung — an ablation row."""
    from ingest.ladder import build_ladder_tree
    tree, diag = build_ladder_tree(ctx.blocks, ctx.title, pdf_path=ctx.pdf,
                                   ocr_scale=OCR_SCALE, max_rung=max_rung)
    return {"skeleton": tree,
            "diag": {k: diag.get(k) for k in ("rung", "outline", "gate_share")}}


def run_ceiling(ctx: DocCtx, ours_skeleton: Node) -> dict:
    """Two bounds, neither of them a competitor: how good could any PDF-based
    method get on this document?

    CONTENT — how much ground-truth content is even PRESENT in the rendered
    text layer.

    Ground-truth text is LaTeX-cleaned — math, macros and environments
    stripped — while any PDF-side pipeline reads the rendered layer, so a
    fraction of ground-truth content words has no rendered counterpart and no
    pipeline can recover it. This measures that fraction directly, per
    ground-truth leaf, against the WHOLE text layer with no partition and no
    pipeline involved:

        floor_recall = mean over leaves of |gt_words & pdf_words| / |gt_words|

    Being partition-free is what makes it a bound rather than a competitor:
    it caps the recall component of content fidelity for any system reading
    this PDF, so 0.870 can be read as 93% of what is achievable instead of
    87% of a target nobody can reach.

    Two earlier designs were discarded as ill-posed. Both anchored our own
    extracted text under the ground-truth tree, which varies the text-assembly
    path as well as the structure, and so scored a cruder extractor rather
    than the representation limit — each produced a "ceiling" that sat BELOW
    the pipeline it was meant to bound.

    STRUCTURE — the nesting a perfect hierarchy stage would have reached from
    the headings this pipeline detected. Whatever it leaves below 1.0 is lost
    to detection; the gap between it and OURS is what the hierarchy logic
    costs. See bench.metrics.structure_ceiling for why it is a real bound.
    """
    from bench.metrics import content_words, structure_ceiling

    pdf_words = content_words(ctx.pdf_text())
    recalls = []
    for n in ctx.gt.tree.all_nodes():
        if n.kind != "content":
            continue
        gw = content_words(n.content)
        if gw:
            recalls.append(len(gw & pdf_words) / len(gw))

    from bench.score import structure_row
    row = structure_row(ctx.truth, structure_ceiling(ctx.truth, ours_skeleton))
    # Levelling is deliberately NOT reported for this condition. Contraction
    # maximises EDGE overlap, not depth: when an internal heading is missed,
    # its children rise to the nearest surviving ancestor and so sit
    # shallower than ground truth, whereas the real ladder can still level
    # such a heading correctly from its printed numbering. Measured on the
    # corpus, the contracted tree's depth accuracy falls BELOW OURS on 9 of
    # 60 documents — so it is not a bound, and publishing it in a column
    # headed "ceiling" would invite exactly the wrong reading. Detection and
    # nesting are bounds and hold on all 60.
    for k in ("depth_acc", "depth_matched", "depth_correct", "depth_n_truth"):
        row.pop(k, None)
    row.update({
        "floor_recall": round(sum(recalls) / len(recalls), 4) if recalls else None,
        "floor_n_leaves": len(recalls)})
    return row


def build_baseline_prompt(ctx: DocCtx) -> str:
    return baseline_prompt(ctx.markitdown())


def build_refine_prompt(ctx: DocCtx, ours_skeleton: Node) -> str:
    return refine_prompt(flatten(ours_skeleton), clean_text(ctx.blocks, ctx.pdf))


def run_offline(ctx: DocCtx, cond: str) -> dict:
    """Score a saved model reply for `cond` on this document.

    Raises ReplyMissing when nobody has run it yet, which parks the unit and
    leaves every cheaper tier complete and reportable.
    """
    raw = read_reply(cond, ctx.name)
    if raw is None:
        raise ReplyMissing(
            f"no reply saved at out1a/llm/{cond}/{ctx.name}.reply.txt")
    heads, levels = parse_headings(clean_llm_json(raw))
    if not heads:
        raise ValueError(f"reply for {cond}/{ctx.name} contained no headings")
    return {"skeleton": build_tree(ctx.title, heads, levels),
            "n_headings": len(heads)}


# ── the registry ───────────────────────────────────────────────────────────
#
# One table describing every condition, so adding or retiring one is a single
# edit and the executor never matches on a string prefix.

@dataclass(frozen=True)
class Condition:
    name: str
    tier: int             # 0 = free, 1 = one model call per document
    label: str            # how it appears in the report
    macro: str            # LaTeX macro fragment for numbers.tex
    note: str             # one line, printed by `plan`


REGISTRY: dict[str, Condition] = {c.name: c for c in [
    Condition("ours", 0, "OURS", "Ours",
              "the shipped pipeline, scored as itself"),
    Condition("ceiling", 0, "CEILING", "Ceiling",
              "representation bound on content fidelity — not a competitor"),
    Condition("ladder0", 0, "LADDER-0", "LadderZero",
              "hierarchy from the embedded outline alone"),
    Condition("ladder1", 0, "LADDER-1", "LadderOne",
              "+ marker-schema induction"),
    Condition("ladder2", 0, "LADDER-2", "LadderTwo",
              "+ typography calibration"),
    Condition("base_small", 1, "BASE-small", "BaseSmall",
              "markitdown + a small model rebuilding the hierarchy"),
    Condition("base_big", 1, "BASE-big", "BaseBig",
              "markitdown + a larger model rebuilding the hierarchy"),
    Condition("refine", 1, "REFINE", "Refine",
              "our output handed back to a model for correction"),
]}

ALL_CONDS = list(REGISTRY)
TIER0 = [c for c, v in REGISTRY.items() if v.tier == 0]
TIER1 = [c for c, v in REGISTRY.items() if v.tier == 1]

# The paired comparisons the paper reports, as (a, b, direction).
COMPARISONS = [("ours", "ladder0", "greater"),
               ("ours", "base_small", "greater"),
               ("ours", "base_big", "greater"),
               ("ours", "refine", "greater")]
