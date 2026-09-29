# `bench/` — the evaluation

Scores the pipeline against ground truth derived from the author's own LaTeX
source, so nothing here needs a human annotator.

| module | role |
|---|---|
| `latex.py` | **the ruler.** LaTeX source → ground-truth tree, assets, references |
| `tree.py` | the shared `Node`, title normalisation, and the core scores |
| `metrics.py` | levelling, reading order, and the coverage decomposition |
| `score.py` | one (document, condition) → one scored row, all eight measures |
| `conditions.py` | the condition registry, prompts, and per-condition runners |
| `offline.py` | the model-assisted conditions, run by hand |
| `stats.py` | means, sd, n, paired differences, one rank test. Nothing else |
| `ledger.py` | the resumable (document, condition) unit table |
| `report.py` | report card, CSV, `numbers.tex`, `tables.tex` |
| `layout_verify.py` | column count from the render, not the source |
| `transport.py`, `cache_db.py` | live-model plumbing. **Nothing scored uses these** |

## The rule this directory is built on

**A score is only a verdict on the pipeline once the ruler is proven able to
measure it.** Much of this directory's history is ruler bugs caught before a
number was trusted. Two consequences visible in the code:

- Every comparison goes through one `normalise_title`. Rendered numbering,
  markdown emphasis, smart quotes and appendix letters are evaluation-schema
  artifacts, not content differences, and folding them in two places is how
  the two definitions drift apart.
- `parse_latex` and `parse_doc` share one heading walk. They used to have two,
  which meant the ruler could disagree with itself about what a heading is.

## Things that look like bugs and are not

**Asset means exclude documents with no assets.** Scoring a figure-free paper
as a perfect 1.0 is right per document and would inflate a corpus mean, so
`report.GUARDED` drops those rows from the denominator.

**Coverage is decomposed into five shares that sum to 1.** A single coverage
number would bury a defect behind deliberate exclusions, and would reward a
pipeline that dropped *more* content by letting it move that content into a
policy bucket. Only `unaccounted_rate` is a defect. A test pins the sum,
because without it "unaccounted" would not mean anything.

**Reading order matches only titles that are unique on both sides.** Matching
by consuming a queue in document order — as `depth_accuracy` does — would
impose the very ordering the metric is trying to measure and return τ = 1 by
construction.

**CEILING is not a competitor.** It measures how much ground-truth text exists
in the rendered layer at all, with no partition and no pipeline involved, so
it bounds what any PDF-based method could reach. Two earlier designs were
discarded for anchoring our own extracted text under the ground-truth tree —
each produced a "ceiling" that sat *below* the pipeline it was meant to bound.
