# Canonical Annotation Schema

**Schema version:** `1.0`

The canonical schema is the stable format used by the annotation tool after producer-specific machine output has been converted by an adapter.

## 1. Coordinate system

Bounding boxes use normalized source-PDF coordinates with a top-left origin:

```json
{
  "x0": 0.10,
  "y0": 0.20,
  "x1": 0.70,
  "y1": 0.35
}
```

Invariant:

```text
0 <= x0 < x1 <= 1
0 <= y0 < y1 <= 1
```

The coordinates refer to the source PDF page, not a rendered browser image.

## 2. Session files

| File | Meaning |
|---|---|
| `source.pdf` | immutable source document |
| `machine_output.original.json` | exact uploaded machine JSON |
| `initial_state.json` | canonical machine state shown to reviewer |
| `events.jsonl` | append-only committed human actions |
| `working_state.json` | resumable current-state cache |
| `session.json` | session metadata/status/timing |
| `final_state.json` | approved canonical state |
| `metrics.json` | derived evaluation metrics |

`working_state.json` is operational. Canonical state can be reconstructed from `initial_state.json + events.jsonl`.

## 3. Canonical state

`initial_state.json`, `working_state.json` and `final_state.json` use the same state shape.

Example:

```json
{
  "schema_version": "1.0",
  "document": {
    "document_id": "doc-001",
    "filename": "guideline.pdf",
    "pdf_sha256": "sha256-hex",
    "page_count": 1,
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
    "ocr_version": null,
    "config_hash": null,
    "processed_at": null,
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
      "ocr_confidence": null,
      "reading_order": 4,
      "heading_level": 1,
      "heading_level_source": null,
      "heading_level_uncertain": false,
      "uncertainty_reason": null,
      "origin": "machine",
      "ignored": false,
      "uncertain": false,
      "note": null,
      "metadata": {}
    }
  ],
  "state_revision": 0,
  "metadata": {}
}
```

## 4. Document

| Field | Type | Notes |
|---|---|---|
| `document_id` | string | stable document identifier |
| `filename` | string | display filename |
| `pdf_sha256` | string | source PDF hash |
| `page_count` | integer | number of pages |
| `pages` | array | page geometry metadata |

`page_index` is zero-based.

## 5. Pipeline

| Field | Type |
|---|---|
| `name` | string |
| `version` | string/null |
| `ocr_engine` | string/null |
| `ocr_version` | string/null |
| `config_hash` | string/null |
| `processed_at` | string/null |
| `adapter` | string/null |
| `metadata` | object |

Producer-specific data should remain in `metadata` unless needed by the canonical model.

The exact producer payload remains separately preserved in `machine_output.original.json`.

## 6. Region

| Field | Type | Meaning |
|---|---|---|
| `region_id` | string/UUID | stable canonical region ID |
| `source_region_id` | string/null | producer lineage ID |
| `page` | integer | zero-based page |
| `bbox` | object | normalized PDF box |
| `type` | string | current region class |
| `text` | string | OCR/reviewer text |
| `ocr_confidence` | number/null | optional confidence in `[0,1]` |
| `reading_order` | integer/null | reading position |
| `heading_level` | integer/null | level 1–6 when present |
| `heading_level_source` | string/null | source of machine heading decision |
| `heading_level_uncertain` | boolean | machine heading uncertainty |
| `uncertainty_reason` | string/null | optional uncertainty reason |
| `origin` | string | `machine` or `human` |
| `ignored` | boolean | excluded from approved representation |
| `uncertain` | boolean | reviewer uncertainty |
| `note` | string/null | reviewer note |
| `metadata` | object | extension metadata |

Machine region:

```json
{
  "origin": "machine",
  "source_region_id": "block:p3:i8"
}
```

Human-created region:

```json
{
  "origin": "human",
  "source_region_id": null
}
```

A `region_id` must remain stable for the life of the region.

## 7. Event log

`events.jsonl` contains one JSON object per line.

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
    "regions": []
  },
  "after": {
    "regions": []
  },
  "target_event_id": null,
  "reason_code": null,
  "metadata": {}
}
```

`before` and `after` contain complete snapshots of the affected regions in real events.

## 8. Event fields

| Field | Type | Meaning |
|---|---|---|
| `event_id` | string/UUID | unique event |
| `session_id` | string/UUID | owning session |
| `sequence` | integer | session-local order |
| `timestamp_utc` | datetime string | UTC timestamp |
| `annotator_id` | string | reviewer ID/pseudonym |
| `action` | string | semantic action |
| `mutates_state` | boolean | whether state changes |
| `target_region_ids` | array | affected regions |
| `page` | integer/null | relevant page |
| `before` | object/null | previous affected state |
| `after` | object/null | resulting affected state |
| `target_event_id` | string/null | undo/redo linkage |
| `reason_code` | string/null | optional reason |
| `metadata` | object | extension data |

Events are append-only.

## 9. Current review actions

State-changing actions exposed by the current review workflow include:

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

A completed user operation creates one semantic event. Raw pointer movement is not logged as repeated events.

Example:

```text
pointer down -> pointer moves -> pointer up
                              -> one RESIZE_REGION
```

Undo/redo append new events and do not delete earlier history.

The domain code may contain additional experimental actions; they are not part of the supported MVP UI contract unless exposed and tested through the review workflow.

## 10. Session metadata

Typical `session.json`:

```json
{
  "schema_version": "1.0",
  "app_version": "1.0.0",
  "session_id": "18dde386-2dd4-4bda-8e72-66ff8b411e6c",
  "document_id": "doc-001",
  "filename": "guideline.pdf",
  "annotator_id": "reviewer-01",
  "created_at": "2026-08-20T17:00:00.000Z",
  "updated_at": "2026-08-20T17:20:00.000Z",
  "finalised_at": null,
  "status": "active",
  "active_seconds": 0,
  "initial_state_sha256": "sha256-hex",
  "events_sha256": null,
  "final_state_sha256": null,
  "replay_valid": null,
  "metadata": {}
}
```

Status flow:

```text
active -> approved
```

Approved sessions reject normal annotation mutations.

`active_seconds` is an activity estimate, not exact cognitive-effort time.

## 11. Approval

The final checklist covers:

1. all pages reviewed
2. missing/spurious regions checked
3. region boundaries checked
4. region types checked
5. heading levels and reading order checked where applicable
6. remaining uncertainty documented

Approval writes a complete `final_state.json`.

Integrity rule:

```text
replay(initial_state.json, events.jsonl) == final_state.json
```

The comparison is semantic/canonical, not byte-for-byte JSON equality.

## 12. Metrics

`metrics.json` is derived data.

It may include:

- initial/final region counts
- added/deleted/changed regions
- geometry/type/text/structure/order changes
- corrected-region rate
- committed edit count
- undo/redo count
- active review time
- replay validity

Metrics can evolve without rewriting the raw initial/event/final records.

## 13. Validation

At minimum:

### State

- recognized schema version
- unique region IDs
- valid page references
- valid normalized bounding boxes
- valid heading level when present
- valid origin values

### Events

- unique event IDs
- correct session ID
- ordered sequence values
- valid target region references for the action
- replayable before/after data
- no annotation mutation after approval

### Finalisation

- checklist completed
- replay matches current/final state
- final state becomes read-only

## 14. Schema evolution

Rules:

1. do not change the meaning of existing fields
2. prefer new optional fields for compatible additions
3. add new action names rather than overloading old ones
4. bump `schema_version` for incompatible changes
5. retain adapter/version metadata
6. do not rewrite historical event logs to fit a newer schema

## 15. Producer adapter contract

An adapter must:

1. validate the producer payload
2. preserve the original payload separately
3. map page geometry and region labels
4. normalize bounding boxes
5. produce stable canonical region IDs
6. retain source-region lineage where possible
7. preserve useful producer metadata
8. fail explicitly when the producer output cannot be interpreted safely
