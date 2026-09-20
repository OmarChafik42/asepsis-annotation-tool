from __future__ import annotations

import os
import threading
import uuid
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image


# PDFium must not be called concurrently from multiple threads.
_pdfium_lock = threading.Lock()

# Prevent duplicate work when the same output page is requested twice.
_render_locks: dict[str, threading.Lock] = {}
_render_locks_guard = threading.Lock()


def _render_lock(path: Path) -> threading.Lock:
    key = str(path.resolve())
    with _render_locks_guard:
        return _render_locks.setdefault(key, threading.Lock())


def _is_valid_png(path: Path) -> bool:
    """Return True only for a readable, non-empty PNG with valid dimensions."""
    try:
        if not path.is_file():
            return False

        if path.stat().st_size < 128:
            return False

        with Image.open(path) as image:
            if image.format != "PNG":
                return False

            width, height = image.size
            if width <= 0 or height <= 0:
                return False

            image.verify()

        return True
    except (OSError, SyntaxError, ValueError):
        return False


def _remove_invalid_cache(path: Path) -> None:
    try:
        path.unlink(missing_ok=True)
    except OSError:
        pass


def render_page(
    pdf_path: Path,
    cache_dir: Path,
    page_index: int,
    scale: float = 1.6,
) -> Path:
    """
    Render one PDF page to a PNG cache safely.

    Guarantees:
    - valid cached PNGs are reused;
    - corrupt/truncated cached PNGs are regenerated;
    - duplicate requests for the same output do not render twice;
    - PDFium access is serialized because PDFium is not thread-safe;
    - temporary filenames stay deliberately short for Windows MAX_PATH;
    - cache replacement is atomic.
    """
    pdf_path = Path(pdf_path)
    cache_dir = Path(cache_dir)

    if not pdf_path.is_file():
        raise FileNotFoundError(f"Source PDF not found: {pdf_path}")

    cache_dir.mkdir(parents=True, exist_ok=True)

    tag = str(scale).replace(".", "_")
    out = cache_dir / f"page-{page_index}-{tag}.png"

    # Fast path.
    if _is_valid_png(out):
        return out

    with _render_lock(out):
        # Another request may have completed while this request waited.
        if _is_valid_png(out):
            return out

        if out.exists():
            _remove_invalid_cache(out)

        # IMPORTANT:
        # Keep this filename short. The user's dataset/session path is already
        # close to Windows' traditional MAX_PATH limit. Appending the complete
        # output filename plus a 32-character UUID can push the full path above
        # 260 characters and PIL then raises FileNotFoundError even though the
        # directory exists.
        tmp = cache_dir / f".{uuid.uuid4().hex[:8]}.tmp"

        try:
            with _pdfium_lock:
                doc = pdfium.PdfDocument(str(pdf_path))
                try:
                    page_count = len(doc)
                    if page_index < 0 or page_index >= page_count:
                        raise IndexError(
                            f"Page index {page_index} is outside PDF range "
                            f"0..{page_count - 1}"
                        )

                    page = doc[page_index]
                    try:
                        image = page.render(scale=scale).to_pil()
                        image.save(
                            tmp,
                            format="PNG",
                            compress_level=3,
                            optimize=False,
                        )
                    finally:
                        page.close()
                finally:
                    doc.close()

            if not _is_valid_png(tmp):
                raise RuntimeError(
                    f"Rendered page {page_index} did not produce a valid PNG: {tmp}"
                )

            # Same-directory replace is atomic.
            os.replace(tmp, out)

            if not _is_valid_png(out):
                _remove_invalid_cache(out)
                raise RuntimeError(
                    f"Cached page {page_index} failed PNG validation after write: {out}"
                )

            return out
        finally:
            tmp.unlink(missing_ok=True)
