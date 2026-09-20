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

from .domain import (
    apply_event,
    build_command_event,
    build_interaction_event,
    build_undo_redo_event,
    replay,
)
from .models import (
    AnnotationEvent,
    AnnotationState,
    CommandRequest,
    InteractionRequest,
    SessionMeta,
    utc_now_iso,
)


class SessionStore:
    """Disk-backed event-sourced annotation session store.

    The public file format is unchanged. Performance improvements are internal:
    session-local locks make sequence assignment atomic, hot metadata/state/event
    objects are cached in memory, and normal commands avoid rescanning the full
    JSONL event history merely to obtain the next sequence number.
    """

    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self._locks: dict[str, threading.RLock] = {}
        self._locks_guard = threading.Lock()
        self._cache_guard = threading.RLock()

        self._meta_cache: dict[str, SessionMeta] = {}
        self._initial_cache: dict[str, AnnotationState] = {}
        self._working_cache: dict[str, AnnotationState] = {}
        self._final_cache: dict[str, AnnotationState] = {}
        self._events_cache: dict[str, list[AnnotationEvent]] = {}
        self._last_sequence_cache: dict[str, int] = {}

        # Keep the original durability guarantee by default. Users who explicitly
        # accept weaker power-loss durability can set ANNOTATION_FSYNC_EVENTS=0.
        self._fsync_events = os.environ.get("ANNOTATION_FSYNC_EVENTS", "1").strip().lower() not in {
            "0", "false", "no", "off"
        }

    def _lock(self, session_id: str) -> threading.RLock:
        with self._locks_guard:
            return self._locks.setdefault(session_id, threading.RLock())

    def session_dir(self, session_id: str) -> Path:
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
    def _atomic_state(path: Path, state: AnnotationState, *, pretty: bool = False) -> None:
        """Atomically persist a state.

        working_state.json is compact because it is rewritten frequently. Initial
        and final states may remain pretty-printed for human inspection.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        if pretty:
            text = json.dumps(state.model_dump(mode="json"), indent=2, ensure_ascii=False)
        else:
            text = state.model_dump_json()
        tmp.write_text(text, encoding="utf-8")
        os.replace(tmp, path)

    @staticmethod
    def _sha256(path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()

    def _clear_session_cache(self, session_id: str) -> None:
        with self._cache_guard:
            self._meta_cache.pop(session_id, None)
            self._initial_cache.pop(session_id, None)
            self._working_cache.pop(session_id, None)
            self._final_cache.pop(session_id, None)
            self._events_cache.pop(session_id, None)
            self._last_sequence_cache.pop(session_id, None)

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

        self._atomic_state(d / "initial_state.json", canonical_state, pretty=True)
        self._atomic_state(d / "working_state.json", canonical_state, pretty=False)
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
            metadata={"last_sequence": 0, "state_revision": canonical_state.state_revision},
        )
        self._atomic_json(d / "session.json", meta.model_dump(mode="json"))

        with self._cache_guard:
            self._meta_cache[session_id] = meta.model_copy(deep=True)
            self._initial_cache[session_id] = canonical_state
            self._working_cache[session_id] = canonical_state
            self._events_cache[session_id] = []
            self._last_sequence_cache[session_id] = 0
        return meta

    def list_sessions(self) -> list[SessionMeta]:
        out: list[SessionMeta] = []
        if not self.root.exists():
            return out
        for d in self.root.iterdir():
            path = d / "session.json"
            if not d.is_dir() or not path.exists():
                continue
            try:
                meta = SessionMeta.model_validate_json(path.read_text(encoding="utf-8"))
                out.append(meta)
                with self._cache_guard:
                    self._meta_cache[meta.session_id] = meta.model_copy(deep=True)
            except Exception:
                continue
        return sorted(out, key=lambda m: m.updated_at, reverse=True)

    def load_meta(self, session_id: str) -> SessionMeta:
        with self._cache_guard:
            cached = self._meta_cache.get(session_id)
            if cached is not None:
                return cached.model_copy(deep=True)

        p = self._path(session_id, "session.json")
        if not p.exists():
            raise FileNotFoundError(session_id)
        meta = SessionMeta.model_validate_json(p.read_text(encoding="utf-8"))
        with self._cache_guard:
            self._meta_cache[session_id] = meta.model_copy(deep=True)
        return meta

    def save_meta(self, meta: SessionMeta) -> None:
        meta.updated_at = utc_now_iso()
        self._atomic_json(self._path(meta.session_id, "session.json"), meta.model_dump(mode="json"))
        with self._cache_guard:
            self._meta_cache[meta.session_id] = meta.model_copy(deep=True)

    def load_initial(self, session_id: str) -> AnnotationState:
        with self._cache_guard:
            cached = self._initial_cache.get(session_id)
            if cached is not None:
                return cached
        state = AnnotationState.model_validate_json(
            self._path(session_id, "initial_state.json").read_text(encoding="utf-8")
        )
        with self._cache_guard:
            self._initial_cache[session_id] = state
        return state

    def load_working(self, session_id: str) -> AnnotationState:
        with self._cache_guard:
            cached = self._working_cache.get(session_id)
            if cached is not None:
                return cached
        p = self._path(session_id, "working_state.json")
        if not p.exists():
            raise FileNotFoundError(session_id)
        state = AnnotationState.model_validate_json(p.read_text(encoding="utf-8"))
        with self._cache_guard:
            self._working_cache[session_id] = state
        return state

    def save_working(self, session_id: str, state: AnnotationState) -> None:
        # Update the in-memory canonical state first so a later request in this
        # process remains coherent even if an exceptional disk failure occurs.
        with self._cache_guard:
            self._working_cache[session_id] = state
        self._atomic_state(self._path(session_id, "working_state.json"), state, pretty=False)

    def load_final(self, session_id: str) -> AnnotationState | None:
        with self._cache_guard:
            cached = self._final_cache.get(session_id)
            if cached is not None:
                return cached
        p = self._path(session_id, "final_state.json")
        if not p.exists():
            return None
        state = AnnotationState.model_validate_json(p.read_text(encoding="utf-8"))
        with self._cache_guard:
            self._final_cache[session_id] = state
        return state

    def events(self, session_id: str) -> list[AnnotationEvent]:
        with self._cache_guard:
            cached = self._events_cache.get(session_id)
            if cached is not None:
                return list(cached)

        p = self._path(session_id, "events.jsonl")
        if not p.exists():
            raise FileNotFoundError(session_id)
        result: list[AnnotationEvent] = []
        with p.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    result.append(AnnotationEvent.model_validate_json(line))

        with self._cache_guard:
            self._events_cache[session_id] = result
            self._last_sequence_cache[session_id] = result[-1].sequence if result else 0
        return list(result)

    def _last_sequence_from_file(self, session_id: str) -> int:
        """Read only the last JSONL record instead of parsing the entire event log."""
        p = self._path(session_id, "events.jsonl")
        if not p.exists():
            raise FileNotFoundError(session_id)
        if p.stat().st_size == 0:
            return 0

        with p.open("rb") as f:
            f.seek(0, os.SEEK_END)
            pos = f.tell()
            data = bytearray()
            while pos > 0:
                read_size = min(8192, pos)
                pos -= read_size
                f.seek(pos)
                data[:0] = f.read(read_size)
                lines = [line for line in data.splitlines() if line.strip()]
                if len(lines) >= 2 or pos == 0:
                    last = lines[-1]
                    obj = json.loads(last.decode("utf-8"))
                    return int(obj["sequence"])
        return 0

    def _last_sequence_locked(self, session_id: str) -> int:
        with self._cache_guard:
            cached = self._last_sequence_cache.get(session_id)
            if cached is not None:
                return cached
        value = self._last_sequence_from_file(session_id)
        with self._cache_guard:
            self._last_sequence_cache[session_id] = value
        return value

    def next_sequence(self, session_id: str) -> int:
        # Retained for compatibility with older callers. New command methods assign
        # the sequence under the same session lock as the append operation.
        with self._lock(session_id):
            return self._last_sequence_locked(session_id) + 1

    def _append_event_line_locked(self, session_id: str, event: AnnotationEvent) -> None:
        expected = self._last_sequence_locked(session_id) + 1
        if event.sequence != expected:
            raise ValueError(f"Event sequence must be {expected}")

        event_path = self._path(session_id, "events.jsonl")
        with event_path.open("a", encoding="utf-8") as f:
            f.write(event.model_dump_json() + "\n")
            f.flush()
            if self._fsync_events:
                os.fsync(f.fileno())

        with self._cache_guard:
            cached_events = self._events_cache.get(session_id)
            if cached_events is not None:
                cached_events.append(event)
            self._last_sequence_cache[session_id] = event.sequence

    def _commit_event_locked(
        self,
        session_id: str,
        event: AnnotationEvent,
        *,
        meta: SessionMeta,
        new_state: AnnotationState | None = None,
    ) -> None:
        self._append_event_line_locked(session_id, event)

        if event.mutates_state and new_state is not None:
            self.save_working(session_id, new_state)
            meta.metadata["state_revision"] = new_state.state_revision

        meta.metadata["last_sequence"] = event.sequence
        self.save_meta(meta)

    def process_command(self, session_id: str, request: CommandRequest) -> tuple[AnnotationEvent, AnnotationState]:
        """Build, sequence, persist, and apply one mutating command atomically."""
        with self._lock(session_id):
            meta = self.load_meta(session_id)
            if meta.status != "active":
                raise ValueError("Approved sessions are read-only")
            state = self.load_working(session_id)
            sequence = self._last_sequence_locked(session_id) + 1
            event = build_command_event(
                session_id=session_id,
                annotator_id=meta.annotator_id,
                sequence=sequence,
                state=state,
                command=request,
            )
            new_state = apply_event(state, event)
            self._commit_event_locked(session_id, event, meta=meta, new_state=new_state)
            return event, new_state

    def process_interaction(self, session_id: str, request: InteractionRequest) -> AnnotationEvent:
        """Persist a non-mutating interaction without loading the large working state."""
        with self._lock(session_id):
            meta = self.load_meta(session_id)
            if meta.status != "active" and request.action.upper().strip() not in {"EXPORT_SESSION"}:
                raise ValueError("Session is already approved")
            sequence = self._last_sequence_locked(session_id) + 1
            event = build_interaction_event(
                session_id=session_id,
                annotator_id=meta.annotator_id,
                sequence=sequence,
                action=request.action,
                page=request.page,
                region_id=request.region_id,
                metadata=request.metadata,
            )
            self._commit_event_locked(session_id, event, meta=meta)
            return event

    def process_undo_redo(self, session_id: str, *, redo: bool) -> tuple[AnnotationEvent, AnnotationState]:
        with self._lock(session_id):
            meta = self.load_meta(session_id)
            if meta.status != "active":
                raise ValueError("Approved sessions are read-only")
            state = self.load_working(session_id)
            history = self.events(session_id)
            sequence = self._last_sequence_locked(session_id) + 1
            event = build_undo_redo_event(
                session_id=session_id,
                annotator_id=meta.annotator_id,
                sequence=sequence,
                state=state,
                events=history,
                redo=redo,
            )
            new_state = apply_event(state, event)
            self._commit_event_locked(session_id, event, meta=meta, new_state=new_state)
            return event, new_state

    def append_event(
        self,
        session_id: str,
        event: AnnotationEvent,
        *,
        apply_to_working: bool = True,
    ) -> AnnotationState:
        """Compatibility API for pre-built events.

        Prefer process_command/process_interaction/process_undo_redo for new code,
        because those assign the sequence under the same lock as persistence.
        """
        with self._lock(session_id):
            meta = self.load_meta(session_id)
            if meta.status != "active" and event.action not in {"EXPORT_SESSION"}:
                raise ValueError("Session is already approved")
            state = self.load_working(session_id)
            new_state = apply_event(state, event) if apply_to_working else state
            self._commit_event_locked(
                session_id,
                event,
                meta=meta,
                new_state=new_state if (event.mutates_state and apply_to_working) else None,
            )
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
            history = self.events(session_id)
            working = self.load_working(session_id)
            replayed = replay(initial, history)
            replay_valid = replayed.model_dump(exclude={"state_revision"}) == working.model_dump(
                exclude={"state_revision"}
            )
            if not replay_valid:
                raise ValueError("Replay invariant failed; refusing to finalise")

            final_path = self._path(session_id, "final_state.json")
            self._atomic_state(final_path, working, pretty=True)
            with self._cache_guard:
                self._final_cache[session_id] = working

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
