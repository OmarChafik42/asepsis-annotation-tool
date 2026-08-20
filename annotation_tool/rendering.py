from __future__ import annotations

from pathlib import Path

import pypdfium2 as pdfium


def render_page(pdf_path: Path, cache_dir: Path, page_index: int, scale: float = 1.6) -> Path:
    cache_dir.mkdir(parents=True, exist_ok=True)
    tag = str(scale).replace(".", "_")
    out = cache_dir / f"page-{page_index}-{tag}.png"
    if out.exists():
        return out
    doc = pdfium.PdfDocument(str(pdf_path))
    try:
        if page_index < 0 or page_index >= len(doc):
            raise IndexError(page_index)
        page = doc[page_index]
        image = page.render(scale=scale).to_pil()
        image.save(out, format="PNG")
    finally:
        doc.close()
    return out
