# Run: python3 -m pytest tests/test_latex.py -v
from __future__ import annotations

from tests.corpus_paths import doc_path

from pathlib import Path

import pytest

from bench.latex import clean_latex, parse_latex
from bench.tree import section_titles


def _tex(tmp_path, body, title="Doc"):
    p = tmp_path / "d.tex"
    p.write_text(f"\\title{{{title}}}\n\\begin{{document}}\n{body}\n\\end{{document}}\n")
    return p


# ── clean_latex ───────────────────────────────────────────────────────────────

class TestCleanLatex:
    def test_plain(self):
        assert clean_latex("Introduction") == "Introduction"

    def test_textbf(self):
        assert clean_latex(r"\textbf{Bold} title") == "Bold title"

    def test_cite_dropped(self):
        assert clean_latex(r"shown\cite{x} here") == "shown here"

    def test_math_dropped(self):
        assert clean_latex(r"area $x^2$ here") == "area here"

    def test_nested(self):
        assert clean_latex(r"\textbf{\emph{deep}}") == "deep"


# ── parse_latex ───────────────────────────────────────────────────────────────

class TestParseLatex:
    def test_title_is_root(self, tmp_path):
        t = parse_latex(_tex(tmp_path, r"\section{A}", title="My Paper"))
        assert t.title == "My Paper"

    def test_relative_levels(self, tmp_path):
        t = parse_latex(_tex(tmp_path, r"\section{S}\subsection{Sub}"))
        assert t.children[0].title == "S"
        assert t.children[0].children[0].title == "Sub"

    def test_starred_sections(self, tmp_path):
        t = parse_latex(_tex(tmp_path, r"\section*{A}\section*{B}"))
        assert [c.title for c in t.children] == ["A", "B"]

    def test_printbibliography_is_references(self, tmp_path):
        t = parse_latex(_tex(tmp_path, r"\section{A}\printbibliography"))
        assert "references" in [c.title.lower() for c in t.children]

    def test_comments_ignored(self, tmp_path):
        t = parse_latex(_tex(tmp_path, "% \\section{Ghost}\n\\section{Real}"))
        assert [c.title for c in t.children] == ["Real"]

    def test_real_corpus(self):
        """The ruler on real sources, asserted on invariants rather than on
        one document's headings: every frozen document must parse, produce
        headings, and normalise them."""
        from tests.corpus_paths import frozen_names
        seen = 0
        for name in frozen_names():
            p = Path(doc_path(name, ".tex"))
            if not p.exists():
                continue
            seen += 1
            t = parse_latex(p)
            titles = section_titles(t)
            assert titles, f"{name}: no headings recovered from the source"
            assert all(s == s.strip().lower() for s in titles), \
                f"{name}: a title escaped normalisation"
            assert t.title, f"{name}: no document title"
        if not seen:
            pytest.skip("no frozen corpus documents on disk")
        assert seen >= 10
