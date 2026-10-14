import { api, esc, toast } from "../api.js";
import { fromMm, toMm, unitLabel } from "../measure.js";
import { refreshStyles, state, typeLabel, unit } from "../state.js";

export async function stylesView(view) {
  await refreshStyles();
  view.innerHTML = `
    <div class="card">
      <div class="row"><h2 class="grow" style="margin:0">Styles &amp; specs</h2>
        <a class="btn primary" href="#/styles/new">New style</a></div>
    </div>
    <div class="card" id="list"></div>
    <div class="card stack">
      <h3>Import a spec sheet (CSV)</h3>
      <p class="muted small">One row per style, size and point: <code>style_code, style_name, customer, garment_type, size,
        point, target_cm, tol_minus_cm, tol_plus_cm</code>. Point names like “1/2 chest”, “body length”, “sleeve length”,
        “cuff” are recognised. Existing styles are updated.</p>
      <div class="btn-row">
        <label class="btn primary" for="csv">Import CSV</label>
        <a class="btn" href="/api/styles/template.csv">Template</a>
      </div>
      <input id="csv" type="file" accept=".csv,text/csv" class="hidden">
      <div id="importMsg"></div>
    </div>`;
  const list = view.querySelector("#list");
  list.innerHTML = state.styles.length ? state.styles.map((s) => `
      <a class="list-link" href="#/styles/${s.id}">
        <div><b>${esc(s.code)}</b> ${s.name ? "· " + esc(s.name) : ""}
          <div class="muted small">${esc(typeLabel(s.garment_type))}${s.customer ? " · " + esc(s.customer) : ""} · sizes ${esc(s.sizes.join(", ") || "–")}</div></div>
        <span class="muted">›</span></a>`).join("")
    : `<p class="muted">No styles yet. Add one with its spec so each scan shows pass/fail.</p>`;

  view.querySelector("#csv").addEventListener("change", async (e) => {
    const f = e.target.files?.[0];
    if (!f) return;
    const fd = new FormData();
    fd.append("file", f);
    try {
      const r = await api("/api/styles/import", { method: "POST", body: fd });
      view.querySelector("#importMsg").innerHTML =
        `<p class="notice info">Imported: ${esc(r.imported.join(", ") || "nothing")}</p>` +
        r.errors.map((x) => `<p class="notice">${esc(x)}</p>`).join("");
      await refreshStyles();
      toast(`Imported ${r.imported.length} style(s)`);
      setTimeout(() => stylesView(view), r.errors.length ? 4000 : 800);
    } catch (err) {
      toast(err.message);
    }
  });
}

export async function styleEditView(view, id) {
  const isNew = id === "new";
  const u = unit();
  const style = isNew ? { code: "", name: "", customer: "", garment_type: "sweater", sizes: ["S", "M", "L"], params: {}, notes: "", spec: [] }
    : await api(`/api/styles/${id}`);
  const typeOpts = Object.entries(state.catalogue.types)
    .map(([k, t]) => `<option value="${k}" ${k === style.garment_type ? "selected" : ""}>${esc(t.label)}</option>`).join("");

  view.innerHTML = `
    <form class="card stack" id="f">
      <div class="row"><a href="#/styles" class="muted">‹ Styles</a></div>
      <h2>${isNew ? "New style" : esc(style.code)}</h2>
      <div class="grid2">
        <label class="field"><span>Style code *</span><input name="code" required value="${esc(style.code)}"></label>
        <label class="field"><span>Name</span><input name="name" value="${esc(style.name)}"></label>
        <label class="field"><span>Customer</span><input name="customer" value="${esc(style.customer)}"></label>
        <label class="field"><span>Garment type</span><select name="garment_type">${typeOpts}</select></label>
      </div>
      <label class="field"><span>Sizes (comma separated)</span><input name="sizes" value="${esc(style.sizes.join(", "))}"></label>
      <div id="params" class="grid2"></div>
      <h3 style="margin-top:8px">Spec (${unitLabel(u)})</h3>
      <p class="muted small">Leave a target empty to skip that point. Tolerance applies to all sizes.</p>
      <div class="spec-wrap"><table class="spec" id="spec"></table></div>
      <label class="field"><span>Notes</span><textarea name="notes">${esc(style.notes)}</textarea></label>
      <div class="btn-row">
        <button class="btn primary" type="submit">Save style</button>
        ${isNew ? `<a class="btn" href="#/styles">Cancel</a>` : `<button class="btn danger" type="button" id="del">Delete</button>`}
      </div>
    </form>`;

  const form = view.querySelector("#f");
  const specByKey = {};
  for (const p of style.spec) {
    specByKey[p.key] ??= { tol_minus_mm: p.tol_minus_mm, tol_plus_mm: p.tol_plus_mm, sizes: {} };
    specByKey[p.key].sizes[p.size] = p.target_mm;
  }

  const sizes = () => form.sizes.value.split(",").map((s) => s.trim()).filter(Boolean);

  function collect() {
    // keep typed values when the size list or type changes
    view.querySelectorAll("#spec tr[data-key]").forEach((tr) => {
      const k = tr.dataset.key;
      const e = (specByKey[k] ??= { sizes: {} });
      e.tol_minus_mm = toMm(tr.querySelector('[data-f="tm"]').value, u);
      e.tol_plus_mm = toMm(tr.querySelector('[data-f="tp"]').value, u);
      tr.querySelectorAll("[data-size]").forEach((inp) => { e.sizes[inp.dataset.size] = toMm(inp.value, u); });
    });
  }

  function renderParams() {
    const t = form.garment_type.value, fam = state.catalogue.types[t].family;
    const p = { ...state.catalogue.params, ...style.params };
    const fields = fam === "top" ? [["chest_offset_mm", "Chest measured below armhole (cm)"], ["bicep_offset_mm", "Upper arm below armhole (cm)"]]
      : [["hip_offset_mm", "Hip measured below waist (cm)"]].concat(fam === "trousers" ? [["thigh_offset_mm", "Thigh below crotch (cm)"]] : []);
    view.querySelector("#params").innerHTML = fields.map(([k, label]) =>
      `<label class="field"><span>${label}</span><input inputmode="decimal" data-param="${k}" value="${p[k] / 10}"></label>`).join("");
  }

  function renderSpec() {
    const t = form.garment_type.value;
    const defs = state.catalogue.defs[t];
    const zs = sizes();
    const tol = (e, f) => (e && e[f] != null ? fromMm(e[f], u) : fromMm(10, u));
    view.querySelector("#spec").innerHTML = `
      <thead><tr><th>Point</th>${zs.map((z) => `<th>${esc(z)}</th>`).join("")}<th>Tol −</th><th>Tol +</th></tr></thead>
      <tbody>${defs.map((d) => {
        const e = specByKey[d.key];
        return `<tr data-key="${d.key}"><td>${esc(d.label)}</td>
          ${zs.map((z) => `<td><input inputmode="decimal" data-size="${esc(z)}" value="${fromMm(e?.sizes?.[z], u)}" aria-label="${esc(d.label)} ${esc(z)}"></td>`).join("")}
          <td><input inputmode="decimal" data-f="tm" value="${tol(e, "tol_minus_mm")}" aria-label="${esc(d.label)} tolerance minus"></td>
          <td><input inputmode="decimal" data-f="tp" value="${tol(e, "tol_plus_mm")}" aria-label="${esc(d.label)} tolerance plus"></td></tr>`;
      }).join("")}</tbody>`;
  }

  renderParams();
  renderSpec();
  form.sizes.addEventListener("change", () => { collect(); renderSpec(); });
  form.garment_type.addEventListener("change", () => { collect(); renderParams(); renderSpec(); });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    collect();
    const zs = sizes();
    const keys = new Set(state.catalogue.defs[form.garment_type.value].map((d) => d.key));
    const spec = [];
    for (const [k, e2] of Object.entries(specByKey)) {
      if (!keys.has(k)) continue;
      for (const z of zs) {
        const v = e2.sizes?.[z];
        if (v == null) continue;
        spec.push({ size: z, key: k, target_mm: v, tol_minus_mm: e2.tol_minus_mm ?? 10, tol_plus_mm: e2.tol_plus_mm ?? e2.tol_minus_mm ?? 10 });
      }
    }
    const params = {};
    view.querySelectorAll("[data-param]").forEach((inp) => { const v = parseFloat(inp.value.replace(",", ".")); if (isFinite(v)) params[inp.dataset.param] = v * 10; });
    const body = { code: form.code.value.trim(), name: form.name.value.trim(), customer: form.customer.value.trim(),
      garment_type: form.garment_type.value, sizes: zs, params, notes: form.notes.value, spec };
    try {
      const saved = await api(isNew ? "/api/styles" : `/api/styles/${id}`, { method: isNew ? "POST" : "PUT", json: body });
      await refreshStyles();
      toast("Style saved");
      location.hash = `#/styles/${saved.id}`;
      if (!isNew) styleEditView(view, saved.id);
    } catch (err) {
      toast(err.message);
    }
  });

  view.querySelector("#del")?.addEventListener("click", async () => {
    if (!confirm(`Delete style ${style.code}? Saved measurements are kept.`)) return;
    await api(`/api/styles/${id}`, { method: "DELETE" });
    await refreshStyles();
    location.hash = "#/styles";
  });
}
