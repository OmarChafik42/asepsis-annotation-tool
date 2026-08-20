from __future__ import annotations

from collections import Counter
from typing import Any

from .domain import replay
from .models import AnnotationEvent, AnnotationState, SessionMeta


def _region_map(state: AnnotationState):
    return {r.region_id: r for r in state.regions}


def compute_metrics(initial: AnnotationState, final: AnnotationState, events: list[AnnotationEvent], meta: SessionMeta) -> dict[str, Any]:
    im = _region_map(initial)
    fm = _region_map(final)
    common = set(im) & set(fm)
    added = sorted(set(fm) - set(im))
    deleted = sorted(set(im) - set(fm))

    geometry_changed = []
    reclassified = []
    text_changed = []
    heading_changed = []
    order_changed = []
    ignored_changed = []
    uncertain_changed = []
    materially_changed = set()

    for rid in common:
        a, b = im[rid], fm[rid]
        if a.bbox != b.bbox:
            geometry_changed.append(rid); materially_changed.add(rid)
        if a.type != b.type:
            reclassified.append(rid); materially_changed.add(rid)
        if a.text != b.text:
            text_changed.append(rid); materially_changed.add(rid)
        if a.heading_level != b.heading_level:
            heading_changed.append(rid); materially_changed.add(rid)
        if a.reading_order != b.reading_order:
            order_changed.append(rid); materially_changed.add(rid)
        if a.ignored != b.ignored:
            ignored_changed.append(rid); materially_changed.add(rid)
        if a.uncertain != b.uncertain or a.note != b.note:
            uncertain_changed.append(rid); materially_changed.add(rid)

    mutating = [e for e in events if e.mutates_state]
    human_edits = [e for e in mutating if e.action not in {"UNDO", "REDO"}]
    counts = Counter(e.action for e in events)
    page_count = initial.document.page_count
    initial_n = len(initial.regions)

    replayed = replay(initial, events)
    replay_valid = replayed.model_dump(exclude={"state_revision"}) == final.model_dump(exclude={"state_revision"})

    return {
        "session_id": meta.session_id,
        "document_id": meta.document_id,
        "pages": page_count,
        "initial_regions": initial_n,
        "final_regions": len(final.regions),
        "final_correction_burden": {
            "added_regions": len(added),
            "deleted_regions": len(deleted),
            "existing_regions_materially_changed": len(materially_changed),
            "corrected_initial_regions": len(set(deleted) | materially_changed),
            "corrected_region_rate": ((len(set(deleted) | materially_changed) / initial_n) if initial_n else 0.0),
            "geometry_changed": len(geometry_changed),
            "reclassified": len(reclassified),
            "text_changed": len(text_changed),
            "heading_level_changed": len(heading_changed),
            "reading_order_changed": len(order_changed),
            "ignored_status_changed": len(ignored_changed),
            "uncertainty_or_note_changed": len(uncertain_changed),
        },
        "interaction_effort": {
            "all_logged_interactions": len(events),
            "committed_edit_events": len(human_edits),
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
