"""
ingest/order.py — reading order over layout blocks.

The one geometric decision the pipeline makes. A PDF's block list arrives in
whatever order the detector emitted; reading order is what turns it into a
document. Getting this wrong is the failure that opens the paper — section 2.1
emitted before section 2, and everything downstream corrupted at once — so it
lives in its own module with nothing else in it.
"""

from __future__ import annotations

from ingest.ocr import Block


def reading_order(blocks: list[Block]) -> list[Block]:
    """Sort blocks into reading order, column-aware (for 2-column layouts).

    Per page: a block is in the right column if its LEFT edge starts past the
    page midline (1-column blocks all start at the left margin, so they stay
    column 0). Within a column, top-to-bottom; left column before right.
    """
    by_page: dict[int, list[Block]] = {}
    for b in blocks:
        by_page.setdefault(b.page, []).append(b)

    ordered: list[Block] = []
    for page in sorted(by_page):
        pb = by_page[page]
        left = min(b.bbox[0] for b in pb)
        right = max(b.bbox[2] for b in pb)
        mid = (left + right) / 2
        ordered += sorted(pb, key=lambda b: (1 if b.bbox[0] > mid else 0, b.bbox[1]))
    return ordered


def heading_blocks(blocks: list[Block]) -> list[Block]:
    """The detected section headings, in reading order.

    Headings are identified by the detector's LABEL, never by their text —
    the choice the paper defends in §sec:pipeline. A caption the detector
    mislabels `paragraph_title` therefore shows up as an honest false
    positive rather than being filtered away by a text heuristic tuned on
    this corpus.
    """
    return [b for b in reading_order(blocks) if b.label == SECTION_TITLE]


SECTION_TITLE = "paragraph_title"


def doc_title(blocks: list[Block], default: str = "") -> str:
    """The document title from the first `doc_title` block, else `default`."""
    for b in blocks:
        if b.label == "doc_title" and b.text.strip():
            return b.text.strip()
    return default
