import { api, esc, toast } from "../api.js";
import { compare, evaluate, fmt, resultKey, unitLabel } from "../measure.js";
import { state, typeLabel, unit } from "../state.js";

const COLORS = { pass: "#1e8a4c", fail: "#d63a3a", no_spec: "#2b6fd6", missing: "#888" };
const LOW = "#f08c00";

function specText(r, u) {
  if (r.target_mm == null) return "–";
  const tol = r.tol_minus_mm === r.tol_plus_mm ? `±${fmt(r.tol_plus_mm, u)}`
    : `−${fmt(r.tol_minus_mm, u)}/+${fmt(r.tol_plus_mm, u)}`;
  return `${fmt(r.target_mm, u)} <span class="muted small">${tol}</span>`;
}

export async function resultView(view, id) {
  let scan = await api(`/api/scans/${id}`);
  const u = unit();
  let landmarks = structuredClone(scan.landmarks);
  let conf = { ...scan.confidence };
  let spec = scan.spec || [];
  let styleId = scan.style?.id ? String(scan.style.id) : "";
  let size = scan.size;
  let measurements = [];
  let results = {};
  let selected = null;
  let showValues = false;
  let enlarged = false;
  const dirty = new Set();
  const [W, H] = scan.debug.rect_size;
  let poll = null;

  const recompute = () => {
    measurements = evaluate(scan.defs, landmarks, scan.px_per_mm);
    results = compare(measurements, spec);
  };
  recompute();

  view.innerHTML = `
    <div id="banner"></div>
    <div class="card flush">
      <div class="editor-scroll" id="scroller">
        <div class="editor" id="ed">
          <img id="img" src="${scan.images.rect}" alt="Straightened photo of the garment" crossorigin="anonymous">
          <svg id="svg" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none"></svg>
          <canvas class="loupe" id="loupe" width="240" height="240"></canvas>
        </div>
      </div>
      <div class="row" style="padding:8px 12px">
        <span class="small muted grow">Drag a point to correct it. Orange points are worth a check. Tap a row to see its line.</span>
        <button class="btn" id="zoom" type="button" style="min-height:36px;padding:4px 12px">Enlarge</button>
        <button class="btn" id="vals" type="button" style="min-height:36px;padding:4px 12px">Values</button>
      </div>
    </div>
    <div class="card flush"><table class="meas" id="table"></table></div>
    <div id="warns"></div>
    <div class="card" id="ai"></div>
    <div class="card stack">
      <div class="grid2">
        <label class="field"><span>Style</span><select id="style"><option value="">— No style —</option>
          ${state.styles.map((s) => `<option value="${s.id}">${esc(s.code)}${s.name ? " · " + esc(s.name) : ""}</option>`).join("")}
        </select></label>
        <label class="field"><span>Size</span><select id="size"></select></label>
      </div>
      <label class="field"><span>Label / PO / sample</span><input id="label" autocomplete="off"></label>
      <label class="field"><span>Notes</span><textarea id="notes"></textarea></label>
      <div class="btn-row">
        <button class="btn primary" id="save" type="button">Save</button>
        <a class="btn" href="#/scan">New scan</a>
      </div>
      <div class="row">
        <a class="btn grow" id="dl" href="${scan.images.annotated}" download="measurement-${scan.id}.jpg">Download image</a>
        <button class="btn danger" id="del" type="button">Delete</button>
      </div>
      <p class="muted small">${esc(typeLabel(scan.garment_type))} · ${new Date(scan.created_at).toLocaleString()} ·
        photo ${scan.debug.photo_px_per_mm} px/mm · ${scan.debug.sheets.length} sheet(s) · tilt ${scan.debug.tilt_deg}°</p>
    </div>`;

  const $ = (s) => view.querySelector("#" + s);
  const svg = $("svg"), img = $("img"), ed = $("ed"), loupe = $("loupe");
  $("label").value = scan.label || "";
  $("notes").value = scan.notes || "";
  $("style").value = styleId;

  function renderBanner() {
    const all = Object.values(results);
    const checked = all.filter((r) => r.status === "pass" || r.status === "fail");
    const fails = checked.filter((r) => r.status === "fail");
    const meta = [styleCode(), size, $("label").value].filter(Boolean).map(esc).join(" · ");
    let cls = "none", title = "Measured – no spec for this style/size";
    if (checked.length && !fails.length) { cls = "pass"; title = `PASS · all ${checked.length} points within tolerance`; }
    if (fails.length) { cls = "fail"; title = `FAIL · ${fails.length} of ${checked.length} points out of tolerance`; }
    const status = scan.status === "saved" && !dirty.size ? "Saved" : "Not saved yet";
    $("banner").innerHTML = `<div class="banner ${cls}">${title}<div class="sub">${meta || typeLabel(scan.garment_type)} · ${status}</div></div>`;
  }

  function styleCode() {
    return state.styles.find((s) => String(s.id) === styleId)?.code || "";
  }

  function renderTable() {
    const rows = measurements.map((m) => {
      const k = resultKey(m), r = results[k];
      const side = m.side ? `<span class="side"> ${m.side === "l" ? "L" : "R"}</span>` : "";
      const low = m.points.some((p) => (conf[p] ?? 1) < 0.9);
      return `<tr data-k="${k}" class="${r.status} ${selected === k ? "sel" : ""}">
        <td class="pt">${esc(m.label)}${side}${low ? ' <span class="chip warn">check</span>' : ""}</td>
        <td>${specText(r, u)}</td>
        <td><b>${fmt(m.value_mm, u)}</b></td>
        <td class="diff">${r.diff_mm == null ? "" : fmt(r.diff_mm, u, true)}</td></tr>`;
    }).join("");
    $("table").innerHTML = `<thead><tr><th>Point</th><th>Spec</th><th>Actual ${unitLabel(u)}</th><th>Diff</th></tr></thead><tbody>${rows}</tbody>`;
  }

  function renderSvg() {
    const k = W / (ed.clientWidth || 360);
    const parts = [];
    const used = new Set();
    for (const m of measurements) {
      if (m.value_mm == null) continue;
      const k2 = resultKey(m), r = results[k2];
      let pts = m.points.map((n) => landmarks[n]);
      m.points.forEach((n) => used.add(n));
      if (m.kind === "dy") pts = [pts[0], [pts[0][0], pts[1][1]]];
      const dim = selected && selected !== k2;
      const col = COLORS[r.status] || COLORS.no_spec;
      parts.push(`<polyline points="${pts.map((p) => p.join(",")).join(" ")}" fill="none" stroke="${col}"
        stroke-width="${selected === k2 ? 5 : 3}" vector-effect="non-scaling-stroke" opacity="${dim ? 0.18 : 0.95}"/>`);
      if (selected === k2 || (showValues && !selected)) {
        const mid = pts.length === 2 ? [(pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2] : pts[1];
        parts.push(`<text x="${mid[0]}" y="${mid[1] - 6 * k}" font-size="${13 * k}" font-weight="700" text-anchor="middle"
          fill="${col}" stroke="#fff" stroke-width="${4 * k}" paint-order="stroke">${fmt(m.value_mm, u)}</text>`);
      }
    }
    for (const n of used) {
      const p = landmarks[n];
      if (!p) continue;
      const low = (conf[n] ?? 1) < 0.9;
      parts.push(`<g class="lm" data-n="${n}" transform="translate(${p[0]},${p[1]})">
        <circle r="${22 * k}" fill="transparent"/>
        <circle r="${7 * k}" fill="#fff" stroke="${low ? LOW : "#222"}" stroke-width="${low ? 3 : 2}" vector-effect="non-scaling-stroke"/></g>`);
    }
    svg.innerHTML = parts.join("");
  }

  function renderWarnings() {
    const lows = Object.entries(conf).filter(([, c]) => c < 0.9).length;
    $("warns").innerHTML = (scan.warnings || []).map((w) => `<div class="notice">${esc(w.message)}</div>`).join("")
      + (lows ? `<div class="notice info">${lows} point(s) shown in orange were hard to see in the outline – please check them.</div>` : "");
    if ($("warns").innerHTML) $("warns").style.marginBottom = "14px";
  }

  function renderAI() {
    const el = $("ai");
    const ai = scan.ai || {};
    if (scan.ai_status === "off") {
      el.innerHTML = `<h3>AI check</h3><p class="muted small">AI checks are turned off on the server.</p>`;
      return;
    }
    if (scan.ai_status === "pending") {
      el.innerHTML = `<h3>AI check</h3><div class="row"><div class="spinner" style="width:22px;height:22px;border-width:3px"></div>
        <span class="muted">Qwen is looking at the photo…</span></div>`;
      return;
    }
    const c = ai.check;
    const yesno = (v, good) => `<span class="chip ${v === good ? "pass" : "warn"}">`;
    let html = `<h3>AI check <span class="muted small">(${esc(ai.model || "Qwen")})</span></h3>`;
    if (c) {
      html += `<div class="row" style="margin-bottom:8px">
        ${yesno(c.type_matches, true)}${c.type_matches ? "Type OK" : "Looks like " + esc(c.garment_type)}</span>
        ${yesno(c.lying_flat, true)}${c.lying_flat ? "Flat" : "Not flat"}</span>
        ${yesno(c.sleeves_or_legs_folded, false)}${c.sleeves_or_legs_folded ? "Folded sleeve/leg" : "Spread out"}</span>
        ${yesno(c.wrinkles_or_stretching, false)}${c.wrinkles_or_stretching ? "Wrinkles/stretch" : "Smooth"}</span>
        ${yesno(c.sheet_visible_and_flat, true)}${c.sheet_visible_and_flat ? "Sheet OK" : "Check sheet"}</span></div>`;
      if (c.issues?.length) html += `<ul class="small">${c.issues.map((i) => `<li>${esc(i)}</li>`).join("")}</ul>`;
      if (c.notes) html += `<p class="small muted">${esc(c.notes)}</p>`;
    } else if (ai.check_error) {
      html += `<p class="small muted">Photo check unavailable: ${esc(ai.check_error)}</p>`;
    }
    if (ai.summary) html += `<p>${esc(ai.summary)}</p>`;
    else if (ai.summary_error) html += `<p class="small muted">Summary unavailable: ${esc(ai.summary_error)}</p>`;
    if (ai.error) html += `<p class="small muted">AI check unavailable: ${esc(ai.error)}</p>`;
    html += `<p class="small muted">AI notes are suggestions. Pass/fail comes from the measurements and the spec.</p>`;
    el.innerHTML = html;
  }

  function renderAll() {
    renderBanner();
    renderTable();
    renderSvg();
  }

  function startPoll() {
    clearInterval(poll);
    if (scan.ai_status !== "pending") return;
    poll = setInterval(async () => {
      try {
        const r = await api(`/api/scans/${id}/ai`);
        if (r.ai_status !== "pending") {
          scan.ai_status = r.ai_status;
          scan.ai = r.ai;
          renderAI();
          clearInterval(poll);
        }
      } catch { /* try again */ }
    }, 1500);
  }

  // ---- sizes / style switching
  async function loadSpec() {
    const st = state.styles.find((s) => String(s.id) === styleId);
    const sizes = st ? st.sizes : [];
    $("size").innerHTML = sizes.length ? sizes.map((z) => `<option>${esc(z)}</option>`).join("") : `<option value="">—</option>`;
    $("size").disabled = !sizes.length;
    if (sizes.length && !sizes.includes(size)) size = sizes[0];
    if (sizes.length) $("size").value = size;
    if (!st) { spec = []; size = ""; }
    else {
      const full = await api(`/api/styles/${st.id}`);
      spec = full.spec.filter((p) => p.size === size);
    }
    recompute();
    renderAll();
  }
  $("style").addEventListener("change", () => { styleId = $("style").value; dirty.add("_meta"); loadSpec(); });
  $("size").addEventListener("change", () => { size = $("size").value; dirty.add("_meta"); loadSpec(); });
  $("label").addEventListener("input", () => { dirty.add("_meta"); renderBanner(); });
  $("notes").addEventListener("input", () => dirty.add("_meta"));

  // ---- view options
  $("zoom").addEventListener("click", () => {
    enlarged = !enlarged;
    ed.style.width = enlarged ? "250%" : "";
    $("zoom").textContent = enlarged ? "Fit" : "Enlarge";
    renderSvg();
  });
  $("vals").addEventListener("click", () => {
    showValues = !showValues;
    $("vals").classList.toggle("primary", showValues);
    renderSvg();
  });

  // ---- table selection
  $("table").addEventListener("click", (e) => {
    const tr = e.target.closest("tr[data-k]");
    if (!tr) return;
    selected = selected === tr.dataset.k ? null : tr.dataset.k;
    renderTable();
    renderSvg();
    ed.scrollIntoView({ behavior: "smooth", block: "nearest" });
    if (enlarged && selected) {
      const m = measurements.find((x) => resultKey(x) === selected);
      const p = m && landmarks[m.points[0]];
      if (p) $("scroller").scrollTo({ left: p[0] / W * ed.clientWidth - $("scroller").clientWidth / 2, behavior: "smooth" });
    }
  });

  // ---- dragging landmarks (with a magnifier above the finger)
  let drag = null;
  const toImg = (e) => {
    const r = svg.getBoundingClientRect();
    return [(e.clientX - r.left) * (W / r.width), (e.clientY - r.top) * (H / r.height)];
  };
  const showLoupe = (e, p) => {
    const r = ed.getBoundingClientRect();
    const k = W / r.width;
    const span = 40 * k;
    const ctx = loupe.getContext("2d");
    ctx.fillStyle = "#222";
    ctx.fillRect(0, 0, 240, 240);
    ctx.drawImage(img, p[0] - span / 2, p[1] - span / 2, span, span, 0, 0, 240, 240);
    ctx.strokeStyle = "#ff3b30";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(120, 95); ctx.lineTo(120, 145); ctx.moveTo(95, 120); ctx.lineTo(145, 120);
    ctx.stroke();
    loupe.style.display = "block";
    const x = Math.min(Math.max(e.clientX - 60, 8), window.innerWidth - 128);
    const y = e.clientY - 180 < 8 ? e.clientY + 60 : e.clientY - 180;
    loupe.style.left = x + "px";
    loupe.style.top = y + "px";
  };
  svg.addEventListener("pointerdown", (e) => {
    const g = e.target.closest(".lm");
    if (!g) return;
    e.preventDefault();
    const n = g.dataset.n, p = toImg(e);
    drag = { n, off: [landmarks[n][0] - p[0], landmarks[n][1] - p[1]], id: e.pointerId };
    svg.setPointerCapture(e.pointerId);
    showLoupe(e, landmarks[n]);
  });
  svg.addEventListener("pointermove", (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    e.preventDefault();
    const p = toImg(e);
    const q = [Math.min(Math.max(p[0] + drag.off[0], 0), W), Math.min(Math.max(p[1] + drag.off[1], 0), H)];
    landmarks[drag.n] = q;
    recompute();
    renderSvg();
    renderTable();
    renderBanner();
    showLoupe(e, q);
  });
  const endDrag = (e) => {
    if (!drag) return;
    dirty.add(drag.n);
    conf[drag.n] = 1;
    drag = null;
    loupe.style.display = "none";
    renderAll();
  };
  svg.addEventListener("pointerup", endDrag);
  svg.addEventListener("pointercancel", endDrag);
  svg.addEventListener("touchstart", (e) => { if (e.target.closest(".lm")) e.preventDefault(); }, { passive: false });

  // ---- save / delete
  $("save").addEventListener("click", async () => {
    $("save").disabled = true;
    try {
      const moved = Object.fromEntries([...dirty].filter((n) => n !== "_meta").map((n) => [n, landmarks[n]]));
      scan = await api(`/api/scans/${id}`, { method: "PUT", json: {
        landmarks: moved, label: $("label").value.trim(), notes: $("notes").value, style_id: styleId || null,
        size, status: "saved" } });
      landmarks = structuredClone(scan.landmarks);
      conf = { ...scan.confidence };
      spec = scan.spec || [];
      dirty.clear();
      recompute();
      renderAll();
      renderAI();
      startPoll();
      $("dl").href = scan.images.annotated;
      toast("Saved");
    } catch (e) {
      toast(e.message);
    } finally {
      $("save").disabled = false;
    }
  });
  $("del").addEventListener("click", async () => {
    if (!confirm("Delete this measurement?")) return;
    await api(`/api/scans/${id}`, { method: "DELETE" });
    toast("Deleted");
    location.hash = scan.status === "saved" ? "#/history" : "#/scan";
  });

  const onResize = () => renderSvg();
  window.addEventListener("resize", onResize);
  if (!img.complete) img.addEventListener("load", renderSvg, { once: true });
  if (scan.style && !state.styles.some((s) => s.id === scan.style.id)) state.styles.push(scan.style);
  await loadSpec();
  renderWarnings();
  renderAI();
  startPoll();

  return () => {
    clearInterval(poll);
    window.removeEventListener("resize", onResize);
  };
}
