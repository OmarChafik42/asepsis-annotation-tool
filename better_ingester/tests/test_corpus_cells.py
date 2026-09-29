"""Tests for cell assignment: source pre-filter + render verification.

Cell assignment is what the whole stratification rests on, and it was measurably
wrong before these cases existed — 7 of 47 documents (15%) on the pilot corpus.
"""
from pathlib import Path

import pytest

from bench.layout_verify import verify
from tools.corpus import classify

CORPUS = Path(__file__).resolve().parents[1] / "corpus"


def _doc_dirs():
    """corpus/ is grouped by stratification cell (plus _pilot and _surplus);
    a directory is a document iff it directly contains a .tex."""
    for sub in sorted(p for p in CORPUS.iterdir() if p.is_dir()):
        if any(sub.glob("*.tex")):
            yield sub
        else:
            yield from (d for d in sorted(sub.iterdir())
                        if d.is_dir() and any(d.glob("*.tex")))


def pdfs():
    for sub in _doc_dirs():
        tex = next(iter(sorted(sub.glob("*.tex"))), None)
        if not tex:
            continue
        pdf = sub / f"{tex.stem}.pdf"
        if pdf.exists():
            yield sub.name, tex, pdf


# ── source pre-filter ──────────────────────────────────────────────────────

def test_commented_out_documentclass_is_ignored():
    """A regression: the A&A template ships four commented \\documentclass
    lines above the real one, and the first match won."""
    src = ("%\\documentclass[referee]{aa}\n"
           "%\\documentclass[onecolumn]{aa}\n"
           "\\documentclass{article}\n\\section{A}\n")
    assert classify(src)[2] == "article"


def test_twocolumn_command_in_body_is_detected():
    src = "\\documentclass{article}\n\\begin{document}\n\\twocolumn\n\\section{A}\n"
    assert classify(src)[0] == "two"


def test_multicols_environment_is_detected():
    src = ("\\documentclass{article}\n\\begin{document}\n"
           "\\begin{multicols}{2}\n\\section{A}\n")
    assert classify(src)[0] == "two"


def test_revtex_reprint_is_two_column():
    assert classify("\\documentclass[prl,reprint]{revtex4-1}\n\\section{A}")[0] == "two"


def test_two_column_by_default_classes():
    for cls in ("aa", "IEEEtran", "emulateapj", "mnras"):
        assert classify(f"\\documentclass{{{cls}}}\n\\section{{A}}")[0] == "two", cls


def test_explicit_onecolumn_overrides_class_default():
    """IEEEtran is two-column by default; [onecolumn] is the real single_roman
    cell, not a misclassification."""
    col, num, _ = classify("\\documentclass[onecolumn]{IEEEtran}\n\\section{A}")
    assert (col, num) == ("single", "roman")


def test_starred_sections_read_as_unnumbered():
    src = "\\documentclass{article}\n" + "\\section*{X}\n" * 5
    assert classify(src)[1] == "unnumbered"


def test_secnumdepth_zero_reads_as_unnumbered():
    src = ("\\documentclass{article}\n\\setcounter{secnumdepth}{0}\n"
           + "\\section{X}\n" * 5)
    assert classify(src)[1] == "unnumbered"


def test_mostly_numbered_sections_are_not_unnumbered():
    src = "\\documentclass{article}\n" + "\\section{X}\n" * 5 + "\\section*{Refs}\n"
    assert classify(src)[1] == "arabic"


# ── render verification ────────────────────────────────────────────────────

@pytest.mark.parametrize("name", ["arxiv_2608.10584v2", "arxiv_2608.20830v1"])
def test_render_catches_two_column_the_source_misses(name):
    """Conference style files call \\twocolumn from a plain
    \\documentclass{article}; there is no bounded list of them, which is why
    the render is authoritative. Both documents here are recorded in the
    frozen manifest as columns_source=single, columns_render=two."""
    pdf = next((p for n, _, p in pdfs() if n == name), None)
    if pdf is None:
        pytest.skip(f"{name} not in corpus")
    assert verify(pdf).columns == "two"


def test_manifest_records_every_source_render_disagreement():
    """The render wins, but the disagreement is recorded rather than
    silently resolved — it is what makes the stratification auditable."""
    import json
    from pathlib import Path
    manifest = Path(__file__).resolve().parents[1] / "corpus_manifest.json"
    if not manifest.exists():
        pytest.skip("no frozen manifest")
    docs = json.loads(manifest.read_text())["documents"]
    for d in docs:
        assert d["columns"] == (d["columns_render"]
                                if d["columns_render"] in ("single", "two")
                                else d["columns_source"])
        assert d["cell"] == f"{d['columns']}_{d['numbering']}"


def test_verifier_reaches_a_verdict_on_nearly_every_document():
    verdicts = [verify(pdf).columns for _, _, pdf in pdfs()]
    if not verdicts:
        pytest.skip("no corpus")
    decided = sum(v in ("single", "two") for v in verdicts)
    assert decided / len(verdicts) >= 0.95


def test_span_ratio_separates_the_two_populations():
    """Single- and two-column documents must not overlap in span ratio, or the
    threshold is arbitrary."""
    single, two = [], []
    for _, _, pdf in pdfs():
        v = verify(pdf)
        (single if v.columns == "single" else two).append(v.span_ratio) \
            if v.columns in ("single", "two") else None
    if not (single and two):
        pytest.skip("need both populations")
    assert min(single) > max(two), (min(single), max(two))


def test_missing_text_layer_yields_unknown_not_a_guess(tmp_path):
    import pypdfium2 as pdfium
    p = tmp_path / "blank.pdf"
    doc = pdfium.PdfDocument.new()
    doc.new_page(300, 400)
    doc.save(str(p))
    assert verify(p).columns == "unknown"
