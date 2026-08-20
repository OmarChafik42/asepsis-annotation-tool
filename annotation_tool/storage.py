from __future__ import annotations

import hashlib
import json
import os
import shutil
import threading
import uuid
import zipfile
from pathlib import Path
from typing import Any

from .domain import apply_event, replay
from .models import AnnotationEvent, AnnotationState, SessionMeta, utc_now_iso


class SessionStore:
    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self._locks: dict[str, threading.RLock] = {}
        self._locks_guard = threading.Lock()

    def _lock(self, session_id: str) -> threading.RLock:
        with self._locks_guard:
            return self._locks.setdefault(session_id, threading.RLock())

    def session_dir(self, session_id: str) -> Path:
        # Session identifiers are server-generated UUIDs. Validating them here also
        # prevents path traversal if the API is later exposed beyond localhost.
        try:
            safe_id = str(uuid.UUID(session_id))
        except (ValueError, AttributeError, TypeError) as exc:
            raise FileNotFoundError(session_id) from exc
        return self.root / safe_id

    def _path(self, session_id: str, name: str) -> Path:
        return self.session_dir(session_id) / name

    @staticmethod
    def _atomic_json(path: Path, data: Any) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, path)

    @staticmethod
    def _sha256(path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()

    def create_session(
        self,
        *,
        pdf_path: Path,
        raw_machine_output: Any,
        canonical_state: AnnotationState,
        annotator_id: str,
        raw_machine_bytes: bytes | None = None,
    ) -> SessionMeta:
        session_id = str(uuid.uuid4())
        d = self.session_dir(session_id)
        d.mkdir(parents=True, exist_ok=False)
        shutil.copy2(pdf_path, d / "source.pdf")
        raw_path = d / "machine_output.original.json"
        if raw_machine_bytes is not None:
            raw_path.write_bytes(raw_machine_bytes)
        else:
            self._atomic_json(raw_path, raw_machine_output)
        self._atomic_json(d / "initial_state.json", canonical_state.model_dump(mode="json"))
        self._atomic_json(d / "working_state.json", canonical_state.model_dump(mode="json"))
        (d / "events.jsonl").write_text("", encoding="utf-8")
        (d / "render_cache").mkdir(exist_ok=True)
        now = utc_now_iso()
        meta = SessionMeta(
            session_id=session_id,
            document_id=canonical_state.document.document_id,
            filename=canonical_state.document.filename,
            annotator_id=annotator_id,
            created_at=now,
            updated_at=now,
            initial_state_sha256=self._sha256(d / "initial_state.json"),
        )
        self._atomic_json(d / "session.json", meta.model_dump(mode="json"))
        return meta

    def list_sessions(self) -> list[SessionMeta]:
        out: list[SessionMeta] = []
        for d in sorted(self.root.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            path = d / "session.json"
            if d.is_dir() and path.exists():
                try:
                    out.append(SessionMeta.model_validate_json(path.read_text(encoding="utf-8")))
                except Exception:
                    continue
        return out

    def load_meta(self, session_id: str) -> SessionMeta:
        p = self._path(session_id, "session.json")
        if not p.exists():
            raise FileNotFoundError(session_id)
        return SessionMeta.model_validate_json(p.read_text(encoding="utf-8"))

    def save_meta(self, meta: SessionMeta) -> None:
        meta.updated_at = utc_now_iso()
        self._atomic_json(self._path(meta.session_id, "session.json"), meta.model_dump(mode="json"))

    def load_initial(self, session_id: str) -> AnnotationState:
        return AnnotationState.model_validate_json(self._path(session_id, "initial_state.json").read_text(encoding="utf-8"))

    def load_working(self, session_id: str) -> AnnotationState:
        return AnnotationState.model_validate_json(self._path(session_id, "working_state.json").read_text(encoding="utf-8"))

    def save_working(self, session_id: str, state: AnnotationState) -> None:
        self._atomic_json(self._path(session_id, "working_state.json"), state.model_dump(mode="json"))

    def load_final(self, session_id: str) -> AnnotationState | None:
        p = self._path(session_id, "final_state.json")
        return AnnotationState.model_validate_json(p.read_text(encoding="utf-8")) if p.exists() else None

    def events(self, session_id: str) -> list[AnnotationEvent]:
        p = self._path(session_id, "events.jsonl")
        if not p.exists():
            raise FileNotFoundError(session_id)
        result: list[AnnotationEvent] = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                result.append(AnnotationEvent.model_validate_json(line))
        return result

    def next_sequence(self, session_id: str) -> int:
        events = self.events(session_id)
        return (events[-1].sequence + 1) if events else 1

    def append_event(self, session_id: str, event: AnnotationEvent, *, apply_to_working: bool = True) -> AnnotationState:
        with self._lock(session_id):
            meta = self.load_meta(session_id)
            if meta.status != "active" and event.action not in {"EXPORT_SESSION"}:
                raise ValueError("Session is already approved")
            events = self.events(session_id)
            expected = (events[-1].sequence + 1) if events else 1
            if event.sequence != expected:
                raise ValueError(f"Event sequence must be {expected}")
            state = self.load_working(session_id)
            new_state = apply_event(state, event) if apply_to_working else state
            event_path = self._path(session_id, "events.jsonl")
            with event_path.open("a", encoding="utf-8") as f:
                f.write(event.model_dump_json() + "\n")
                f.flush()
                os.fsync(f.fileno())
            if event.mutates_state and apply_to_working:
                self.save_working(session_id, new_state)
            meta.updated_at = utc_now_iso()
            self.save_meta(meta)
            return new_state

    def add_active_seconds(self, session_id: str, seconds: int) -> SessionMeta:
        with self._lock(session_id):
            meta = self.load_meta(session_id)
            if meta.status == "active":
                meta.active_seconds += int(seconds)
                self.save_meta(meta)
            return meta

    def finalise(self, session_id: str) -> tuple[AnnotationState, SessionMeta]:
        with self._lock(session_id):
            meta = self.load_meta(session_id)
            if meta.status == "approved":
                final = self.load_final(session_id)
                if final is None:
                    raise RuntimeError("Approved session is missing final_state.json")
                return final, meta
            initial = self.load_initial(session_id)
            events = self.events(session_id)
            working = self.load_working(session_id)
            replayed = replay(initial, events)
            replay_valid = replayed.model_dump(exclude={"state_revision"}) == working.model_dump(exclude={"state_revision"})
            if not replay_valid:
                raise ValueError("Replay invariant failed; refusing to finalise")
            final_path = self._path(session_id, "final_state.json")
            self._atomic_json(final_path, working.model_dump(mode="json"))
            meta.status = "approved"
            meta.finalised_at = utc_now_iso()
            meta.events_sha256 = self._sha256(self._path(session_id, "events.jsonl"))
            meta.final_state_sha256 = self._sha256(final_path)
            meta.replay_valid = True
            self.save_meta(meta)
            return working, meta

    def export_zip(self, session_id: str) -> Path:
        d = self.session_dir(session_id)
        if not d.exists():
            raise FileNotFoundError(session_id)
        out = d / f"{session_id}.zip"
        include = [
            "source.pdf",
            "machine_output.original.json",
            "initial_state.json",
            "events.jsonl",
            "final_state.json",
            "session.json",
            "metrics.json",
        ]
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for name in include:
                p = d / name
                if p.exists():
                    zf.write(p, arcname=name)
        return out
