#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from annotation_tool.metrics import compute_metrics
from annotation_tool.storage import SessionStore


def main():
    ap = argparse.ArgumentParser(description="Export one row of descriptive correction metrics per annotation session")
    ap.add_argument("--data-dir", default="annotation-data")
    ap.add_argument("--out", default="annotation_metrics.csv")
    args = ap.parse_args()

    store = SessionStore(Path(args.data_dir).resolve() / "sessions")
    rows = []
    for meta in reversed(store.list_sessions()):
        initial = store.load_initial(meta.session_id)
        final = store.load_final(meta.session_id) or store.load_working(meta.session_id)
        m = compute_metrics(initial, final, store.events(meta.session_id), meta)
        b, i, t = m["final_correction_burden"], m["interaction_effort"], m["timing"]
        rows.append({
            "session_id": meta.session_id,
            "filename": meta.filename,
            "annotator_id": meta.annotator_id,
            "status": meta.status,
            "pages": m["pages"],
            "initial_regions": m["initial_regions"],
            "final_regions": m["final_regions"],
            "corrected_initial_regions": b["corrected_initial_regions"],
            "corrected_region_rate": b["corrected_region_rate"],
            "geometry_changed": b["geometry_changed"],
            "reclassified": b["reclassified"],
            "committed_edit_events": i["committed_edit_events"],
            "undo_count": i["undo_count"],
            "redo_count": i["redo_count"],
            "active_seconds": t["active_seconds"],
            "active_minutes_per_page": t["active_minutes_per_page"],
            "replay_valid": m["integrity"]["replay_matches_final_state"],
        })

    out = Path(args.out).resolve()
    fields = list(rows[0]) if rows else ["session_id"]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    print(out)


if __name__ == "__main__":
    main()
