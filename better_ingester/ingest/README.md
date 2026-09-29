# `ingest/` — the pipeline

Deterministic, CPU-only, local. No language model on the main path.

A PDF enters as bytes and leaves as markdown plus a content-at-leaves tree.
The modules are in dataflow order:

| module | what it decides |
|---|---|
| `ocr.py` | what regions exist on each page, and what the title regions say |
| `order.py` | what order those regions are read in |
| `outline.py` | whether the PDF's own bookmark tree can be trusted (rung 0) |
| `levels.py` | how deep each heading sits (rungs 0b, 1, 2, 3) |
| `ladder.py` | which of those signals to believe, in what order |
| `text.py` | what the body text is |
| `assets.py` | what the figures and tables are, and who refers to them |
| `document.py` | how all of that assembles into a tree, and into markdown |
| `betteringest.py` | the class that runs the above and is the deliverable |
| `pageindex_vendor.py` | the seam onto PageIndex — deferred, nothing scored uses it |

## Two decisions worth knowing before reading the code

**Headings are identified by the detector's label, never by their text.** A
caption the layout model mislabels as a heading becomes an honest false
positive rather than something a text heuristic quietly filters out. The
heuristic would score better on this corpus and generalise worse, which is the
wrong trade for a benchmark.

**Almost nothing is recognised.** Running a document vision-language model over
every block costs about 48 minutes for a 14-page paper on this hardware,
because the time goes into generating text word by word. Labelling every block
generates nothing and is cheap; the small recogniser then reads a handful of
short heading crops. Body text comes from the PDF's own text layer, which is
exact and costs about a millisecond per block.

## The ladder

Signals are tried in order of how much they can be trusted, and the ladder
stops at the first one that earns it. Printed section numbers survive
rendering exactly; font size does not — in IEEE-style papers the section
headings are set in small caps *smaller* than the subsections beneath them, so
a naive size rule inverts the hierarchy.

No rung can fabricate depth. When the evidence conflicts the ladder returns a
flat document, which is the honest floor.

`build_ladder_tree(max_rung=N)` caps which rungs may fire — that is what makes
the ablation in the paper measurable, and capping never changes the rungs
below it, so each row differs from the one above by exactly one stage.

## The invariant

**Text lives only in leaves.** A section with both subsections and its own
introductory prose has that prose pushed into its own leaf, so internal nodes
are pure structure. This is what makes the tree a *segmentation* rather than a
hierarchy of containers, and it mirrors how the LaTeX ruler builds ground
truth, so the two are comparable leaf for leaf.
