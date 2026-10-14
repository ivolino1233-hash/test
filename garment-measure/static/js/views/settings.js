import { api, esc, toast } from "../api.js";
import { state } from "../state.js";

export async function settingsView(view) {
  const s = state.settings;
  view.innerHTML = `
    <div class="card stack">
      <h2>Settings</h2>
      <label class="field"><span>Units</span>
        <select id="unit"><option value="cm">Centimetres</option><option value="in">Inches (⅛)</option></select></label>
      <label class="row"><input type="checkbox" id="auto" style="width:auto;min-height:0">
        <span>Take the photo automatically when the garment is steady</span></label>
    </div>

    <div class="card stack">
      <h3>Reference sheet</h3>
      <p class="muted small">Print at <b>100 % / Actual size</b> and glue it to card so it stays flat. Use two sheets
        (one each side of the garment) for the best accuracy on big garments.</p>
      <div class="btn-row">
        <a class="btn primary" href="/marker.pdf?sheets=1" target="_blank">Print 1 sheet</a>
        <a class="btn" href="/marker.pdf?sheets=2" target="_blank">Print 2 sheets</a>
      </div>
      <p class="small">Printers often shrink pages slightly. Measure the two rulers on your printout with a steel ruler
        and enter what you read:</p>
      <div class="grid2">
        <label class="field"><span>Bottom ruler (should be 150 mm)</span><input id="rh" inputmode="decimal"></label>
        <label class="field"><span>Side ruler (should be 250 mm)</span><input id="rv" inputmode="decimal"></label>
      </div>
      <button class="btn" id="saveRulers" type="button">Save ruler lengths</button>
    </div>

    <div class="card stack" id="ai">
      <h3>AI (Qwen)</h3>
      <div id="aiInfo" class="muted small">Checking…</div>
      <button class="btn" id="aiRefresh" type="button">Check again</button>
    </div>

    <div class="card stack">
      <h3>Phones</h3>
      <p class="muted small">To set up another phone (certificate for the live camera, link, QR code), open the setup page.</p>
      <a class="btn" href="/onboarding">Open setup page</a>
    </div>`;

  const $ = (id) => view.querySelector("#" + id);
  $("unit").value = s.unit;
  $("auto").checked = s.auto_capture !== false;
  $("rh").value = s.ruler_h_mm;
  $("rv").value = s.ruler_v_mm;

  const save = async (patch, msg) => {
    try {
      state.settings = await api("/api/settings", { method: "PUT", json: patch });
      toast(msg || "Saved");
    } catch (e) {
      toast(e.message);
    }
  };
  $("unit").addEventListener("change", () => save({ unit: $("unit").value }, "Units changed"));
  $("auto").addEventListener("change", () => save({ auto_capture: $("auto").checked }));
  $("saveRulers").addEventListener("click", () => save({
    ruler_h_mm: parseFloat($("rh").value.replace(",", ".")), ruler_v_mm: parseFloat($("rv").value.replace(",", ".")),
  }, "Ruler lengths saved"));

  async function ai() {
    $("aiInfo").textContent = "Checking…";
    try {
      const st = await api("/api/status");
      const q = st.qwen;
      if (!q.enabled) { $("aiInfo").textContent = "AI checks are turned off (QWEN_ENABLED=false)."; return; }
      $("aiInfo").innerHTML = `
        <div><b>${q.ok ? "Connected" : "Not available"}</b> – ${esc(q.base_url)}</div>
        <div>Model: ${esc(q.model || "–")}</div>
        ${q.error ? `<div style="color:var(--fail)">${esc(q.error)}</div>` : ""}
        <div>Waiting jobs: ${st.queue}</div>`;
    } catch (e) {
      $("aiInfo").textContent = e.message;
    }
  }
  $("aiRefresh").addEventListener("click", ai);
  ai();
}
