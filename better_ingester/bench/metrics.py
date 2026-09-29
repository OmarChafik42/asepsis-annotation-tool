"""
bench/metrics.py — the measures the report card is built from.

Three additions to the scoring in bench/tree.py, each closing a specific gap
that the existing metric set cannot express:

  depth_accuracy   Detection and nesting were entangled: a fall in edge_f1
                   could not be attributed between "the heading was missed"
                   and "the heading was found and misplaced".  This scores
                   ONLY the second, over the headings that were detected, so
                   it is free of the edge-metric's N-fold cascade.

  reading_order    Kendall's tau between the ground-truth and recovered leaf
                   sequences.  Reading order is the failure mode two-column
                   geometry produces and is half of what the corpus is
                   stratified on; nothing scored it before.

  coverage         Fraction of the PDF text layer's characters that appear
                   anywhere in the emitted markdown, plus the share sitting in
                   blocks we deliberately discard (running heads, page
                   numbers, marginalia).  Consults NO ground truth, so it
                   separates "text in the wrong leaf" from "text lost
                   entirely" — and transfers unchanged to documents with no
                   LaTeX source (Section 1b).

All three take the same trees the rest of the bench uses and go through the
same `normalise_title`, so nothing here introduces a second comparison schema.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from bench.tree import Node, normalise_title
from ingest.text import labelled_text

# Layout labels whose text is page furniture: dropped on purpose, and so not
# counted against coverage.  Everything else is content the pipeline owes us.
FURNITURE_LABELS = frozenset({
    "header", "footer", "number", "page_number", "aside_text",
    "header_image", "footer_image",
})

# Content the pipeline excludes by POLICY rather than by failure. Measured on
# the pilot corpus, the bibliography alone is 15.4% of text-layer characters —
# large enough that a single "coverage" number is uninterpretable without
# separating it out. Excluding it is a defensible choice for a retrieval
# substrate; leaving it indistinguishable from content that was simply lost is
# not, because only the second kind is a defect.
#
# `doc_title` is here because it is metadata, and it already becomes the tree's
# root rather than a passage. `abstract` was here too, until we noticed the
# omission was invisible: the pipeline dropped pre-heading frontmatter and so
# did the LaTeX ruler, so no ground-truth-relative metric could see it. Both
# now record the abstract as body content, and it is scored like any other leaf.
EXCLUDED_LABELS = frozenset({"reference_content", "bibliography", "doc_title"})

# Content that IS captured, just not as body text — it lives in the asset
# records (caption, crop, page, citing sections) instead. Charging it against
# body-text coverage would report a loss the pipeline did not incur.
ASSET_LABELS = frozenset({"figure_title", "table", "image", "chart",
                          "figure", "table_title"})

_WORD = re.compile(r"[a-z0-9]+")


def content_words(s: str) -> set[str]:
    """The bench's content-word definition, shared so no metric invents a
    second one: >=3 chars and containing at least one letter."""
    return {w for w in s.lower().split()
            if len(w) >= 3 and any(c.isalpha() for c in w)}


# ── levelling: depth accuracy over detected headings ────────────────────────

@dataclass
class DepthScore:
    accuracy: float      # of detected headings, fraction at the correct depth
    n_matched: int       # headings present in both trees (the denominator)
    n_correct: int
    n_truth: int         # for context: how much of the truth was detected

    def row(self) -> dict:
        return {"depth_acc": round(self.accuracy, 3),
                "depth_matched": self.n_matched,
                "depth_correct": self.n_correct,
                "depth_n_truth": self.n_truth}


def _titles_with_depth(root: Node) -> list[tuple[str, int]]:
    """(normalised title, depth) for every non-root node, in pre-order.
    Depth is distance from the root, which is the tree's *relative* level —
    the same convention the LaTeX ruler uses."""
    out: list[tuple[str, int]] = []

    def walk(n: Node, d: int) -> None:
        for c in n.children:
            out.append((normalise_title(c.title), d + 1))
            walk(c, d + 1)

    walk(root, 0)
    return out


def depth_accuracy(truth: Node, recovered: Node) -> DepthScore:
    """Of the headings the pipeline actually detected, what fraction did it
    place at the right relative depth?

    Matching is queue-consuming by normalised title in pre-order, so repeated
    titles ("Discussion" twice) resolve by position rather than arbitrarily.
    Headings that were never detected are simply absent from the denominator:
    this metric answers "given detection, was levelling right", and detection
    is title_f1's job."""
    t = _titles_with_depth(truth)
    r = _titles_with_depth(recovered)
    queue = list(r)
    matched = correct = 0
    for title, tdepth in t:
        for i, (rt, rdepth) in enumerate(queue):
            if rt == title:
                matched += 1
                correct += (rdepth == tdepth)
                del queue[:i + 1]
                break
    return DepthScore(accuracy=(correct / matched if matched else 0.0),
                      n_matched=matched, n_correct=correct, n_truth=len(t))


# ── the structural ceiling: nesting achievable given detection ─────────────

def contract_to_detected(truth: Node, detected: Counter) -> Node:
    """Ground truth restricted to the headings a pipeline actually found,
    with removed internal nodes CONTRACTED — their children reattach to the
    nearest surviving ancestor.

    This is the best-case tree for a given detection: every heading that was
    found sits exactly where the author put it, relative to the other
    headings that were found.
    """
    available = Counter(detected)

    def walk(src: Node, dst: Node) -> None:
        for c in src.children:
            key = normalise_title(c.title)
            if available[key] > 0:
                available[key] -= 1
                kept = Node(title=c.title)
                dst.children.append(kept)
                walk(c, kept)
            else:
                walk(c, dst)          # contract: descendants rise to `dst`

    root = Node(title=truth.title)
    walk(truth, root)
    return root


def structure_ceiling(truth: Node, recovered: Node) -> Node:
    """The tree a PERFECT hierarchy stage would have produced from the
    headings this pipeline detected.

    Scoring it against ground truth bounds nesting the way CEILING bounds
    content: whatever it leaves on the table is lost to DETECTION, and the
    gap between it and the pipeline's own nesting is what the hierarchy
    logic actually costs.

    It is a genuine upper bound, and cheap to see why. Ground truth's edge
    multiset is fixed; an edge can only match if both endpoints are headings
    that exist in ground truth, so a spurious heading contributes no matching
    edge under any arrangement and is dropped. Among arrangements of the
    remaining headings, preserving ground truth's own parent-child relation
    wherever both endpoints survive maximises the overlap, which is exactly
    what contraction does.

    The bound is therefore optimistic about precision: it charges nothing for
    the false positives the pipeline really emits. It answers "how well could
    the hierarchy stage have done with what detection handed it", not "how
    well could this exact output have scored".
    """
    detected = Counter(normalise_title(n.title)
                       for n in recovered.all_nodes()[1:])
    return contract_to_detected(truth, detected)


# ── reading order: Kendall's tau over the leaf sequence ────────────────────

@dataclass
class OrderScore:
    tau: float | None    # None when there are too few anchors to define it
    exact: bool | None   # matched subsequence in identical relative order
    n_anchors: int

    def row(self) -> dict:
        return {"order_tau": None if self.tau is None else round(self.tau, 3),
                "order_exact": self.exact, "order_anchors": self.n_anchors}


def _leaf_sequence(root: Node) -> list[str]:
    """Normalised titles of content leaves in document order (pre-order over a
    tree built in reading order IS document order)."""
    return [normalise_title(n.title) for n in root.all_nodes()
            if n.kind == "content"]


def _kendall_tau(xs: list[int]) -> float:
    """tau-b of the permutation xs against 0..n-1 (the identity)."""
    try:
        from scipy.stats import kendalltau  # type: ignore[import-untyped]
        t = kendalltau(list(range(len(xs))), xs).statistic
        return 0.0 if t != t else float(t)          # NaN → 0
    except Exception:
        pass
    n = len(xs)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            if xs[i] < xs[j]:
                conc += 1
            elif xs[i] > xs[j]:
                disc += 1
    total = conc + disc
    return (conc - disc) / total if total else 0.0


def reading_order(truth: Node, recovered: Node) -> OrderScore:
    """Kendall's tau between the GT and recovered leaf sequences.

    Anchors are leaves whose normalised title occurs EXACTLY ONCE on both
    sides.  This restriction is load-bearing: matching by consuming a queue in
    document order — as depth_accuracy does — would impose the very ordering
    the metric is trying to measure and return tau = 1 by construction.
    Unique titles are the only pairs whose correspondence is established
    without reference to position."""
    t_seq, r_seq = _leaf_sequence(truth), _leaf_sequence(recovered)
    t_count, r_count = Counter(t_seq), Counter(r_seq)
    anchors = [s for s in t_seq if t_count[s] == 1 and r_count.get(s) == 1]
    if len(anchors) < 2:
        return OrderScore(tau=None, exact=None, n_anchors=len(anchors))
    r_pos = {s: i for i, s in enumerate(r_seq)}
    # anchors are already in GT order; their recovered ranks form the
    # permutation whose disorder we measure
    ranks = [r_pos[s] for s in anchors]
    tau = _kendall_tau(ranks)
    return OrderScore(tau=tau, exact=(ranks == sorted(ranks)),
                      n_anchors=len(anchors))


# ── coverage: how much of the text layer survived, ground-truth-free ───────

@dataclass
class CoverageScore:
    """A three-way decomposition of the PDF text layer.

    coverage + excluded_rate + furniture_rate + unaccounted_rate = 1.

    `unaccounted_rate` is the number that matters: content the pipeline neither
    emitted, nor excluded by policy, nor stored as an asset. It is the only
    bucket that represents a defect, and it is the one to drive toward zero.
    A bare `coverage` figure hides it behind deliberate exclusions."""
    coverage: float          # present in the emitted markdown
    excluded_rate: float     # excluded by policy (bibliography)
    asset_rate: float        # captured in asset records, not body text
    furniture_rate: float    # running heads, page numbers, marginalia
    unaccounted_rate: float  # neither emitted nor accounted for — the defect
    n_pdf_chars: int
    n_missing_chars: int

    def row(self) -> dict:
        return {"coverage": round(self.coverage, 3),
                "excluded_rate": round(self.excluded_rate, 3),
                "asset_rate": round(self.asset_rate, 3),
                "furniture_rate": round(self.furniture_rate, 3),
                "unaccounted_rate": round(self.unaccounted_rate, 3),
                "cov_pdf_chars": self.n_pdf_chars,
                "cov_missing_chars": self.n_missing_chars}


def _char_bag(text: str) -> Counter:
    """Multiset of word tokens, lower-cased.  Character counts are recovered
    by weighting each token by its length, which is what makes the headline
    number a *character* share while staying robust to reflow, hyphenation
    differences and whitespace normalisation."""
    return Counter(_WORD.findall(text.lower()))


def _weighted_total(bag: Counter) -> int:
    return sum(len(w) * c for w, c in bag.items())


def coverage(pdf_text: str, markdown: str, furniture_text: str = "",
             excluded_text: str = "", asset_text: str = "") -> CoverageScore:
    """Decompose the PDF text layer into recovered / excluded / asset /
    furniture / unaccounted.

    Overlap is multiset intersection over word tokens, weighted by token
    length, so a word appearing three times in the PDF and once in the output
    is charged for the two missing occurrences.

    The three accounting buckets are measured against what the markdown did NOT
    recover, so a passage that appears both in the body and in a caption counts
    once, as recovered."""
    pdf_bag = _char_bag(pdf_text)
    md_bag = _char_bag(markdown)
    total = _weighted_total(pdf_bag)
    if not total:
        return CoverageScore(1.0, 0.0, 0.0, 0.0, 0.0, 0, 0)
    overlap = _weighted_total(pdf_bag & md_bag)
    missing = pdf_bag - md_bag          # what the markdown failed to carry

    def share(text: str, pool: Counter) -> tuple[float, Counter]:
        if not text:
            return 0.0, pool
        hit = pool & _char_bag(text)
        return _weighted_total(hit) / total, pool - hit

    excl, missing = share(excluded_text, missing)
    asset, missing = share(asset_text, missing)
    furn, missing = share(furniture_text, missing)
    unaccounted = _weighted_total(missing) / total
    return CoverageScore(coverage=overlap / total, excluded_rate=excl,
                         asset_rate=asset, furniture_rate=furn,
                         unaccounted_rate=unaccounted,
                         n_pdf_chars=total, n_missing_chars=total - overlap)


def furniture_text(blocks, pdf_path, ocr_scale: float = 2.0) -> str:
    """Text sitting in blocks the pipeline discards on purpose."""
    return labelled_text(blocks, pdf_path, FURNITURE_LABELS, ocr_scale)
