from __future__ import annotations

from pathlib import Path
from typing import Any

from .models import SessionMeta
from .storage import SessionStore


class DatasetStore:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self._stores: dict[str, SessionStore] = {}

    def document_dir(self, document: str) -> Path:
        safe = str(document).strip()
        if not safe or "/" in safe or "\\" in safe or safe in {".", ".."}:
            raise ValueError(f"Invalid document name: {document!r}")
        return self.root / safe / "auto"

    def sessions_root(self, document: str) -> Path:
        return self.document_dir(document) / "sessions"

    def store(self, document: str) -> SessionStore:
        key = str(document).strip()
        if key not in self._stores:
            root = self.sessions_root(key)
            root.mkdir(parents=True, exist_ok=True)
            self._stores[key] = SessionStore(root)
        return self._stores[key]

    def source_files(self, document: str) -> tuple[Path, Path]:
        auto = self.document_dir(document)
        pdf = auto / f"{document}_origin.pdf"
        model = auto / f"{document}_model.json"
        if not pdf.exists():
            candidates = sorted(auto.glob("*_origin.pdf"))
            if len(candidates) == 1:
                pdf = candidates[0]
        if not model.exists():
            candidates = sorted(auto.glob("*_model.json"))
            if len(candidates) == 1:
                model = candidates[0]
        if not pdf.exists() or not model.exists():
            raise FileNotFoundError(f"Source files for {document!r} are incomplete")
        return pdf, model

    def documents(self) -> list[str]:
        if not self.root.exists():
            return []
        docs: list[str] = []
        for child in sorted(self.root.iterdir(), key=lambda p: p.name.lower()):
            if child.is_dir() and (child / "auto").exists():
                docs.append(child.name)
        return docs

    def status(self) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for document in self.documents():
            sessions_root = self.sessions_root(document)
            session_dirs = (
                [
                    child
                    for child in sessions_root.iterdir()
                    if child.is_dir() and (child / "session.json").is_file()
                ]
                if sessions_root.is_dir()
                else []
            )
            session_dirs.sort(key=lambda p: p.stat().st_mtime, reverse=True)
            session_paths = [p / "session.json" for p in session_dirs]
            if session_paths:
                latest = session_paths[0]
                try:
                    meta = SessionMeta.model_validate_json(latest.read_text(encoding="utf-8"))
                except Exception:
                    meta = None
                rows.append(
                    {
                        "document": document,
                        "status": "annotated",
                        "sessions": [p.parent.name for p in session_paths],
                        "latest_finalised_at": getattr(meta, "finalised_at", None) if meta else None,
                        "annotator": getattr(meta, "annotator_id", None) if meta else None,
                    }
                )
            else:
                rows.append({
                    "document": document,
                    "status": "pending",
                    "sessions": [],
                    "latest_finalised_at": None,
                    "annotator": None,
                })
        return rows
