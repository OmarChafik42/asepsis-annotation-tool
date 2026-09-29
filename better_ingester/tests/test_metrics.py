"""Tests for the metrics added in the 1(a) harness.

Each test pins a property the metric exists to have — not just a golden value —
because the failure modes here are subtle: a matcher that imposes the ordering
it claims to measure, or a mean that silently averages in undefined documents.
"""
import pytest

from bench.metrics import (content_words, coverage, depth_accuracy,
                           reading_order, structure_ceiling)
from bench.tree import Node, score


def tree(spec):
    """('A', [('B', []), ...]) -> Node"""
    title, kids = spec
    return Node(title=title, children=[tree(k) for k in kids])


def leaves(root, titles):
    for t in titles:
        root.children.append(Node(title=t, kind="content", content=f"body of {t}"))
    return root


# ── depth accuracy ─────────────────────────────────────────────────────────

def test_depth_accuracy_perfect_when_identical():
    t = tree(("doc", [("A", [("A1", [])]), ("B", [])]))
    d = depth_accuracy(t, tree(("doc", [("A", [("A1", [])]), ("B", [])])))
    assert d.accuracy == 1.0 and d.n_matched == 3


def test_depth_accuracy_penalises_wrong_depth_only():
    """A1 detected but hoisted to top level: detected 3/3, one at wrong depth."""
    truth = tree(("doc", [("A", [("A1", [])]), ("B", [])]))
    rec = tree(("doc", [("A", []), ("A1", []), ("B", [])]))
    d = depth_accuracy(truth, rec)
    assert d.n_matched == 3
    assert d.n_correct == 2
    assert d.accuracy == pytest.approx(2 / 3)


def test_depth_accuracy_ignores_undetected_headings():
    """Missed headings are title_f1's business, not levelling's."""
    truth = tree(("doc", [("A", []), ("B", []), ("C", [])]))
    rec = tree(("doc", [("A", [])]))
    d = depth_accuracy(truth, rec)
    assert d.n_matched == 1 and d.accuracy == 1.0 and d.n_truth == 3


def test_depth_accuracy_empty_recovered_is_zero_not_crash():
    d = depth_accuracy(tree(("doc", [("A", [])])), tree(("doc", [])))
    assert d.accuracy == 0.0 and d.n_matched == 0


# ── reading order ──────────────────────────────────────────────────────────

def test_reading_order_identity_is_tau_one():
    gt = leaves(Node(title="doc"), ["intro", "method", "results"])
    rec = leaves(Node(title="doc"), ["intro", "method", "results"])
    o = reading_order(gt, rec)
    assert o.tau == pytest.approx(1.0) and o.exact is True


def test_reading_order_detects_swapped_columns():
    """The two-column failure: content comes back out of order."""
    gt = leaves(Node(title="doc"), ["a", "b", "c", "d"])
    rec = leaves(Node(title="doc"), ["b", "a", "d", "c"])
    o = reading_order(gt, rec)
    assert o.tau < 1.0 and o.exact is False


def test_reading_order_full_reversal_is_tau_minus_one():
    gt = leaves(Node(title="doc"), ["a", "b", "c", "d"])
    rec = leaves(Node(title="doc"), ["d", "c", "b", "a"])
    assert reading_order(gt, rec).tau == pytest.approx(-1.0)


def test_reading_order_anchors_must_be_unique_both_sides():
    """Load-bearing: matching by consuming a queue in document order would
    impose the ordering being measured and return tau=1 by construction. Only
    titles unique on BOTH sides may anchor."""
    gt = leaves(Node(title="doc"), ["dup", "x", "dup", "y"])
    rec = leaves(Node(title="doc"), ["dup", "y", "dup", "x"])
    o = reading_order(gt, rec)
    assert o.n_anchors == 2               # x and y only; 'dup' excluded
    assert o.tau == pytest.approx(-1.0)   # x,y are genuinely inverted


def test_reading_order_undefined_below_two_anchors():
    gt = leaves(Node(title="doc"), ["only"])
    rec = leaves(Node(title="doc"), ["only"])
    o = reading_order(gt, rec)
    assert o.tau is None and o.exact is None


# ── coverage ───────────────────────────────────────────────────────────────

def test_coverage_full_when_markdown_has_everything():
    txt = "alpha beta gamma delta"
    c = coverage(txt, "# heading\n\nalpha beta gamma delta")
    assert c.coverage == pytest.approx(1.0) and c.n_missing_chars == 0


def test_coverage_counts_missing_by_characters_not_words():
    """A long dropped word costs more than a short one — the metric is a
    character share, so it must be length-weighted."""
    short = coverage("keep abc", "keep")
    long_ = coverage("keep abcdefghijkl", "keep")
    assert long_.coverage < short.coverage


def test_coverage_charges_repeated_occurrences():
    c = coverage("word word word", "word")
    assert c.coverage == pytest.approx(1 / 3)


def test_coverage_furniture_is_reported_not_silently_forgiven():
    c = coverage("body running head", "body", furniture_text="running head")
    assert c.coverage < 1.0
    assert c.furniture_rate > 0.0


def test_coverage_empty_pdf_layer_is_one_not_division_error():
    assert coverage("", "anything").coverage == 1.0


def test_content_words_shared_definition():
    assert content_words("The cat42 a is on x9") == {"the", "cat42"}


# ── coverage decomposition ─────────────────────────────────────────────────

def test_decomposition_is_exhaustive():
    """coverage + excluded + asset + furniture + unaccounted == 1, always.
    If the buckets do not sum, some content is being counted twice or lost from
    the accounting, and the 'unaccounted' figure stops meaning anything."""
    c = coverage("alpha beta gamma delta epsilon zeta",
                 "alpha beta", excluded_text="gamma",
                 asset_text="delta", furniture_text="epsilon")
    total = (c.coverage + c.excluded_rate + c.asset_rate
             + c.furniture_rate + c.unaccounted_rate)
    assert total == pytest.approx(1.0)
    assert c.unaccounted_rate > 0        # 'zeta' is unaccounted for


def test_buckets_do_not_double_count_recovered_content():
    """A passage present in both the body and a caption is recovered once, not
    recovered *and* charged to the asset bucket."""
    c = coverage("alpha beta", "alpha beta", asset_text="alpha beta")
    assert c.coverage == pytest.approx(1.0)
    assert c.asset_rate == pytest.approx(0.0)


def test_buckets_are_claimed_in_priority_order():
    """One missing token is claimed by exactly one bucket."""
    c = coverage("alpha lost", "alpha", excluded_text="lost", asset_text="lost")
    assert c.excluded_rate > 0 and c.asset_rate == pytest.approx(0.0)


def test_unaccounted_is_everything_nobody_claimed():
    c = coverage("alpha orphan", "alpha")
    assert c.unaccounted_rate == pytest.approx(c.n_missing_chars / c.n_pdf_chars)


# ── the structural ceiling ─────────────────────────────────────────────────

class TestStructureCeiling:
    def test_missing_parent_contracts_children_upward(self):
        gt = Node("D", [Node("A", [Node("A1"), Node("A2")]), Node("B")])
        found = Node("D", [Node("A1"), Node("B")])        # "A" was never detected
        c = structure_ceiling(gt, found)
        assert [n.title for n in c.children] == ["A1", "B"]

    def test_detected_headings_take_their_ground_truth_nesting(self):
        gt = Node("D", [Node("A", [Node("A1")]), Node("B")])
        found = Node("D", [Node("A1"), Node("A"), Node("B")])   # all found, misnested
        c = structure_ceiling(gt, found)
        assert score(gt, c).edge_f1 == 1.0

    def test_spurious_headings_are_dropped(self):
        """A heading absent from ground truth cannot make a matching edge
        under any arrangement, so the bound ignores it."""
        gt = Node("D", [Node("A")])
        found = Node("D", [Node("A"), Node("Invented")])
        assert [n.title for n in structure_ceiling(gt, found).children] == ["A"]

    def test_is_an_upper_bound_on_nesting(self):
        gt = Node("D", [Node("A", [Node("A1"), Node("A2")]), Node("B", [Node("B1")])])
        found = Node("D", [Node("A1"), Node("A", [Node("B1")]), Node("A2")])
        assert (score(gt, structure_ceiling(gt, found)).edge_f1
                >= score(gt, found).edge_f1)

    def test_perfect_recovery_gives_a_ceiling_of_one(self):
        gt = Node("D", [Node("A", [Node("A1")]), Node("B")])
        assert score(gt, structure_ceiling(gt, gt)).edge_f1 == 1.0

    def test_repeated_titles_are_consumed_not_duplicated(self):
        gt = Node("D", [Node("A", [Node("Notes")]), Node("B", [Node("Notes")])])
        found = Node("D", [Node("Notes")])           # only one of the two found
        c = structure_ceiling(gt, found)
        assert [n.title for n in c.all_nodes()[1:]] == ["Notes"]
