from pathlib import Path

from annotation_tool.domain import build_command_event
from annotation_tool.metrics import compute_metrics
from annotation_tool.models import AnnotationState, BBox, CommandRequest, DocumentInfo, PageInfo, PipelineInfo, Region
from annotation_tool.storage import SessionStore


def make_state():
    return AnnotationState(
        document=DocumentInfo(document_id="doc", filename="x.pdf", pdf_sha256="abc", page_count=1,
                              pages=[PageInfo(page_index=0,width=100,height=100)]),
        pipeline=PipelineInfo(name="test"),
        regions=[Region(region_id="r1", page=0, bbox=BBox(x0=.1,y0=.1,x1=.2,y1=.2), type="text")],
    )


def test_store_preserves_initial_event_and_final_separately(tmp_path):
    root = tmp_path / "sessions"
    store = SessionStore(root)
    pdf = tmp_path / "x.pdf"; pdf.write_bytes(b"pdf")
    raw_bytes = b'{"raw": true, "spacing": "preserved"}\n'
    meta = store.create_session(
        pdf_path=pdf, raw_machine_output={"raw": True}, raw_machine_bytes=raw_bytes,
        canonical_state=make_state(), annotator_id="a"
    )
    original_initial = (store.session_dir(meta.session_id)/"initial_state.json").read_text()
    state = store.load_working(meta.session_id)
    event = build_command_event(
        session_id=meta.session_id, annotator_id="a", sequence=1, state=state,
        command=CommandRequest(action="RECLASSIFY_REGION", region_id="r1", payload={"type":"table"}),
    )
    store.append_event(meta.session_id, event)
    assert (store.session_dir(meta.session_id)/"initial_state.json").read_text() == original_initial
    final, meta2 = store.finalise(meta.session_id)
    assert final.regions[0].type == "table"
    assert (store.session_dir(meta.session_id)/"machine_output.original.json").read_bytes() == raw_bytes
    assert (store.session_dir(meta.session_id)/"events.jsonl").exists()
    assert (store.session_dir(meta.session_id)/"final_state.json").exists()
    assert meta2.replay_valid is True


def test_metrics_separate_final_burden_from_interaction_effort(tmp_path):
    store = SessionStore(tmp_path / "sessions")
    pdf = tmp_path / "x.pdf"; pdf.write_bytes(b"pdf")
    meta = store.create_session(pdf_path=pdf, raw_machine_output={}, canonical_state=make_state(), annotator_id="a")
    state = store.load_working(meta.session_id)
    for seq, new_type in [(1,"table"),(2,"figure")]:
        event = build_command_event(
            session_id=meta.session_id, annotator_id="a", sequence=seq, state=state,
            command=CommandRequest(action="RECLASSIFY_REGION", region_id="r1", payload={"type":new_type}),
        )
        state = store.append_event(meta.session_id, event)
    m = compute_metrics(store.load_initial(meta.session_id), state, store.events(meta.session_id), store.load_meta(meta.session_id))
    assert m["interaction_effort"]["committed_edit_events"] == 2
    assert m["final_correction_burden"]["existing_regions_materially_changed"] == 1


def test_session_store_rejects_non_uuid_paths(tmp_path):
    import pytest
    store = SessionStore(tmp_path / "sessions")
    with pytest.raises(FileNotFoundError):
        store.session_dir("../escape")
