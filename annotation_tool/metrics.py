from __future__ import annotations

from collections import Counter
from typing import Any

from .domain import replay
from .models import AnnotationEvent, AnnotationState, SessionMeta


def _region_map(state: AnnotationState) -> dict:
    return {r.region_id: r for r in state.regions}


def compute_metrics(
    initial: AnnotationState,
    final: AnnotationState,
    events: list[AnnotationEvent],
    meta: SessionMeta,
) -> dict[str, Any]:
    """Compute the same public metrics as before with less intermediate allocation."""
    im = _region_map(initial)
    fm = _region_map(final)
    initial_ids = set(im)
    final_ids = set(fm)
    common = initial_ids & final_ids
    added_count = len(final_ids - initial_ids)
    deleted_ids = initial_ids - final_ids

    geometry_changed = 0
    reclassified = 0
    text_changed = 0
    heading_changed = 0
    order_changed = 0
    ignored_changed = 0
    uncertain_changed = 0
    materially_changed: set[str] = set()

    for rid in common:
        a, b = im[rid], fm[rid]
        if a.bbox != b.bbox:
            geometry_changed += 1
            materially_changed.add(rid)
        if a.type != b.type:
            reclassified += 1
            materially_changed.add(rid)
        if a.text != b.text:
            text_changed += 1
            materially_changed.add(rid)
        if a.heading_level != b.heading_level:
            heading_changed += 1
            materially_changed.add(rid)
        if a.reading_order != b.reading_order:
            order_changed += 1
            materially_changed.add(rid)
        if a.ignored != b.ignored:
            ignored_changed += 1
            materially_changed.add(rid)
        if a.uncertain != b.uncertain or a.note != b.note:
            uncertain_changed += 1
            materially_changed.add(rid)

    counts = Counter(e.action for e in events)
    human_edit_count = sum(1 for e in events if e.mutates_state and e.action not in {"UNDO", "REDO"})
    page_count = initial.document.page_count
    initial_n = len(initial.regions)
    corrected_initial = len(deleted_ids | materially_changed)

    # The domain replay path is optimized so non-mutating VIEW/SELECT events no
    # longer copy the entire document state.
    replayed = replay(initial, events)
    replay_valid = replayed.model_dump(exclude={"state_revision"}) == final.model_dump(
        exclude={"state_revision"}
    )

    return {
        "session_id": meta.session_id,
        "document_id": meta.document_id,
        "pages": page_count,
        "initial_regions": initial_n,
        "final_regions": len(final.regions),
        "final_correction_burden": {
            "added_regions": added_count,
            "deleted_regions": len(deleted_ids),
            "existing_regions_materially_changed": len(materially_changed),
            "corrected_initial_regions": corrected_initial,
            "corrected_region_rate": (corrected_initial / initial_n) if initial_n else 0.0,
            "geometry_changed": geometry_changed,
            "reclassified": reclassified,
            "text_changed": text_changed,
            "heading_level_changed": heading_changed,
            "reading_order_changed": order_changed,
            "ignored_status_changed": ignored_changed,
            "uncertainty_or_note_changed": uncertain_changed,
        },
        "interaction_effort": {
            "all_logged_interactions": len(events),
            "committed_edit_events": human_edit_count,
            "undo_count": counts["UNDO"],
            "redo_count": counts["REDO"],
            "actions_by_type": dict(sorted(counts.items())),
        },
        "timing": {
            "active_seconds": meta.active_seconds,
            "active_minutes_per_page": (meta.active_seconds / 60.0 / page_count) if page_count else None,
        },
        "integrity": {
            "replay_matches_final_state": replay_valid,
        },
    }
