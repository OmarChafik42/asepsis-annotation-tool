from annotation_tool.domain import apply_event, build_command_event, build_undo_redo_event, replay
from annotation_tool.models import (
    AnnotationState, BBox, CommandRequest, DocumentInfo, PageInfo, PipelineInfo, Region
)


def state():
    return AnnotationState(
        document=DocumentInfo(
            document_id="doc-1", filename="x.pdf", pdf_sha256="abc", page_count=1,
            pages=[PageInfo(page_index=0, width=100, height=100)],
        ),
        pipeline=PipelineInfo(name="test"),
        regions=[Region(region_id="r1", source_region_id="s1", page=0,
                        bbox=BBox(x0=.1,y0=.1,x1=.4,y1=.3), type="figure")],
    )


def test_resize_replay():
    s = state()
    e = build_command_event(
        session_id="sess", annotator_id="a", sequence=1, state=s,
        command=CommandRequest(action="RESIZE_REGION", region_id="r1", payload={"bbox":{"x0":.1,"y0":.1,"x1":.5,"y1":.35}}),
    )
    after = apply_event(s, e)
    assert after.regions[0].bbox.x1 == .5
    assert replay(s, [e]).model_dump() == after.model_dump()


def test_undo_redo_are_replayable_mutations():
    s = state()
    e1 = build_command_event(
        session_id="sess", annotator_id="a", sequence=1, state=s,
        command=CommandRequest(action="RECLASSIFY_REGION", region_id="r1", payload={"type":"table"}),
    )
    s1 = apply_event(s, e1)
    undo = build_undo_redo_event(
        session_id="sess", annotator_id="a", sequence=2, state=s1, events=[e1], redo=False,
    )
    s2 = apply_event(s1, undo)
    assert s2.regions[0].type == "figure"
    redo = build_undo_redo_event(
        session_id="sess", annotator_id="a", sequence=3, state=s2, events=[e1, undo], redo=True,
    )
    s3 = apply_event(s2, redo)
    assert s3.regions[0].type == "table"
    assert replay(s, [e1, undo, redo]).model_dump() == s3.model_dump()


def test_create_delete_round_trip():
    s = state()
    create = build_command_event(
        session_id="sess", annotator_id="a", sequence=1, state=s,
        command=CommandRequest(action="CREATE_REGION", payload={"page":0,"bbox":{"x0":.5,"y0":.5,"x1":.7,"y1":.7},"type":"text"}),
    )
    s1 = apply_event(s, create)
    new_id = create.target_region_ids[0]
    delete = build_command_event(
        session_id="sess", annotator_id="a", sequence=2, state=s1,
        command=CommandRequest(action="DELETE_REGION", region_id=new_id),
    )
    s2 = apply_event(s1, delete)
    assert {r.region_id for r in s2.regions} == {"r1"}


def test_review_checklist_requires_all_items():
    import pytest
    from pydantic import ValidationError
    from annotation_tool.models import ReviewChecklist

    with pytest.raises(ValidationError):
        ReviewChecklist(reviewed_all_pages=True)

    checklist = ReviewChecklist(
        reviewed_all_pages=True,
        missing_spurious_regions_checked=True,
        boundaries_checked=True,
        types_checked=True,
        structure_checked=True,
        uncertainty_documented=True,
    )
    assert checklist.checklist_version == "1.0"
