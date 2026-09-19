#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from annotation_tool.dataset import DatasetStore


def main() -> None:
    root = Path(os.environ.get("ANNOTATION_DATA_DIR", Path.cwd() / "data")).resolve()
    store = DatasetStore(root)
    rows = store.status()
    if not rows:
        print("No documents found.")
        return
    print(f"{'document':<40} | {'status':<8} | {'session':<36} | {'annotator':<16} | {'finalised_at'}")
    print("-" * 140)
    for row in rows:
        session_id = row["sessions"][-1] if row["sessions"] else "-"
        annotator = row["annotator"] or "-"
        finalised_at = row["latest_finalised_at"] or "-"
        print(f"{row['document']:<40} | {row['status']:<8} | {session_id:<36} | {annotator:<16} | {finalised_at}")


if __name__ == "__main__":
    main()
