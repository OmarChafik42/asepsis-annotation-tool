from __future__ import annotations

import threading
from pathlib import Path
from typing import Any

from .storage import SessionStore


class DatasetStore:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self._stores: dict[str, SessionStore] = {}
        self._stores_lock = threading.RLock()

    def document_dir(self, document: str) -> Path:
        safe = str(document).strip()
        if not safe or "/" in safe or "\\" in safe or safe in {".", ".."}:
            raise ValueError(f"Invalid document name: {document!r}")
        return self.root / safe / "auto"

    def sessions_root(self, document: str) -> Path:
        return self.document_dir(document) / "sessions"

    def store(self, document: str) -> SessionStore:
        key = str(document).strip()
        with self._stores_lock:
            cached = self._stores.get(key)
            if cached is not None:
                return cached
            root = self.sessions_root(key)
            root.mkdir(parents=True, exist_ok=True)
            created = SessionStore(root)
            self._stores[key] = created
            return created

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
        for child in self.root.iterdir():
            if child.is_dir() and (child / "auto").exists():
                docs.append(child.name)
        return sorted(docs, key=str.lower)

    def status(self) -> list[dict[str, Any]]:
        """Return the same frontend-compatible pending/annotated status as before.

        The latest session metadata is loaded through SessionStore, allowing its
        in-memory metadata cache to be reused instead of reparsing session.json here.
        """
        rows: list[dict[str, Any]] = []
        for document in self.documents():
            sessions = self.store(document).list_sessions()
            if sessions:
                latest = sessions[0]
                rows.append(
                    {
                        "document": document,
                        "status": "annotated",
                        "sessions": [m.session_id for m in sessions],
                        "latest_finalised_at": latest.finalised_at,
                        "annotator": latest.annotator_id,
                        # Extra field is backwards-compatible and useful for later UI
                        # improvements without changing the existing annotated/pending logic.
                        "latest_session_status": latest.status,
                    }
                )
            else:
                rows.append(
                    {
                        "document": document,
                        "status": "pending",
                        "sessions": [],
                        "latest_finalised_at": None,
                        "annotator": None,
                        "latest_session_status": None,
                    }
                )
        return rows
