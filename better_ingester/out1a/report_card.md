# Intrinsic evaluation — results

Generated 2026-09-14 12:10 · corpus N = 60 documents.

Every condition builds a heading tree for the same document and is scored by the same ruler: the author's own LaTeX source, which states the structure exactly and needed no annotation. Conditions differ in exactly one respect — where the hierarchy comes from — so a difference between two rows is attributable to that.

## The conditions

- **OURS** (`ours`, tier 0) — the shipped pipeline, scored as itself
- **CEILING** (`ceiling`, tier 0) — representation bound on content fidelity — not a competitor
- **LADDER-0** (`ladder0`, tier 0) — hierarchy from the embedded outline alone
- **LADDER-1** (`ladder1`, tier 0) — + marker-schema induction
- **LADDER-2** (`ladder2`, tier 0) — + typography calibration
- **BASE-small** (`base_small`, tier 1) — markitdown + a small model rebuilding the hierarchy
- **BASE-big** (`base_big`, tier 1) — markitdown + a larger model rebuilding the hierarchy
- **REFINE** (`refine`, tier 1) — our output handed back to a model for correction

Tier 0 costs nothing and runs unattended. Tier 1 needs one model call per document, supplied offline; see the completeness table for what has been answered.

## Main results

Cells are `mean ± sd (n)` over the corpus. Higher is better everywhere in this table.

- **title_f1** — of the headings in the source, how many did we find?
- **depth_acc** — of the headings we found, how many sit at the right depth?
- **edge_f1** — parent-child pairs recovered — identity and structure together
- **order_tau** — Kendall's tau over the leaf sequence; 1.0 is exact order
- **content_f1** — word overlap of the text under each matched heading
- **coverage** — share of the text layer that reached the markdown

| condition | title_f1 | title_f2 | edge_f1 | edge_f2 | depth_acc | order_tau | content_f1 | content_f2 | content_r | leaf_match | coverage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OURS | 0.838 ± 0.183 (60) | 0.832 ± 0.182 (60) | 0.793 ± 0.221 (60) | 0.789 ± 0.220 (60) | 0.987 ± 0.053 (60) | 1.000 ± 0.002 (58) | 0.870 ± 0.103 (60) | 0.883 ± 0.084 (60) | 0.907 ± 0.056 (60) | 0.853 ± 0.197 (60) | 0.743 ± 0.089 (60) |
| CEILING | 0.893 ± 0.158 (60) | 0.855 ± 0.176 (60) | 0.859 ± 0.206 (60) | 0.824 ± 0.217 (60) | — | — | — | — | — | — | — |
| LADDER-0 | 0.828 ± 0.208 (60) | 0.804 ± 0.216 (60) | 0.641 ± 0.295 (60) | 0.621 ± 0.290 (60) | 0.757 ± 0.324 (60) | — | — | — | — | — | — |
| LADDER-1 | 0.828 ± 0.208 (60) | 0.804 ± 0.216 (60) | 0.716 ± 0.273 (60) | 0.693 ± 0.270 (60) | 0.883 ± 0.264 (60) | — | — | — | — | — | — |
| LADDER-2 | 0.828 ± 0.208 (60) | 0.804 ± 0.216 (60) | 0.790 ± 0.243 (60) | 0.767 ± 0.246 (60) | 0.959 ± 0.182 (60) | — | — | — | — | — | — |
| BASE-small | 0.833 ± 0.147 (60) | 0.817 ± 0.141 (60) | 0.761 ± 0.199 (60) | 0.747 ± 0.192 (60) | 0.918 ± 0.182 (60) | — | — | — | — | — | — |
| BASE-big | 0.876 ± 0.125 (60) | 0.883 ± 0.116 (60) | 0.826 ± 0.188 (60) | 0.832 ± 0.182 (60) | 0.942 ± 0.165 (60) | — | — | — | — | — | — |

A dash means the condition does not produce that measure: the LADDER rows recover hierarchy only, so they carry no text, no assets and no reading order; CEILING is a bound on content and competes on nothing.

## Where the text goes

Coverage is decomposed rather than reported as one number. The five shares sum to 1 by construction and a test enforces it — without that, *unaccounted* would not mean anything. Only **unaccounted** is a defect: the others are deliberate. A single coverage figure would bury a defect behind the exclusions, and would reward a pipeline that dropped MORE content by letting it move that content into a policy bucket.

- **coverage** = 0.743 — share of the text layer that reached the markdown
- **excluded_rate** = 0.102 — dropped by policy (bibliography, front matter)
- **asset_rate** = 0.080 — held in asset records rather than body text
- **furniture_rate** = 0.004 — running heads, page numbers, marginalia
- **unaccounted_rate** = 0.070 — text neither emitted nor accounted for — the defect

## Figures, tables, and the representation ceiling

Asset and reachability means cover only documents with at least one ground-truth asset: scoring a figure-free paper as a perfect 1.0 is right per document but would quietly inflate the corpus mean.

| condition | measure | mean | sd | n | what it is |
|---|---|---|---|---|---|
| OURS | asset_f1 | 0.886 | 0.143 | 57 | figures and tables detected |
| OURS | asset_f2 | 0.920 | 0.114 | 57 | the same, weighting recall higher |
| OURS | asset_type_acc | 0.907 | 0.225 | 57 | of those, how many typed figure/table correctly |
| OURS | reach_f1 | 0.707 | 0.295 | 54 | asset attached to the section that refers to it |
| OURS | reach_f2 | 0.686 | 0.298 | 54 | the same, weighting recall higher |
| CEILING | floor_recall | 0.938 | 0.038 | 60 | how much ground-truth text exists in the layer at all |

The ceiling is what any PDF-based method could reach at best, because the ruler's text is LaTeX-cleaned and therefore cleaner than any rendered layer will ever be. Read the content score against it rather than against 1.0 — but note there are two ways to do that, and they do not agree:

- **content F1 against the ceiling: 93%** (0.870 / 0.938). This is the figure the paper quotes. It is the conservative reading: an F1 is compared against a bound that is pure recall, so precision losses are charged to the pipeline without the ceiling being allowed the same.
- **content recall against the ceiling: 97%** (0.907 / 0.938). This is the like-for-like comparison — `floor_recall` is a recall bound, so recall is what it actually bounds.

## Per-cell strata (condition: OURS)

The corpus is stratified on page layout and section-numbering style — the two things the pipeline reacts to — not on subject matter, which it never sees.

| cell | n | title_f1 | edge_f1 | depth_acc | order_tau | content_f1 |
|---|---|---|---|---|---|---|
| single / arabic | 12 | 0.680 | 0.625 | 0.976 | 1.000 | 0.814 |
| single / roman | 6 | 0.837 | 0.731 | 1.000 | 1.000 | 0.852 |
| single / unnumbered | 12 | 0.891 | 0.866 | 0.973 | 1.000 | 0.881 |
| two / arabic | 12 | 0.836 | 0.767 | 0.983 | 1.000 | 0.914 |
| two / roman | 12 | 0.900 | 0.886 | 1.000 | 0.999 | 0.851 |
| two / unnumbered | 6 | 0.924 | 0.913 | 1.000 | 1.000 | 0.925 |

## Paired comparisons

Every condition sees the same documents, so each comparison is *paired*: the difference is taken within a document and then averaged, which removes document-to-document variation from the comparison. `p` is one one-sided Wilcoxon signed-rank test — rank-based because per-document scores are bounded in [0, 1] and skewed.

| comparison | measure | n | mean A | mean B | difference | p |
|---|---|---|---|---|---|---|
| OURS vs LADDER-0 | title_f1 | 60 | 0.838 | 0.828 | +0.010 | 0.2573 |
| OURS vs LADDER-0 | title_f2 | 60 | 0.832 | 0.804 | +0.028 | 0.08904 |
| OURS vs LADDER-0 | edge_f1 | 60 | 0.793 | 0.641 | +0.152 | 0.00015 |
| OURS vs LADDER-0 | edge_f2 | 60 | 0.789 | 0.621 | +0.168 | 1e-05 |
| OURS vs LADDER-0 | depth_acc | 60 | 0.987 | 0.757 | +0.230 | 1e-05 |
| OURS vs BASE-small | title_f1 | 60 | 0.838 | 0.833 | +0.005 | 0.2338 |
| OURS vs BASE-small | title_f2 | 60 | 0.832 | 0.817 | +0.016 | 0.1313 |
| OURS vs BASE-small | edge_f1 | 60 | 0.793 | 0.761 | +0.032 | 0.05338 |
| OURS vs BASE-small | edge_f2 | 60 | 0.789 | 0.747 | +0.042 | 0.02022 |
| OURS vs BASE-small | depth_acc | 60 | 0.987 | 0.918 | +0.068 | 0.00066 |
| OURS vs BASE-big | title_f1 | 60 | 0.838 | 0.876 | -0.038 | 0.9769 |
| OURS vs BASE-big | title_f2 | 60 | 0.832 | 0.883 | -0.050 | 0.9963 |
| OURS vs BASE-big | edge_f1 | 60 | 0.793 | 0.826 | -0.033 | 0.9154 |
| OURS vs BASE-big | edge_f2 | 60 | 0.789 | 0.832 | -0.043 | 0.9688 |
| OURS vs BASE-big | depth_acc | 60 | 0.987 | 0.942 | +0.044 | 0.02186 |


## BASE against OpenKB's own dispatch threshold

OpenKB reads a document under 20 pages in one call after converting it with markitdown — which is exactly what BASE does — but hands a longer one to PageIndex's multi-call tree indexing instead. BASE is therefore a faithful reproduction of the ecosystem default only on the shorter subset; on the longer one it is the short-document recipe applied beyond where OpenKB would apply it, and reads as a lower bound on what that stack would actually do.

| condition | subset | n | detection F1 | nesting F1 | levelling |
|---|---|---|---|---|---|
| BASE-small | < 20 pages (faithful) | 36 | 0.843 | 0.761 | 0.926 |
| BASE-small | >= 20 pages (extrapolated) | 24 | 0.817 | 0.762 | 0.906 |
| BASE-big | < 20 pages (faithful) | 36 | 0.881 | 0.838 | 0.981 |
| BASE-big | >= 20 pages (extrapolated) | 24 | 0.867 | 0.809 | 0.885 |

### Paired tests within each subset

Same test as the *Paired comparisons* section above — one one-sided Wilcoxon signed-rank test of the hypothesis that OURS exceeds the baseline, paired within document — computed on each subset separately.

| comparison | subset | measure | n | mean A | mean B | difference | p |
|---|---|---|---|---|---|---|---|
| OURS vs BASE-small | < 20 pp | title_f1 | 36 | 0.885 | 0.843 | +0.042 | 0.1094 |
| OURS vs BASE-small | < 20 pp | title_f2 | 36 | 0.872 | 0.825 | +0.046 | 0.08485 |
| OURS vs BASE-small | < 20 pp | edge_f1 | 36 | 0.839 | 0.761 | +0.078 | 0.00797 |
| OURS vs BASE-small | < 20 pp | edge_f2 | 36 | 0.827 | 0.745 | +0.082 | 0.00863 |
| OURS vs BASE-small | < 20 pp | depth_acc | 36 | 0.994 | 0.926 | +0.068 | 0.00253 |
| OURS vs BASE-big | < 20 pp | title_f1 | 36 | 0.885 | 0.881 | +0.004 | 0.5249 |
| OURS vs BASE-big | < 20 pp | title_f2 | 36 | 0.872 | 0.889 | -0.017 | 0.8717 |
| OURS vs BASE-big | < 20 pp | edge_f1 | 36 | 0.839 | 0.838 | +0.001 | 0.3824 |
| OURS vs BASE-big | < 20 pp | edge_f2 | 36 | 0.827 | 0.844 | -0.017 | 0.6839 |
| OURS vs BASE-big | < 20 pp | depth_acc | 36 | 0.994 | 0.981 | +0.014 | 0.02156 |
| OURS vs BASE-small | >= 20 pp | title_f1 | 24 | 0.767 | 0.817 | -0.050 | 0.6137 |
| OURS vs BASE-small | >= 20 pp | title_f2 | 24 | 0.773 | 0.803 | -0.030 | 0.4157 |
| OURS vs BASE-small | >= 20 pp | edge_f1 | 24 | 0.724 | 0.762 | -0.038 | 0.607 |
| OURS vs BASE-small | >= 20 pp | edge_f2 | 24 | 0.731 | 0.749 | -0.018 | 0.3463 |
| OURS vs BASE-small | >= 20 pp | depth_acc | 24 | 0.975 | 0.906 | +0.068 | 0.05706 |
| OURS vs BASE-big | >= 20 pp | title_f1 | 24 | 0.767 | 0.867 | -0.100 | 0.999 |
| OURS vs BASE-big | >= 20 pp | title_f2 | 24 | 0.773 | 0.873 | -0.099 | 0.9982 |
| OURS vs BASE-big | >= 20 pp | edge_f1 | 24 | 0.724 | 0.809 | -0.084 | 0.9846 |
| OURS vs BASE-big | >= 20 pp | edge_f2 | 24 | 0.731 | 0.814 | -0.083 | 0.9814 |
| OURS vs BASE-big | >= 20 pp | depth_acc | 24 | 0.975 | 0.885 | +0.090 | 0.0844 |

## Completeness

Work is scheduled tier-major: every document is scored on the free conditions before any condition that costs a model call. An interruption therefore always leaves a complete, reportable result set for every tier cheaper than the one that stalled — which is why a pending tier-1 row below is a schedule state, not a failure.

| condition | tier | done | failed | parked | pending |
|---|---|---|---|---|---|
| CEILING | 0 | 60 | 0 | 0 | 0 |
| LADDER-0 | 0 | 60 | 0 | 0 | 0 |
| LADDER-1 | 0 | 60 | 0 | 0 | 0 |
| LADDER-2 | 0 | 60 | 0 | 0 | 0 |
| OURS | 0 | 60 | 0 | 0 | 0 |
| BASE-big | 1 | 60 | 0 | 0 | 0 |
| BASE-small | 1 | 60 | 0 | 0 | 0 |
| REFINE | 1 | 0 | 0 | 60 | 0 |

### Offline model conditions

These are run by hand: the harness writes a prompt per document, a person pastes it into a chat model, and the reply is saved beside the prompt. Prompts and replies are in the repository, so what the baseline was asked and what it answered can both be read.

| condition | model | prompts written | replies saved | of |
|---|---|---|---|---|
| BASE-small | google/gemma-4-31b-it (OpenRouter, temperature 0, max_tokens 2048, JSON mode) | 60 | 60 | 60 |
| BASE-big | deepseek/deepseek-v4-pro-0813 (OpenRouter, temperature 0, max_tokens 2048, JSON mode) | 60 | 60 | 60 |
| REFINE | — | 0 | 0 | 60 |
