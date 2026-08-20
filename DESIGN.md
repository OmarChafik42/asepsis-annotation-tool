# Software Design: Asepsis Annotation & Correction Tool

**Status:** MVP architecture  
**Audience:** project developers, reviewers and future maintainers  
**Primary objective:** provide a reproducible human-review layer between machine document ingestion and downstream use.

## 1. Executive summary

The Asepsis Annotation & Correction Tool is a standalone browser-based application for reviewing OCR/layout output against the source PDF.

The design is intentionally optimized for a research MVP:

- deterministic provenance
- inspectable local persistence
- low operational complexity
- clean separation from the ingestion pipeline
- portability through Docker
- enough instrumentation to measure correction burden without coupling the editor to a fixed evaluation protocol

The central architectural invariant is:

```text
replay(initial_state, events) == final_state
```

The system preserves four distinct artifacts:

```text
machine_output.original.json   exact producer payload
initial_state.json             canonical machine state reviewed by the human
events.jsonl                   append-only committed human actions
final_state.json               frozen human-approved state
```

The first three are sufficient to reconstruct the review process. `final_state.json` is a materialized approved snapshot used for downstream consumption and integrity checking.

## 2. Goals and non-goals

### 2.1 Goals

The MVP SHALL:

1. render the source PDF and overlay machine-produced regions;
2. allow a reviewer to correct region geometry, classification and selected structural attributes;
3. preserve the original machine payload without modification;
4. persist a canonical initial state before human editing;
5. append one durable event for each committed semantic correction;
6. support undo/redo without deleting historical events;
7. allow interrupted sessions to be resumed;
8. require an explicit final-review checklist before approval;
9. freeze an approved final state;
10. verify that the approved state is reproducible from initial state + event history;
11. expose enough raw data to derive correction and interaction metrics later;
12. run natively for development and in Docker for cross-platform/private deployment.

### 2.2 Non-goals

The MVP does NOT attempt to provide:

- simultaneous collaborative editing of one session;
- user-account provisioning or role management;
- multi-stage clinical approval workflows;
- distributed transactions across multiple application replicas;
- large-scale document-management/search infrastructure;
- production-grade public-internet security controls;
- a hard-coded, study-specific evaluation protocol; the tool preserves raw review data so metrics can be derived and revised independently;
- direct dependency on PaddleOCR or BetterIngest internal Python classes; producer output is consumed through a versioned adapter and canonical schema.

Some of these can be added behind stable interfaces if the deployment or study later requires them.

## 3. Design principles

### 3.1 Preserve provenance before convenience

Machine state, human interaction history and approved state are separate records. Operational caches must never replace those records.

### 3.2 One authoritative mutation path

Committed annotation changes pass through the backend domain layer. The browser may hold transient UI state for dragging/editing, but durable state changes are represented as commands/events.

### 3.3 Append history; do not rewrite it

The event log is append-only. Undo/redo are new events, not destructive edits to prior history.

### 3.4 Canonicalize at the system boundary

Producer-specific JSON is converted once through an adapter into a stable annotation schema. The editor is therefore insulated from future ingestion-pipeline changes.

### 3.5 Keep the MVP operationally simple

A single FastAPI instance plus persistent file storage is sufficient for the expected research-scale workload. Distributed infrastructure is deferred until there is an actual concurrency/scale requirement.

## 4. High-level architecture

```text
                   +----------------------+
                   | Source PDF           |
                   | Machine annotation   |
                   +-----------+----------+
                               |
                               v
                   +----------------------+
                   | Input Adapter        |
                   | producer -> canonical|
                   +-----------+----------+
                               |
                               v
+----------------+    HTTP/JSON    +--------------------------+
| Browser UI     | <-------------> | FastAPI Application      |
| PDF viewer     |                 |                          |
| Region editor  |                 | API / session lifecycle  |
| Review/approve |                 | domain commands/events   |
+----------------+                 | replay / validation      |
                                   | metrics orchestration    |
                                   +------------+-------------+
                                                |
                                                v
                                   +--------------------------+
                                   | Session Repository       |
                                   | JSON / JSONL / PDF       |
                                   +--------------------------+
```

Docker packages this same application. Docker is a deployment/runtime boundary, not a separate application architecture.

## 5. Component responsibilities

### 5.1 Browser presentation layer

Primary files:

- `annotation_tool/static/index.html`
- `annotation_tool/static/style.css`
- `annotation_tool/static/app.js`

Responsibilities:

- render session list and review workspace;
- render PDF pages and region overlays;
- collect reviewer gestures/input;
- maintain transient interaction state;
- convert completed interactions into API commands;
- display errors, metrics and approval UI.

The frontend is not the system of record. A browser refresh may lose in-progress, uncommitted UI input but must not lose committed events.

### 5.2 HTTP/API layer

Primary file:

- `annotation_tool/app.py`

Responsibilities:

- validate HTTP input;
- create/open/list sessions;
- serve source/rendered pages;
- accept annotation commands;
- expose undo/redo/finalisation/export operations;
- enforce session status and request-level preconditions;
- translate domain/storage failures into API responses.

Business rules should remain in domain/storage modules rather than being duplicated in route handlers.

### 5.3 Domain layer

Primary file:

- `annotation_tool/domain.py`

Responsibilities:

- define how each semantic event transforms annotation state;
- create before/after event snapshots;
- replay event history deterministically;
- implement undo/redo semantics;
- reject invalid state transitions where applicable.

The domain layer is independent of browser implementation and file-storage layout.

### 5.4 Data models

Primary file:

- `annotation_tool/models.py`

Responsibilities:

- define canonical document/page/region models;
- define event records;
- define session metadata and command payloads;
- validate coordinates, identifiers and typed fields.

This module defines the stable in-process contract used by adapters, domain logic, storage and API endpoints.

### 5.5 Input adapters

Primary file:

- `annotation_tool/adapters.py`

Responsibilities:

- detect supported input shape;
- preserve producer metadata;
- map BetterIngest `prepare_layout_review()` output into the canonical schema;
- normalize bounding boxes into PDF-relative coordinates;
- assign/retain stable region lineage identifiers where available.

The adapter is the anti-corruption layer between 1(a) and the annotation application.

### 5.6 Persistence/repository layer

Primary file:

- `annotation_tool/storage.py`

Responsibilities:

- create UUID session directories;
- preserve immutable/raw session artifacts;
- append event records;
- materialize/load working state;
- persist final state and metrics;
- hash relevant artifacts;
- enforce path/session-ID safety;
- provide per-session synchronization;
- produce export ZIPs.

The current implementation is file-backed. The API/domain layers should not depend on filesystem details beyond this repository boundary.

### 5.7 Rendering

Primary file:

- `annotation_tool/rendering.py`

Responsibilities:

- render PDF pages for browser display;
- cache render artifacts;
- keep display rendering separate from canonical PDF coordinates.

Render cache content is disposable and must not be treated as research data.

### 5.8 Metrics

Primary file:

- `annotation_tool/metrics.py`

Responsibilities:

- derive correction burden from initial vs final/current state;
- derive interaction effort from event history;
- calculate review-time summaries;
- report replay/integrity results.

Metrics are derived outputs. Raw states/events are preserved so metrics can be changed or recomputed later.

## 6. Canonical data model

### 6.1 Coordinate model

All canonical bounding boxes use top-left-origin normalized page coordinates:

```text
0.0 <= x0 < x1 <= 1.0
0.0 <= y0 < y1 <= 1.0
```

This decouples annotation data from browser zoom, render DPI and OCR raster scale.

### 6.2 Region identity

Each region has a stable `region_id`.

Machine-originated regions should retain a producer lineage reference through `source_region_id` when available.

Human-created regions use:

```text
origin = "human"
source_region_id = null
```

Region IDs must not be reused after deletion.

### 6.3 Authoritative records

| Record | Purpose | Mutability |
|---|---|---|
| `machine_output.original.json` | Exact producer payload | immutable |
| `initial_state.json` | Canonical machine state presented for review | immutable |
| `events.jsonl` | Ordered committed human history | append-only |
| `final_state.json` | Approved canonical snapshot | write once |
| `session.json` | Session metadata/status/timing | mutable metadata |
| `working_state.json` | Resume cache/materialized active state | replaceable |
| `metrics.json` | Derived evaluation output | recomputable |
| `source.pdf` | Reviewed source | immutable |
| `render_cache/` | Browser rendering cache | disposable |

The authoritative research record is not `working_state.json`.

## 7. Session lifecycle

### 7.1 Create

Inputs:

- source PDF;
- machine annotation JSON;
- annotator ID.

The server:

1. validates upload size/type at the application boundary;
2. creates a UUID session;
3. stores `source.pdf`;
4. stores exact machine JSON bytes as `machine_output.original.json`;
5. converts machine output through the adapter;
6. writes the canonical `initial_state.json`;
7. writes `working_state.json`;
8. creates empty `events.jsonl`;
9. initializes `session.json`.

If canonicalization fails, no review should start with a partially initialized state.

### 7.2 Edit

The browser loads the current working state.

A completed semantic interaction generates one command. Example:

```text
pointer down -> many pointer moves -> pointer up
                                      |
                                      v
                              one RESIZE_REGION
```

The backend serializes the command into a timestamped event containing sufficient before/after state for deterministic replay.

The event is appended and the materialized `working_state.json` is updated.

### 7.3 Resume

Committed work is server-side.

After a page refresh or process restart, the session can be reopened from persisted state. `working_state.json` is a convenience cache; correctness should be recoverable from `initial_state.json + events.jsonl`.

### 7.4 Approve

Approval requires:

- active session status;
- completion of the final-review checklist;
- replayed event history matching the current working state;
- valid canonical final state.

The server writes `final_state.json`, records approval metadata, derives metrics and marks the session approved/read-only.

No annotation mutation is accepted after approval.

## 8. Event model

### 8.1 Event semantics

An event represents a **committed semantic user action**, not raw UI activity.

Representative actions include:

- `CREATE_REGION`
- `DELETE_REGION`
- `MOVE_REGION`
- `RESIZE_REGION`
- `RECLASSIFY_REGION`
- text edit
- heading-level change
- reading-order change
- ignore/restore
- uncertainty/note changes
- `UNDO`
- `REDO`
- finalisation metadata where implemented

The precise serialized action vocabulary is defined in `docs/SCHEMA.md` and the code models.

### 8.2 Before/after snapshots

Events store complete affected-region snapshots rather than only field deltas.

Trade-off:

- higher log size;
- simpler deterministic replay;
- simpler audit/debugging;
- easier future metric calculation;
- lower risk of schema-evolution ambiguity.

For the expected research-scale sessions, this is the preferred trade-off.

### 8.3 Undo/redo

Undo does not remove the original event.

Example:

```text
event 12: RECLASSIFY figure -> table
event 13: UNDO event 12     table -> figure
```

This distinction lets evaluation separately measure:

- final correction burden;
- actual reviewer interaction effort.

## 9. Consistency and concurrency

### 9.1 Supported concurrency model

The MVP supports:

- multiple independent sessions;
- multiple users reviewing different sessions.

The MVP does not support:

- two users collaboratively editing the same active session;
- multiple tabs safely co-editing the same active session;
- multiple FastAPI replicas concurrently mutating the same file-backed repository.

Operational rule:

> One active reviewer per session.

### 9.2 Same-session conflicts

The backend uses per-session synchronization and ordered event sequencing to avoid silently corrupting an event log.

If two stale clients attempt to mutate the same session, one request may be rejected or the later client may need to reload. This is preferable to silent last-write-wins corruption.

A future collaborative implementation would require explicit optimistic versioning or leases plus identity-aware commands and merge/conflict semantics.

### 9.3 Multi-instance deployment

File locks are process-local and are not a distributed coordination primitive.

Therefore the Docker/cloud MVP must run as a **single application instance/worker** against its persistent storage.

A multi-instance architecture would require a transactional shared repository such as PostgreSQL plus appropriate object storage for PDFs/artifacts.

## 10. Persistence and failure recovery

### 10.1 Durability expectations

A semantic edit is considered committed only after the backend accepts and persists it.

The browser should communicate save failures rather than assuming persistence.

### 10.2 Working-state recovery

`working_state.json` is a materialized resume cache. If it is lost or suspected to be inconsistent, the canonical recovery path is:

```text
initial_state.json
        +
events.jsonl
        |
        v
replayed working state
```

### 10.3 Final-state integrity

Before approval:

```text
replay(initial_state, events) == working_state
```

After approval:

```text
replay(initial_state, events) == final_state
```

The equality comparison should be canonical/semantic rather than dependent on JSON formatting or key order.

## 11. Evaluation instrumentation

The system intentionally captures raw evidence before committing to a single study metric.

### 11.1 Final correction burden

Derived from initial vs final state, for example:

- regions added/deleted;
- regions materially changed;
- geometry corrections;
- classification corrections;
- OCR text corrections;
- hierarchy/order corrections;
- corrected-region rate.

### 11.2 Interaction effort

Derived from event history, for example:

- committed edit-event count;
- repeated edits to the same region;
- undo/redo count;
- interaction distribution by action type.

One region resized five times may count as:

```text
1 final corrected region
5 interaction events
```

### 11.3 Time

Active-review time is kept separate from edit count.

The timing metric is an approximation suitable for the MVP and should not be presented as precise cognitive effort.

### 11.4 Approval standard

The checklist makes the project's "satisfactory" state operationally more consistent by requiring review of:

- all pages;
- missing/spurious regions;
- region boundaries;
- region classes;
- heading level/reading order where applicable;
- remaining uncertainty.

The checklist is not a substitute for an independent quality audit; it defines a common stopping condition for the reviewer.

## 12. API design principles

The HTTP API should remain resource/session oriented.

Desired properties:

- session IDs are validated UUIDs;
- active/approved status is enforced server-side;
- mutation endpoints are idempotent only where explicitly designed;
- file paths are never accepted directly from untrusted client input;
- upload limits are enforced;
- API responses expose stable domain data, not filesystem implementation details;
- approved sessions reject further mutation.

The browser should not require direct filesystem access.

## 13. Deployment

### 13.1 Native development

```text
Browser -> 127.0.0.1 FastAPI -> ./annotation-data
```

Best for PyCharm development and debugging.

### 13.2 Docker

```text
Browser
   |
   v
published port
   |
Docker container
   |
   +-- FastAPI
   +-- application code
   |
   v
/data
   |
named persistent Docker volume
```

Docker provides:

- consistent Python version;
- reproducible dependencies;
- cross-platform execution;
- straightforward private-server deployment.

Docker does not itself provide authentication, authorization, data-governance or clinical compliance.

### 13.3 Private remote deployment

Recommended MVP topology:

```text
Reviewer browser
      |
    HTTPS
      |
institution auth / reverse proxy
      |
single Asepsis application container
      |
persistent approved storage
```

Run one application instance unless the storage/concurrency design is upgraded.

## 14. Security and privacy

The current tool is a research MVP and should be treated accordingly.

Required controls before using real sensitive medical documents in a remote environment include institution-approved:

- authentication;
- authorization;
- TLS/HTTPS;
- storage encryption;
- backup/retention policy;
- access logging;
- secrets management;
- host/network controls.

Repository policy:

- commit source code and synthetic mock data only;
- never commit `annotation-data/`;
- never commit real session exports;
- never commit `.env`, credentials, keys or tokens.

Session export contains the source PDF and should be treated with the same sensitivity as the original document.

## 15. Scalability boundaries

The file-backed model is intentionally appropriate for a small research study.

Expected pain points as scale grows:

1. unbounded session listing;
2. many rendered-page cache files;
3. same-session coordination;
4. multi-process/multi-instance mutation;
5. centralized access control;
6. backup/query requirements.

Evolution path:

```text
Current
FastAPI + file repository + persistent volume

Next
FastAPI + repository interface
        + PostgreSQL session/event metadata
        + object storage for PDFs/exports

Later, only if required
multiple replicas + distributed coordination + role/workflow services
```

Do not adopt the later architecture until the workload requires it.

## 16. Testing strategy

### 16.1 Domain tests

Verify:

- each event produces the expected state;
- invalid state transitions are rejected;
- replay is deterministic;
- undo/redo preserve history;
- final state can be reconstructed.

### 16.2 Adapter tests

Verify:

- BetterIngest input converts correctly;
- canonical input remains semantically stable;
- coordinates are normalized correctly;
- page/region identifiers are valid;
- malformed inputs fail explicitly.

### 16.3 Storage tests

Verify:

- session creation writes required files;
- original machine payload is preserved;
- events append in order;
- path/session-ID validation prevents unsafe access;
- approved state cannot be mutated;
- export includes intended research artifacts.

### 16.4 End-to-end smoke test

At minimum:

```text
create session
-> render PDF
-> correct region
-> persist event
-> refresh/reopen
-> approve
-> verify replay
-> export
```

Run this against both the synthetic mock data and representative real 1(a) output.

## 17. Observability and operations

For the MVP:

- application startup/shutdown should be visible in logs;
- failed session mutations should log session ID and error class without dumping sensitive PDF/text content;
- health endpoints should expose service status/version, not internal filesystem paths;
- disk/volume capacity must be monitored in remote deployments because PDFs and render caches can grow independently of event-log size.

Avoid logging OCR text or document contents by default in a medical-document environment.

## 18. Key design decisions

| Decision | Choice | Rationale |
|---|---|---|
| UI | Browser | cross-platform, simple deployment |
| API | FastAPI | existing Python ecosystem and ingestion compatibility |
| Persistence | JSON/JSONL + PDF | inspectable, low complexity, research-friendly |
| History | append-only semantic events | provenance and reproducibility |
| State | initial + working + final | separate truth from operational cache |
| Coordinates | normalized PDF coordinates | render/device independence |
| Input integration | adapter | decouple 1(a) implementation |
| Deployment | native + Docker | developer convenience + portability |
| Concurrency | one reviewer per session | avoids premature collaboration complexity |
| Scale | single instance | matches MVP/file-store assumptions |

## 19. Acceptance criteria for the MVP

The MVP is considered functionally ready when all of the following hold:

1. a source PDF + supported machine JSON can create a session;
2. overlays align with the corresponding PDF regions for representative 1(a) documents;
3. supported corrections persist across refresh/reopen;
4. events are append-only and semantically replayable;
5. initial machine state cannot be overwritten through normal review operations;
6. approval requires the checklist;
7. approved sessions become read-only;
8. replay produces the approved final state;
9. export contains the intended research artifacts;
10. automated tests and a representative end-to-end smoke test pass;
11. Docker and native execution produce equivalent application behavior.

## 20. Future work

Only add these when there is a concrete requirement:

- filename search/status filtering/pagination for large session lists;
- reviewer assignment and authentication;
- independent audit mode;
- PostgreSQL/object-storage repository;
- distributed locking/version checks;
- collaborative or sequential multi-review workflow;
- institution-specific SSO and deployment controls.
