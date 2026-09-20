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

# These commands cannot change the canonical region ordering. Keeping the existing
# list order avoids an O(n log n) sort after common edits such as changing H2 -> H3.
_ORDER_STABLE_ACTIONS = {
    "RECLASSIFY_REGION",
    "UPDATE_TEXT",
    "CHANGE_HEADING_LEVEL",
    "IGNORE_REGION",
    "RESTORE_REGION",
    "MARK_UNCERTAIN",
    "ADD_NOTE",
}


def _state_map(state: AnnotationState) -> dict[str, Region]:
    # Regions are treated immutably by this module. Do not deep-copy every region
    # merely to look one up; copy only the region(s) captured into an event.
    return {r.region_id: r for r in state.regions}


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


def apply_patch(
    state: AnnotationState,
    patch_before: StatePatch | None,
    patch_after: StatePatch | None,
    *,
    resort: bool = True,
) -> AnnotationState:
    """Apply a complete-region snapshot patch without copying the whole document state.

    Event patches contain validated Region models. We therefore copy only changed
    regions and reuse unchanged Region objects. This preserves the event-sourced
    semantics while making single-region edits much cheaper on large documents.
    """
    before = patch_before.regions if patch_before else []
    after = patch_after.regions if patch_after else []
    affected = {r.region_id for r in before} | {r.region_id for r in after}

    after_ids = [r.region_id for r in after]
    if len(after_ids) != len(set(after_ids)):
        raise ValueError("Patch contains duplicate region_id values")

    existing_unaffected = {r.region_id for r in state.regions if r.region_id not in affected}
    collisions = existing_unaffected & set(after_ids)
    if collisions:
        raise ValueError(f"Patch would create duplicate region(s): {', '.join(sorted(collisions))}")

    for region in after:
        if region.page >= state.document.page_count:
            raise ValueError(f"region {region.region_id} references invalid page {region.page}")

    replacement = {r.region_id: r.model_copy(deep=True) for r in after}
    new_regions: list[Region] = []
    inserted: set[str] = set()

    # Preserve list position for order-stable edits. For deletes/replacements we
    # substitute the after snapshot at the first affected position.
    for region in state.regions:
        rid = region.region_id
        if rid not in affected:
            new_regions.append(region)
            continue
        if rid in replacement and rid not in inserted:
            new_regions.append(replacement[rid])
            inserted.add(rid)

    # CREATE/SPLIT/MERGE may introduce IDs not present in the prior state.
    for region in after:
        if region.region_id not in inserted:
            new_regions.append(replacement[region.region_id])
            inserted.add(region.region_id)

    if resort:
        new_regions = _sorted_regions(new_regions)

    # model_copy(update=...) avoids serialising and revalidating thousands of
    # unchanged regions. All newly introduced regions were already validated.
    return state.model_copy(
        update={
            "regions": new_regions,
            "state_revision": state.state_revision + 1,
        },
        deep=False,
    )


def apply_event(state: AnnotationState, event: AnnotationEvent) -> AnnotationState:
    if not event.mutates_state:
        # Non-mutating interactions (VIEW_PAGE, SELECT_REGION, etc.) do not need
        # a deep copy of the entire annotation state during replay.
        return state
    return apply_patch(
        state,
        event.before,
        event.after,
        resort=event.action not in _ORDER_STABLE_ACTIONS,
    )


def replay(initial: AnnotationState, events: list[AnnotationEvent]) -> AnnotationState:
    state = initial.model_copy(deep=True)
    # Files are normally already in sequence order, but sorting keeps replay robust
    # to callers that provide an unsorted list.
    for event in sorted(events, key=lambda e: e.sequence):
        state = apply_event(state, event)
    return state


def _snapshot(state: AnnotationState, ids: Iterable[str]) -> list[Region]:
    m = _state_map(state)
    ids = list(ids)
    missing = [rid for rid in ids if rid not in m]
    if missing:
        raise ValueError(f"Unknown region(s): {', '.join(missing)}")
    return [m[rid].model_copy(deep=True) for rid in ids]


def _replace_fields(region: Region, **changes) -> Region:
    data = region.model_dump()
    data.update(changes)
    return Region.model_validate(data)


def _assert_new_ids_available(state: AnnotationState, new_ids: Iterable[str], replaced_ids: Iterable[str] = ()) -> None:
    replaced = set(replaced_ids)
    existing = {r.region_id for r in state.regions if r.region_id not in replaced}
    new_ids = list(new_ids)
    if len(new_ids) != len(set(new_ids)):
        raise ValueError("Replacement regions must have unique region_id values")
    collisions = existing & set(new_ids)
    if collisions:
        raise ValueError(f"region_id already exists: {', '.join(sorted(collisions))}")


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
        if page < 0 or page >= state.document.page_count:
            raise ValueError("Invalid page")
        _assert_new_ids_available(state, [rid])
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
        new_ids: list[str] = []
        for spec in specs:
            rid = str(spec.get("region_id") or uuid.uuid4())
            new_ids.append(rid)
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
        _assert_new_ids_available(state, new_ids, replaced_ids=[source.region_id])
        target_ids = [source.region_id] + new_ids

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
        _assert_new_ids_available(state, [rid], replaced_ids=ids)
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
            reading_order=p.get(
                "reading_order",
                min((r.reading_order for r in before_regions if r.reading_order is not None), default=None),
            ),
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
    *,
    session_id: str,
    annotator_id: str,
    sequence: int,
    action: str,
    page: int | None = None,
    region_id: str | None = None,
    metadata: dict | None = None,
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
    *,
    session_id: str,
    annotator_id: str,
    sequence: int,
    state: AnnotationState,
    events: list[AnnotationEvent],
    redo: bool = False,
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
    current = [current_map[rid].model_copy(deep=True) for rid in affected if rid in current_map]
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
