# Mock data

Use these two files together in **Start a review session**:

- `mock_document.pdf`
- `mock_machine_output.json`

Suggested test edits:

1. Page 1: delete the spurious region near the lower-right area.
2. Page 1: add a region around the missing figure caption.
3. Page 2: reclassify the large `figure` region to `table`.
4. Page 2: change `2.1 Renal impairment` from heading level 1 to level 2.
5. Move or resize one box, then try Undo/Redo.
6. Complete the final review checklist and approve the session.
7. Export the session ZIP and inspect `initial_state.json`, `events.jsonl`, and `final_state.json`.

The PDF is synthetic and contains no real medical or patient data.
