# Asepsis Annotation & Correction Tool

Standalone research MVP for human review and correction of OCR/layout output against the source PDF before documents are ingested into a structure-aware medical RAG pipeline.

The tool acts as a quality-control layer between document ingestion and downstream retrieval, particularly where document hierarchy and layout matter, including tree-based retrieval systems such as PageIndex.

To support reproducibility and evaluation, each review session preserves three records separately:

```text
initial_state.json   canonical machine state shown to the reviewer
events.jsonl         append-only committed human corrections
final_state.json     frozen approved state
```

The exact uploaded machine JSON is also preserved as `machine_output.original.json`.

> **Run commands in this README from the repository root.** The annotation tool code lives in `annotation_tool/`, while `run.py`, dependency files, tests, and Docker files remain at the repository root.

## Features

- render PDFs with region overlays
- add, delete, move, resize and reclassify regions
- edit OCR text, heading level and reading order
- ignore/restore regions
- mark uncertainty and add notes
- undo/redo without deleting event history
- resume active sessions after refresh/restart
- required approval checklist
- correction metrics and active-time estimate
- session export
- BetterIngest and MinerU model-output adapters
- separate Layout/OCR edit layers to prevent overlapping sentence boxes from blocking structural annotation
- autosave for inspector edits, with pending changes flushed before navigation/final approval
- native or Docker execution

## Quick start with Docker

Docker is the recommended cross-platform path for Windows, macOS and Linux.

Requirements:

- Docker Desktop on Windows/macOS, or Docker Engine + Compose on Linux

From the repository root:

```bash
docker compose up --build
```

Open:

```text
http://localhost:8765
```

Stop:

```bash
docker compose down
```

Session data is stored in the repo-local bind mount `./data:/data`, so annotated output lands under `data/<document>/auto/sessions/...` and survives normal container rebuilds/restarts.

To keep host-file ownership aligned with your user account, set `UID` and `GID` in `.env` (or export them in your shell before starting Docker).

`docker compose down -v` removes Compose-managed volumes, but it does not delete the host `./data` directory used by this bind mount. Treat `./data` as persistent local research data and back it up separately.

## Native development

Use Python **3.11+**.

The examples below explicitly use `data/` as the annotation dataset:

```text
python run.py --data-dir data
```

### Windows / PyCharm

Run these commands from the **repository root**:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py --data-dir data
```

Open:

```text
http://127.0.0.1:8765
```

In PyCharm, open the **repository root** as the project, select the `.venv` interpreter, and create a Python run configuration with:

- **Script path:** `<repository-root>\run.py`
- **Parameters:** `--data-dir data`
- **Working directory:** `<repository-root>`

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py --data-dir data
```

Open:

```text
http://127.0.0.1:8765
```

## MinerU dataset input

The dataset-first UI discovers documents under:

```text
data/<document>/auto/
    <document>_origin.pdf
    <document>_model.json
```

If exactly one `*_origin.pdf` and one `*_model.json` are present in the `auto/` directory, the tool can also discover them when their filename prefix differs from the document directory name.

The MinerU adapter imports both semantic layout detections and sentence/line-level `ocr_text` detections into the canonical annotation state. The UI keeps both available without forcing them into the same interactive layer:

- **Layout** edit mode: structural regions are editable; OCR boxes can be shown as reference overlays.
- **OCR** edit mode: `ocr_text` boxes become editable; layout boxes remain visible but do not capture clicks.
- discrete inspector changes autosave immediately; text and notes save after a 700 ms typing pause and are flushed before page changes, undo/redo, leaving the session, deletion and final approval.

The backend also accepts compatible BetterIngest/canonical uploads through its session API; the current homepage is dataset-first.

## Supported machine JSON formats

- MinerU `*_model.json` output
- BetterIngest layout-review JSON containing `detected_assets` / `non_assets`
- canonical annotation state described in [`docs/SCHEMA.md`](docs/SCHEMA.md)

## Session lifecycle

### Create

The server creates an independent UUID session and stores the source PDF, raw machine JSON, canonical initial state and an empty event log.

### Review

Each completed semantic edit is persisted by the backend.

For example, a drag may contain many pointer movements in the browser, but it produces one committed `MOVE_REGION` or `RESIZE_REGION` event when the action finishes.

Refreshing the browser does not remove committed work. Reopen the session from the home page to continue.

### Approve

The reviewer completes the final checklist. Approval succeeds only if the current state can be reproduced from the initial state and event history.

Core integrity rule:

```text
replay(initial_state, events) == final_state
```

Approved sessions become read-only.

## Session files

When running with:

```bash
python run.py --data-dir data
```

sessions are stored under:

```text
data/<document>/auto/sessions/<session-id>/
```

Typical contents:

```text
source.pdf
machine_output.original.json
initial_state.json
events.jsonl
working_state.json
session.json
final_state.json
metrics.json
render_cache/
```

`working_state.json` and `render_cache/` are operational files. The research-relevant records are the source, raw machine output, initial state, event history, approved final state, session metadata and derived metrics.

## Multiple documents and reviewers

Each review is stored as a separate session. A document can have multiple sessions.

Multiple reviewers can work on different sessions at the same time.

The MVP does not support collaborative editing of the same active session. Use one reviewer per active session.

The current home page lists documents discovered from the configured dataset directory and opens their available annotation sessions. This is suitable for a research-scale dataset; pagination/search/filtering should be added if the dataset becomes large.

## Tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run:

```bash
pytest -q
```

## Deployment scope

The Docker deployment is intended for a **single application instance with persistent storage**.

For remote use with medical documents, place the service behind institution-approved HTTPS, authentication, access control and storage policies.

Docker provides portability; it does not by itself provide those security controls.

## Repository hygiene

Treat `data/` as the annotation tool's local working dataset and session storage.

Do not commit private or sensitive documents placed there unless they are intentionally part of a public research dataset with appropriate permission and licensing.

Do not commit:

- `.env`
- credentials, keys or tokens
- `.venv/`
- `.idea/`
- unintended local runtime/session artifacts

The repository-level reproducibility datasets, if present, should be documented and licensed separately from the annotation tool's local `data/` directory.

## Documentation

- [`DESIGN.md`](DESIGN.md) — architecture and key engineering decisions
- [`docs/SCHEMA.md`](docs/SCHEMA.md) — canonical state and event formats
