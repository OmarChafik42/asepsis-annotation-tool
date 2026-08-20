# Asepsis Annotation & Correction Tool

Standalone MVP for reviewing OCR/layout output before downstream ingestion.

It preserves three records separately:

- `initial_state.json` — canonical machine output shown to the reviewer
- `events.jsonl` — append-only committed human corrections/interactions
- `final_state.json` — frozen approved output

The raw uploaded machine JSON is also preserved as `machine_output.original.json`.

## Features

- PDF rendering with region overlays
- add, delete, move, resize and reclassify regions
- edit OCR text, heading level and reading order
- ignore/restore, uncertainty flag and reviewer notes
- undo/redo without deleting event history
- active review-time estimate and correction metrics
- required final review checklist
- replay validation before approval
- session ZIP export
- BetterIngest `prepare_layout_review()` adapter

## Run locally / PyCharm

Use Python **3.11+**.

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Open `http://127.0.0.1:8765`.

In PyCharm, open this folder as the project and run `run.py` with a Python 3.11+ interpreter.

## Try the mock data

Upload together:

```text
examples/mock/mock_document.pdf
examples/mock/mock_machine_output.json
```

See `examples/mock/README.md` for suggested corrections.

## Docker

Docker is the quickest way to make the MVP portable and deployable as one service.

```bash
docker compose up --build
```

Then open `http://localhost:8765`.

Session data is kept in the named Docker volume `annotation_data`.

For a remote/private deployment, place the service behind HTTPS and your institution's authentication/reverse proxy. Do not expose this unauthenticated to the public internet when using medical documents.

## Input

Create a session with:

1. source PDF
2. machine annotation JSON
3. annotator ID

Supported JSON formats:

- BetterIngest `prepare_layout_review()` output
- canonical schema in `docs/SCHEMA.md`

## Session files

```text
annotation-data/sessions/<session-id>/
├── source.pdf
├── machine_output.original.json
├── initial_state.json
├── events.jsonl
├── working_state.json
├── final_state.json        # after approval
├── session.json
├── metrics.json
└── render_cache/
```

`working_state.json` is a resume cache. The research records are the initial state, event history and approved final state.

Core integrity rule:

```text
replay(initial_state, events) == final_state
```

## BetterIngest bridge

```bash
python scripts/export_betteringest_review.py \
  --asepsis-root ../asepsis-prototype-main \
  --pdf /path/to/document.pdf \
  --out review.json
```

## Tests

```bash
pip install "pytest>=8,<9"
pytest -q
```

## Deployment scope

This is a research MVP. Docker makes it cloud-deployable as a **single application instance with persistent storage**. Production hospital deployment would additionally require institution-approved authentication, access control, encryption, backups and operational security.
