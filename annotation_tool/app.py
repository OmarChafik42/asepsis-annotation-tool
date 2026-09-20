from __future__ import annotations

import json
import os
import tempfile
import threading
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles

from .adapters import adapt_machine_output
from .dataset import DatasetStore
from .metrics import compute_metrics
from .models import ActivityRequest, CommandRequest, FinaliseRequest, InteractionRequest
from .rendering import render_page
from .storage import SessionStore

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("ANNOTATION_DATA_DIR", Path.cwd() / "annotation-data")).resolve()
MAX_PDF_BYTES = int(float(os.environ.get("ANNOTATION_MAX_PDF_MB", "50")) * 1024 * 1024)
MAX_JSON_BYTES = int(float(os.environ.get("ANNOTATION_MAX_JSON_MB", "10")) * 1024 * 1024)

dataset_store = DatasetStore(DATA_DIR)
legacy_store = SessionStore(DATA_DIR / "sessions")
store = legacy_store

app = FastAPI(title="Asepsis Annotation & Correction Tool", version="1.0.0")


def _session_state_response(meta, state) -> Response:
    # Avoid FastAPI/jsonable_encoder walking thousands of regions into a second
    # Python object graph. Pydantic serialises the models directly to JSON.
    content = f'{{"session":{meta.model_dump_json()},"state":{state.model_dump_json()}}}'
    return Response(content=content, media_type="application/json")


def _event_state_response(event, state) -> Response:
    content = f'{{"event":{event.model_dump_json()},"state":{state.model_dump_json()}}}'
    return Response(content=content, media_type="application/json")

# Fast session lookup. Normal edits never move a session between stores, so this
# index must not be discarded after every command.
_session_index: dict[str, SessionStore] = {}
_session_index_lock = threading.RLock()
_session_index_built = False

# /api/sessions is mainly a discovery/fallback endpoint. Cache it separately from
# the lookup index so edits can invalidate list ordering without making the next
# save rescan every document directory.
_sessions_cache: list | None = None
_sessions_cache_lock = threading.RLock()


def _http_error(exc: Exception) -> None:
    if isinstance(exc, FileNotFoundError):
        raise HTTPException(404, "Session not found")
    raise HTTPException(400, str(exc))


def _infer_document_name(filename: str | None, explicit: str | None = None) -> str:
    if explicit and explicit.strip():
        return explicit.strip()
    name = (filename or "document.pdf").strip()
    if not name:
        return "document"
    stem = Path(name).stem
    for suffix in (
        "_origin",
        "_layout",
        "_span",
        "_model",
        "_content_list",
        "_content_list_v2",
        "_middle",
    ):
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
    return stem or "document"


def _invalidate_session_list_cache() -> None:
    global _sessions_cache
    with _sessions_cache_lock:
        _sessions_cache = None


def _register_session(session_id: str, target_store: SessionStore) -> None:
    with _session_index_lock:
        _session_index[session_id] = target_store


def _all_sessions() -> list:
    global _sessions_cache
    with _sessions_cache_lock:
        if _sessions_cache is not None:
            return list(_sessions_cache)

    sessions: list = []
    for document in dataset_store.documents():
        sessions.extend(dataset_store.store(document).list_sessions())
    sessions.extend(legacy_store.list_sessions())
    result = sorted(sessions, key=lambda m: m.updated_at, reverse=True)

    with _sessions_cache_lock:
        _sessions_cache = result
    return list(result)


def _build_session_index_once() -> None:
    global _session_index_built
    with _session_index_lock:
        if _session_index_built:
            return
        for document in dataset_store.documents():
            candidate = dataset_store.store(document)
            for meta in candidate.list_sessions():
                _session_index[meta.session_id] = candidate
        for meta in legacy_store.list_sessions():
            _session_index[meta.session_id] = legacy_store
        _session_index_built = True


def _resolve_session_store(session_id: str) -> SessionStore:
    with _session_index_lock:
        cached = _session_index.get(session_id)
    if cached is not None:
        return cached

    _build_session_index_once()
    with _session_index_lock:
        cached = _session_index.get(session_id)
    if cached is not None:
        return cached

    # A session might have been created externally after the initial index scan.
    # Do one targeted fallback scan before reporting 404.
    for document in dataset_store.documents():
        candidate = dataset_store.store(document)
        try:
            candidate.load_meta(session_id)
            _register_session(session_id, candidate)
            return candidate
        except FileNotFoundError:
            pass
    try:
        legacy_store.load_meta(session_id)
        _register_session(session_id, legacy_store)
        return legacy_store
    except FileNotFoundError as exc:
        raise FileNotFoundError(session_id) from exc


async def _read_limited(upload: UploadFile, limit: int, label: str) -> bytes:
    data = bytearray()
    while True:
        chunk = await upload.read(1024 * 1024)
        if not chunk:
            break
        data.extend(chunk)
        if len(data) > limit:
            raise HTTPException(413, f"{label} exceeds the configured upload limit")
    if not data:
        raise HTTPException(400, f"{label} is empty")
    return bytes(data)


@app.get("/api/health")
def health():
    return {"status": "ok", "version": app.version}


@app.get("/api/sessions")
def list_sessions():
    return [m.model_dump(mode="json") for m in _all_sessions()]


@app.get("/api/dataset")
def list_dataset():
    return dataset_store.status()


@app.post("/api/dataset/{document}/sessions")
def create_dataset_session(document: str, annotator_id: str = Form("anonymous")):
    try:
        pdf_path, model_path = dataset_store.source_files(document)
        raw_bytes = model_path.read_bytes()
        if len(raw_bytes) > MAX_JSON_BYTES:
            raise HTTPException(413, "annotation JSON exceeds the configured upload limit")
        raw = json.loads(raw_bytes.decode("utf-8"))
        canonical = adapt_machine_output(raw, pdf_path)
        canonical.document.filename = pdf_path.name
        target_store = dataset_store.store(document)
        meta = target_store.create_session(
            pdf_path=pdf_path,
            raw_machine_output=raw,
            raw_machine_bytes=raw_bytes,
            canonical_state=canonical,
            annotator_id=annotator_id.strip() or "anonymous",
        )
        meta.metadata["document"] = document
        target_store.save_meta(meta)
        _register_session(meta.session_id, target_store)
        _invalidate_session_list_cache()
        return _session_state_response(meta, canonical)
    except HTTPException:
        raise
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions")
async def create_session(
    pdf_file: UploadFile = File(...),
    annotation_file: UploadFile = File(...),
    annotator_id: str = Form("anonymous"),
    document: str = Form(""),
):
    if not (pdf_file.filename or "").lower().endswith(".pdf"):
        raise HTTPException(400, "pdf_file must be a PDF")

    raw_bytes = await _read_limited(annotation_file, MAX_JSON_BYTES, "annotation JSON")
    try:
        raw = json.loads(raw_bytes.decode("utf-8"))
    except Exception as exc:
        raise HTTPException(400, f"Invalid annotation JSON: {exc}") from exc

    pdf_bytes = await _read_limited(pdf_file, MAX_PDF_BYTES, "PDF")
    suffix = Path(pdf_file.filename or "source.pdf").suffix or ".pdf"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(pdf_bytes)
        tmp_path = Path(tmp.name)

    document_name = _infer_document_name(pdf_file.filename, document)
    target_store = dataset_store.store(document_name)

    try:
        canonical = adapt_machine_output(raw, tmp_path)
        canonical.document.filename = pdf_file.filename or canonical.document.filename
        meta = target_store.create_session(
            pdf_path=tmp_path,
            raw_machine_output=raw,
            raw_machine_bytes=raw_bytes,
            canonical_state=canonical,
            annotator_id=annotator_id.strip() or "anonymous",
        )
        meta.metadata.setdefault("document", document_name)
        target_store.save_meta(meta)
        _register_session(meta.session_id, target_store)
        _invalidate_session_list_cache()
        return _session_state_response(meta, canonical)
    except Exception as exc:
        _http_error(exc)
    finally:
        tmp_path.unlink(missing_ok=True)


@app.get("/api/sessions/{session_id}")
def get_session(session_id: str):
    try:
        target_store = _resolve_session_store(session_id)
        meta = target_store.load_meta(session_id)
        state = target_store.load_final(session_id) if meta.status == "approved" else target_store.load_working(session_id)
        assert state is not None
        return _session_state_response(meta, state)
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/events")
def get_events(session_id: str):
    try:
        target_store = _resolve_session_store(session_id)
        return [e.model_dump(mode="json") for e in target_store.events(session_id)]
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/pages/{page_index}.png")
def page_image(session_id: str, page_index: int, scale: float = 1.6):
    try:
        target_store = _resolve_session_store(session_id)
        meta = target_store.load_meta(session_id)
        state = target_store.load_working(session_id) if meta.status == "active" else target_store.load_final(session_id)
        assert state is not None
        if page_index < 0 or page_index >= state.document.page_count:
            raise ValueError("Invalid page")
        d = target_store.session_dir(session_id)
        path = render_page(
            d / "source.pdf",
            d / "render_cache",
            page_index,
            min(max(scale, 0.5), 3.0),
        )
        return FileResponse(
            path,
            media_type="image/png",
            headers={"Cache-Control": "private, max-age=3600"},
        )
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/commands")
def command(session_id: str, request: CommandRequest):
    try:
        target_store = _resolve_session_store(session_id)
        event, new_state = target_store.process_command(session_id, request)
        _invalidate_session_list_cache()
        return _event_state_response(event, new_state)
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/interactions")
def interaction(session_id: str, request: InteractionRequest):
    try:
        target_store = _resolve_session_store(session_id)
        event = target_store.process_interaction(session_id, request)
        _invalidate_session_list_cache()
        return event.model_dump(mode="json")
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/undo")
def undo(session_id: str):
    try:
        target_store = _resolve_session_store(session_id)
        event, new_state = target_store.process_undo_redo(session_id, redo=False)
        _invalidate_session_list_cache()
        return _event_state_response(event, new_state)
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/redo")
def redo(session_id: str):
    try:
        target_store = _resolve_session_store(session_id)
        event, new_state = target_store.process_undo_redo(session_id, redo=True)
        _invalidate_session_list_cache()
        return _event_state_response(event, new_state)
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/activity")
def activity(session_id: str, request: ActivityRequest):
    try:
        target_store = _resolve_session_store(session_id)
        meta = target_store.add_active_seconds(session_id, request.seconds)
        _invalidate_session_list_cache()
        return {"active_seconds": meta.active_seconds}
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/metrics")
def metrics(session_id: str):
    try:
        target_store = _resolve_session_store(session_id)
        meta = target_store.load_meta(session_id)

        # Approved metrics are immutable; use the saved report if it exists.
        if meta.status == "approved":
            cached = target_store.session_dir(session_id) / "metrics.json"
            if cached.exists():
                return json.loads(cached.read_text(encoding="utf-8"))

        initial = target_store.load_initial(session_id)
        final = target_store.load_final(session_id) or target_store.load_working(session_id)
        result = compute_metrics(initial, final, target_store.events(session_id), meta)

        # Avoid rewriting metrics.json on every active refresh. The authoritative
        # report is written at finalisation/export.
        if meta.status == "approved":
            target_store._atomic_json(target_store.session_dir(session_id) / "metrics.json", result)
        return result
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/finalise")
def finalise(session_id: str, request: FinaliseRequest):
    try:
        target_store = _resolve_session_store(session_id)
        meta = target_store.load_meta(session_id)
        if meta.status == "active":
            approval = {
                "checklist": request.checklist.model_dump(mode="json"),
                "approval_note": request.approval_note,
            }
            target_store.process_interaction(
                session_id,
                InteractionRequest(action="FINALISE_SESSION", metadata=approval),
            )
            meta = target_store.load_meta(session_id)
            meta.metadata["approval"] = approval
            target_store.save_meta(meta)

        final, meta = target_store.finalise(session_id)
        result = compute_metrics(
            target_store.load_initial(session_id),
            final,
            target_store.events(session_id),
            meta,
        )
        target_store._atomic_json(target_store.session_dir(session_id) / "metrics.json", result)
        _invalidate_session_list_cache()
        return {
            "session": meta.model_dump(mode="json"),
            "state": final.model_dump(mode="json"),
            "metrics": result,
        }
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/export")
def export_session(session_id: str):
    try:
        target_store = _resolve_session_store(session_id)
        meta = target_store.load_meta(session_id)
        metrics_path = target_store.session_dir(session_id) / "metrics.json"
        if meta.status == "approved" and metrics_path.exists():
            result = json.loads(metrics_path.read_text(encoding="utf-8"))
        else:
            initial = target_store.load_initial(session_id)
            final = target_store.load_final(session_id) or target_store.load_working(session_id)
            result = compute_metrics(initial, final, target_store.events(session_id), meta)
            target_store._atomic_json(metrics_path, result)
        path = target_store.export_zip(session_id)
        return FileResponse(
            path,
            filename=f"annotation-session-{session_id}.zip",
            media_type="application/zip",
        )
    except Exception as exc:
        _http_error(exc)


app.mount("/", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")
