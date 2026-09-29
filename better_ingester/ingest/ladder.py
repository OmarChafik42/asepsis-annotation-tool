"""
ingest/ladder.py — the escalation ladder that decides heading depth.

Signals are tried in order of how much they can be trusted, and the ladder
stops at the first one that earns it (§sec:ladder). Printed section numbers
survive rendering exactly; font size does not — in IEEE-style papers the
section headings are set in small caps SMALLER than the subsections beneath
them, so a naive size rule inverts the hierarchy.

  rung -1  no detected headings          -> a root-leaf document
  rung 0   embedded PDF outline          -> ingest/outline.py, per-entry gate
  rung 0b  outline gap fill              -> ingest/levels.assign_levels,
                                            applied by the caller for headings
                                            a validated outline does not name
  rung 1   marker-schema induction       -> ingest/levels.induce_levels
  rung 2   typography clusters           -> ingest/levels.calibrate_typography
  rung 3   confidence gate               -> ingest/levels.gate

There is no language model anywhere on this path, and no rung that can
fabricate depth: when the evidence conflicts the ladder returns a FLAT
document rather than inventing a hierarchy.

`build_ladder_tree` returns the tree plus a diagnostics dict — which rung
resolved the document, per-heading (title, level, confidence, signal), the
gate share, and the outline verdict. The rung firing distribution is itself
a reported result.
"""

from __future__ import annotations

from bench.tree import Node
from ingest.levels import Leveled, calibrate_typography, gate, induce_levels, \
    typography_signatures
from ingest.order import heading_blocks
from ingest.outline import outline_tree, read_outline, validate_outline


def _tree_from_leveled(leveled: list[Leveled], doc_title: str) -> Node:
    root = Node(title=doc_title)
    stack: list[tuple[int, Node]] = [(0, root)]
    for l in leveled:
        lv = l.level if l.level is not None else 1
        node = Node(title=l.title)
        while stack and stack[-1][0] >= lv:
            stack.pop()
        (stack[-1] if stack else (0, root))[1].children.append(node)
        stack.append((lv, node))
    return root


def build_ladder_tree(blocks, doc_title: str = "", pdf_path=None,
                      ocr_scale: float = 2.0,
                      max_rung: int | None = None) -> tuple[Node, dict]:
    """The ladder: (tree, diagnostics). Fully deterministic.

    `max_rung` caps which rungs may fire, which is what makes the ablation
    measurable: 0 is the embedded outline alone, 1 adds marker-schema
    induction, 2 adds typography calibration, None (the default) is the whole
    ladder. Capping never changes the rungs below it, so each ablation row
    differs from the one above by exactly one stage — the property that lets
    a gain be attributed to the stage that produced it.

    A capped rung that cannot answer falls through to the honest floor —
    flat, never fabricated depth — rather than borrowing a stage the ablation
    is meant to exclude."""
    diag: dict = {"rung": None, "outline": None, "gate_share": None,
                  "headings": []}

    head_blocks = heading_blocks(blocks)

    # rung -1 — nothing to level
    if not head_blocks:
        diag["rung"] = -1
        return Node(title=doc_title), diag

    # rung 0 — embedded outline
    if pdf_path is not None:
        entries = read_outline(pdf_path)
        v = validate_outline(entries, blocks)
        diag["outline"] = {"verdict": v.verdict, "match_rate": round(v.match_rate, 3),
                           "notes": v.notes}
        if v.verdict == "full":
            diag["rung"] = 0
            diag["headings"] = [(e.title, e.level + 1, "high", "outline")
                                for e in v.entries]
            return outline_tree(v.entries, doc_title), diag
        # titles_only: keep detection (which has bboxes); levels from below.

    if max_rung is not None and max_rung < 1:
        # outline-only ablation: the outline did not resolve, so report flat
        diag["rung"] = 0
        return _tree_from_leveled(
            [Leveled(b.text, 1, "low", "capped") for b in head_blocks],
            doc_title), diag

    # rung 1' — marker-schema induction
    headings = [b.text for b in head_blocks]
    leveled = induce_levels(headings)

    # rung 2 — typography calibration for the level=None residue
    if max_rung is not None and max_rung < 2:
        diag["rung"] = 1
        leveled = [l if l.level is not None
                   else Leveled(l.title, 1, "low", "capped") for l in leveled]
        diag["headings"] = [(l.title, l.level, l.confidence, l.signal)
                            for l in leveled]
        return _tree_from_leveled(leveled, doc_title), diag
    if pdf_path is not None and any(l.level is None for l in leveled):
        leveled = calibrate_typography(
            leveled, typography_signatures(head_blocks, pdf_path, ocr_scale))
    else:
        leveled = calibrate_typography(leveled, [None] * len(leveled))

    # rung 3 — confidence gate: report how much of the leveling is trusted
    _, share = gate(leveled)
    diag["gate_share"] = round(share, 3)
    diag["rung"] = 2 if any(l.signal == "typography" for l in leveled) else 1
    diag["headings"] = [(l.title, l.level, l.confidence, l.signal)
                        for l in leveled]
    return _tree_from_leveled(leveled, doc_title), diag
