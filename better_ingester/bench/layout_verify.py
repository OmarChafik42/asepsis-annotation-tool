"""
bench/layout_verify.py — verify a document's column count from the RENDER.

Cell assignment reads the LaTeX source (`\\documentclass` options), which is
fast and available before the PDF is fetched — but it is a claim about what the
author asked for, not about what came out. A `onecolumn` option can sit in a
commented-out line, be overridden by a later class option, or be ignored by the
class. Since the pipeline consumes the render, the render is what the
stratification has to be true of.

The discriminator is line spanning, not clustering: in a single-column layout
most body lines cross the page midline; in a two-column layout almost none do,
because each line terminates at the gutter. That holds regardless of margin
width, page size, or where the columns sit, which x-position clustering does
not.

Reads the PDF text layer only — no OCR, no models, milliseconds per document.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# A line must be at least this wide (as a fraction of the text block's width)
# to count as evidence either way; short lines — headings, the last line of a
# paragraph, equation labels — are uninformative and are ignored.
MIN_LINE_FRAC = 0.35
# Above SPAN_HI the document reads as single-column, below SPAN_LO as
# two-column. Between them the evidence is genuinely weak, and the verdict is
# "ambiguous" rather than a coin-flip dressed as a measurement — freeze surfaces
# those for a human look instead of silently assigning a cell.
SPAN_LO, SPAN_HI = 0.25, 0.40
MIN_INFORMATIVE = 20


@dataclass
class LayoutVerdict:
    columns: str            # "single" | "two" | "ambiguous" | "unknown"
    span_ratio: float       # share of informative lines crossing the midline
    n_lines: int
    n_pages: int

    def row(self) -> dict:
        return {"render_columns": self.columns,
                "span_ratio": round(self.span_ratio, 3),
                "n_lines": self.n_lines, "n_pages": self.n_pages}


def _page_lines(page) -> tuple[list[tuple[float, float]], float, float]:
    """(x0, x1) per text rect on the page, plus the page's own x-extent."""
    tp = page.get_textpage()
    n = tp.count_rects()
    rects = []
    for i in range(n):
        try:
            x0, _, x1, _ = tp.get_rect(i)
        except Exception:
            continue
        if x1 > x0:
            rects.append((x0, x1))
    if not rects:
        return [], 0.0, 0.0
    left = min(r[0] for r in rects)
    right = max(r[1] for r in rects)
    return rects, left, right


def verify(pdf_path: Path | str, max_pages: int = 8) -> LayoutVerdict:
    import pypdfium2 as pdfium  # type: ignore[import-untyped]

    doc = pdfium.PdfDocument(str(pdf_path))
    n_pages = len(doc)
    spanning = informative = 0
    for i in range(min(n_pages, max_pages)):
        try:
            rects, left, right = _page_lines(doc[i])
        except Exception:
            continue
        width = right - left
        if width <= 0 or not rects:
            continue
        mid = left + width / 2.0
        for x0, x1 in rects:
            if (x1 - x0) < MIN_LINE_FRAC * width:
                continue                       # too short to be evidence
            informative += 1
            if x0 < mid < x1:                  # the line crosses the midline
                spanning += 1
    if informative < MIN_INFORMATIVE:
        return LayoutVerdict("unknown", 0.0, informative, n_pages)
    ratio = spanning / informative
    if ratio >= SPAN_HI:
        col = "single"
    elif ratio < SPAN_LO:
        col = "two"
    else:
        col = "ambiguous"
    return LayoutVerdict(col, ratio, informative, n_pages)
