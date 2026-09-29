# BetterIngest — structure-faithful PDF ingestion, and the harness that scores it

A deterministic, CPU-only pipeline that converts a PDF into a heading tree with
body text and assets nested beneath each heading, plus an intrinsic evaluation
of that conversion which needs no human annotation (the ground truth is the author's
own LaTeX source)

Nothing here needs an API key, a GPU, or a network connection. Every model call
the study required has already been made, and both the questions and the
answers are committed.

---

## 1. Requirements

| | |
|---|---|
| Python | **3.12.9** (pinned in `.python-version`; 3.11+ should work) |
| OS | macOS or Linux. Developed on macOS, CPU only — no CUDA anywhere |
| Disk | ~200 MB checked out, most of it the 60-document corpus |

Four runtime packages, all in `requirements.txt`:

| package | why |
|---|---|
| `pypdfium2` | renders pages and reads the PDF's own text layer |
| `markitdown[pdf]` | the flat-markdown converter the BASE conditions are built on |
| `scipy` | Kendall's τ and Wilcoxon (both have pure-Python fallbacks in `bench/`) |
| `numpy` | array support for the layout and typography steps |
| `pytest` | the test suite |

**Layout detection is optional.** `paddlepaddle`, `paddlex` and `paddleocr` are
commented out in `requirements.txt` on purpose: `.ocr_cache/` ships the layout
blocks for all 60 corpus documents, so reproducing every reported number needs
none of them. Uncomment them only to ingest a PDF that is not already cached.

---

## 2. Install and reproduce

```bash
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 run_1a.py run --redo
```

`--redo` discards the ledger's cached rows and rescores all 60 documents × 7
scored conditions from the committed PDFs, LaTeX sources and model replies. It
takes about 45 seconds on a laptop CPU from a clean clone, makes no network
calls, and rewrites every artifact in §5. What it prints is what the paper
reports.

```bash
python3 -m pytest tests -q       # 178 tests
python3 tools/corpus.py freeze   # re-verify the frozen 60-document corpus
```

`run_1a.py` is the study's CLI: `plan`, `run`, `prompts`, `report`, `status`.
`report` alone regenerates every reporting artifact from the existing ledger
without rescoring anything.

---

## 3. Use the pipeline on a PDF of your own

The pipeline is a library, not a command — `BetterIngest` is the deliverable
class:

```python
from ingest.betteringest import BetterIngest

doc = BetterIngest(out_dir="out").ingest("paper.pdf")
doc.markdown        # structure-faithful markdown
doc.tree            # the content-at-leaves tree
doc.assets          # figures/tables: crop, page, caption, citing sections
doc.to_pageindex()  # the same tree in PageIndex's own format
```

A PDF outside `.ocr_cache/` needs the three layout packages from §1 installed,
and takes roughly a minute per paper on a CPU. Everything downstream of layout
detection is deterministic: the same PDF gives the same tree every run.

---

## 4. Reading the code, in order

Start at `ingest/`, which is the pipeline, in the order the data moves:

| module | step |
|---|---|
| `ingest/ocr.py` | layout detection + title recognition, cached in `.ocr_cache/` |
| `ingest/order.py` | reading order by column, heading blocks, document title |
| `ingest/outline.py` | ladder rung 0: the embedded PDF outline, validation-gated per entry |
| `ingest/levels.py` | rungs 0b/1/2/3: gap fill, marker induction, typography, confidence gate |
| `ingest/ladder.py` | the escalation ladder that assembles the rungs |
| `ingest/text.py` | the PDF text-layer reader |
| `ingest/assets.py` | captions, crops, reachability |
| `ingest/document.py` | the content-at-leaves tree, and its markdown |
| `ingest/betteringest.py` | the class that runs all of the above |
| `ingest/pageindex_vendor.py` | the seam onto PageIndex — deferred, nothing scored uses it |

**Almost nothing is OCR-recognised** — a vision-language model over every block costs ~48 minutes
for a 14-page paper, while labelling blocks is cheap and the text layer is exact.

Then `bench/`, which is the evaluation:

| module | role |
|---|---|
| `bench/latex.py` | derives the answer key from the LaTeX source — the most load-bearing file here |
| `bench/tree.py` | the one `normalise_title` every comparison goes through |
| `bench/score.py` | one document × one condition → one scored row |
| `bench/metrics.py` | levelling, reading order, the coverage decomposition |
| `bench/stats.py` | means, paired differences, the Wilcoxon test — and nothing else |
| `bench/conditions.py` | `REGISTRY`: every condition defined in one place, plus the baseline prompts |
| `bench/report.py` | writes all seven artifacts of §5 from the same ledger rows |
| `bench/transport.py`, `cache_db.py` | live-model plumbing. **Nothing scored uses these** |

`run_1a.py` ties them together; `bench/README.md` states the rule the directory
is built on — a score is only a verdict on the pipeline once the ruler is
proven able to measure it.

---

## 5. Where every reported number lives

Written together by `bench/report.py` from the same ledger rows, so they cannot
disagree with each other.

| file | what it holds |
|---|---|
| `out1a/results.csv` | **the primary record.** 420 rows = 60 docs × 7 scored conditions, 60 columns in fixed order |
| `out1a/results.json` | the same rows, machine-readable |
| `out1a/summary.json` | the aggregates, machine-readable |
| `out1a/report_card.md` | the human-readable tables: every condition × measure with mean, sd and n, the per-cell strata, and every paired test |
| `out1a/numbers.tex` | one `\newcommand` per number, so no figure need be typed by hand |
| `out1a/tables.tex` | ready-to-paste `tabular` environments |
| `out1a/ledger.db` | the SQLite unit table: one row per (document, condition), its status and payload |

**To check any single figure:** find its `\newcommand` in `numbers.tex`, then
find the column it aggregates in `results.csv` and take the mean over that
condition's 60 rows. The report card carries the same value with its spread and
its test.

Comparisons are **paired**: every condition sees the same 60 documents, so each
difference is taken within a document and then averaged. `p` is a one-sided
Wilcoxon signed-rank test — rank-based because per-document scores are bounded
in [0, 1] and skewed. The report card runs it on the whole corpus and on each
length subset separately, at both F1 and F2.

---

## 6. What is measured, and against what

Every condition builds a heading tree for the same document and is scored by
the same ruler, differing in exactly one respect — where the hierarchy comes
from — so a difference between two rows is attributable to that.

**The ruler is the author's own LaTeX source.** `\section`/`\subsection` give
the tree, `figure`/`table` environments give the floats, a `\ref` inside a
section links that section to that float. The answer key is *derived*, not
annotated: there is no labelling step to audit and no inter-annotator agreement
to report, because there are no annotators.

| condition | where the hierarchy comes from | cost |
|---|---|---|
| `ours` | the shipped pipeline | free |
| `ceiling` | representation bound — **not a competitor** | free |
| `ladder0/1/2` | ablation: outline alone, + marker induction, + typography | free |
| `base_small` | markitdown → a small model rebuilds the hierarchy | 1 call/doc |
| `base_big` | markitdown → a larger model rebuilds the hierarchy | 1 call/doc |
| `refine` | our output handed back to a model — **not run**, see §10 | 1 call/doc |

| measure | CSV column | what it answers |
|---|---|---|
| detection | `title_f1`, `title_f2` | of the headings in the source, how many did we find? |
| levelling | `depth_acc` | of the headings we found, how many sit at the right depth? |
| nesting | `edge_f1`, `edge_f2` | parent–child pairs recovered — identity and structure together |
| reading order | `order_tau` | Kendall's τ over the leaf sequence; 1.0 is exact |
| assets | `asset_f1`, `asset_f2`, `asset_type_acc` | figures/tables found, and typed correctly |
| reachability | `reach_f1`, `reach_f2` | is the asset attached to the section that refers to it? |
| content fidelity | `content_f1`, `content_f2`, `content_r` | word overlap of the text under each matched heading |
| coverage | `coverage` + 4 shares | share of the text layer that reached the markdown |

Detection and levelling are kept separate on purpose: entangled, a fall in
nesting cannot be attributed between "we missed the heading" and "we misfiled
it", which need different fixes.

---

## 7. The corpus

Sixty arXiv papers, stratified on **page layout × section-numbering style** —
the two things the pipeline reacts to — rather than on subject category, which
it never sees (24 categories are balanced within cells).

- `corpus/<cell>/<doc>/` holds the PDF, the `.tex` source and `meta.json`.
- `corpus_manifest.json` is **authoritative**: the runner ignores anything in
  `corpus/` it does not name. It pins each document's sha256, cell, page count,
  category, publication date and ground-truth heading count.
- `tools/corpus.py freeze` re-verifies exactly those 60 and refuses to widen
  the set. `--refreeze` rebuilds from scratch and **would change every reported
  number** — do not run it to check anything.
- `tools/cell_census.py` reports how prevalent each cell is in the wild, which
  is what justifies stratifying rather than drawing uniformly.

**Column count is decided from the render, not the source.**
`bench/layout_verify.py` does this, because a conference style file can call
`\twocolumn` from a plain `\documentclass{article}` with nothing detectable in
the source; source-only classification was wrong on 15% of the pilot.

**Memorisation control.** The corpus is date-gated at `2026-06-01`; every
document was in fact published between 2026-07-22 and 2026-08-26. BASE-small
(`google/gemma-4-31b-it`) has a vendor-stated cutoff of January 2025. BASE-big
(`deepseek/deepseek-v4-pro-0813`) publishes no cutoff; third-party catalogues
infer April 2026 from the V4-Pro release.

---

## 8. The two model-assisted conditions

`BASE-small` and `BASE-big` are the only scored conditions that cost a model
call, and **both are fully answered and committed** — reproducing a number
never makes a call.

| what | where |
|---|---|
| the prompt sent, per document | `out1a/llm/<cond>/<doc>.prompt.md` (60 each) |
| the reply received, per document | `out1a/llm/<cond>/<doc>.reply.txt` (60 each) |
| the same replies as delivered, plus batch metadata | `base_small_answers/`, `base_big_answers/` (`batch.json`) |
| which model answered which condition | `out1a/llm/models.json` |

The prompt hands the model markitdown's flat text and asks for
`{"headings": [{"title", "level"}]}` — it does not name the metric, hint at the
genre, or say how many headings to expect. Parsing (`bench/offline.py`,
`bench/conditions.py:parse_headings`) is deliberately permissive about schema
drift, since being strict would score the baseline's JSON formatting rather
than its structure recovery.

**What BASE reproduces.** The ecosystem default is OpenKB
(`github.com/VectifyAI/OpenKB`): convert with markitdown, one model call to
rebuild the heading list. Its config exposes `pageindex_threshold: 20` — under
20 pages it takes that single-call path, at 20 or more it hands the document to
PageIndex's multi-call tree indexing. BASE reproduces the **short-document path
only**, so it is faithful below the threshold and a lower bound above it; the
report card breaks both subsets out for exactly this reason. Only the first
step — heading reconstruction — is reproduced, which is why BASE is scored on
detection, nesting and levelling alone.

**The baseline is not a strawman.** PageIndex's default model is
`gpt-4o-2024-11-20` (`vendor/pageindex/pageindex/config.yaml:1`, vendored at
pinned commit `f413c66`). On Artificial Analysis' composite Intelligence Index
both baseline tiers score *above* that checkpoint, so each BASE row is an upper
bound on the ecosystem default's structure recovery rather than a weakened
stand-in for it.

The three scripts that made the calls — `process_base_big.py`,
`process_base_small.py` (the same script repointed) and `rerun_base_big.py`
(four documents whose batch replies hit the 2048-token cap, re-issued at
`max_tokens` 10000) — are kept as the record and are **not needed to reproduce
any number**.

---

## 9. Two conventions the paper has to state

**Content against the ceiling.** `floor_recall` = 0.938 is a *recall* bound —
how much ground-truth text exists in the PDF text layer at all. Two readings
follow and the report card prints both: **93%** (`content_f1` / `floor_recall`
= 0.870 / 0.938), conservative, since an F1 is charged for precision losses
while the bound is not; and **97%** (`content_r` / `floor_recall` = 0.907 /
0.938), like-for-like. The paper quotes 93%. Either is defensible; quoting one
without naming which is not.

**Coverage is decomposed, not reported as one number.** The five shares sum to
1 by construction and a test enforces it. Only `unaccounted_rate` is a defect —
the rest are deliberate policy. A single coverage figure would let a pipeline
look better by dropping more content into a policy bucket.

---

## 10. Known limitations, on the record

- **BASE is faithful to OpenKB only under 20 pages**, and reproduces only its
  heading-reconstruction step. §8.
- **`unaccounted_rate` = 0.070.** 7% of the text layer is neither emitted nor
  accounted for.