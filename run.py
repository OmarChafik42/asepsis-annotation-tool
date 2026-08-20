from __future__ import annotations

import argparse
import os
from pathlib import Path

import uvicorn


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Asepsis Annotation & Correction Tool")
    parser.add_argument("--host", default=os.environ.get("ANNOTATION_HOST", "127.0.0.1"))
    parser.add_argument("--port", default=int(os.environ.get("ANNOTATION_PORT", "8765")), type=int)
    parser.add_argument(
        "--data-dir",
        default=os.environ.get("ANNOTATION_DATA_DIR", str(Path.cwd() / "annotation-data")),
    )
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()

    os.environ["ANNOTATION_DATA_DIR"] = str(Path(args.data_dir).resolve())
    uvicorn.run("annotation_tool.app:app", host=args.host, port=args.port, reload=args.reload, workers=1)


if __name__ == "__main__":
    main()
