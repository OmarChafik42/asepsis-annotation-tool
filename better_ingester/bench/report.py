"""
bench/report.py — turn the ledger into numbers you can paste into the paper.

Four artifacts, written together so they can never disagree:

  report_card.md   verbose human table: every condition x metric with mean,
                   sd, n, and a 95% CI, plus per-cell strata and paired tests
  summary.json     the same aggregates, machine-readable
  numbers.tex      \\newcommand definitions — \\resOursEdgeFOne etc. — so the
                   paper references a macro instead of a hand-copied literal
  tables.tex       ready-to-paste tabular environments

The point of numbers.tex is that a number never gets transcribed by hand: the
paper says \\resOursEdgeFOne, this file defines it, and a re-run updates the
paper. A transcription error is then impossible rather than merely unlikely.
"""

from __future__ import annotations

import csv
import time
from pathlib import Path

from bench.conditions import COMPARISONS, REGISTRY
from bench.stats import describe, paired_report

# metric -> (LaTeX macro fragment, human label)
METRICS = {
    "title_f1": ("TitleFOne", "detection F1"),
    "title_f2": ("TitleFTwo", "detection F2"),
    "edge_f1": ("EdgeFOne", "nesting F1"),
    "edge_f2": ("EdgeFTwo", "nesting F2"),
    "depth_acc": ("DepthAcc", "levelling accuracy"),
    "order_tau": ("OrderTau", "reading order tau"),
    "content_f1": ("ContentFOne", "content fidelity F1"),
    "content_f2": ("ContentFTwo", "content fidelity F2"),
    "content_r": ("ContentR", "content recall"),
    "leaf_match": ("LeafMatch", "leaf match rate"),
    "coverage": ("Coverage", "text-layer coverage"),
    "furniture_rate": ("FurnitureRate", "page-furniture share"),
    "excluded_rate": ("ExcludedRate", "policy-excluded share"),
    "asset_rate": ("AssetRate", "captured-as-asset share"),
    "unaccounted_rate": ("UnaccountedRate", "unaccounted share"),
    "floor_recall": ("FloorRecall", "representation ceiling"),
    "asset_f1": ("AssetFOne", "asset detection F1"),
    "asset_f2": ("AssetFTwo", "asset detection F2"),
    "asset_type_acc": ("AssetTypeAcc", "asset type accuracy"),
    "reach_f1": ("ReachFOne", "reachability F1"),
    "reach_f2": ("ReachFTwo", "reachability F2"),
}

# metrics whose corpus mean must exclude documents where the metric is
# undefined: the empty-set convention scores a figure-free document a perfect
# 1.0, which is right per document and inflates a mean taken over a corpus in
# which some papers have no figures at all.
GUARDED = {"asset_f1": "asset_n_truth", "asset_f2": "asset_n_truth",
           "asset_type_acc": "asset_n_truth",
           "reach_f1": "reach_n_truth", "reach_f2": "reach_n_truth"}

CONDITION_MACRO = {name: c.macro for name, c in REGISTRY.items()}

# What each measure means, printed above the table it governs so a reader
# never has to hold the definitions in their head.
GLOSS = {
    "title_f1": "of the headings in the source, how many did we find?",
    "depth_acc": "of the headings we found, how many sit at the right depth?",
    "edge_f1": "parent-child pairs recovered — identity and structure together",
    "order_tau": "Kendall's tau over the leaf sequence; 1.0 is exact order",
    "content_f1": "word overlap of the text under each matched heading",
    "content_f2": "the same, weighting recall higher",
    "content_r": "the recall half of the above — what CEILING bounds",
    "leaf_match": "share of ground-truth leaves that matched a recovered one",
    "coverage": "share of the text layer that reached the markdown",
    "unaccounted_rate": "text neither emitted nor accounted for — the defect",
    "excluded_rate": "dropped by policy (bibliography, front matter)",
    "asset_rate": "held in asset records rather than body text",
    "furniture_rate": "running heads, page numbers, marginalia",
    "asset_f1": "figures and tables detected",
    "asset_f2": "the same, weighting recall higher",
    "asset_type_acc": "of those, how many typed figure/table correctly",
    "reach_f1": "asset attached to the section that refers to it",
    "reach_f2": "the same, weighting recall higher",
    "floor_recall": "how much ground-truth text exists in the layer at all",
}


def _values(rows: list[dict], metric: str) -> list[float]:
    guard = GUARDED.get(metric)
    out = []
    for r in rows:
        v = r.get(metric)
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            continue
        if guard and not r.get(guard, 0):
            continue
        out.append(float(v))
    return out


def _agg(vals: list[float]) -> dict | None:
    return describe(vals)


def aggregate(rows_by_cond: dict[str, list[dict]]) -> dict:
    out: dict[str, dict] = {}
    for cond, rows in rows_by_cond.items():
        m: dict[str, dict] = {}
        for metric in METRICS:
            a = _agg(_values(rows, metric))
            if a:
                m[metric] = a
        if m:
            out[cond] = m
    return out


# ── paired comparisons ─────────────────────────────────────────────────────

STAT_METRICS = ("title_f1", "title_f2", "edge_f1", "edge_f2",
                "depth_acc", "content_f1", "content_f2")


def comparisons(rows_by_cond: dict[str, list[dict]],
                pairs: list[tuple[str, str, str]]) -> list[dict]:
    """Paired document-level differences between conditions."""
    out = []
    for a, b, mode in pairs:
        ra = {r["doc"]: r for r in rows_by_cond.get(a, [])}
        rb = {r["doc"]: r for r in rows_by_cond.get(b, [])}
        shared = sorted(set(ra) & set(rb))
        if len(shared) < 3:
            continue
        for m in STAT_METRICS:
            xs, ys = [], []
            for d in shared:
                va, vb = ra[d].get(m), rb[d].get(m)
                if isinstance(va, (int, float)) and isinstance(vb, (int, float)):
                    xs.append(float(va))
                    ys.append(float(vb))
            if len(xs) < 3:
                continue
            rep = paired_report(f"{a} vs {b}", xs, ys, "greater")
            rep.update(metric=m, a=a, b=b)
            out.append(rep)
    return out


# ── renderers ──────────────────────────────────────────────────────────────

def _fmt(a: dict | None, places: int = 3) -> str:
    return "—" if not a else f"{a['mean']:.{places}f}"


# OpenKB dispatches on document length: under 20 pages it converts with
# markitdown and reads the whole text in ONE call, which is what BASE-small
# and BASE-big reproduce; at 20 pages or more it routes the document to
# PageIndex's multi-call tree indexing instead. So BASE is a faithful
# reproduction only below the threshold, and the report says so per subset
# rather than leaving a reader to assume it holds across the corpus.
OPENKB_PAGE_THRESHOLD = 20


def page_groups(rows: list[dict], pages_of: dict[str, int]) -> dict:
    """Split rows into the subset OpenKB would answer in one call and the
    subset it would hand to PageIndex."""
    out: dict[str, list[dict]] = {"under": [], "over": []}
    for r in rows:
        n = pages_of.get(r["doc"])
        if n is None:
            continue
        out["under" if n < OPENKB_PAGE_THRESHOLD else "over"].append(r)
    return out


def openkb_fidelity(rows_by_cond: dict, pages_of: dict[str, int],
                    conditions: list[str]) -> list[str]:
    """The BASE rows split at OpenKB's own 20-page dispatch threshold."""
    base = [c for c in conditions if c.startswith("base")]
    if not any(rows_by_cond.get(c) for c in base):
        return []
    L = ["", "## BASE against OpenKB's own dispatch threshold", "",
         f"OpenKB reads a document under {OPENKB_PAGE_THRESHOLD} pages in one "
         "call after converting it with markitdown — which is exactly what "
         "BASE does — but hands a longer one to PageIndex's multi-call tree "
         "indexing instead. BASE is therefore a faithful reproduction of the "
         "ecosystem default only on the shorter subset; on the longer one it "
         "is the short-document recipe applied beyond where OpenKB would "
         "apply it, and reads as a lower bound on what that stack would "
         "actually do.", "",
         "| condition | subset | n | detection F1 | nesting F1 | levelling |",
         "|---|---|---|---|---|---|"]
    for cond in base:
        rows = rows_by_cond.get(cond) or []
        if not rows:
            continue
        groups = page_groups(rows, pages_of)
        for key, label in (("under", f"< {OPENKB_PAGE_THRESHOLD} pages "
                                     "(faithful)"),
                           ("over", f">= {OPENKB_PAGE_THRESHOLD} pages "
                                    "(extrapolated)")):
            g = groups[key]
            if not g:
                continue
            vals = [_fmt(_agg(_values(g, m)))
                    for m in ("title_f1", "edge_f1", "depth_acc")]
            name = REGISTRY[cond].label if cond in REGISTRY else cond
            L.append(f"| {name} | {label} | {len(g)} | " + " | ".join(vals) + " |")

    L += _length_paired(rows_by_cond, pages_of)
    return L


def _length_paired(rows_by_cond: dict, pages_of: dict[str, int]) -> list[str]:
    """The paired tests of the section above, run separately on each subset.

    The corpus-level test cannot stand in for these. BASE is a faithful
    reproduction of the ecosystem default only below the threshold, so a claim
    about that subset needs a test computed on that subset rather than an
    inference from the pooled one — and the two subsets point in opposite
    directions on detection, which pooling hides."""
    pairs = [p for p in COMPARISONS if p[1].startswith("base")]
    if not pairs or not pages_of:
        return []
    rows: list[str] = []
    for key, label in (("under", f"< {OPENKB_PAGE_THRESHOLD} pp"),
                       ("over", f">= {OPENKB_PAGE_THRESHOLD} pp")):
        subset = {c: page_groups(rs, pages_of)[key]
                  for c, rs in rows_by_cond.items()}
        for c in comparisons(subset, pairs):
            a_ = REGISTRY[c["a"]].label if c["a"] in REGISTRY else c["a"]
            b_ = REGISTRY[c["b"]].label if c["b"] in REGISTRY else c["b"]
            rows.append(f"| {a_} vs {b_} | {label} | {c['metric']} | "
                        f"{c['n']} | {c['mean_x']} | {c['mean_y']} | "
                        f"{c['mean_diff']:+.3f} | {c['p_wilcoxon']:.4g} |")
    if not rows:
        return []
    return ["", "### Paired tests within each subset", "",
            "Same test as the *Paired comparisons* section above — one "
            "one-sided Wilcoxon signed-rank test of the hypothesis that OURS "
            "exceeds the baseline, paired within document — computed on each "
            "subset separately.", "",
            "| comparison | subset | measure | n | mean A | mean B | "
            "difference | p |",
            "|---|---|---|---|---|---|---|---|"] + rows


def markdown(summary: dict, rows_by_cond: dict, cells: dict, comps: list[dict],
             ledger_summary: dict, corpus_n: int, conditions: list[str],
             pages_of: dict[str, int] | None = None,
             llm_status: dict | None = None) -> str:
    """The human-readable report card.

    Written to be read on its own: every table states what it measures, what
    the numbers are against, and what would count as a good or bad value.
    A number a reader has to reconstruct the meaning of is a number that gets
    quoted wrongly.
    """
    L = ["# Intrinsic evaluation — results", "",
         f"Generated {time.strftime('%Y-%m-%d %H:%M')} · corpus N = {corpus_n} "
         f"documents.", "",
         "Every condition builds a heading tree for the same document and is "
         "scored by the same ruler: the author's own LaTeX source, which "
         "states the structure exactly and needed no annotation. Conditions "
         "differ in exactly one respect — where the hierarchy comes from — so "
         "a difference between two rows is attributable to that.", ""]

    L += ["## The conditions", ""]
    for name in conditions:
        c = REGISTRY.get(name)
        if c:
            L.append(f"- **{c.label}** (`{name}`, tier {c.tier}) — {c.note}")
    L += ["", "Tier 0 costs nothing and runs unattended. Tier 1 needs one "
          "model call per document, supplied offline; see the completeness "
          "table for what has been answered.", ""]

    L += ["## Main results", "",
          "Cells are `mean ± sd (n)` over the corpus. Higher is better "
          "everywhere in this table.", ""]
    for m in ("title_f1", "depth_acc", "edge_f1", "order_tau", "content_f1",
              "coverage"):
        L.append(f"- **{m}** — {GLOSS[m]}")
    L.append("")
    cols = ["title_f1", "title_f2", "edge_f1", "edge_f2", "depth_acc",
            "order_tau", "content_f1", "content_f2", "content_r", "leaf_match",
            "coverage"]
    L += ["| condition | " + " | ".join(cols) + " |",
          "|" + "---|" * (len(cols) + 1)]
    for cond in conditions:
        s_ = summary.get(cond)
        if not s_:
            continue
        label = REGISTRY[cond].label if cond in REGISTRY else cond
        out = []
        for c in cols:
            a = s_.get(c)
            out.append("—" if not a else
                       f"{a['mean']:.3f} ± {a['sd']:.3f} ({a['n']})")
        L.append(f"| {label} | " + " | ".join(out) + " |")
    L += ["",
          "A dash means the condition does not produce that measure: the "
          "LADDER rows recover hierarchy only, so they carry no text, no "
          "assets and no reading order; CEILING is a bound on content and "
          "competes on nothing.", ""]

    L += ["## Where the text goes", "",
          "Coverage is decomposed rather than reported as one number. The "
          "five shares sum to 1 by construction and a test enforces it — "
          "without that, *unaccounted* would not mean anything. Only "
          "**unaccounted** is a defect: the others are deliberate. A single "
          "coverage figure would bury a defect behind the exclusions, and "
          "would reward a pipeline that dropped MORE content by letting it "
          "move that content into a policy bucket.", ""]
    for m in ("coverage", "excluded_rate", "asset_rate", "furniture_rate",
              "unaccounted_rate"):
        a = summary.get("ours", {}).get(m)
        if a:
            L.append(f"- **{m}** = {a['mean']:.3f} — {GLOSS[m]}")
    L.append("")

    L += ["## Figures, tables, and the representation ceiling", "",
          "Asset and reachability means cover only documents with at least "
          "one ground-truth asset: scoring a figure-free paper as a perfect "
          "1.0 is right per document but would quietly inflate the corpus "
          "mean.", "",
          "| condition | measure | mean | sd | n | what it is |",
          "|---|---|---|---|---|---|"]
    for cond in conditions:
        for m in ("asset_f1", "asset_f2", "asset_type_acc",
                  "reach_f1", "reach_f2", "floor_recall"):
            a = summary.get(cond, {}).get(m)
            if a:
                label = REGISTRY[cond].label if cond in REGISTRY else cond
                L.append(f"| {label} | {m} | {a['mean']:.3f} | {a['sd']:.3f} "
                         f"| {a['n']} | {GLOSS.get(m, '')} |")
    ceiling = summary.get("ceiling", {}).get("floor_recall")
    ours_r = summary.get("ours", {}).get("content_r")
    ours_f = summary.get("ours", {}).get("content_f1")
    if ceiling and ceiling["mean"]:
        L += ["", "The ceiling is what any PDF-based method could reach at "
              "best, because the ruler's text is LaTeX-cleaned and therefore "
              "cleaner than any rendered layer will ever be. Read the content "
              "score against it rather than against 1.0 — but note there are "
              "two ways to do that, and they do not agree:", ""]
        if ours_f:
            L.append(f"- **content F1 against the ceiling: "
                     f"{100.0 * ours_f['mean'] / ceiling['mean']:.0f}%** "
                     f"({ours_f['mean']:.3f} / {ceiling['mean']:.3f}). This is "
                     "the figure the paper quotes. It is the conservative "
                     "reading: an F1 is compared against a bound that is pure "
                     "recall, so precision losses are charged to the pipeline "
                     "without the ceiling being allowed the same.")
        if ours_r:
            L.append(f"- **content recall against the ceiling: "
                     f"{100.0 * ours_r['mean'] / ceiling['mean']:.0f}%** "
                     f"({ours_r['mean']:.3f} / {ceiling['mean']:.3f}). This is "
                     "the like-for-like comparison — `floor_recall` is a "
                     "recall bound, so recall is what it actually bounds.")
        L.append("")

    if cells:
        L += ["## Per-cell strata (condition: OURS)", "",
              "The corpus is stratified on page layout and section-numbering "
              "style — the two things the pipeline reacts to — not on subject "
              "matter, which it never sees.", "",
              "| cell | n | title_f1 | edge_f1 | depth_acc | order_tau | "
              "content_f1 |", "|---|---|---|---|---|---|---|"]
        for cell in sorted(cells):
            g = cells[cell]
            row = [cell.replace("_", " / "), str(len(g))]
            for m in ("title_f1", "edge_f1", "depth_acc", "order_tau",
                      "content_f1"):
                row.append(_fmt(_agg(_values(g, m))))
            L.append("| " + " | ".join(row) + " |")
        L.append("")

    if comps:
        L += ["## Paired comparisons", "",
              "Every condition sees the same documents, so each comparison is "
              "*paired*: the difference is taken within a document and then "
              "averaged, which removes document-to-document variation from "
              "the comparison. `p` is one one-sided Wilcoxon signed-rank "
              "test — rank-based because per-document scores are bounded in "
              "[0, 1] and skewed.", "",
              "| comparison | measure | n | mean A | mean B | difference | p |",
              "|---|---|---|---|---|---|---|"]
        for c in comps:
            a_ = REGISTRY[c["a"]].label if c["a"] in REGISTRY else c["a"]
            b_ = REGISTRY[c["b"]].label if c["b"] in REGISTRY else c["b"]
            L.append(f"| {a_} vs {b_} | {c['metric']} | {c['n']} | "
                     f"{c['mean_x']} | {c['mean_y']} | {c['mean_diff']:+.3f} | "
                     f"{c['p_wilcoxon']:.4g} |")
        L.append("")

    L += openkb_fidelity(rows_by_cond, pages_of or {}, conditions)

    L += ["", "## Completeness", "",
          "Work is scheduled tier-major: every document is scored on the free "
          "conditions before any condition that costs a model call. An "
          "interruption therefore always leaves a complete, reportable result "
          "set for every tier cheaper than the one that stalled — which is "
          "why a pending tier-1 row below is a schedule state, not a "
          "failure.", "",
          "| condition | tier | done | failed | parked | pending |",
          "|---|---|---|---|---|---|"]
    for cond, st in sorted(ledger_summary.items(),
                           key=lambda kv: (kv[1]["tier"], kv[0])):
        label = REGISTRY[cond].label if cond in REGISTRY else cond
        L.append(f"| {label} | {st['tier']} | {st.get('done', 0)} | "
                 f"{st.get('failed', 0)} | {st.get('parked', 0)} | "
                 f"{st.get('pending', 0)} |")

    if llm_status:
        L += ["", "### Offline model conditions", "",
              "These are run by hand: the harness writes a prompt per "
              "document, a person pastes it into a chat model, and the reply "
              "is saved beside the prompt. Prompts and replies are in the "
              "repository, so what the baseline was asked and what it "
              "answered can both be read.", "",
              "| condition | model | prompts written | replies saved | of |",
              "|---|---|---|---|---|"]
        for cond, st in llm_status.items():
            label = REGISTRY[cond].label if cond in REGISTRY else cond
            L.append(f"| {label} | {st.get('model') or '—'} | "
                     f"{st['prompts']} | {st['replies']} | {st['documents']} |")
    return "\n".join(L)


def latex_numbers(summary: dict, comps: list[dict], cells: dict,
                  corpus_n: int) -> str:
    """\\newcommand definitions, one per reported number."""
    L = ["% Auto-generated by run_1a.py — DO NOT EDIT BY HAND.",
         f"% {time.strftime('%Y-%m-%d %H:%M')}  ·  corpus N = {corpus_n}",
         "%",
         "% Usage: \\input{numbers.tex} in the preamble, then write e.g.",
         "%   our pipeline reaches \\resOursEdgeFOne\\ on nesting",
         "% Re-running the harness updates every number in the paper at once.",
         "",
         f"\\newcommand{{\\resCorpusN}}{{{corpus_n}}}"]
    for cond, metrics in sorted(summary.items()):
        cm = CONDITION_MACRO.get(cond)
        if not cm:
            continue
        L.append(f"% --- {cond} ---")
        for metric, a in sorted(metrics.items()):
            mm = METRICS.get(metric, (None,))[0]
            if not mm:
                continue
            L.append(f"\\newcommand{{\\res{cm}{mm}}}{{{a['mean']:.3f}}}")
            L.append(f"\\newcommand{{\\res{cm}{mm}N}}{{{a['n']}}}")
    if cells:
        L.append("% --- per-cell n (stratification table) ---")
        for cell in sorted(cells):
            name = "".join(w.capitalize() for w in cell.split("_"))
            L.append(f"\\newcommand{{\\resCell{name}N}}{{{len(cells[cell])}}}")
    if comps:
        L.append("% --- paired comparisons ---")
        for c in comps:
            a_ = CONDITION_MACRO.get(c["a"], c["a"])
            b_ = CONDITION_MACRO.get(c["b"], c["b"])
            mm = METRICS.get(c["metric"], (c["metric"],))[0]
            L.append(f"\\newcommand{{\\res{a_}Vs{b_}{mm}Diff}}"
                     f"{{{c['mean_diff']:+.3f}}}")
            L.append(f"\\newcommand{{\\res{a_}Vs{b_}{mm}P}}"
                     f"{{{c['p_wilcoxon']:.4g}}}")
    return "\n".join(L) + "\n"


def latex_tables(summary: dict, cells: dict, conditions: list[str]) -> str:
    L = ["% Auto-generated by run_1a.py — paste or \\input directly.", ""]
    # §sec:metrics promises F_beta for beta in {1,2}, so both are emitted.
    # F2 leans toward recall, the direction that matters clinically: a section
    # missing from the knowledge base can never be retrieved, while a spurious
    # one merely competes.
    L += ["% ---- main results ----",
          "% detection and nesting carry both F1 and F2, per sec:metrics.",
          "\\begin{center}",
          "\\begin{tabular}{lcccccccc}", "\\hline",
          "condition & detection $F_1$ & detection $F_2$ & nesting $F_1$ & "
          "nesting $F_2$ & levelling & order $\\tau$ & content $F_1$ & "
          "coverage \\\\",
          "\\hline"]
    for cond in conditions:
        s = summary.get(cond)
        if not s:
            continue
        row = [REGISTRY[cond].label if cond in REGISTRY else cond]
        for m in ("title_f1", "title_f2", "edge_f1", "edge_f2", "depth_acc",
                  "order_tau", "content_f1", "coverage"):
            row.append(_fmt(s.get(m)))
        L.append(" & ".join(row) + " \\\\")
    L += ["\\hline", "\\end{tabular}", "\\end{center}", ""]

    if cells:
        L += ["% ---- stratification ----", "\\begin{center}",
              "\\begin{tabular}{lcccc}", "\\hline",
              "cell & n & detection & nesting & order \\\\", "\\hline"]
        for cell in sorted(cells):
            g = cells[cell]
            row = [cell.replace("_", "/"), str(len(g))]
            for m in ("title_f1", "edge_f1", "order_tau"):
                row.append(_fmt(_agg(_values(g, m))))
            L.append(" & ".join(row) + " \\\\")
        L += ["\\hline", "\\end{tabular}", "\\end{center}"]
    return "\n".join(L) + "\n"


# ── CSV: one row per (document, condition), everything in a fixed order ────

# Column order is the reading order of the evaluation: what document, which
# condition, then the eight measures in the order the paper introduces them,
# then the bookkeeping that explains a row. Fixed here rather than derived
# from whatever keys a row happens to carry, so the file is diffable across
# runs and a column never moves.
CSV_COLUMNS = [
    # identity
    "doc", "cell", "columns", "numbering", "pages", "documentclass",
    "category", "published", "gt_headings",
    "cond", "condition_label", "tier",
    # 1 detection
    "title_p", "title_r", "title_f1", "title_f2",
    # 2 levelling
    "depth_acc", "depth_matched", "depth_correct", "depth_n_truth",
    # 3 nesting
    "edge_p", "edge_r", "edge_f1", "edge_f2",
    # 4 reading order
    "order_tau", "order_exact", "order_anchors",
    # 5 assets
    "asset_p", "asset_r", "asset_f1", "asset_f2", "asset_type_acc",
    "asset_n_truth",
    "n_assets_recovered",
    # 6 reachability
    "reach_p", "reach_r", "reach_f1", "reach_f2", "reach_n_truth",
    # 7 content fidelity
    "content_f1", "content_f2", "content_r", "leaf_match", "overall",
    "n_gt", "n_rec",
    "n_matched",
    # 8 coverage, decomposed (the five sum to 1)
    "coverage", "excluded_rate", "asset_rate", "furniture_rate",
    "unaccounted_rate", "cov_pdf_chars", "cov_missing_chars",
    # the ceiling condition's own measure
    "floor_recall", "floor_n_leaves",
    # bookkeeping
    "n_truth", "n_recovered", "ladder_rung", "n_headings_returned",
]


def write_csv(path: Path, rows: list[dict], manifest: dict,
              conditions: list[str]) -> int:
    """One row per scored (document, condition), sorted and fully populated.

    Every row carries its document's stratification covariates, so the file
    answers per-cell questions without a join against the manifest. Rows sort
    by cell, then document, then the condition's order in the registry —
    stable across runs, so two CSVs diff cleanly.
    """
    meta = {d["name"]: d for d in manifest.get("documents", [])}
    order = {c: i for i, c in enumerate(conditions)}

    def key(r: dict) -> tuple:
        m = meta.get(r["doc"], {})
        return (m.get("cell", "~"), r["doc"], order.get(r["cond"], 99))

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=key):
            m = meta.get(r["doc"], {})
            cond = REGISTRY.get(r["cond"])
            w.writerow({**r,
                        "cell": m.get("cell"), "columns": m.get("columns"),
                        "numbering": m.get("numbering"), "pages": m.get("pages"),
                        "documentclass": m.get("documentclass"),
                        "category": m.get("category"),
                        "published": m.get("published"),
                        "gt_headings": m.get("gt_headings"),
                        "condition_label": cond.label if cond else r["cond"],
                        "tier": cond.tier if cond else None})
    return len(rows)
