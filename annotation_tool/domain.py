from __future__ import annotations

import copy
import uuid
from typing import Iterable

from .models import AnnotationEvent, AnnotationState, BBox, CommandRequest, Region, StatePatch, utc_now_iso

MUTATING_ACTIONS = {
    "CREATE_REGION",
    "DELETE_REGION",
    "MOVE_REGION",
    "RESIZE_REGION",
    "RECLASSIFY_REGION",
    "UPDATE_TEXT",
    "CHANGE_HEADING_LEVEL",
    "CHANGE_READING_ORDER",
    "IGNORE_REGION",
    "RESTORE_REGION",
    "MARK_UNCERTAIN",
    "ADD_NOTE",
    "SPLIT_REGION",
    "MERGE_REGIONS",
    "UNDO",
    "REDO",
}

NON_MUTATING_ACTIONS = {
    "OPEN_SESSION",
    "VIEW_PAGE",
    "SELECT_REGION",
    "FINALISE_SESSION",
    "EXPORT_SESSION",
}


def _state_map(state: AnnotationState) -> dict[str, Region]:
    return {r.region_id: r.model_copy(deep=True) for r in state.regions}


def _sorted_regions(regions: Iterable[Region]) -> list[Region]:
    return sorted(
        regions,
        key=lambda r: (
            r.page,
            r.reading_order if r.reading_order is not None else 10**9,
            r.bbox.y0,
            r.bbox.x0,
            r.region_id,
        ),
    )


def apply_patch(state: AnnotationState, patch_before: StatePatch | None, patch_after: StatePatch | None) -> AnnotationState:
    """Apply a state patch by replacing the complete snapshots of its affected regions."""
    result = state.model_copy(deep=True)
    m = _state_map(result)
    before = patch_before.regions if patch_before else []
    after = patch_after.regions if patch_after else []
    affected = {r.region_id for r in before} | {r.region_id for r in after}
    for rid in affected:
        m.pop(rid, None)
    for region in after:
        m[region.region_id] = region.model_copy(deep=True)
    result.regions = _sorted_regions(m.values())
    result.state_revision += 1
    return AnnotationState.model_validate(result.model_dump())


def apply_event(state: AnnotationState, event: AnnotationEvent) -> AnnotationState:
    if not event.mutates_state:
        return state.model_copy(deep=True)
    return apply_patch(state, event.before, event.after)


def replay(initial: AnnotationState, events: list[AnnotationEvent]) -> AnnotationState:
    state = initial.model_copy(deep=True)
    for event in sorted(events, key=lambda e: e.sequence):
        state = apply_event(state, event)
    return state


def _snapshot(state: AnnotationState, ids: Iterable[str]) -> list[Region]:
    m = _state_map(state)
    missing = [rid for rid in ids if rid not in m]
    if missing:
        raise ValueError(f"Unknown region(s): {', '.join(missing)}")
    return [m[rid].model_copy(deep=True) for rid in ids]


def _replace_fields(region: Region, **changes) -> Region:
    data = region.model_dump()
    data.update(changes)
    return Region.model_validate(data)


def build_command_event(
    *,
    session_id: str,
    annotator_id: str,
    sequence: int,
    state: AnnotationState,
    command: CommandRequest,
) -> AnnotationEvent:
    action = command.action.upper().strip()
    if action not in MUTATING_ACTIONS - {"UNDO", "REDO"}:
        raise ValueError(f"Unsupported command action: {action}")

    before_regions: list[Region] = []
    after_regions: list[Region] = []
    target_ids: list[str] = []
    page = None

    if action == "CREATE_REGION":
        p = command.payload
        rid = str(p.get("region_id") or uuid.uuid4())
        bbox = BBox.model_validate(p["bbox"])
        page = int(p["page"])
        if page >= state.document.page_count:
            raise ValueError("Invalid page")
        if any(r.region_id == rid for r in state.regions):
            raise ValueError("region_id already exists")
        region = Region(
            region_id=rid,
            source_region_id=None,
            page=page,
            bbox=bbox,
            type=str(p.get("type", "text")),
            text=str(p.get("text", "")),
            reading_order=p.get("reading_order"),
            heading_level=p.get("heading_level"),
            origin="human",
            ignored=bool(p.get("ignored", False)),
            uncertain=bool(p.get("uncertain", False)),
            note=p.get("note"),
            metadata=dict(p.get("metadata") or {}),
        )
        after_regions = [region]
        target_ids = [rid]

    elif action == "DELETE_REGION":
        if not command.region_id:
            raise ValueError("region_id is required")
        before_regions = _snapshot(state, [command.region_id])
        target_ids = [command.region_id]
        page = before_regions[0].page

    elif action in {
        "MOVE_REGION",
        "RESIZE_REGION",
        "RECLASSIFY_REGION",
        "UPDATE_TEXT",
        "CHANGE_HEADING_LEVEL",
        "CHANGE_READING_ORDER",
        "IGNORE_REGION",
        "RESTORE_REGION",
        "MARK_UNCERTAIN",
        "ADD_NOTE",
    }:
        if not command.region_id:
            raise ValueError("region_id is required")
        before_regions = _snapshot(state, [command.region_id])
        old = before_regions[0]
        page = old.page
        p = command.payload

        if action in {"MOVE_REGION", "RESIZE_REGION"}:
            new = _replace_fields(old, bbox=BBox.model_validate(p["bbox"]))
        elif action == "RECLASSIFY_REGION":
            new = _replace_fields(old, type=str(p["type"]))
        elif action == "UPDATE_TEXT":
            new = _replace_fields(old, text=str(p.get("text", "")))
        elif action == "CHANGE_HEADING_LEVEL":
            level = p.get("heading_level")
            new = _replace_fields(old, heading_level=int(level) if level not in (None, "") else None)
        elif action == "CHANGE_READING_ORDER":
            order = p.get("reading_order")
            new = _replace_fields(old, reading_order=int(order) if order not in (None, "") else None)
        elif action == "IGNORE_REGION":
            new = _replace_fields(old, ignored=True)
        elif action == "RESTORE_REGION":
            new = _replace_fields(old, ignored=False)
        elif action == "MARK_UNCERTAIN":
            new = _replace_fields(old, uncertain=bool(p.get("uncertain", True)))
        elif action == "ADD_NOTE":
            note = p.get("note")
            new = _replace_fields(old, note=str(note) if note not in (None, "") else None)
        else:  # pragma: no cover
            raise AssertionError(action)

        after_regions = [new]
        target_ids = [old.region_id]

    elif action == "SPLIT_REGION":
        if not command.region_id:
            raise ValueError("region_id is required")
        before_regions = _snapshot(state, [command.region_id])
        source = before_regions[0]
        page = source.page
        specs = command.payload.get("regions")
        if not isinstance(specs, list) or len(specs) < 2:
            raise ValueError("SPLIT_REGION requires at least two replacement regions")
        for spec in specs:
            rid = str(spec.get("region_id") or uuid.uuid4())
            after_regions.append(
                Region(
                    region_id=rid,
                    source_region_id=source.region_id,
                    page=source.page,
                    bbox=BBox.model_validate(spec["bbox"]),
                    type=str(spec.get("type", source.type)),
                    text=str(spec.get("text", source.text)),
                    reading_order=spec.get("reading_order", source.reading_order),
                    heading_level=spec.get("heading_level", source.heading_level),
                    origin="human",
                    metadata={**source.metadata, "split_from": source.region_id},
                )
            )
        target_ids = [source.region_id] + [r.region_id for r in after_regions]

    elif action == "MERGE_REGIONS":
        ids = command.region_ids
        if len(ids) < 2:
            raise ValueError("MERGE_REGIONS requires at least two region_ids")
        before_regions = _snapshot(state, ids)
        pages = {r.page for r in before_regions}
        if len(pages) != 1:
            raise ValueError("Regions can only be merged within one page")
        page = next(iter(pages))
        p = command.payload
        rid = str(p.get("region_id") or uuid.uuid4())
        if "bbox" in p:
            bbox = BBox.model_validate(p["bbox"])
        else:
            bbox = BBox(
                x0=min(r.bbox.x0 for r in before_regions),
                y0=min(r.bbox.y0 for r in before_regions),
                x1=max(r.bbox.x1 for r in before_regions),
                y1=max(r.bbox.y1 for r in before_regions),
            )
        merged = Region(
            region_id=rid,
            source_region_id=None,
            page=page,
            bbox=bbox,
            type=str(p.get("type", before_regions[0].type)),
            text=str(p.get("text", "\n".join(r.text for r in before_regions if r.text))),
            reading_order=p.get("reading_order", min((r.reading_order for r in before_regions if r.reading_order is not None), default=None)),
            heading_level=p.get("heading_level"),
            origin="human",
            metadata={"merged_from": ids},
        )
        after_regions = [merged]
        target_ids = ids + [rid]

    return AnnotationEvent(
        event_id=str(uuid.uuid4()),
        session_id=session_id,
        sequence=sequence,
        timestamp_utc=utc_now_iso(),
        annotator_id=annotator_id,
        action=action,
        mutates_state=True,
        target_region_ids=target_ids,
        page=page,
        before=StatePatch(regions=before_regions),
        after=StatePatch(regions=after_regions),
        reason_code=command.reason_code,
        metadata=copy.deepcopy(command.metadata),
    )


def build_interaction_event(
    *, session_id: str, annotator_id: str, sequence: int, action: str,
    page: int | None = None, region_id: str | None = None, metadata: dict | None = None,
) -> AnnotationEvent:
    action = action.upper().strip()
    if action not in NON_MUTATING_ACTIONS:
        raise ValueError(f"Unsupported interaction action: {action}")
    return AnnotationEvent(
        event_id=str(uuid.uuid4()),
        session_id=session_id,
        sequence=sequence,
        timestamp_utc=utc_now_iso(),
        annotator_id=annotator_id,
        action=action,
        mutates_state=False,
        target_region_ids=[region_id] if region_id else [],
        page=page,
        metadata=metadata or {},
    )


def build_history_stacks(events: list[AnnotationEvent]) -> tuple[list[str], list[str]]:
    by_id = {e.event_id: e for e in events}
    undo_stack: list[str] = []
    redo_stack: list[str] = []
    for e in sorted(events, key=lambda x: x.sequence):
        if e.action == "UNDO" and e.target_event_id:
            if e.target_event_id in undo_stack:
                undo_stack.remove(e.target_event_id)
            redo_stack.append(e.target_event_id)
        elif e.action == "REDO" and e.target_event_id:
            if e.target_event_id in redo_stack:
                redo_stack.remove(e.target_event_id)
            undo_stack.append(e.target_event_id)
        elif e.mutates_state:
            undo_stack.append(e.event_id)
            redo_stack.clear()
    return undo_stack, redo_stack


def build_undo_redo_event(
    *, session_id: str, annotator_id: str, sequence: int, state: AnnotationState,
    events: list[AnnotationEvent], redo: bool = False,
) -> AnnotationEvent:
    undo_stack, redo_stack = build_history_stacks(events)
    stack = redo_stack if redo else undo_stack
    if not stack:
        raise ValueError("Nothing to redo" if redo else "Nothing to undo")
    target_id = stack[-1]
    target = next(e for e in events if e.event_id == target_id)
    desired = target.after if redo else target.before
    affected = set(target.target_region_ids)
    current_map = _state_map(state)
    current = [current_map[rid] for rid in affected if rid in current_map]
    return AnnotationEvent(
        event_id=str(uuid.uuid4()),
        session_id=session_id,
        sequence=sequence,
        timestamp_utc=utc_now_iso(),
        annotator_id=annotator_id,
        action="REDO" if redo else "UNDO",
        mutates_state=True,
        target_region_ids=list(target.target_region_ids),
        page=target.page,
        before=StatePatch(regions=current),
        after=desired.model_copy(deep=True) if desired else StatePatch(),
        target_event_id=target_id,
        metadata={"original_action": target.action},
    )
