# Run: python3 -m pytest tests/test_tree.py -v
from __future__ import annotations

from bench.tree import Node, normalise_title, score


def n(title, *kids):
    return Node(title=title, children=list(kids))


# ── normalise_title: the two eval-schema artifacts ────────────────────────────

class TestNormaliseTitle:
    def test_plain(self):
        assert normalise_title("Introduction") == "introduction"

    def test_markdown_bold(self):
        assert normalise_title("**Motivation**") == "motivation"

    def test_roman_numbering(self):
        assert normalise_title("I. INTRODUCTION") == normalise_title("Introduction")

    def test_letter_numbering(self):
        assert normalise_title("A. Related research") == "related research"

    def test_paren_digit(self):
        assert normalise_title("1) Load forecasting") == "load forecasting"

    def test_article_not_stripped(self):
        assert normalise_title("A problem statement") == "a problem statement"


# ── scoring ───────────────────────────────────────────────────────────────────

class TestScore:
    def test_perfect(self):
        t = n("Doc", n("A", n("A1")), n("B"))
        s = score(t, n("Doc", n("A", n("A1")), n("B")))
        assert s.title_f1 == 1.0 and s.edge_f1 == 1.0

    def test_numbering_ignored(self):
        truth = n("Doc", n("Introduction"), n("Methods"))
        recov = n("Doc", n("I. INTRODUCTION"), n("II. METHODS"))
        assert score(truth, recov).title_f1 == 1.0
        assert score(truth, recov).edge_f1 == 1.0

    def test_missing_section_drops_recall(self):
        truth = n("Doc", n("A"), n("B"), n("C"))
        s = score(truth, n("Doc", n("A"), n("B")))
        assert s.title_r < 1.0 and s.title_p == 1.0

    def test_wrong_nesting_drops_edge_f1(self):
        truth = n("Doc", n("A", n("A1")))
        flat = n("Doc", n("A"), n("A1"))     # A1 reparented to top level
        s = score(truth, flat)
        assert s.title_f1 == 1.0             # same headings present
        assert s.edge_f1 < 1.0              # but nesting differs

    def test_counts(self):
        s = score(n("D", n("A")), n("D", n("A"), n("B")))
        assert s.n_truth == 1 and s.n_recovered == 2
