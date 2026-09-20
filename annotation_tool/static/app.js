const $ = (id) => document.getElementById(id);

const appState = {
  session: null,
  state: null,
  currentPage: 0,
  selectedRegionId: null,
  addMode: false,
  busy: false,
  drag: null,
  draw: null,
  lastActivity: Date.now(),
  editLayer: "layout",
  autosaveTimer: null,
  saveQueue: Promise.resolve(),
  saveError: null,
};

function toast(message, error = false) {
  const el = $("toast");
  el.textContent = message;
  el.classList.toggle("error", error);
  el.classList.remove("hidden");
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => el.classList.add("hidden"), 3000);
}

async function api(url, options = {}, timeoutMs = 15000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);
  let response;
  try {
    response = await fetch(url, {...options, signal: controller.signal});
  } catch (err) {
    if (err?.name === "AbortError") throw new Error("Request timed out. Is the local server still running?");
    throw err;
  } finally {
    clearTimeout(timeoutId);
  }
  if (!response.ok) {
    let message = `${response.status} ${response.statusText}`;
    try {
      const body = await response.json();
      message = body.detail || message;
    } catch (_) {}
    throw new Error(message);
  }
  const ct = response.headers.get("content-type") || "";
  return ct.includes("application/json") ? response.json() : response;
}

function setBusy(value, text = "Saving…") {
  appState.busy = value;

  if (value) {
    // A new save attempt supersedes the previous failure state.
    appState.saveError = null;
    $("saveStateText").textContent = text;
  } else {
    $("saveStateText").textContent = appState.saveError ? "Save failed" : "Saved";
  }

  $("undoBtn").disabled = value || appState.session?.status === "approved";
  $("redoBtn").disabled = value || appState.session?.status === "approved";
}

function recordSaveFailure(err, showToast = false) {
  const message = err?.message || "Unknown save error";
  appState.saveError = message;
  $("saveStateText").textContent = "Save failed";

  if (showToast) {
    toast(`Save failed: ${message}`, true);
  }
}

function markActivity() { appState.lastActivity = Date.now(); }
["pointerdown", "keydown", "wheel"].forEach(evt => window.addEventListener(evt, markActivity, {passive:true}));

async function loadDatasetStatus() {
  const box = $("datasetList");
  box.innerHTML = `<div class="muted">Loading…</div>`;
  try {
    const docs = await api("/api/dataset");
    if (!docs.length) {
      box.innerHTML = `<div class="muted">No documents discovered yet.</div>`;
      return;
    }
    box.innerHTML = "";
    for (const doc of docs) {
      const row = document.createElement("div");
      row.className = "session-item";
      const isAnnotated = doc.status === "annotated";
      const status = isAnnotated ? "annotated" : "pending";
      const badgeClass = isAnnotated ? "red" : "grey";
      const latest = isAnnotated ? (doc.latest_finalised_at ? new Date(doc.latest_finalised_at).toLocaleString() : "Previous annotation session") : "Not annotated yet";
      const buttonText = isAnnotated ? "Open" : "Start annotation";
      row.innerHTML = `
        <div>
          <div class="session-name" title="${escapeHtml(doc.document)}">${escapeHtml(doc.document)} <span class="status-badge ${badgeClass}">${status}</span></div>
          <div class="session-meta">${escapeHtml(doc.annotator || "—")} · ${escapeHtml(latest)}</div>
        </div>
        <button class="secondary small">${buttonText}</button>`;
      row.querySelector("button").addEventListener("click", async () => {
        try {
          if (!isAnnotated) {
            const form = new FormData();
            form.append("annotator_id", "anonymous");
            const result = await api(`/api/dataset/${encodeURIComponent(doc.document)}/sessions`, {method: "POST", body: form});
            await openSession(result.session.session_id);
            return;
          }
          const latestSessionId = Array.isArray(doc.sessions) && doc.sessions.length ? doc.sessions[0] : null;
          if (latestSessionId) {
            await openSession(latestSessionId);
            return;
          }

          // Fallback for older backend responses that do not include session IDs.
          const sessions = await api("/api/sessions");
          const match = sessions.find(s => s.filename === doc.document || s.metadata?.document === doc.document);
          if (match) await openSession(match.session_id);
          else throw new Error("No existing annotation session found for this document.");
        } catch (err) {
          toast(err.message, true);
        }
      });
      box.appendChild(row);
    }
  } catch (err) {
    box.innerHTML = `<div class="muted">Could not load dataset status.</div>`;
    toast(err.message, true);
  }
}

$("refreshDatasetBtn").addEventListener("click", loadDatasetStatus);

async function openSession(sessionId) {
  try {
    const result = await api(`/api/sessions/${sessionId}`);
    appState.session = result.session;
    appState.state = result.state;
    appState.currentPage = 0;
    appState.selectedRegionId = null;
    appState.addMode = false;
    appState.editLayer = "layout";
    clearTimeout(appState.autosaveTimer);
    appState.autosaveTimer = null;
    appState.saveQueue = Promise.resolve();
    appState.saveError = null;
    updateLayerControls();
    $("homeView").classList.add("hidden");
    $("workspaceView").classList.remove("hidden");
    $("docTitle").textContent = appState.session.filename;
    $("sessionSubline").textContent = `${appState.session.annotator_id} · ${appState.session.status} · session ${appState.session.session_id.slice(0, 8)}`;
    $("exportBtn").href = `/api/sessions/${sessionId}/export`;
    const readOnly = appState.session.status === "approved";
    $("approveBtn").disabled = readOnly;
    $("addRegionBtn").disabled = readOnly;
    $("undoBtn").disabled = readOnly;
    $("redoBtn").disabled = readOnly;
    await renderPage();

    // These panels are useful, but they are not part of the annotation save path.
    // Load them in the background so a slow metrics/event request never blocks work.
    refreshEvents().catch(() => {});
    refreshMetrics().catch(() => {});

    if (!readOnly) logInteraction("OPEN_SESSION", { page: appState.currentPage }).catch(() => {});
  } catch (err) {
    toast(err.message, true);
  }
}

$("backHomeBtn").addEventListener("click", async () => {
  try {
    await flushInspectorChanges();
  } catch (err) {
    toast(err.message, true);
    return;
  }
  $("workspaceView").classList.add("hidden");
  $("homeView").classList.remove("hidden");
  appState.session = null;
  appState.state = null;
  appState.selectedRegionId = null;
  appState.currentPage = 0;
  await loadDatasetStatus();
});

function currentRegions() {
  return (appState.state?.regions || []).filter(r => r.page === appState.currentPage);
}

function isOcrRegion(region) {
  return region?.type === "ocr_text";
}

function structuralRegions() {
  return currentRegions().filter(r => !isOcrRegion(r));
}

function ocrRegions() {
  return currentRegions().filter(isOcrRegion);
}

function activeLayerRegions() {
  return appState.editLayer === "ocr" ? ocrRegions() : structuralRegions();
}

function isRegionEditable(region) {
  return appState.editLayer === "ocr" ? isOcrRegion(region) : !isOcrRegion(region);
}

function isRegionVisible(region) {
  // Layout mode keeps the structural/layout layer clean by hiding sentence-level
  // OCR boxes. OCR mode shows both layers: OCR is editable and layout remains
  // visible as non-interactive context.
  if (appState.editLayer === "layout") return !isOcrRegion(region);
  return true;
}

function updateLayerControls() {
  const ocrMode = appState.editLayer === "ocr";
  $("editLayoutBtn").classList.toggle("active", !ocrMode);
  $("editOcrBtn").classList.toggle("active", ocrMode);
  $("regionListTitle").textContent = ocrMode ? "OCR text boxes" : "Layout regions";
  $("modeText").textContent = ocrMode
    ? "OCR editing: sentence/line boxes are editable; layout boxes are shown for reference."
    : "Layout editing: layout regions are editable; sentence-level OCR boxes are hidden.";
}

async function setEditLayer(layer) {
  if (!["layout", "ocr"].includes(layer) || layer === appState.editLayer) return;

  try {
    await flushInspectorChanges();
  } catch (err) {
    toast(err.message, true);
    return;
  }

  appState.editLayer = layer;
  appState.selectedRegionId = null;
  appState.addMode = false;

  $("addRegionBtn").classList.remove("primary");
  $("addRegionBtn").classList.add("secondary");

  updateLayerControls();
  renderOverlays();
  renderRegionList();
  renderInspector();
}

function regionById(id) {
  return (appState.state?.regions || []).find(r => r.region_id === id) || null;
}

async function renderPage() {
  if (!appState.state) return;
  const count = appState.state.document.page_count;
  appState.currentPage = Math.max(0, Math.min(count - 1, appState.currentPage));
  $("pageIndicator").textContent = `${appState.currentPage + 1} / ${count}`;
  $("prevPageBtn").disabled = appState.currentPage <= 0;
  $("nextPageBtn").disabled = appState.currentPage >= count - 1;
  const img = $("pageImage");
  img.src = `/api/sessions/${appState.session.session_id}/pages/${appState.currentPage}.png?scale=1.7`;
  await new Promise((resolve, reject) => {
    if (img.complete && img.naturalWidth) return resolve();
    img.onload = () => resolve();
    img.onerror = reject;
  });
  renderOverlays();
  renderRegionList();
  renderInspector();

  // Preload the next page while the reviewer is working on the current page.
  // The URL is stable, so the browser can reuse the backend's cached render
  // when Next is clicked.
  const nextPage = appState.currentPage + 1;
  if (nextPage < count) {
    const preload = new Image();
    preload.src = `/api/sessions/${appState.session.session_id}/pages/${nextPage}.png?scale=1.7`;
  }
}

function renderOverlays() {
  const overlay = $("overlay");
  overlay.innerHTML = "";
  overlay.classList.toggle("add-mode", appState.addMode);

  for (const r of currentRegions()) {
    if (!isRegionVisible(r)) continue;

    const ocrDetail = isOcrRegion(r);
    const editable = isRegionEditable(r);
    const box = document.createElement("div");
    box.className = "region-box";
    box.dataset.regionId = r.region_id;
    setBoxStyle(box, r.bbox);

    box.classList.add(ocrDetail ? "ocr-detail" : "structure-region");
    if (!editable) box.classList.add("inactive-layer");
    if (editable && r.region_id === appState.selectedRegionId) box.classList.add("selected");
    if (r.ignored) box.classList.add("ignored");
    if (r.uncertain || r.heading_level_uncertain) box.classList.add("uncertain");

    // Structural labels are useful in both modes. OCR boxes intentionally avoid
    // hundreds of repeated labels; their text is available in the inspector/list.
    if (!ocrDetail) {
      const label = document.createElement("div");
      label.className = "region-label";
      label.textContent = r.type + (r.heading_level ? ` · H${r.heading_level}` : "");
      box.appendChild(label);
    } else {
      box.title = r.text || "OCR text";
    }

    if (editable) {
      box.addEventListener("pointerdown", (e) => startMove(e, r));
      box.addEventListener("click", (e) => {
        e.stopPropagation();
        selectRegion(r.region_id);
      });

      if (r.region_id === appState.selectedRegionId && appState.session.status !== "approved") {
        for (const dir of ["nw", "ne", "sw", "se"]) {
          const h = document.createElement("div");
          h.className = `handle ${dir}`;
          h.dataset.dir = dir;
          h.addEventListener("pointerdown", (e) => startResize(e, r, dir));
          box.appendChild(h);
        }
      }
    }

    overlay.appendChild(box);
  }

  $("pageRegionCount").textContent = activeLayerRegions().length;
}

function setBoxStyle(el, bbox) {
  el.style.left = `${bbox.x0 * 100}%`;
  el.style.top = `${bbox.y0 * 100}%`;
  el.style.width = `${(bbox.x1 - bbox.x0) * 100}%`;
  el.style.height = `${(bbox.y1 - bbox.y0) * 100}%`;
}

function renderRegionList() {
  const list = $("regionList");
  const regions = [...activeLayerRegions()].sort((a,b) => (a.reading_order ?? 1e9) - (b.reading_order ?? 1e9) || a.bbox.y0-b.bbox.y0);
  list.innerHTML = "";
  for (const r of regions) {
    const row = document.createElement("div");
    row.className = `region-row${r.region_id === appState.selectedRegionId ? " selected" : ""}${r.ignored ? " ignored" : ""}`;
    row.innerHTML = `<span class="region-dot"></span><div><div class="region-type">${escapeHtml(r.type)}</div><div class="region-snippet">${escapeHtml((r.text || r.note || r.region_id).slice(0, 90))}</div></div>`;
    row.addEventListener("click", () => selectRegion(r.region_id));
    list.appendChild(row);
  }
}

function selectRegion(id) {
  // Capture pending edits for the previous region before changing selection.
  // They are queued, so selection remains instant while persistence stays ordered.
  if (appState.selectedRegionId && appState.selectedRegionId !== id) {
    enqueueInspectorSave(inspectorSnapshot()).catch((err) => recordSaveFailure(err, true));
  }

  appState.selectedRegionId = id;
  appState.addMode = false;
  $("addRegionBtn").classList.remove("primary");
  $("addRegionBtn").classList.add("secondary");
  $("modeText").textContent = appState.editLayer === "ocr"
    ? "OCR box selected. Edit text/properties, drag to move, or use a corner to resize."
    : "Layout region selected. Edit structure/properties, drag to move, or use a corner to resize.";
  renderOverlays();
  renderRegionList();
  renderInspector();
  logInteraction("SELECT_REGION", { page: appState.currentPage, region_id: id }).catch(() => {});
}

function renderInspector() {
  const r = regionById(appState.selectedRegionId);
  if (!r) {
    $("emptyInspector").classList.remove("hidden");
    $("inspectorForm").classList.add("hidden");
    $("selectedOrigin").textContent = "—";
    return;
  }
  $("emptyInspector").classList.add("hidden");
  $("inspectorForm").classList.remove("hidden");
  $("selectedOrigin").textContent = r.origin;
  $("regionIdText").textContent = r.region_id;
  ensureTypeOption(r.type);
  $("regionType").value = r.type;
  $("regionText").value = r.text || "";
  $("headingLevel").value = r.heading_level ?? "";
  $("readingOrder").value = r.reading_order ?? "";
  $("ignoredCheck").checked = !!r.ignored;
  $("uncertainCheck").checked = !!r.uncertain;
  $("regionNote").value = r.note || "";
  $("bboxReadout").textContent = `bbox: ${[r.bbox.x0,r.bbox.y0,r.bbox.x1,r.bbox.y1].map(v=>v.toFixed(4)).join(", ")}`;
  const ro = appState.session?.status === "approved";
  for (const input of $("inspectorForm").querySelectorAll("input,select,textarea,button")) input.disabled = ro;
}

function ensureTypeOption(value) {
  const select = $("regionType");
  if (![...select.options].some(o => o.value === value)) {
    const opt = document.createElement("option"); opt.value = value; opt.textContent = value; select.appendChild(opt);
  }
}

$("prevPageBtn").addEventListener("click", () => gotoPage(appState.currentPage - 1));
$("nextPageBtn").addEventListener("click", () => gotoPage(appState.currentPage + 1));
async function gotoPage(page) {
  if (!appState.state) return;
  try {
    // Navigation never waits for the 700 ms debounce: pending text is flushed now.
    await flushInspectorChanges();
  } catch (err) {
    toast(err.message, true);
    return;
  }
  appState.currentPage = Math.max(0, Math.min(appState.state.document.page_count - 1, page));
  appState.selectedRegionId = null;
  await renderPage();
  logInteraction("VIEW_PAGE", { page: appState.currentPage }).catch(() => {});
}

$("addRegionBtn").addEventListener("click", async () => {
  if (appState.session?.status === "approved") return;
  try {
    await flushInspectorChanges();
  } catch (err) {
    toast(err.message, true);
    return;
  }
  appState.addMode = !appState.addMode;
  appState.selectedRegionId = null;
  $("addRegionBtn").classList.toggle("primary", appState.addMode);
  $("addRegionBtn").classList.toggle("secondary", !appState.addMode);
  $("modeText").textContent = appState.addMode
    ? (appState.editLayer === "ocr" ? "Draw a rectangle to create an OCR text region." : "Draw a rectangle to create a layout region.")
    : (appState.editLayer === "ocr" ? "OCR editing: select a sentence/line box." : "Layout editing: select a structural region.");
  renderOverlays(); renderRegionList(); renderInspector();
});

$("editLayoutBtn").addEventListener("click", () => setEditLayer("layout"));
$("editOcrBtn").addEventListener("click", () => setEditLayer("ocr"));

function normalizedPointer(e) {
  const rect = $("overlay").getBoundingClientRect();
  return {
    x: Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width)),
    y: Math.max(0, Math.min(1, (e.clientY - rect.top) / rect.height)),
  };
}

$("overlay").addEventListener("pointerdown", (e) => {
  if (!appState.addMode || appState.session?.status === "approved" || e.target !== $("overlay")) return;
  e.preventDefault();
  const start = normalizedPointer(e);
  const temp = document.createElement("div");
  temp.className = "draw-box";
  $("overlay").appendChild(temp);
  appState.draw = { pointerId: e.pointerId, start, temp };
  $("overlay").setPointerCapture(e.pointerId);
});

$("overlay").addEventListener("pointermove", (e) => {
  if (appState.draw && appState.draw.pointerId === e.pointerId) {
    const p = normalizedPointer(e), s = appState.draw.start;
    const box = { x0: Math.min(s.x,p.x), y0:Math.min(s.y,p.y), x1:Math.max(s.x,p.x), y1:Math.max(s.y,p.y) };
    setBoxStyle(appState.draw.temp, box);
  }
  if (appState.drag && appState.drag.pointerId === e.pointerId) updateDrag(e);
});

$("overlay").addEventListener("pointerup", async (e) => {
  if (appState.draw && appState.draw.pointerId === e.pointerId) {
    const p = normalizedPointer(e), s = appState.draw.start;
    const bbox = { x0: Math.min(s.x,p.x), y0:Math.min(s.y,p.y), x1:Math.max(s.x,p.x), y1:Math.max(s.y,p.y) };
    appState.draw.temp.remove(); appState.draw = null;
    if (bbox.x1-bbox.x0 > .006 && bbox.y1-bbox.y0 > .006) {
      try {
        const result = await sendCommand("CREATE_REGION", null, {
          page: appState.currentPage,
          bbox,
          type: appState.editLayer === "ocr" ? "ocr_text" : "text"
        });
        appState.selectedRegionId = result.event.target_region_ids[0];
        appState.addMode = false;
        $("addRegionBtn").classList.remove("primary"); $("addRegionBtn").classList.add("secondary");
        $("modeText").textContent = appState.editLayer === "ocr"
          ? "New OCR region created. Correct its text/properties on the right."
          : "New layout region created. Adjust its structural properties on the right.";
      } catch (err) { toast(err.message, true); }
    }
    renderOverlays(); renderRegionList(); renderInspector();
  }
  if (appState.drag && appState.drag.pointerId === e.pointerId) await finishDrag(e);
});

function startMove(e, region) {
  if (appState.addMode || appState.session?.status === "approved") return;
  if (e.target.classList.contains("handle")) return;
  e.stopPropagation(); e.preventDefault();
  selectRegion(region.region_id);
  const p = normalizedPointer(e);
  appState.drag = { pointerId:e.pointerId, kind:"move", regionId:region.region_id, start:p, original:{...region.bbox}, current:{...region.bbox} };
  $("overlay").setPointerCapture(e.pointerId);
}

function startResize(e, region, dir) {
  if (appState.session?.status === "approved") return;
  e.stopPropagation(); e.preventDefault();
  const p = normalizedPointer(e);
  appState.drag = { pointerId:e.pointerId, kind:"resize", dir, regionId:region.region_id, start:p, original:{...region.bbox}, current:{...region.bbox} };
  $("overlay").setPointerCapture(e.pointerId);
}

function updateDrag(e) {
  const d = appState.drag;
  const p = normalizedPointer(e);
  const min = .004;
  let b = {...d.original};
  if (d.kind === "move") {
    const dx = p.x-d.start.x, dy=p.y-d.start.y;
    const w=b.x1-b.x0, h=b.y1-b.y0;
    b.x0=Math.max(0,Math.min(1-w,b.x0+dx)); b.x1=b.x0+w;
    b.y0=Math.max(0,Math.min(1-h,b.y0+dy)); b.y1=b.y0+h;
  } else {
    if (d.dir.includes("n")) b.y0=Math.max(0,Math.min(b.y1-min,p.y));
    if (d.dir.includes("s")) b.y1=Math.min(1,Math.max(b.y0+min,p.y));
    if (d.dir.includes("w")) b.x0=Math.max(0,Math.min(b.x1-min,p.x));
    if (d.dir.includes("e")) b.x1=Math.min(1,Math.max(b.x0+min,p.x));
  }
  d.current=b;
  const el = [...$("overlay").querySelectorAll(".region-box")].find(x=>x.dataset.regionId===d.regionId);
  if (el) setBoxStyle(el,b);
  $("bboxReadout").textContent = `bbox: ${[b.x0,b.y0,b.x1,b.y1].map(v=>v.toFixed(4)).join(", ")}`;
}

async function finishDrag(e) {
  const d = appState.drag; appState.drag = null;
  const changed = JSON.stringify(d.original) !== JSON.stringify(d.current);
  if (!changed) return renderOverlays();
  try {
    await appState.saveQueue;
    await sendCommand(d.kind === "move" ? "MOVE_REGION" : "RESIZE_REGION", d.regionId, { bbox: d.current });
  } catch (err) { toast(err.message, true); }
  renderOverlays(); renderRegionList(); renderInspector();
}

function inspectorSnapshot() {
  const regionId = appState.selectedRegionId;
  if (!regionId || !regionById(regionId)) return null;
  return {
    regionId,
    type: $("regionType").value,
    text: $("regionText").value,
    headingLevel: $("headingLevel").value === "" ? null : Number($("headingLevel").value),
    readingOrder: $("readingOrder").value === "" ? null : Number($("readingOrder").value),
    ignored: $("ignoredCheck").checked,
    uncertain: $("uncertainCheck").checked,
    note: $("regionNote").value,
  };
}

async function saveInspectorSnapshot(snapshot) {
  if (!snapshot || appState.session?.status === "approved") return;
  const id = snapshot.regionId;
  let now = regionById(id);
  if (!now) return;

  if (snapshot.type !== now.type) {
    await sendCommand("RECLASSIFY_REGION", id, {type: snapshot.type});
  }
  now = regionById(id);

  if (snapshot.text !== (now.text || "")) {
    await sendCommand("UPDATE_TEXT", id, {text: snapshot.text});
  }
  now = regionById(id);

  if (snapshot.headingLevel !== (now.heading_level ?? null)) {
    await sendCommand("CHANGE_HEADING_LEVEL", id, {heading_level: snapshot.headingLevel});
  }
  now = regionById(id);

  if (snapshot.readingOrder !== (now.reading_order ?? null)) {
    await sendCommand("CHANGE_READING_ORDER", id, {reading_order: snapshot.readingOrder});
  }
  now = regionById(id);

  if (snapshot.ignored !== !!now.ignored) {
    await sendCommand(snapshot.ignored ? "IGNORE_REGION" : "RESTORE_REGION", id, {});
  }
  now = regionById(id);

  if (snapshot.uncertain !== !!now.uncertain) {
    await sendCommand("MARK_UNCERTAIN", id, {uncertain: snapshot.uncertain});
  }
  now = regionById(id);

  if (snapshot.note !== (now.note || "")) {
    await sendCommand("ADD_NOTE", id, {note: snapshot.note});
  }

  // Do not call renderInspector() here: autosave must never reset the text
  // caret while the reviewer is typing.
  renderOverlays();
  renderRegionList();
}

function enqueueInspectorSave(snapshot) {
  if (!snapshot) return appState.saveQueue;

  // Recover before starting the next queued save so one transient failure does
  // not permanently poison the queue. The current caller still receives the
  // rejection and can surface it to the reviewer.
  appState.saveQueue = appState.saveQueue
    .catch(() => {})
    .then(() => saveInspectorSnapshot(snapshot));

  return appState.saveQueue;
}

function scheduleTextAutosave() {
  clearTimeout(appState.autosaveTimer);
  appState.autosaveTimer = setTimeout(() => {
    appState.autosaveTimer = null;
    enqueueInspectorSave(inspectorSnapshot()).catch((err) => recordSaveFailure(err, true));
  }, 700);
}

async function flushInspectorChanges() {
  clearTimeout(appState.autosaveTimer);
  appState.autosaveTimer = null;

  const snapshot = inspectorSnapshot();
  if (snapshot) enqueueInspectorSave(snapshot);
  await appState.saveQueue;
}

// Discrete values have a clear semantic commit point, so persist immediately.
["regionType", "headingLevel", "readingOrder", "ignoredCheck", "uncertainCheck"].forEach((id) => {
  $(id).addEventListener("change", () => {
    enqueueInspectorSave(inspectorSnapshot()).catch((err) => recordSaveFailure(err, true));
  });
});

// Text and notes are debounced so typing a sentence creates one useful event
// instead of an event for every keystroke. Blur always forces an immediate save.
["regionText", "regionNote"].forEach((id) => {
  $(id).addEventListener("input", scheduleTextAutosave);
  $(id).addEventListener("blur", () => {
    clearTimeout(appState.autosaveTimer);
    appState.autosaveTimer = null;
    enqueueInspectorSave(inspectorSnapshot()).catch((err) => recordSaveFailure(err, true));
  });
});

// Keep the button as an explicit fallback while reviewers get used to autosave.
$("inspectorForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  try {
    await flushInspectorChanges();
    toast("Region properties saved.");
  } catch (err) {
    toast(err.message, true);
  }
});

$("deleteRegionBtn").addEventListener("click", async () => {
  const id=appState.selectedRegionId; if(!id) return;
  if (!confirm("Delete this region? The deletion will remain recoverable through the event history/undo.")) return;
  try {
    await flushInspectorChanges();
    await sendCommand("DELETE_REGION",id,{});
    appState.selectedRegionId=null;
    renderOverlays(); renderRegionList(); renderInspector();
  } catch(err){toast(err.message,true);}
});

function prependEventToList(event) {
  if (!event) return;
  const box = $("eventList");
  if (!box) return;

  const row = document.createElement("div");
  row.className = "event-row";
  row.innerHTML = `<span class="event-action">${escapeHtml(event.action)}</span><span class="event-time">#${event.sequence}</span><div class="muted">${new Date(event.timestamp_utc).toLocaleTimeString()}</div>`;
  box.prepend(row);

  while (box.children.length > 30) {
    box.lastElementChild.remove();
  }
}

async function sendCommand(action, regionId, payload, regionIds=[]) {
  setBusy(true);
  try {
    const result = await api(`/api/sessions/${appState.session.session_id}/commands`, {
      method:"POST", headers:{"Content-Type":"application/json"},
      body:JSON.stringify({action, region_id:regionId, region_ids:regionIds, payload})
    }, 60000);

    appState.state=result.state;

    // The command response already contains the committed event and canonical
    // state. Update the visible event list locally instead of downloading the
    // full event log after every correction.
    prependEventToList(result.event);

    return result;
  } catch (err) {
    // Keep the visible status at "Save failed". Do not let finally() change it
    // back to "Saved" when the browser never received a successful response.
    recordSaveFailure(err, false);
    throw err;
  } finally {
    setBusy(false);
  }
}

$("undoBtn").addEventListener("click", async()=>historyAction("undo"));
$("redoBtn").addEventListener("click", async()=>historyAction("redo"));
async function historyAction(kind){
  if(appState.session?.status==="approved")return;
  try {
    await flushInspectorChanges();
  } catch (err) {
    toast(err.message, true);
    return;
  }
  setBusy(true, kind === "undo" ? "Undoing…" : "Redoing…");
  try{
    const result=await api(`/api/sessions/${appState.session.session_id}/${kind}`,{method:"POST"});
    appState.state=result.state;
    if(appState.selectedRegionId && !regionById(appState.selectedRegionId)) appState.selectedRegionId=null;
    renderOverlays();renderRegionList();renderInspector();await refreshEvents();await refreshMetrics();
  }catch(err){toast(err.message,true);}finally{setBusy(false);}
}

window.addEventListener("keydown", (e)=>{
  if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==="z" && !e.shiftKey){e.preventDefault();historyAction("undo");}
  if((e.ctrlKey||e.metaKey)&&((e.key.toLowerCase()==="y")||(e.shiftKey&&e.key.toLowerCase()==="z"))){e.preventDefault();historyAction("redo");}
});

async function logInteraction(action, {page=null, region_id=null, metadata={}}={}) {
  if (!appState.session || appState.session.status === "approved") return;
  return api(`/api/sessions/${appState.session.session_id}/interactions`, {
    method:"POST", headers:{"Content-Type":"application/json"},
    body:JSON.stringify({action,page,region_id,metadata})
  });
}

async function refreshEvents(){
  if(!appState.session)return;
  try{
    const events=await api(`/api/sessions/${appState.session.session_id}/events`);
    const box=$("eventList");box.innerHTML="";
    for(const e of events.slice(-30).reverse()){
      const row=document.createElement("div");row.className="event-row";
      row.innerHTML=`<span class="event-action">${escapeHtml(e.action)}</span><span class="event-time">#${e.sequence}</span><div class="muted">${new Date(e.timestamp_utc).toLocaleTimeString()}</div>`;
      box.appendChild(row);
    }
  }catch(_){ }
}

async function refreshMetrics(){
  if(!appState.session)return;
  try{
    const m=await api(`/api/sessions/${appState.session.session_id}/metrics`, {}, 8000);
    const b=m.final_correction_burden, i=m.interaction_effort, t=m.timing;
    $("metricsBox").innerHTML=`
      <div class="metric"><div class="value">${m.initial_regions}</div><div class="label">initial regions</div></div>
      <div class="metric"><div class="value">${m.final_regions}</div><div class="label">current/final regions</div></div>
      <div class="metric"><div class="value">${b.corrected_initial_regions}</div><div class="label">initial regions changed/deleted</div></div>
      <div class="metric"><div class="value">${(b.corrected_region_rate*100).toFixed(1)}%</div><div class="label">corrected-region rate</div></div>
      <div class="metric"><div class="value">${i.committed_edit_events}</div><div class="label">committed edit events</div></div>
      <div class="metric"><div class="value">${Math.round(t.active_seconds/60)}</div><div class="label">active minutes</div></div>
      <div class="metric full"><div class="value">${m.integrity.replay_matches_final_state ? "✓" : "!"}</div><div class="label">event replay reproduces current/final state</div></div>`;
  }catch(err){
    $("metricsBox").innerHTML=`<div class="muted">Metrics temporarily unavailable. Annotation saves are unaffected.</div>`;
  }
}
$("refreshMetricsBtn").addEventListener("click",refreshMetrics);

$("approveBtn").addEventListener("click", ()=>{
  if(!appState.session || appState.session.status==="approved")return;
  // Reset the checklist every time the approval dialog is opened.
  for (const id of ["checkAllPages","checkCoverage","checkBoundaries","checkTypes","checkStructure","checkUncertainty"]) $(id).checked=false;
  $("approvalNote").value="";
  $("approvalModal").classList.remove("hidden");
});

$("cancelApprovalBtn").addEventListener("click", ()=>$("approvalModal").classList.add("hidden"));

$("confirmApprovalBtn").addEventListener("click", async()=>{
  if(!appState.session || appState.session.status==="approved")return;
  const checklist={
    checklist_version:"1.0",
    reviewed_all_pages:$("checkAllPages").checked,
    missing_spurious_regions_checked:$("checkCoverage").checked,
    boundaries_checked:$("checkBoundaries").checked,
    types_checked:$("checkTypes").checked,
    structure_checked:$("checkStructure").checked,
    uncertainty_documented:$("checkUncertainty").checked,
  };
  if(!Object.entries(checklist).filter(([k])=>k!=="checklist_version").every(([,v])=>v)){
    toast("Complete all review checks before approval.",true);return;
  }
  try{
    await flushInspectorChanges();
  }catch(err){
    toast(err.message,true);
    return;
  }
  setBusy(true,"Finalising…");
  try{
    const result=await api(`/api/sessions/${appState.session.session_id}/finalise`,{
      method:"POST",headers:{"Content-Type":"application/json"},
      body:JSON.stringify({checklist,approval_note:$("approvalNote").value.trim()||null})
    });
    appState.session=result.session;appState.state=result.state;
    $("approvalModal").classList.add("hidden");
    $("sessionSubline").textContent=`${appState.session.annotator_id} · approved · session ${appState.session.session_id.slice(0,8)}`;
    $("approveBtn").disabled=true;$("addRegionBtn").disabled=true;$("undoBtn").disabled=true;$("redoBtn").disabled=true;
    renderOverlays();renderInspector();refreshEvents();refreshMetrics();toast("Session approved. Final state is now frozen.");
  }catch(err){toast(err.message,true);}finally{setBusy(false);}
});

$("exportBtn").addEventListener("click",()=>{
  logInteraction("EXPORT_SESSION",{}).catch(()=>{});
});

setInterval(()=>{
  if(!appState.session || appState.session.status!=="active" || document.hidden)return;
  if(Date.now()-appState.lastActivity>60000)return;
  api(`/api/sessions/${appState.session.session_id}/activity`,{
    method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({seconds:10})
  }).catch(()=>{});
},10000);

function escapeHtml(value){
  return String(value ?? "").replace(/[&<>'"]/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;","\"":"&quot;"}[ch]));
}

loadDatasetStatus();
