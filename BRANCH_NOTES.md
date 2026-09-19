# MinerU improved UI branch

Suggested branch name: `feature/mineru-improved-ui`

This source is based on the uploaded MinerU-enabled version of the Asepsis annotation tool, with focused UI changes for large annotation runs.

## Changes in this branch

- keeps MinerU `ocr_text` sentence/line boxes in canonical state;
- adds a `Show OCR text boxes` visibility toggle;
- adds separate `Layout` and `OCR` edit layers;
- in Layout mode, layout regions are interactive and visible OCR boxes are reference-only;
- in OCR mode, OCR boxes are interactive and layout regions are reference-only;
- the left region list follows the active edit layer;
- new regions are created as `text` in Layout mode and `ocr_text` in OCR mode;
- inspector fields autosave: discrete fields immediately, text/note after 700 ms of inactivity;
- pending inspector edits are flushed before page navigation, add mode, leaving the session, delete, undo/redo, and final approval;
- the manual save button remains as a fallback (`Save now`).

## Deliberately not changed

This branch does not change MinerU heading inference or merge `*_model.json` with `*_content_list.json`. In particular, the existing MinerU adapter can still import heading regions without a populated canonical `heading_level` when that information is not present in the model JSON. Keep that as a separate adapter change so it can be reviewed independently from the UI work.

## Verification performed

Run from the repository root:

```bash
python -m pytest -q
node --check annotation_tool/static/app.js
```
