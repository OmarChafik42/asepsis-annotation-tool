from pathlib import Path

from annotation_tool import adapters
from annotation_tool.models import PageInfo


def test_betteringest_adapter_normalizes_boxes(monkeypatch, tmp_path):
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"not-a-real-pdf")
    monkeypatch.setattr(adapters, "sha256_file", lambda _: "a" * 64)
    monkeypatch.setattr(adapters, "pdf_pages", lambda _: [PageInfo(page_index=0,width=612,height=792)])

    raw = {
        "stem":"x", "ocr_scale":2.0,
        "pages":[{"page_index":0,"width":1224,"height":1584}],
        "detected_assets":[{"type":"figure","page":0,"bbox":[122.4,158.4,612,792]}],
        "non_assets":[{"label":"paragraph_title","text":"Methods","page":0,"bbox":[100,100,500,180],"level":2,"scanned":False}],
    }
    state = adapters.adapt_machine_output(raw, pdf)
    assert state.document.page_count == 1
    assert len(state.regions) == 2
    fig = next(r for r in state.regions if r.type == "figure")
    assert abs(fig.bbox.x0 - .1) < 1e-9
    assert abs(fig.bbox.y0 - .1) < 1e-9
    heading = next(r for r in state.regions if r.type == "paragraph_title")
    assert heading.heading_level == 2
    assert heading.origin == "machine"


def test_mineru_adapter_maps_layout_dets(monkeypatch, tmp_path):
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"not-a-real-pdf")
    monkeypatch.setattr(adapters, "sha256_file", lambda _: "b" * 64)
    monkeypatch.setattr(
        adapters,
        "pdf_pages",
        lambda _: [
            PageInfo(page_index=0, width=612, height=792),
            PageInfo(page_index=1, width=612, height=792),
        ],
    )

    raw = [
        {
            "page_info": {"page_no": 0, "width": 1224, "height": 1584},
            "layout_dets": [
                {"cls_id": 12, "label": "header", "score": 0.9, "bbox": [122.4, 158.4, 612.0, 396.0], "index": 1},
                {
                    "cls_id": 21,
                    "label": "table",
                    "score": 0.85,
                    "bbox": [100, 500, 1100, 900],
                    "index": 2,
                    "html": "<table><tr><td>a</td></tr></table>",
                },
            ],
        },
        {
            "page_info": {"page_no": 1, "width": 1224, "height": 1584},
            "layout_dets": [
                {"cls_id": 22, "label": "ocr_text", "score": 0.5, "bbox": [61.2, 79.2, 306, 158.4], "index": 1},
            ],
        },
    ]
    state = adapters.adapt_machine_output(raw, pdf)
    assert state.pipeline.name == "MinerU"
    assert state.pipeline.adapter == "mineru-model-v1"
    assert state.document.page_count == 2
    assert len(state.regions) == 3
    header = next(r for r in state.regions if r.type == "header")
    # pixel coords normalized by page_info dims
    assert abs(header.bbox.x0 - 0.1) < 1e-9
    assert abs(header.bbox.y1 - 0.25) < 1e-9
    assert header.ocr_confidence == 0.9
    assert header.reading_order == 1
    assert header.origin == "machine"
    table = next(r for r in state.regions if r.type == "table")
    assert table.metadata["html"].startswith("<table>")
    # multi-page region on page 1 survives
    p1 = next(r for r in state.regions if r.page == 1)
    assert p1.type == "ocr_text"


def test_mineru_adapter_rejects_without_detections(monkeypatch, tmp_path):
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"not-a-real-pdf")
    monkeypatch.setattr(adapters, "sha256_file", lambda _: "c" * 64)
    monkeypatch.setattr(adapters, "pdf_pages", lambda _: [PageInfo(page_index=0, width=612, height=792)])

    import pytest

    raw = [{"page_info": {"page_no": 0, "width": 1224, "height": 1584}, "layout_dets": []}]
    with pytest.raises(ValueError, match="No regions"):
        adapters.adapt_machine_output(raw, pdf)
