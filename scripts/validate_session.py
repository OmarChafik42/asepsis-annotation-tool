#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from annotation_tool.domain import replay
from annotation_tool.models import AnnotationEvent, AnnotationState


def main():
    ap = argparse.ArgumentParser(description="Verify replay(initial_state, events) == final/current state")
    ap.add_argument("session_dir")
    args = ap.parse_args()
    d = Path(args.session_dir).resolve()

    initial = AnnotationState.model_validate_json((d / "initial_state.json").read_text(encoding="utf-8"))
    events = [AnnotationEvent.model_validate_json(line) for line in (d / "events.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    target_path = d / "final_state.json" if (d / "final_state.json").exists() else d / "working_state.json"
    target = AnnotationState.model_validate_json(target_path.read_text(encoding="utf-8"))
    rebuilt = replay(initial, events)
    ok = rebuilt.model_dump(exclude={"state_revision"}) == target.model_dump(exclude={"state_revision"})
    print(json.dumps({"session_dir": str(d), "target": target_path.name, "events": len(events), "replay_valid": ok}, indent=2))
    raise SystemExit(0 if ok else 2)


if __name__ == "__main__":
    main()
