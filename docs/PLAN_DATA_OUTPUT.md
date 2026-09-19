# Plan: Annotation Output into `data/` + GitHub Tracking

**Status:** Core implementation complete
**Date:** 2026-09-01
**Change from v1/v2:** the dataset format mismatch is solved, source documents
and model JSON are inferred from the mounted `data/` directory, and the landing
page starts annotation directly from a selected document. The UI shows
**red = a session directory already exists, grey = no session directory exists**.

---

## 1. TL;DR — Is it possible with the existing Docker architecture?

**Yes.** Everything already persists through one configurable root
(`ANNOTATION_DATA_DIR` / `SessionStore`), and `SessionStore` is already
"root + `<uuid>` per session" — so the new layout is mostly a matter of **which
root each document's store points at**. Required changes:

1. **Docker Compose:** replace the named volume `annotation_data` with a **bind
   mount** `./data:/data` so results land directly in the repo's `data/` directory.
2. **Per-document storage roots:** each document's sessions live in
   `data/<document>/auto/sessions/<uuid>/…`. The existing `SessionStore` class is
   reused unchanged — one store instance per document.
3. **Dataset adapter (previously a blocker):** the `_model.json` files were not
   consumable by `adapt_machine_output()`. **Implemented:** a MinerU adapter is
   now in place, so uploads from `data/` work end-to-end.
4. **Dataset status endpoint + UI:** server scans `data/*/auto/` and its
   `sessions/` children to report processed vs pending; home page renders
   **red** (annotated) / **grey** (to-do) document cards. Selecting a pending
   document automatically reads its `<Document>_origin.pdf` and
   `<Document>_model.json` files and creates the session.
5. **Git workflow:** commit the JSON artifacts under
   `data/<document>/auto/sessions/<uuid>/`; presence in git history + disk gives
   full tracking of generated files and progress.

GitHub-tracking of *binary medical media* (PDFs, JPGs) is the main decision point —
see §5 and §7.

---

## 2. Current state

| Item | Location / value |
|---|---|
| Storage root (Docker) | named volume `annotation_data` → `/data` inside container |
| Storage root (native) | `annotation-data/` (default) |
| Session layout | `<root>/sessions/<uuid>/{source.pdf, events.jsonl, working_state.json, final_state.json, session.json, metrics.json, …}` |
| SessionStore | `root` + `session_dir = root/<uuid>` — reusable as-is |
| Export | `export_zip()` → per-session `<uuid>.zip` |
| repo | `github.com/OmarChafik42/asepsis-annotation-tool` |
| `data/` in git | **untracked** |

## 3. Dataset shape (observed)

```
data/                                   # 116 MB total, 107 topics
└── <Document>/                         # e.g. "3MRGN", "COVID-19", German hygiene documents (UKR)
    └── auto/
        ├── <Document>.md               # 107 markdown files
        ├── <Document>_model.json       # 107 machine layout detections
        │                               #   [ { page_info: {page_no,width,height},
        │                               #       layout_dets: [ {cls_id,label,score,bbox,index} ] } ]
        ├── <Document>_origin.pdf       # source PDF (also _span.pdf, _layout.pdf variants)
        ├── <Document>_content_list.json / _content_list_v2.json
        ├── <Document>_middle.json
        └── images/*.jpg                # 477 page images (sha-named)
```

Counts: 107 `.md`, 107 `*_model.json`, 428 JSON total, 320 PDFs, 477 JPGs.
Largest topic: `ASH-Anleitung Verbandwechsel` ≈ 21 MB. No file exceeds GitHub's
100 MB hard limit.

**Key finding (resolved):** `_model.json` is a list of pages with `layout_dets`
(labels include `header`, `header_image`, `table`, `paragraph_title`, `text`,
`ocr_text`, `footer`, `image`, `vision_footnote`, `chart`, etc.) and pixel `bbox`
+ `page_info`. This is now directly consumable by the MinerU adapter in
`annotation_tool/adapters.py`.

---

## 4. Target architecture (v2 schema)

```
Host repo
└── data/                                  (bind-mounted into container as /data)
    └── <Document>/
        └── auto/
            ├── …existing source files…    (model.json, PDFs, images, md)
            └── sessions/                  ← NEW: created by the annotation tool
                └── <uuid>/                ← one folder per annotation session
                    ├── session.json              (metadata: status=approved, annotator, timestamps)
                    ├── final_state.json          (human-approved result)        ← TRACKED
                    ├── events.jsonl              (full human edit history)      ← TRACKED
                    ├── metrics.json              (derived metrics)              ← TRACKED
                    ├── initial_state.json        (pre-annotation state)         ← TRACKED
                    ├── machine_output.original.json  (input)                    ← TRACKED (small JSON)
                    ├── working_state.json        (resumable state)              ← gitignored
                    ├── source.pdf                (copy)                         ← gitignored
                    ├── render_cache/             (disposable page renders)      ← gitignored
                    └── <uuid>.zip                (export bundle)                ← gitignored
```

**Processed / pending detection — presence-based (no manifest needed):**

> A document is **processed (green)** iff `data/<Document>/auto/sessions/` exists
> and contains at least one session with `session.json` status `approved`
> (i.e. `final_state.json` present).
> A document is **pending (grey)** iff it has no `sessions/` dir or no approved
> session yet.

Optional refinement (cheap): a document with only *active* (unapproved) sessions
shows **amber/yellow "in progress"** — but the minimum viable version is
green/grey as requested.

**Why this shape:**
- The presence of `sessions/<uuid>` *is* the "this has been processed" signal —
  visible on disk and in git without any extra index file.
- Each document keeps its full audit trail next to its source, inside `auto/`.
- `SessionStore` code is almost untouched: one store instance per document root
  (`data/<Document>/auto/sessions`).
- No cross-document manifest to keep in sync (dropped from v1).
- UUID session folders avoid name collisions and keep the existing
  create/replay/finalise/export logic intact.

---

## 5. GitHub tracking strategy — options

The layout above is identical under every option; only *what gets committed*
changes.

### Option A (recommended): track only generated JSON artifacts
- Track: `data/*/auto/sessions/*/{session.json, final_state.json, events.jsonl,
  metrics.json, initial_state.json, machine_output.original.json}`.
- Gitignore: PDFs, JPGs, `.md` (optional), `*.zip`, `working_state.json`,
  `render_cache/`, `source.pdf`, `.DS_Store`.
- Pros: tiny repo; readable per-session diffs; progress visible in git (new
  session dirs appear per approved document); no medical media on GitHub.
- Cons: source media not versioned by git (keep a separate backup).

### Option B: Git LFS for binary media
- Track everything; `*.pdf`, `*.jpg` → LFS.
- Pros: full provenance incl. inputs; 116 MB fits GitHub's 1 GB free LFS quota.
- Cons: `git lfs` required on every workstation; LFS bandwidth caps; still pushes
  medical media to GitHub (see §7).

### Option C: everything in plain git
- Not recommended: 116 MB of binaries bloats history, and medical media goes to
  GitHub without LFS benefits.

**Decision needed:** A vs B. Sessions/status/git-history work identically in both.

---

## 6. Implementation steps

### Phase 0 — Compliance check (before anything is pushed)
1. Confirm the repo is **private** (or make it private): `github.com/OmarChafik42/asepsis-annotation-tool`.
2. Verify with the data owner that the UKR documents are de-identified/anonymised
   and may be shared on GitHub (GDPR/patient-data review). If not: **Option A only**.

### Phase 1 — Docker: bind mount instead of named volume
```yaml
# docker-compose.yml
services:
  annotation-tool:
    build: .
    ports: ["8765:8765"]
    environment:
      ANNOTATION_DATA_DIR: /data
      ANNOTATION_MAX_PDF_MB: "50"
      ANNOTATION_MAX_JSON_MB: "10"
    volumes:
      - ./data:/data          # bind mount into repo data/ (replaces named volume)
    user: "${UID}:${GID}"     # avoid root-owned files (Linux); macOS handles perms via Docker Desktop
    restart: unless-stopped
```
- Add `UID`/`GID` to `.env` (or export in shell) so files are owned by the host
  user → `git add`/`commit` works without `sudo`/chown.
- Verify: after one session, `data/<document>/auto/sessions/<uuid>/` exists.

### Phase 2 — Dataset adapter (unblocks the real data)
Add `adapt_model_json(raw, pdf_path)` in `annotation_tool/adapters.py`:
- Accept the dataset format (list of `{page_info, layout_dets}`).
- Map each `layout_det` → `Region` via existing `_normalize_bbox()` (pixel
  coordinates + `page_info` width/height — already supported).
- Label mapping: `table` → table; `paragraph_title` + `heading_level_uncertain`/
  `score`; `header`/`footer` → header/footer; `text`/`ocr_text` → text;
  `header_image` → image.
- Register in `adapt_machine_output()` dispatch.
- Unit test with `data/3MRGN/auto/3MRGN_model.json`; run `python3 -m pytest tests/`.

### Phase 3 — Per-document storage root + dataset status endpoint
- New `annotation_tool/dataset.py` (`DatasetStore`):
  - `document_dir(document)` → `DATA_ROOT/<document>/auto`
  - `sessions_root(document)` → `DATA_ROOT/<document>/auto/sessions`
  - `store(document)` → cached `SessionStore(sessions_root)` (class unchanged)
  - `documents()` → scan `DATA_ROOT` for dirs containing `auto/`
  - `status()` → `[{document, status: approved|active|pending,
    sessions: [...], latest_finalised_at, annotator}]`
    - approved iff `sessions/<uuid>/session.json.status == "approved"` exists
- `annotation_tool/app.py`:
  - session creation: accept optional `document` form field; if absent, derive
    from uploaded filename (`<Document>_origin.pdf` → `<Document>`). Store the
    value in `SessionMeta.metadata["document"]`.
  - use `dataset.store(document)` for create/get/events/commands/finalise/export…
  (replaces the single module-level `store`).
  - new `GET /api/dataset` → list of documents + status (drives the UI).
- `scripts/status_report.py`: prints `document | status | session | annotator |
  finalised_at` table (same answer as git history, from disk).

### Phase 4 — Git workflow
- `.gitignore` additions:
  ```gitignore
  # operational per-session files (keep these out of git)
  data/*/auto/sessions/*/working_state.json
  data/*/auto/sessions/*/source.pdf
  data/*/auto/sessions/*/render_cache/
  data/**/*.zip
  ```
  plus Option-A media ignores if chosen (`.pdf`, `*.jpg`, optionally `*.md`).
- New `scripts/commit_annotations.sh`:
  ```bash
  git add data/*/auto/sessions/
  git commit -m "annotate: <Document> (approved)"  # or all changed sessions
  git push
  ```
  `--document <name>` to commit a single document; default commits all new/updated
  session artifacts already on disk.
- (Optional, later) auto-commit hook on finalise — **not** recommended in v1
  (credentials in containers, merge conflicts); the script is sufficient.

### Phase 5 — UI: green / grey dataset view
- Home page (`static/index.html` + `static/app.js`):
  - fetch `GET /api/dataset`
  - render one card/tile per document:
    - **green** + "processed" badge → has approved session (link opens the final
      session view / export)
    - **grey** + "pending" badge → not yet annotated (button "Start annotation"
      pre-fills uploads from `data/<Document>/auto/` via the server)
  - optional **amber "in progress"** if active session exists.
- Keep the session list view for detail; dataset view is the default landing page.

### Phase 6 — End-to-end validation
1. `docker compose up --build` with bind mount.
2. `GET /api/dataset` → all 107 documents **grey/pending**.
3. Annotate `3MRGN` (upload `3MRGN_origin.pdf` + `3MRGN_model.json`), finalise.
4. Verify `data/3MRGN/auto/sessions/<uuid>/final_state.json` exists;
   `GET /api/dataset` → `3MRGN` **green**.
5. `docker compose restart` → status persists (bind mount).
6. Run `scripts/commit_annotations.sh`, `git status` clean, `git push`.

---

## 7. Risks & mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| **Medical data on GitHub** (public/private) | GDPR / data-protection violation | Phase 0; private repo; Option A keeps media out of git |
| Repo size / history bloat (116 MB) | Slow clones, painful history | Option A (JSON only) or Option B (LFS) |
| `_model.json` format not supported | Real dataset cannot be annotated | Phase 2 adapter (small, well-scoped) |
| Root-owned files in bind mount | Can't `git add` as host user | `user: ${UID}:${GID}` in compose |
| GitHub 100 MB per-file limit | Push rejected | Not triggered (max file ~21 MB), keep in mind |
| `docker compose down -v` | Data loss (current named volume) | Bind mount makes `-v` harmless for `./data`; still document it |
| Nested `data/<doc>/auto/sessions/` naming | Path traversal / weird chars in doc names (spaces, `+`, German umlauts) | Validate/`slugify` document names; same UUID validation as today |
| Concurrent commits | Merge noise | One reviewer per session; commit script per document |
| Green/grey misdetection (session abandoned mid-way) | Document shown processed with no final state | Define "processed" = *approved* session exists (final_state.json), not any session dir |

---

## 8. Open questions for you

1. **Private or public repo?** (required before any push)
2. **Track media too?** Option A (JSON only) vs Option B (LFS) vs C?
3. Which PDF is the canonical input per document: `_origin.pdf`, `_span.pdf`, or
   `_layout.pdf`?
4. Should a document with an unfinished (active) session show grey or amber?
5. Batch-import all 107 documents up front, or annotate on demand (start from
   the dataset view)?