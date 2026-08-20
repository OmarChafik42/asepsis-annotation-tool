#!/usr/bin/env python3
"""Run the existing 1(a) BetterIngest review preparation and write JSON for the standalone tool.

This is deliberately a bridge script, not a dependency of the annotation application.
The annotation tool remains usable with any producer that emits its canonical schema.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--asepsis-root", required=True, help="Path to asepsis-prototype-main")
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    root = Path(args.asepsis_root).resolve()
    if not (root / "modules" / "ingest" / "betteringest_pdf.py").exists():
        raise SystemExit("Could not find modules/ingest/betteringest_pdf.py under --asepsis-root")
    sys.path.insert(0, str(root))

    from modules.ingest.betteringest_pdf import prepare_layout_review  # type: ignore

    result = prepare_layout_review([str(Path(args.pdf).resolve())])
    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result[0], indent=2, ensure_ascii=False), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
