# Software Design

## 1. Goal

Provide a small standalone review tool for OCR/layout output that can also support evaluation of correction burden.

The main requirement is to preserve independently:

1. machine-produced state
2. committed human interaction history
3. human-approved final state

## 2. Architecture

```text
PDF + machine JSON
        |
        v
+------------------------+
| Browser UI             |
| PDF + region editing   |
+-----------+------------+
            |
            | HTTP/JSON
            v
+------------------------+
| FastAPI application    |
| commands + events      |
| replay + validation    |
| metrics                |
+-----------+------------+
            |
            v
+------------------------+
| Session storage        |
| JSON / JSONL / PDF     |
+------------------------+
```

The input adapter isolates the annotation tool from the internal Python classes used by the ingestion pipeline.

## 3. Canonical state

Regions use stable IDs and normalized top-left PDF coordinates in `[0,1]`.

A region can contain:

- page and bounding box
- type and OCR text
- reading order
- heading level
- machine/human origin
- ignored/uncertain flags
- reviewer note

See `docs/SCHEMA.md`.

## 4. Session lifecycle

### Start

The application stores:

- `machine_output.original.json` — original uploaded JSON bytes
- `initial_state.json` — canonical immutable interpretation
- `working_state.json` — resumable current state
- empty `events.jsonl`

### Edit

Every committed semantic change creates one timestamped event with before/after region snapshots. Pointer movement is only a preview; one completed drag produces one event.

Undo and redo create additional events rather than removing history.

### Approve

The reviewer completes a short checklist covering page review, missing/spurious regions, boundaries, types, structure and remaining uncertainty.

Approval is refused unless replaying the event history reproduces the working state. The approved snapshot is then written to `final_state.json` and becomes read-only.

## 5. Evaluation data

The MVP derives:

- initial/final region counts
- changed/deleted/added regions
- geometry, type, text, hierarchy and order corrections
- corrected-region rate
- committed edit-event count
- undo/redo count
- active review time per page
- replay integrity result

Final correction burden and interaction effort remain separate measures.

## 6. Storage and integrity

Local JSON/JSONL storage is intentional for the MVP because it is inspectable and easy to analyse in Python.

Important rules:

- initial and final states are separate snapshots
- event log is append-only
- session IDs are UUID validated
- final state is frozen after approval
- exports contain the research records and metrics

## 7. Deployment

Local development uses `python run.py`.

Docker packages the same application for a single-instance private deployment with persistent storage. Runtime configuration is provided through environment variables:

- `ANNOTATION_HOST`
- `ANNOTATION_PORT`
- `ANNOTATION_DATA_DIR`
- `ANNOTATION_MAX_PDF_MB`
- `ANNOTATION_MAX_JSON_MB`

A remote deployment should be placed behind HTTPS and institution-managed authentication. Multi-instance/database architecture is outside the MVP scope.

## 8. MVP boundary

Included: single-reviewer sessions, correction UI, provenance, approval, metrics and export.

Not included: collaborative editing, user-account management, multi-stage clinical review, database clustering or public-internet security controls.
