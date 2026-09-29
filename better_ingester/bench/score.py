"""
bench/score.py — turn one (document, condition) into one scored row.

The eight measures the paper reports, assembled in one place so the CLI does
no scoring of its own and every condition is measured by the same ruler:

  1 detection      were the right headings found?           title_f1 / _f2
  2 levelling      of those found, how many sit at the
                   right depth?                             depth_acc
  3 nesting        parent-child pairs, identity and
                   structure together                       edge_f1 / _f2
  4 reading order  Kendall's tau over the leaf sequence     order_tau
  5 assets         figures and tables found, and typed      asset_f1 / _f2,
                                                            asset_type_acc
  6 reachability   asset attached to the section that
                   refers to it                             reach_f1 / _f2
  7 content        word overlap under each matched
                   heading, reported next to how many
                   matched at all                           content_f1 / _f2,
                                                            leaf_match
  8 coverage       what fraction of the text layer
                   survived, decomposed so a deliberate
                   exclusion cannot hide a defect           coverage + four
                                                            accounting rates

Every measure that is a set overlap carries both F1 and F2: the paper reports
F2 because a missed section can never be retrieved while a spurious one merely
competes, and that argument applies to a missed figure and an unreachable one
exactly as it does to a missed heading. Levelling and typing are accuracies,
reading order is a rank correlation and coverage is a share, so none of those
four takes a beta.

Detection and levelling are separate on purpose. Entangled, a fall in nesting
cannot be attributed between "the heading was missed" and "the heading was
found and misfiled", and those need different fixes.
"""

from __future__ import annotations

from pathlib import Path

from bench import conditions as C
from bench.metrics import (ASSET_LABELS, EXCLUDED_LABELS, content_words,
                           coverage, depth_accuracy, furniture_text,
                           labelled_text, reading_order as order_metric)
from bench.tree import Node, normalise_title, score, score_assets, score_content


def fbeta(p: float, r: float, beta: float) -> float:
    b2 = beta * beta
    return (1 + b2) * p * r / (b2 * p + r) if (b2 * p + r) else 0.0


def prf(truth: set, got: set) -> tuple[float, float]:
    tp = len(truth & got)
    return (tp / len(got) if got else (1.0 if not truth else 0.0),
            tp / len(truth) if truth else (1.0 if not got else 0.0))


def structure_row(truth: Node, recovered: Node) -> dict:
    """Detection, nesting and levelling — every condition reports these, and
    only these, so the ablation rows are directly comparable."""
    s = score(truth, recovered)
    return {**s.row(),
            "title_f2": round(fbeta(s.title_p, s.title_r, 2), 3),
            "edge_f2": round(fbeta(s.edge_p, s.edge_r, 2), 3),
            **depth_accuracy(truth, recovered).row()}


def content_recall(gt_tree: Node, rec_tree: Node) -> float | None:
    """Mean content-word RECALL over title-matched leaves.

    Reported alongside content F1 because it is the component CEILING bounds:
    the ceiling is a recall bound, so only recall can be read against it.
    """
    rec: dict[str, str] = {}
    for n in rec_tree.all_nodes():
        if n.kind == "content":
            k = normalise_title(n.title)
            rec[k] = (rec.get(k, "") + " " + n.content).strip()
    vals = []
    for n in gt_tree.all_nodes():
        if n.kind != "content":
            continue
        gw = content_words(n.content)
        if not gw:
            continue
        k = normalise_title(n.title)
        if k in rec:
            vals.append(len(gw & content_words(rec[k])) / len(gw))
    return round(sum(vals) / len(vals), 4) if vals else None


def _ours_skeleton(ctx: C.DocCtx, out_dir: Path, shared: dict) -> Node:
    """The OURS heading skeleton, computed once per document and shared by
    every condition that needs it (CEILING bounds it, REFINE corrects it)."""
    if "ours_skeleton" not in shared:
        shared["ours_skeleton"] = C.run_ours(ctx, out_dir)["skeleton"]
    return shared["ours_skeleton"]


def score_unit(cond: str, ctx: C.DocCtx, out_dir: Path,
               shared: dict) -> dict:
    """Run one condition on one document and return its scored row.

    `shared` caches work reused across conditions within a document — chiefly
    the OURS skeleton, which REFINE corrects.
    """
    if cond == "ours":
        return _score_ours(ctx, out_dir, shared)
    if cond == "ceiling":
        # needs the headings OURS actually detected. Tier-major scheduling
        # runs conditions alphabetically within a document, so `ours` may not
        # have run yet; recomputing is deterministic and costs no model call.
        return C.run_ceiling(ctx, _ours_skeleton(ctx, out_dir, shared))
    if cond.startswith("ladder"):
        rung = int(cond[-1])
        r = C.run_ladder(ctx, rung)
        return {**structure_row(ctx.truth, r["skeleton"]),
                "ladder_rung": r["diag"].get("rung")}
    if cond in C.TIER1:
        r = C.run_offline(ctx, cond)
        return {**structure_row(ctx.truth, r["skeleton"]),
                "n_headings_returned": r["n_headings"]}
    raise ValueError(f"unknown condition {cond!r}")


def _score_ours(ctx: C.DocCtx, out_dir: Path, shared: dict) -> dict:
    """OURS is the only condition scored on all eight measures: it is the only
    one that produces body text, assets and markdown as well as a tree."""
    from ingest.assets import recovered_assets, recovered_reachability

    r = C.run_ours(ctx, out_dir)
    shared["ours_skeleton"] = r["skeleton"]
    row = structure_row(ctx.truth, r["skeleton"])

    # content fidelity, and the recall component the ceiling bounds
    row.update(score_content(ctx.gt.tree, r["content_tree"]).__dict__)
    row["content_r"] = content_recall(ctx.gt.tree, r["content_tree"])

    # figures and tables: found, and typed correctly
    a = score_assets(ctx.gt.assets, recovered_assets(ctx.blocks))
    row.update({"asset_p": round(a.precision, 3), "asset_r": round(a.recall, 3),
                "asset_f1": round(a.f1, 3),
                "asset_f2": round(fbeta(a.precision, a.recall, 2), 3),
                "asset_type_acc": round(a.type_acc, 3),
                "asset_n_truth": a.n_truth})

    # reachability: is the asset attached to the section that refers to it?
    rp, rr = prf(ctx.gt.reach_keys(),
                 recovered_reachability(ctx.blocks, ctx.pdf, C.OCR_SCALE))
    row.update({"reach_p": round(rp, 3), "reach_r": round(rr, 3),
                "reach_f1": round(fbeta(rp, rr, 1), 3),
                "reach_f2": round(fbeta(rp, rr, 2), 3),
                "reach_n_truth": len(ctx.gt.reach_keys())})

    row.update(order_metric(ctx.gt.tree, r["content_tree"]).row())
    row.update(coverage(
        ctx.pdf_text(), r["markdown"],
        furniture_text=furniture_text(ctx.blocks, ctx.pdf, C.OCR_SCALE),
        excluded_text=labelled_text(ctx.blocks, ctx.pdf, EXCLUDED_LABELS,
                                    C.OCR_SCALE),
        asset_text=labelled_text(ctx.blocks, ctx.pdf, ASSET_LABELS,
                                 C.OCR_SCALE)).row())
    row["ladder_rung"] = r["diag"].get("rung")
    row["n_assets_recovered"] = len(r["assets"])
    return row
