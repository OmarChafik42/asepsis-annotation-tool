from __future__ import annotations

import hashlib
import json
import uuid
from pathlib import Path
from typing import Any

import pypdfium2 as pdfium

from .models import AnnotationState, BBox, DocumentInfo, PageInfo, PipelineInfo, Region

ADAPTER_NAMESPACE = uuid.UUID("4ee36d0d-e606-48f3-977a-0d7684433cf8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pdf_pages(path: Path) -> list[PageInfo]:
    doc = pdfium.PdfDocument(str(path))
    pages: list[PageInfo] = []
    try:
        for idx, page in enumerate(doc):
            width, height = page.get_size()
            pages.append(PageInfo(page_index=idx, width=float(width), height=float(height)))
    finally:
        doc.close()
    return pages


def _doc_id(pdf_hash: str) -> str:
    return f"doc-{pdf_hash[:16]}"


def _stable_region_id(document_id: str, source_region_id: str) -> str:
    return str(uuid.uuid5(ADAPTER_NAMESPACE, f"{document_id}:{source_region_id}"))


def _normalize_bbox(raw_bbox: Any, width: float, height: float) -> BBox:
    if isinstance(raw_bbox, dict):
        if {"x0", "y0", "x1", "y1"}.issubset(raw_bbox):
            vals = [float(raw_bbox[k]) for k in ("x0", "y0", "x1", "y1")]
        elif {"x", "y", "width", "height"}.issubset(raw_bbox):
            x, y = float(raw_bbox["x"]), float(raw_bbox["y"])
            w, h = float(raw_bbox["width"]), float(raw_bbox["height"])
            vals = [x, y, x + w, y + h]
        else:
            raise ValueError("bbox dictionary must use x0/y0/x1/y1 or x/y/width/height")
    elif isinstance(raw_bbox, (list, tuple)) and len(raw_bbox) == 4:
        vals = [float(v) for v in raw_bbox]
    else:
        raise ValueError("bbox must have four coordinates")

    # Canonical files are normally already normalized. For imported machine output,
    # coordinates greater than 1 are interpreted in the supplied source page space.
    if max(vals) <= 1.000001 and min(vals) >= -0.000001:
        x0, y0, x1, y1 = vals
    else:
        x0, y0, x1, y1 = vals[0] / width, vals[1] / height, vals[2] / width, vals[3] / height

    eps = 1e-9
    x0 = min(max(x0, 0.0), 1.0 - eps)
    y0 = min(max(y0, 0.0), 1.0 - eps)
    x1 = min(max(x1, x0 + eps), 1.0)
    y1 = min(max(y1, y0 + eps), 1.0)
    return BBox(x0=x0, y0=y0, x1=x1, y1=y1)


def _canonical(raw: dict[str, Any], pdf_path: Path) -> AnnotationState:
    state = AnnotationState.model_validate(raw)
    actual_hash = sha256_file(pdf_path)
    if state.document.pdf_sha256 and state.document.pdf_sha256 != actual_hash:
        raise ValueError("PDF SHA-256 does not match canonical annotation package")
    return state


def _betteringest(raw: dict[str, Any], pdf_path: Path) -> AnnotationState:
    # prepare_layout_review can return either one document object or a list.
    if isinstance(raw, list):
        if len(raw) != 1:
            raise ValueError("This tool creates one annotation session at a time; provide one BetterIngest document")
        raw = raw[0]

    actual_hash = sha256_file(pdf_path)
    document_id = _doc_id(actual_hash)
    real_pages = pdf_pages(pdf_path)

    machine_pages = raw.get("pages") or []
    source_dims: dict[int, tuple[float, float]] = {}
    for p in machine_pages:
        idx = int(p.get("page_index", len(source_dims)))
        source_dims[idx] = (float(p["width"]), float(p["height"]))

    # If source dimensions are absent, use PDF point dimensions. BetterIngest output
    # normally includes rendered-image dimensions, so its pixel boxes normalize correctly.
    for p in real_pages:
        source_dims.setdefault(p.page_index, (p.width, p.height))

    regions: list[Region] = []
    ordinal = 0

    for idx, asset in enumerate(raw.get("detected_assets", [])):
        page = int(asset["page"])
        width, height = source_dims[page]
        source_id = f"asset:p{page}:i{idx}"
        regions.append(
            Region(
                region_id=_stable_region_id(document_id, source_id),
                source_region_id=source_id,
                page=page,
                bbox=_normalize_bbox(asset["bbox"], width, height),
                type=str(asset.get("type", "figure")),
                text=str(asset.get("text", "")),
                reading_order=ordinal,
                origin="machine",
                metadata={"source": "detected_assets", "name": asset.get("name")},
            )
        )
        ordinal += 1

    for idx, item in enumerate(raw.get("non_assets", [])):
        page = int(item["page"])
        width, height = source_dims[page]
        source_id = f"block:p{page}:i{idx}"
        label = str(item.get("label", "text"))
        level = item.get("level")
        regions.append(
            Region(
                region_id=_stable_region_id(document_id, source_id),
                source_region_id=source_id,
                page=page,
                bbox=_normalize_bbox(item["bbox"], width, height),
                type=label,
                text=str(item.get("text", "")),
                heading_level=int(level) if level not in (None, "") and label == "paragraph_title" else None,
                heading_level_source=item.get("heading_level_source"),
                heading_level_uncertain=bool(item.get("heading_level_uncertain", False)),
                uncertainty_reason=item.get("uncertainty_reason"),
                reading_order=ordinal,
                origin="machine",
                metadata={"source": "non_assets", "scanned": bool(item.get("scanned", False))},
            )
        )
        ordinal += 1

    if not regions:
        raise ValueError("No regions were found. Expected canonical 'regions' or BetterIngest detected_assets/non_assets")

    regions.sort(key=lambda r: (r.page, r.reading_order if r.reading_order is not None else 10**9))

    return AnnotationState(
        document=DocumentInfo(
            document_id=document_id,
            filename=pdf_path.name,
            pdf_sha256=actual_hash,
            page_count=len(real_pages),
            pages=real_pages,
        ),
        pipeline=PipelineInfo(
            name="BetterIngest",
            version=raw.get("pipeline_version"),
            ocr_engine=raw.get("ocr_engine", "PaddleOCR/PP-DocLayoutV3"),
            processed_at=raw.get("processed_at"),
            adapter="betteringest-layout-review-v1",
            metadata={"ocr_scale": raw.get("ocr_scale"), "stem": raw.get("stem")},
        ),
        regions=regions,
        metadata={"import_format": "betteringest-layout-review"},
    )


def adapt_machine_output(raw: Any, pdf_path: Path) -> AnnotationState:
    """Convert supported machine-output formats to the tool's stable canonical schema."""
    if isinstance(raw, dict) and "document" in raw and "regions" in raw:
        return _canonical(raw, pdf_path)
    if isinstance(raw, (dict, list)):
        return _betteringest(raw, pdf_path)
    raise ValueError("Unsupported annotation JSON format")
