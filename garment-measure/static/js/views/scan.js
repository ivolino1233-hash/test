import { api, esc, toast } from "../api.js";
import { LiveCamera, liveCameraSupported } from "../camera.js";
import { recall, remember, state, typeLabel } from "../state.js";

const ICON_CAM = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8V6a2 2 0 0 1 2-2h2M16 4h2a2 2 0 0 1 2 2v2M20 16v2a2 2 0 0 1-2 2h-2M8 20H6a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="3.5"/></svg>`;
const ICON_PHOTO = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>`;

export async function scanView(view) {
  const styles = state.styles;
  const last = recall("scan", {});
  const typeOpts = Object.entries(state.catalogue.types)
    .map(([k, t]) => `<option value="${k}">${esc(t.label)}</option>`).join("");
  const live = liveCameraSupported();

  view.innerHTML = `
    <div class="card stack">
      <h2>New measurement</h2>
      <label class="field"><span>Style</span>
        <select id="style"><option value="">— No style (measure only) —</option>
          ${styles.map((s) => `<option value="${s.id}">${esc(s.code)}${s.name ? " · " + esc(s.name) : ""}</option>`).join("")}
        </select></label>
      <div class="grid2">
        <label class="field"><span>Size</span><select id="size"></select></label>
        <label class="field"><span>Garment type</span>
          <select id="type"><option value="auto">Detect automatically</option>${typeOpts}</select></label>
      </div>
      <label class="field"><span>Label / PO / sample (optional)</span>
        <input id="label" autocomplete="off" placeholder="e.g. PO-2291 #3"></label>
    </div>

    <div class="stack">
      ${live ? `<button class="btn primary big block" id="live" type="button">${ICON_CAM} Live camera</button>` : ""}
      <label class="btn ${live ? "" : "primary big"} block" for="shoot">${ICON_PHOTO} Take photo</label>
      <input id="shoot" type="file" accept="image/*" capture="environment" class="hidden">
      <label class="btn block" for="pick">Choose a photo</label>
      <input id="pick" type="file" accept="image/*" class="hidden">
    </div>
    ${live ? "" : `<p class="notice" style="margin-top:12px">Live camera needs the secure (https) link.
       <a href="/onboarding">Set it up once</a> – until then, <b>Take photo</b> works the same way.</p>`}

    <details class="card" style="margin-top:14px">
      <summary><b>How to lay out the garment</b></summary>
      <ol class="steps" style="margin-top:12px">
        <li>Plain table that contrasts with the garment colour; even light, no strong shadows.</li>
        <li>Garment flat, front up, collar or waistband towards the top of the phone screen. Smooth it out without stretching.</li>
        <li>Spread sleeves away from the body, straight. Keep trouser legs slightly apart.</li>
        <li>Put the printed reference sheet flat on the table next to the garment, not touching it. For big garments a second sheet on the other side improves accuracy.</li>
        <li>Hold the phone above the middle, as straight down as you can, with everything in view.</li>
      </ol>
    </details>`;

  const $ = (id) => view.querySelector("#" + id);
  const fillSizes = () => {
    const st = styles.find((s) => String(s.id) === $("style").value);
    const sizes = st ? st.sizes : [];
    $("size").innerHTML = sizes.length ? sizes.map((z) => `<option>${esc(z)}</option>`).join("")
      : `<option value="">—</option>`;
    $("size").disabled = !sizes.length;
    if (st) { $("type").value = st.garment_type; $("type").disabled = true; }
    else { $("type").disabled = false; $("type").value = last.type || "auto"; }
    if (last.size && sizes.includes(last.size)) $("size").value = last.size;
  };
  if (last.style && styles.some((s) => String(s.id) === String(last.style))) $("style").value = last.style;
  fillSizes();
  $("label").value = last.label || "";
  $("style").addEventListener("change", fillSizes);

  const choices = () => {
    const c = { style: $("style").value, size: $("size").value, type: $("type").value, label: $("label").value.trim() };
    remember("scan", c);
    return c;
  };

  const run = async (blob) => {
    const c = choices();
    view.innerHTML = `<div class="busy"><div class="spinner"></div><b>Measuring…</b>
      <span class="muted small">Straightening the photo and finding the edges</span></div>`;
    const fd = new FormData();
    fd.append("image", blob, "photo.jpg");
    fd.append("style_id", c.style);
    fd.append("size", c.size);
    fd.append("garment_type", c.type);
    fd.append("label", c.label);
    try {
      const scan = await api("/api/measure", { method: "POST", body: fd });
      location.hash = `#/scan/${scan.id}`;
    } catch (e) {
      const warns = e.data?.warnings || [];
      view.innerHTML = `
        <div class="banner fail">Could not measure<div class="sub">${esc(e.message)}</div></div>
        ${warns.map((w) => `<div class="notice">${esc(w.message)}</div>`).join("")}
        <div class="btn-row" style="margin-top:14px">
          <a class="btn primary" href="#/scan" id="again">Try again</a>
          <a class="btn" href="/onboarding">Setup help</a>
        </div>`;
      view.querySelector("#again").addEventListener("click", (ev) => { ev.preventDefault(); scanView(view); });
    }
  };

  for (const id of ["shoot", "pick"]) {
    $(id).addEventListener("change", (e) => {
      const f = e.target.files?.[0];
      if (f) run(f);
    });
  }
  $("live")?.addEventListener("click", async () => {
    choices();
    const cam = new LiveCamera({
      autoCapture: state.settings.auto_capture !== false,
      onCapture: (blob) => run(blob),
      onClose: () => toast("Camera closed"),
    });
    await cam.open();
  });
}

export { typeLabel };
