# Canonical Annotation Schema

**Schema version:** `1.0`

This document defines the stable interchange and persistence format used by the Asepsis Annotation & Correction Tool.

The schema is deliberately producer-independent. BetterIngest/PaddleOCR output is converted through an adapter before the reviewer edits it.

## 1. Coordinate system

Canonical bounding boxes use normalized source-PDF page coordinates with a top-left origin:

```json
{
  "x0": 0.10,
  "y0": 0.20,
  "x1": 0.70,
  "y1": 0.35
}
```

Required invariant:

```text
0 <= x0 < x1 <= 1
0 <= y0 < y1 <= 1
```

Normalization makes annotations independent of:

- OCR render scale
- browser zoom
- screen resolution
- rendered image DPI

The canonical annotation must always refer to the source PDF page, not to a browser-rendered bitmap.

## 2. Authoritative files

A session may contain the following records:

| File | Meaning |
|---|---|
| `source.pdf` | immutable source document |
| `machine_output.original.json` | exact uploaded machine JSON |
| `initial_state.json` | canonical machine state shown to reviewer |
| `events.jsonl` | append-only committed human interaction history |
| `working_state.json` | resumable current-state cache |
| `session.json` | session metadata/status/timing |
| `final_state.json` | frozen approved canonical state |
| `metrics.json` | derived evaluation metrics |

`working_state.json` is not an authoritative research record. It may be regenerated from `initial_state.json + events.jsonl`.

## 3. Canonical annotation state

`initial_state.json`, `working_state.json` and `final_state.json` use the same canonical state shape.

Example:

```json
{
  "schema_version": "1.0",
  "document": {
    "document_id": "doc-2ee34f16",
    "filename": "guideline.pdf",
    "pdf_sha256": "sha256-hex",
    "page_count": 12,
    "pages": [
      {
        "page_index": 0,
        "width": 595.3,
        "height": 841.9
      }
    ]
  },
  "pipeline": {
    "name": "BetterIngest",
    "version": null,
    "ocr_engine": "PaddleOCR/PP-DocLayoutV3",
    "adapter": "betteringest-layout-review-v1",
    "metadata": {
      "ocr_scale": 2.0
    }
  },
  "regions": [
    {
      "region_id": "75e5a322-f3de-4f3c-946c-c76f57d69cc2",
      "source_region_id": "block:p0:i4",
      "page": 0,
      "bbox": {
        "x0": 0.10,
        "y0": 0.20,
        "x1": 0.80,
        "y1": 0.30
      },
      "type": "paragraph_title",
      "text": "2 Methods",
      "reading_order": 4,
      "heading_level": 1,
      "heading_level_source": null,
      "heading_level_uncertain": false,
      "origin": "machine",
      "ignored": false,
      "uncertain": false,
      "note": null,
      "metadata": {}
    }
  ]
}
```

## 4. Document object

Recommended fields:

| Field | Type | Notes |
|---|---|---|
| `document_id` | string | stable application/document identifier |
| `filename` | string | display filename only; not a trusted filesystem path |
| `pdf_sha256` | string | hash of the reviewed source PDF |
| `page_count` | integer | number of source PDF pages |
| `pages` | array | page geometry metadata |

Each page entry contains:

```json
{
  "page_index": 0,
  "width": 595.3,
  "height": 841.9
}
```

`page_index` is zero-based unless a later schema version explicitly changes this rule.

## 5. Pipeline object

The `pipeline` object records provenance of the machine annotation that was canonicalized.

Example:

```json
{
  "name": "BetterIngest",
  "version": null,
  "ocr_engine": "PaddleOCR/PP-DocLayoutV3",
  "adapter": "betteringest-layout-review-v1",
  "metadata": {
    "ocr_scale": 2.0
  }
}
```

Producer-specific information belongs under `metadata` rather than becoming mandatory canonical fields unless it is needed by the reviewer/domain model.

The exact producer payload remains separately preserved in `machine_output.original.json`.

## 6. Region object

Core fields:

| Field | Type | Meaning |
|---|---|---|
| `region_id` | UUID/string | stable canonical region identity |
| `source_region_id` | string/null | producer lineage identifier |
| `page` | integer | zero-based source page |
| `bbox` | object | normalized canonical box |
| `type` | string | current region class |
| `text` | string/null | OCR/reviewer text |
| `reading_order` | integer/null | order on/through document representation |
| `heading_level` | integer/null | inferred/approved structural level |
| `heading_level_source` | string/null | provenance of heading-level decision |
| `heading_level_uncertain` | boolean | machine structural uncertainty |
| `origin` | string | `machine` or `human` |
| `ignored` | boolean | excluded from approved downstream representation |
| `uncertain` | boolean | reviewer uncertainty flag |
| `note` | string/null | reviewer note |
| `metadata` | object | non-canonical extension metadata |

### 6.1 Identity rules

Machine regions:

```json
{
  "origin": "machine",
  "source_region_id": "block:p3:i8"
}
```

Human-created regions:

```json
{
  "origin": "human",
  "source_region_id": null
}
```

A `region_id` must remain stable for the lifetime of a region and must not be reused for a different region.

### 6.2 Type vocabulary

The canonical schema permits producer/application-defined string region types, for example:

```text
text
paragraph_title
figure
table
caption
```

The application may constrain the selectable vocabulary in the UI.

Unknown producer labels should be mapped deliberately by the adapter rather than silently discarded.

## 7. Raw machine output

`machine_output.original.json` preserves the uploaded machine JSON bytes and is never overwritten by reviewer actions.

It answers:

> What exactly did the producer supply?

`initial_state.json` answers:

> What canonical annotation state did the review application interpret and present?

These records must remain separate because canonicalization may normalize coordinates, identifiers, field names or metadata.

## 8. Event log

`events.jsonl` contains one JSON object per line.

Each event represents one committed semantic interaction.

Example:

```json
{
  "event_id": "40f45aa0-c504-4863-95fa-f4906876e940",
  "session_id": "18dde386-2dd4-4bda-8e72-66ff8b411e6c",
  "sequence": 8,
  "timestamp_utc": "2026-08-20T17:30:00.000Z",
  "annotator_id": "reviewer-01",
  "action": "RESIZE_REGION",
  "mutates_state": true,
  "target_region_ids": [
    "75e5a322-f3de-4f3c-946c-c76f57d69cc2"
  ],
  "page": 2,
  "before": {
    "regions": [
      {
        "region_id": "75e5a322-f3de-4f3c-946c-c76f57d69cc2",
        "bbox": {
          "x0": 0.10,
          "y0": 0.20,
          "x1": 0.70,
          "y1": 0.35
        }
      }
    ]
  },
  "after": {
    "regions": [
      {
        "region_id": "75e5a322-f3de-4f3c-946c-c76f57d69cc2",
        "bbox": {
          "x0": 0.10,
          "y0": 0.20,
          "x1": 0.75,
          "y1": 0.36
        }
      }
    ]
  },
  "target_event_id": null,
  "reason_code": null,
  "metadata": {}
}
```

## 9. Event fields

| Field | Type | Requirement |
|---|---|---|
| `event_id` | UUID/string | unique event identity |
| `session_id` | UUID/string | owning session |
| `sequence` | integer | monotonically increasing session-local order |
| `timestamp_utc` | datetime string | UTC timestamp |
| `annotator_id` | string | reviewer identity/pseudonym |
| `action` | string | semantic action name |
| `mutates_state` | boolean | whether canonical state changes |
| `target_region_ids` | array | affected region IDs |
| `page` | integer/null | relevant page when applicable |
| `before` | object/null | complete prior affected snapshot |
| `after` | object/null | complete resulting affected snapshot |
| `target_event_id` | UUID/string/null | used for undo/redo linkage where applicable |
| `reason_code` | string/null | optional structured reason |
| `metadata` | object | extension data |

Complete affected snapshots are intentionally preferred over minimal field-only deltas. The extra storage cost is acceptable for the MVP and simplifies replay, audit and future metrics.

## 10. Semantic actions

The implementation's event vocabulary should remain explicit and versioned.

Representative state-changing actions include:

```text
CREATE_REGION
DELETE_REGION
MOVE_REGION
RESIZE_REGION
RECLASSIFY_REGION
EDIT_TEXT
CHANGE_HEADING_LEVEL
CHANGE_READING_ORDER
IGNORE_REGION
RESTORE_REGION
MARK_UNCERTAIN
ADD_NOTE
```

History/control actions include:

```text
UNDO
REDO
```

The serialized implementation is authoritative if action naming differs slightly. Adding new action types must not change the meaning of previously written events.

## 11. Event commit boundary

Raw browser activity is not persisted as domain events.

Example resize:

```text
pointer down
pointer move
pointer move
pointer move
pointer up
```

produces:

```text
one committed RESIZE_REGION event
```

This ensures event counts reflect meaningful reviewer operations rather than browser frame/input frequency.

## 12. Undo and redo

Undo/redo append new events and never remove historical lines.

A reversal event links to the relevant prior event through `target_event_id` where implemented.

This preserves both:

- final state correctness;
- actual human interaction history.

## 13. Session metadata

`session.json` contains operational/research metadata for a review.

Typical concepts include:

```json
{
  "session_id": "18dde386-2dd4-4bda-8e72-66ff8b411e6c",
  "annotator_id": "reviewer-01",
  "status": "active",
  "created_at": "2026-08-20T17:00:00.000Z",
  "approved_at": null,
  "schema_version": "1.0",
  "application_version": "1.0.0"
}
```

The exact implementation may include additional timing, hash or checklist metadata.

Session status is conceptually:

```text
active -> approved
```

Approved sessions are immutable through normal annotation APIs.

## 14. Approval checklist

Approval metadata records the reviewer's confirmation that the common stopping condition was applied.

The MVP checklist covers:

1. every page reviewed;
2. missing/spurious regions checked;
3. region boundaries checked/corrected;
4. region classes checked/corrected;
5. heading levels and reading order checked where applicable;
6. remaining uncertainty marked/noted.

An optional approval note may record remaining limitations.

Checklist completion does not alter the historical machine state and should not silently modify region data.

## 15. Final state

`final_state.json` is a complete canonical annotation state, not a patch.

It is written only after approval validation succeeds.

Integrity requirement:

```text
replay(initial_state.json, events.jsonl) == final_state.json
```

The comparison is semantic/canonical, not byte-for-byte JSON serialization equality.

## 16. Metrics file

`metrics.json` contains derived values and is not the sole source of research evidence.

Metrics may include:

- initial/final region counts;
- regions added/deleted/changed;
- geometry changes;
- classification/text/structure/order changes;
- corrected-region rate;
- committed edit-event count;
- undo/redo count;
- active review time;
- active review time per page;
- replay integrity status.

Metric definitions may evolve while raw states/events remain stable.

## 17. Validation rules

At minimum:

### State

- `schema_version` must be recognized;
- document page count must match page metadata;
- every region must reference a valid page;
- every region ID must be unique;
- bounding boxes must satisfy canonical coordinate invariants;
- machine/human origin must be valid;
- approved states must be internally valid.

### Events

- `event_id` must be unique;
- `session_id` must match the owning session;
- sequences must be ordered/continuous according to implementation rules;
- target region IDs must be valid for the event context;
- before/after snapshots must be sufficient to replay the action;
- timestamps must be parseable UTC values;
- no state mutation is accepted after approval.

### Finalisation

- checklist requirements must be satisfied;
- replay must reproduce the final/current state;
- final state is written once and becomes read-only.

## 18. Schema evolution

Backward compatibility rules:

1. never reinterpret the meaning of an existing field in place;
2. add optional fields with safe defaults when possible;
3. add new action names rather than overloading old event semantics;
4. bump `schema_version` for incompatible canonical changes;
5. retain adapter/version metadata so historical producer inputs remain interpretable;
6. never rewrite historical `events.jsonl` merely to match a newer schema.

Migration tooling, if needed later, should produce a new derived representation while retaining the original session export.

## 19. Producer adapter contract

A producer adapter must:

1. validate the incoming producer payload;
2. preserve the original payload separately;
3. identify source PDF page geometry;
4. map producer region labels;
5. convert producer bounding boxes into canonical normalized coordinates;
6. produce stable `region_id`s;
7. retain `source_region_id` lineage where possible;
8. retain relevant producer metadata without polluting core canonical fields;
9. fail explicitly when coordinates/pages cannot be interpreted safely.

The annotation UI should depend only on the canonical state after this boundary.

## 20. Example lifecycle

```text
PDF + BetterIngest review JSON
            |
            v
machine_output.original.json
            |
         adapter
            |
            v
initial_state.json
            |
      reviewer events
            |
            +------> events.jsonl
            |
            v
working_state.json
            |
      final checklist
            |
       replay check
            |
            v
final_state.json
            |
            v
metrics.json / export
```
