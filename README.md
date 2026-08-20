# Asepsis Annotation & Correction Tool

Standalone research MVP for reviewing OCR/layout output before downstream ingestion.

The tool is designed around one core provenance requirement: keep the machine output, the committed human correction history, and the approved output independently recoverable.

```text
machine_output.original.json   exact uploaded machine output
initial_state.json             canonical state shown to the reviewer
events.jsonl                   append-only committed human actions
final_state.json               frozen approved state
```

`working_state.json` exists only to support resume/recovery while a review is active.

## Features

- PDF rendering with region overlays
- add, delete, move, resize, ignore and restore regions
- reclassify regions
- edit OCR text
- edit heading level and reading order
- mark uncertainty and add reviewer notes
- undo/redo without deleting prior history
- active review-time estimate
- correction metrics
- required final review checklist
- replay validation before approval
- session ZIP export
- BetterIngest `prepare_layout_review()` adapter
- local native execution or Docker deployment

## Quick start with Docker

Docker is the recommended way to run the project across Windows, macOS and Linux because every reviewer gets the same Python runtime and dependencies.

Prerequisite: Docker Desktop on Windows/macOS, or Docker Engine + Compose on Linux.

```bash
git clone <repository-url>
cd asepsis-annotation-tool
docker compose up --build
```

Open:

```text
http://localhost:8765
```

Stop the service with:

```bash
docker compose down
```

Session data is stored in the named Docker volume `annotation_data` and survives normal container rebuilds/restarts.

> Do not run `docker compose down -v` unless you intentionally want to delete the Docker volume and all annotation sessions stored in it.

### Where Docker stores data

Inside the container the application writes to the configured data directory, typically `/data`. Docker maps that directory to the persistent `annotation_data` volume.

The volume is managed by Docker, so you should not expect to see an `annotation-data/` folder beside the source code when using the Docker deployment.

## Native development

Use Python **3.11+**.

### Windows / PyCharm

Create or select a Python 3.11+ interpreter. Python 3.12 is recommended.

PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

Open:

```text
http://127.0.0.1:8765
```

In PyCharm, open the repository root as the project. Do not create another project inside the repository. Point the project interpreter to `.venv` and run `run.py`.

If PowerShell blocks virtual-environment activation, either use PyCharm's interpreter directly or use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Open:

```text
http://127.0.0.1:8765
```

## Try the mock data

The repository includes synthetic test data with deliberate annotation errors.

Upload these two files together:

```text
examples/mock/mock_document.pdf
examples/mock/mock_machine_output.json
```

Use an annotator ID such as:

```text
reviewer-01
```

The mock data can be used to test moving/resizing regions, reclassification, heading-level correction, deleting spurious regions, adding missing regions, undo/redo and final approval.

See `examples/mock/README.md` for the intended corrections.

## Input

A new review session requires:

1. source PDF
2. machine annotation JSON
3. annotator ID

Supported machine JSON inputs:

- BetterIngest `prepare_layout_review()` output
- the canonical state format documented in [`docs/SCHEMA.md`](docs/SCHEMA.md)

The source PDF and machine JSON are copied into the session when it is created. The original machine JSON is preserved separately from the canonical state produced by the input adapter.

## Session lifecycle

### 1. Create

The backend creates a UUID session directory and stores the PDF, raw machine JSON, canonical initial state, empty event log and resumable working state.

### 2. Review

The frontend loads one session at a time. Each completed semantic correction is sent to the backend and persisted immediately.

For example, dragging a box may involve many pointer-move events in the browser, but releasing the box produces one committed `MOVE_REGION` or `RESIZE_REGION` event.

Refreshing the browser does not delete committed work. Re-open the session from the home page to resume it.

### 3. Approve

The reviewer completes the final checklist. Approval succeeds only if the current state can be reproduced by replaying the event history from the initial state.

The approved state is then written to `final_state.json` and the session becomes read-only.

Core integrity rule:

```text
replay(initial_state, events) == final_state
```

## Session files

Native/local sessions are stored under:

```text
annotation-data/sessions/<session-id>/
```

Typical session contents:

```text
source.pdf
machine_output.original.json
initial_state.json
events.jsonl
working_state.json
session.json
final_state.json        # after approval
metrics.json            # after/around approval
render_cache/
```

Research-relevant records:

- `machine_output.original.json` — exactly what the producer supplied
- `initial_state.json` — normalized interpretation shown to the reviewer
- `events.jsonl` — ordered committed human interaction history
- `final_state.json` — approved snapshot
- `session.json` — session metadata/timing/status
- `metrics.json` — derived evaluation data
- `source.pdf` — reviewed source document

`working_state.json` and `render_cache/` are operational files, not authoritative research records.

## Multiple documents and reviewers

Each uploaded document/review is stored as an independent UUID session.

Multiple reviewers may work on different sessions at the same time.

The MVP does **not** support collaborative editing of the same active session. Assign one reviewer to one active session at a time. Opening the same active session in multiple tabs or by multiple reviewers can create stale frontend state and conflicting commands.

Approved sessions are read-only.

The current session list is intentionally simple and suited to a research-scale number of documents. If the repository is later used for a much larger corpus, add server-side pagination/search/filtering rather than loading an unbounded session list.

## BetterIngest bridge

To export review input from the existing ingestion project:

```bash
python scripts/export_betteringest_review.py \
  --asepsis-root ../asepsis-prototype-main \
  --pdf /path/to/document.pdf \
  --out review.json
```

On Windows PowerShell the same command can be written on one line:

```powershell
python scripts/export_betteringest_review.py --asepsis-root "..\asepsis-prototype-main" --pdf "C:\path\to\document.pdf" --out "review.json"
```

The annotation application does not import the ingestion pipeline's internal Python classes directly. The adapter converts producer output into the stable canonical schema.

## Tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run:

```bash
pytest -q
```

Useful validation scripts are also available under `scripts/`.

## Runtime configuration

The application supports environment-based runtime configuration, including:

```text
ANNOTATION_HOST
ANNOTATION_PORT
ANNOTATION_DATA_DIR
ANNOTATION_MAX_PDF_MB
ANNOTATION_MAX_JSON_MB
```

Use `.env.example` as documentation for local values. Do not commit a real `.env` containing credentials or environment-specific secrets.

## Docker and private deployment

The Docker image packages the same FastAPI/browser application used for local development.

For the MVP, deploy it as a **single application instance with persistent storage**.

A remote deployment should be placed behind:

- HTTPS
- institution-managed authentication/reverse proxy
- persistent storage
- institution-approved backup/retention controls

Do not expose this MVP directly to the public internet for medical-document use.

Docker makes the application portable and deployable; Docker itself does not provide authentication, authorization, encryption policy or clinical compliance.

## GitHub / repository hygiene

The repository should contain source code, documentation and synthetic mock data only.

Do not commit:

- `annotation-data/`
- real medical PDFs
- real exported session ZIPs
- `.env`
- API keys, passwords or tokens
- `.venv/`
- `.idea/`
- local database files or logs

Recommended `.gitignore` entries:

```gitignore
# Python
.venv/
__pycache__/
*.pyc
.pytest_cache/

# PyCharm
.idea/

# Runtime / research data
annotation-data/
*.zip
*.log
*.db
*.sqlite
*.sqlite3

# Secrets / local configuration
.env
.env.*
!.env.example

# OS
.DS_Store
Thumbs.db
```

Before every commit:

```bash
git status
```

To confirm local runtime folders are actually ignored:

```bash
git status --ignored
```

If real clinical data is ever used, follow the institution's approved storage and source-control policy even when the GitHub repository is private.

## Project documentation

- [`DESIGN.md`](DESIGN.md) — architecture, invariants, concurrency and deployment decisions
- [`docs/SCHEMA.md`](docs/SCHEMA.md) — canonical annotation and event formats

## MVP scope

Included:

- standalone single-reviewer review sessions
- OCR/layout correction UI
- provenance preservation
- resumable sessions
- approval checklist
- metrics
- research export
- Docker packaging

Not included:

- simultaneous collaborative editing of one session
- user-account management
- role-based clinical workflow
- multi-stage approval
- distributed/multi-instance coordination
- production hospital security controls
