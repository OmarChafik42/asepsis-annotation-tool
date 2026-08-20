# Canonical annotation schema

## Coordinate system

All canonical bounding boxes are normalized to the source PDF page using a top-left origin:

```json
{"x0": 0.10, "y0": 0.20, "x1": 0.70, "y1": 0.35}
```

The values are in `[0,1]`, which makes annotations independent of render DPI, browser zoom, and OCR render scale.

## Initial/final state

```json
{
  "schema_version": "1.0",
  "document": {
    "document_id": "doc-...",
    "filename": "guideline.pdf",
    "pdf_sha256": "...",
    "page_count": 12,
    "pages": [
      {"page_index": 0, "width": 595.3, "height": 841.9}
    ]
  },
  "pipeline": {
    "name": "BetterIngest",
    "version": null,
    "ocr_engine": "PaddleOCR/PP-DocLayoutV3",
    "adapter": "betteringest-layout-review-v1",
    "metadata": {"ocr_scale": 2.0}
  },
  "regions": [
    {
      "region_id": "uuid",
      "source_region_id": "block:p0:i4",
      "page": 0,
      "bbox": {"x0": 0.1, "y0": 0.2, "x1": 0.8, "y1": 0.3},
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

## Event record

Every line in `events.jsonl` is one JSON object:

```json
{
  "event_id": "uuid",
  "session_id": "uuid",
  "sequence": 8,
  "timestamp_utc": "2026-08-09T19:30:00.000Z",
  "annotator_id": "reviewer-01",
  "action": "RESIZE_REGION",
  "mutates_state": true,
  "target_region_ids": ["region-uuid"],
  "page": 2,
  "before": {"regions": [{"...": "complete previous region snapshot"}]},
  "after": {"regions": [{"...": "complete new region snapshot"}]},
  "target_event_id": null,
  "reason_code": null,
  "metadata": {}
}
```

Complete snapshots are intentionally used rather than field-only deltas. This increases file size slightly but makes replay, audit, and future metric calculation much simpler and safer.

## Raw machine output

`machine_output.original.json` preserves the original uploaded JSON bytes and is never overwritten. The adapter creates `initial_state.json` from it. The two files answer different questions:

- raw machine output: exactly what the producer supplied;
- canonical initial state: what the annotation tool interpreted and displayed.
