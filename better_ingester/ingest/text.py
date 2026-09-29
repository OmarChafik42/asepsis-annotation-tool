"""
ingest/text.py — body text, read from the PDF's own text layer.

The pipeline does not *recognise* body text. A born-digital PDF already
carries it, exactly as the author typeset it, and reading it costs about a
millisecond per block against the tens of seconds a vision-language model
would spend generating it back. This is the single decision behind the
speed claim in §sec:speed.

`block_text` returning "" is the seam where an OCR fallback for scanned
documents plugs in; nothing else in the pipeline needs to change for that.
"""

from __future__ import annotations

import re

from ingest.ocr import Block

# join a word broken across a line by hyphenation ("hyphen- ation")
_LINEBREAK_HYPHEN = re.compile(r"(\w)-\s(\w)")


class PageText:
    """Lazily-opened text layer for one PDF, cached per page.

    Every consumer that reads body text needs the same (textpage, height)
    pair per page, and opening one costs real time; this holds them so a
    document is walked once rather than once per caller.
    """

    def __init__(self, pdf_path, ocr_scale: float = 2.0):
        import pypdfium2 as pdfium  # type: ignore[import-untyped]

        self._doc = pdfium.PdfDocument(str(pdf_path)) if pdf_path else None
        self._pages: dict[int, tuple] = {}
        self.ocr_scale = ocr_scale

    def page(self, index: int) -> tuple:
        if index not in self._pages:
            pg = self._doc[index]
            self._pages[index] = (pg.get_textpage(), pg.get_height())
        return self._pages[index]

    def of(self, block: Block) -> str:
        """Text under one block's bounding box, or "" with no text layer."""
        if self._doc is None:
            return ""
        textpage, height = self.page(block.page)
        return block_text(block, textpage, height, self.ocr_scale)

    def whole_document(self) -> str:
        """Every page's text layer, concatenated — the coverage denominator."""
        if self._doc is None:
            return ""
        return "\n".join(self._doc[i].get_textpage().get_text_range()
                         for i in range(len(self._doc)))


def block_text(block: Block, textpage, page_height: float,
               ocr_scale: float = 2.0) -> str:
    """Text for one block from the PDF text layer.

    Block bboxes are in rendered-image pixels at `ocr_scale`, with y growing
    downward; PDF user space has y growing upward from the page bottom, so
    the box is scaled and flipped before the lookup.
    """
    s = 1.0 / ocr_scale
    x0, y0, x1, y1 = block.bbox
    txt = textpage.get_text_bounded(
        left=x0 * s, bottom=page_height - y1 * s,
        right=x1 * s, top=page_height - y0 * s)
    txt = txt.replace("\x02", "").replace("\xad", "")   # discretionary/soft hyphens
    txt = " ".join(txt.split())
    return _LINEBREAK_HYPHEN.sub(r"\1\2", txt)


def labelled_text(blocks: list[Block], pdf_path, labels,
                  ocr_scale: float = 2.0) -> str:
    """Text sitting in blocks carrying any of `labels`.

    The coverage decomposition is built from this: each accounting bucket is
    just a label set, so "what the pipeline dropped on purpose" is stated as
    data rather than reimplemented as logic.
    """
    pages = PageText(pdf_path, ocr_scale)
    return "\n".join(pages.of(b) for b in blocks if b.label in labels)
