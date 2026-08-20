# Software Design

## 1. Overview

The Asepsis Annotation & Correction Tool is a standalone review application for OCR/layout output.

Its primary responsibility is to preserve a reproducible human-review trail between machine ingestion and downstream use.

The system keeps the following records separate:

```text
machine_output.original.json   exact producer payload
initial_state.json             canonical machine state reviewed by the human
events.jsonl                   ordered committed human actions
final_state.json               approved canonical result
```

The central integrity invariant is:

```text
replay(initial_state, events) == final_state
```

## 2. Goals

The MVP must:

- display a source PDF and machine-produced regions
- allow common layout/structure corrections
- preserve the original machine payload
- preserve an immutable canonical initial state
- persist committed human actions as append-only events
- support undo/redo without deleting history
- resume interrupted sessions
- require a consistent approval checklist
- freeze the approved final state
- derive correction metrics without changing the raw review record
- run locally or as a single Dockerized service

## 3. Non-goals

The MVP does not provide:

- collaborative editing of one active session
- account/role management
- multi-stage clinical approval workflows
- distributed multi-instance coordination
- large-scale document-management infrastructure
- production public-internet security controls
- a fixed evaluation metric built into the annotation logic; metrics are derived from the preserved session data
- direct coupling to BetterIngest/PaddleOCR internals; their output is converted through an adapter into the tool’s canonical schema


## 4. Architecture

```text
PDF + machine JSON
        |
        v
+-------------------+
| Input adapter     |
| producer -> state |
+---------+---------+
          |
          v
+-------------------+      HTTP/JSON      +----------------------+
| Browser UI        | <-----------------> | FastAPI application  |
| PDF + correction  |                     | session/API logic    |
+-------------------+                     +----------+-----------+
                                                   |
                           +-----------------------+----------------------+
                           |                       |                      |
                           v                       v                      v
                    +-------------+         +-------------+       +-------------+
                    | Domain      |         | Metrics     |       | Rendering   |
                    | events/replay|        | derived data|       | PDF -> image|
                    +------+------+         +-------------+       +-------------+
                           |
                           v
                    +-------------+
                    | Storage     |
                    | JSON/JSONL  |
                    +-------------+
```

Docker packages the same application; it does not change the architecture.

## 5. Component responsibilities

### Browser UI

Files:

- `annotation_tool/static/index.html`
- `annotation_tool/static/style.css`
- `annotation_tool/static/app.js`

Responsibilities:

- display PDF pages and overlays
- collect reviewer input
- maintain transient interaction state
- send completed semantic edits to the backend
- display metrics, history and approval UI

The browser is not the system of record.

### API layer

File:

- `annotation_tool/app.py`

Responsibilities:

- create/list/open sessions
- serve rendered pages
- accept annotation commands
- expose undo/redo, approval and export
- enforce session status and request validation

### Domain layer

File:

- `annotation_tool/domain.py`

Responsibilities:

- define event/state transitions
- apply events
- replay history
- implement undo/redo semantics
- keep annotation behavior independent of storage and UI

### Models

File:

- `annotation_tool/models.py`

Responsibilities:

- define canonical documents, pages, regions, events and session metadata
- validate identifiers and typed fields

### Adapters

File:

- `annotation_tool/adapters.py`

Responsibilities:

- convert supported machine-output formats into the canonical state
- normalize coordinates
- preserve producer metadata and lineage

### Storage

File:

- `annotation_tool/storage.py`

Responsibilities:

- create UUID session directories
- preserve raw/initial/final artifacts
- append events
- persist resumable working state
- create exports
- validate session paths
- serialize same-process writes per session

### Rendering

File:

- `annotation_tool/rendering.py`

Responsibilities:

- render PDF pages for the browser
- maintain disposable render cache

### Metrics

File:

- `annotation_tool/metrics.py`

Responsibilities:

- derive correction burden from initial vs final/current state
- derive interaction effort from event history
- calculate timing summaries
- report replay integrity

Metrics are derived; raw states/events remain the source of truth.

## 6. Canonical state

Canonical regions use normalized PDF-page coordinates:

```text
0 <= x0 < x1 <= 1
0 <= y0 < y1 <= 1
```

This prevents browser zoom, render DPI and OCR raster scale from changing annotation meaning.

Each region has a stable `region_id`.

Machine regions should retain `source_region_id` where available. Human-created regions have `origin = "human"`.

See `docs/SCHEMA.md` for the exact data contract.

## 7. Session lifecycle

### Create

Inputs:

- source PDF
- machine JSON
- annotator ID

The application:

1. validates the request
2. converts machine JSON through the adapter
3. creates a UUID session
4. stores the source and raw machine payload
5. writes `initial_state.json`
6. writes `working_state.json`
7. creates `events.jsonl`
8. initializes `session.json`

### Edit

A completed semantic action produces one event.

Example:

```text
pointer down
pointer move
pointer move
pointer up
    |
    v
one RESIZE_REGION event
```

The backend appends the event and updates the materialized working state.

### Resume

Committed edits are stored server-side.

After refresh/restart, the session can be reopened from persisted state.

The replay implementation can reconstruct canonical state from:

```text
initial_state.json + events.jsonl
```

`working_state.json` is a resume cache; the MVP does not automatically repair a stale/corrupt cache on startup.

### Approve

Approval requires:

- active session
- completed review checklist
- replayed event state matching current state
- valid final canonical state

The application writes `final_state.json`, records approval metadata and makes the session read-only.

## 8. Event model

An event represents a committed semantic action, not raw browser activity.

Examples include:

```text
CREATE_REGION
DELETE_REGION
MOVE_REGION
RESIZE_REGION
RECLASSIFY_REGION
UPDATE_TEXT
CHANGE_HEADING_LEVEL
CHANGE_READING_ORDER
IGNORE_REGION
RESTORE_REGION
MARK_UNCERTAIN
ADD_NOTE
UNDO
REDO
```

Events store before/after affected-region snapshots.

This uses slightly more storage than minimal deltas but makes replay, audit and later metric calculation simpler.

Undo/redo append new events instead of removing old ones.

## 9. Consistency and concurrency

### Supported

- multiple independent sessions
- multiple reviewers working on different sessions

### Not supported

- simultaneous collaborative editing of the same active session
- multiple application workers/replicas writing to the same file-backed store

Operational rule:

> One active reviewer per session.

The backend uses a process-local per-session lock and ordered event sequences to protect event-log writes.

This is not full stale-client conflict detection. The client does not send a state revision/ETag with every command, so two stale tabs can still overwrite each other's field values in later requests.

A collaborative version would need optimistic versioning or session leases.

## 10. Persistence and integrity

Authoritative/relevant records:

| Record | Purpose |
|---|---|
| `source.pdf` | reviewed source |
| `machine_output.original.json` | exact producer payload |
| `initial_state.json` | immutable canonical machine state |
| `events.jsonl` | append-only human history |
| `final_state.json` | approved canonical state |
| `session.json` | metadata/status/timing |
| `metrics.json` | derived evaluation output |

Operational records:

| Record | Purpose |
|---|---|
| `working_state.json` | resume cache |
| `render_cache/` | disposable page rendering |

Before/at approval:

```text
replay(initial_state, events) == current/final state
```

The current implementation compares canonical model dumps rather than JSON text formatting.

## 11. Evaluation instrumentation

The system stores raw review evidence so metrics can be changed later without changing annotation history.

### Correction burden

Examples:

- added/deleted regions
- geometry changes
- type changes
- OCR text changes
- heading/order changes
- corrected-region rate

### Interaction effort

Examples:

- committed edit count
- repeated edits to the same region
- undo/redo count
- action-type distribution

These are intentionally separate.

One region resized five times can be:

```text
1 final corrected region
5 interaction events
```

### Time

Active time is an estimate derived from reviewer activity and should be treated as a workflow metric, not exact cognitive effort.

### Approval checklist

The checklist gives reviewers a common stopping condition:

- all pages reviewed
- missing/spurious regions checked
- boundaries checked
- types checked
- heading/order checked where applicable
- remaining uncertainty documented

## 12. Deployment

### Native

```text
Browser -> FastAPI -> ./annotation-data
```

Best for development/debugging.

### Docker

```text
Browser -> containerized FastAPI -> persistent Docker volume
```

Docker provides:

- consistent Python/dependency versions
- cross-platform execution
- simple private deployment

The MVP should run as one application instance/worker.

For remote medical-document use, deploy behind institution-approved HTTPS, authentication, access control and storage/backup policies.

## 13. Scale boundaries

The file-backed architecture is appropriate for a small research study.

Likely first scale issues:

- large unfiltered session list
- many PDF/render-cache files
- same-session concurrency
- multiple application replicas
- centralized user/access management

If needed later, evolve toward:

```text
FastAPI
  |
  +-- PostgreSQL for session/event metadata
  +-- object storage for PDFs/exports
```

Do not add this complexity until the workload requires it.

## 14. Testing

The MVP should cover:

### Domain

- event application
- deterministic replay
- undo/redo
- invalid state transitions

### Adapter

- BetterIngest conversion
- coordinate normalization
- malformed input handling

### Storage

- session creation
- raw machine-output preservation
- ordered event append
- path/session validation
- final-state immutability
- export contents

### End-to-end smoke test

```text
create
-> render
-> edit
-> persist
-> refresh/reopen
-> approve
-> replay validate
-> export
```

Test this with both synthetic mock data and representative real 1(a) output.

## 15. Key decisions

| Decision | Choice | Reason |
|---|---|---|
| UI | browser | cross-platform and simple |
| API | FastAPI | Python integration and low complexity |
| Persistence | JSON/JSONL + PDF | inspectable and research-friendly |
| History | append-only semantic events | provenance and replay |
| Coordinates | normalized PDF coordinates | render independence |
| Integration | adapter + canonical schema | decouple ingestion internals |
| Concurrency | one reviewer/session | sufficient for MVP |
| Deployment | native + Docker | development + portability |
| Scale | single instance | matches file-backed storage |

## 16. MVP acceptance criteria

The MVP is ready when:

1. supported PDF + machine JSON creates a session
2. region overlays align correctly on representative documents
3. supported edits persist across refresh/reopen
4. initial state remains unchanged
5. event history is append-only and replayable
6. approval requires the checklist
7. approved sessions are read-only
8. replay matches the approved final state
9. export contains the intended research artifacts
10. automated tests and an end-to-end smoke test pass
11. native and Docker execution behave equivalently
