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
