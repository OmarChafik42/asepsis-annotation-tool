from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .adapters import adapt_machine_output
from .domain import build_command_event, build_interaction_event, build_undo_redo_event
from .metrics import compute_metrics
from .models import ActivityRequest, CommandRequest, FinaliseRequest, InteractionRequest
from .rendering import render_page
from .storage import SessionStore

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("ANNOTATION_DATA_DIR", Path.cwd() / "annotation-data")).resolve()
MAX_PDF_BYTES = int(float(os.environ.get("ANNOTATION_MAX_PDF_MB", "50")) * 1024 * 1024)
MAX_JSON_BYTES = int(float(os.environ.get("ANNOTATION_MAX_JSON_MB", "10")) * 1024 * 1024)
store = SessionStore(DATA_DIR / "sessions")

app = FastAPI(title="Asepsis Annotation & Correction Tool", version="1.0.0")


def _http_error(exc: Exception) -> None:
    if isinstance(exc, FileNotFoundError):
        raise HTTPException(404, "Session not found")
    raise HTTPException(400, str(exc))


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
    return [m.model_dump(mode="json") for m in store.list_sessions()]


@app.post("/api/sessions")
async def create_session(
    pdf_file: UploadFile = File(...),
    annotation_file: UploadFile = File(...),
    annotator_id: str = Form("anonymous"),
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

    try:
        canonical = adapt_machine_output(raw, tmp_path)
        canonical.document.filename = pdf_file.filename or canonical.document.filename
        meta = store.create_session(
            pdf_path=tmp_path,
            raw_machine_output=raw,
            raw_machine_bytes=raw_bytes,
            canonical_state=canonical,
            annotator_id=annotator_id.strip() or "anonymous",
        )
        return {"session": meta.model_dump(mode="json"), "state": canonical.model_dump(mode="json")}
    except Exception as exc:
        _http_error(exc)
    finally:
        tmp_path.unlink(missing_ok=True)


@app.get("/api/sessions/{session_id}")
def get_session(session_id: str):
    try:
        meta = store.load_meta(session_id)
        state = store.load_final(session_id) if meta.status == "approved" else store.load_working(session_id)
        assert state is not None
        return {"session": meta.model_dump(mode="json"), "state": state.model_dump(mode="json")}
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/events")
def get_events(session_id: str):
    try:
        return [e.model_dump(mode="json") for e in store.events(session_id)]
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/pages/{page_index}.png")
def page_image(session_id: str, page_index: int, scale: float = 1.6):
    try:
        meta = store.load_meta(session_id)
        state = store.load_working(session_id) if meta.status == "active" else store.load_final(session_id)
        assert state is not None
        if page_index < 0 or page_index >= state.document.page_count:
            raise ValueError("Invalid page")
        d = store.session_dir(session_id)
        path = render_page(d / "source.pdf", d / "render_cache", page_index, min(max(scale, 0.5), 3.0))
        return FileResponse(path, media_type="image/png", headers={"Cache-Control": "private, max-age=3600"})
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/commands")
def command(session_id: str, request: CommandRequest):
    try:
        meta = store.load_meta(session_id)
        if meta.status != "active":
            raise ValueError("Approved sessions are read-only")
        state = store.load_working(session_id)
        event = build_command_event(
            session_id=session_id,
            annotator_id=meta.annotator_id,
            sequence=store.next_sequence(session_id),
            state=state,
            command=request,
        )
        new_state = store.append_event(session_id, event)
        return {"event": event.model_dump(mode="json"), "state": new_state.model_dump(mode="json")}
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/interactions")
def interaction(session_id: str, request: InteractionRequest):
    try:
        meta = store.load_meta(session_id)
        event = build_interaction_event(
            session_id=session_id,
            annotator_id=meta.annotator_id,
            sequence=store.next_sequence(session_id),
            action=request.action,
            page=request.page,
            region_id=request.region_id,
            metadata=request.metadata,
        )
        store.append_event(session_id, event, apply_to_working=False)
        return event.model_dump(mode="json")
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/undo")
def undo(session_id: str):
    try:
        meta = store.load_meta(session_id)
        state = store.load_working(session_id)
        event = build_undo_redo_event(
            session_id=session_id,
            annotator_id=meta.annotator_id,
            sequence=store.next_sequence(session_id),
            state=state,
            events=store.events(session_id),
            redo=False,
        )
        new_state = store.append_event(session_id, event)
        return {"event": event.model_dump(mode="json"), "state": new_state.model_dump(mode="json")}
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/redo")
def redo(session_id: str):
    try:
        meta = store.load_meta(session_id)
        state = store.load_working(session_id)
        event = build_undo_redo_event(
            session_id=session_id,
            annotator_id=meta.annotator_id,
            sequence=store.next_sequence(session_id),
            state=state,
            events=store.events(session_id),
            redo=True,
        )
        new_state = store.append_event(session_id, event)
        return {"event": event.model_dump(mode="json"), "state": new_state.model_dump(mode="json")}
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/activity")
def activity(session_id: str, request: ActivityRequest):
    try:
        meta = store.add_active_seconds(session_id, request.seconds)
        return {"active_seconds": meta.active_seconds}
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/metrics")
def metrics(session_id: str):
    try:
        meta = store.load_meta(session_id)
        initial = store.load_initial(session_id)
        final = store.load_final(session_id) or store.load_working(session_id)
        result = compute_metrics(initial, final, store.events(session_id), meta)
        store._atomic_json(store.session_dir(session_id) / "metrics.json", result)
        return result
    except Exception as exc:
        _http_error(exc)


@app.post("/api/sessions/{session_id}/finalise")
def finalise(session_id: str, request: FinaliseRequest):
    try:
        meta = store.load_meta(session_id)
        if meta.status == "active":
            approval = {
                "checklist": request.checklist.model_dump(mode="json"),
                "approval_note": request.approval_note,
            }
            event = build_interaction_event(
                session_id=session_id,
                annotator_id=meta.annotator_id,
                sequence=store.next_sequence(session_id),
                action="FINALISE_SESSION",
                metadata=approval,
            )
            store.append_event(session_id, event, apply_to_working=False)
            meta = store.load_meta(session_id)
            meta.metadata["approval"] = approval
            store.save_meta(meta)

        final, meta = store.finalise(session_id)
        result = compute_metrics(store.load_initial(session_id), final, store.events(session_id), meta)
        store._atomic_json(store.session_dir(session_id) / "metrics.json", result)
        return {"session": meta.model_dump(mode="json"), "state": final.model_dump(mode="json"), "metrics": result}
    except Exception as exc:
        _http_error(exc)


@app.get("/api/sessions/{session_id}/export")
def export_session(session_id: str):
    try:
        meta = store.load_meta(session_id)
        initial = store.load_initial(session_id)
        final = store.load_final(session_id) or store.load_working(session_id)
        result = compute_metrics(initial, final, store.events(session_id), meta)
        store._atomic_json(store.session_dir(session_id) / "metrics.json", result)
        path = store.export_zip(session_id)
        return FileResponse(path, filename=f"annotation-session-{session_id}.zip", media_type="application/zip")
    except Exception as exc:
        _http_error(exc)


app.mount("/", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")
