# `tools/` — corpus construction

| tool | what |
|---|---|
| `corpus.py` | build and freeze the corpus: `status`, `scan`, `select`, `download`, `freeze`, `topup` |
| `cell_census.py` | prevalence of each layout × numbering cell across arXiv |
| `fetch_arxiv.py` | the polite arXiv client both of the above use |

## Why the corpus is stratified the way it is

On **page layout × section-numbering style**, not subject category — those are
the two variables that select distinct code paths in the pipeline, and the
pipeline never sees subject matter. Category is balanced *within* cells, so it
is controlled rather than ignored.

Two of the six cells are genuinely rare combinations and carry no claim on
their own. "Rare" is a statement about the world, so `cell_census.py` records
every paper it classifies — including ones it has no use for — and reports each
cell's observed prevalence with a confidence interval. That is what makes the
two small cells a measured fact rather than an assumption.

The scan is deliberately **not** a neutral sample. A negative result is only
worth reporting if the search was aimed where the thing would be if it existed,
so the deficit categories lean toward the venues where a missing cell would
show up.

## The render is authoritative

Cell assignment starts from the LaTeX source, which is fast and available
before the PDF is fetched — but it is a claim about what the author asked for,
not about what came out. Source-only classification was wrong on 15% of the
pilot. `freeze` re-verifies every document from the render and the render
wins; documents that move between cells are printed every run.

This is also why `topup` exists and why it over-pulls: a document's true cell
is only known after verification, so more are fetched than are kept, and
`freeze` trims each cell to its target.

## Freezing

```bash
python3 tools/corpus.py freeze              # re-verify the frozen corpus
python3 tools/corpus.py freeze --refreeze   # rebuild it — changes every number
```

With a manifest already frozen, `freeze` re-verifies exactly the documents it
names and refuses to widen the set: that set is the artifact every reported
number is computed over. `--refreeze` is the explicit escape hatch and should
be treated as destructive.
