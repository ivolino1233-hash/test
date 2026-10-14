import { api, esc } from "../api.js";
import { recall, remember, state, typeLabel } from "../state.js";

export async function historyView(view) {
  let styleId = recall("historyStyle", "");
  let offset = 0;
  const PAGE = 30;

  view.innerHTML = `
    <div class="card stack">
      <h2>History</h2>
      <label class="field"><span>Style</span>
        <select id="style"><option value="">All styles</option>
          ${state.styles.map((s) => `<option value="${s.id}">${esc(s.code)}${s.name ? " · " + esc(s.name) : ""}</option>`).join("")}
        </select></label>
      <div class="btn-row">
        <a class="btn" id="xlsx">Export Excel</a>
        <a class="btn" id="csv">Export CSV</a>
      </div>
    </div>
    <div class="card flush" id="list"></div>
    <button class="btn block hidden" id="more" type="button">Load more</button>`;

  const $ = (s) => view.querySelector("#" + s);
  if (state.styles.some((s) => String(s.id) === String(styleId))) $("style").value = styleId;
  else styleId = "";

  const links = () => {
    const q = styleId ? `?style_id=${styleId}` : "";
    $("xlsx").href = `/api/export.xlsx${q}`;
    $("csv").href = `/api/export.csv${q}`;
  };

  const item = (s) => {
    const chips = s.pass_count + s.fail_count
      ? `${s.fail_count ? `<span class="chip fail">${s.fail_count} fail</span>` : ""}<span class="chip pass">${s.pass_count} pass</span>`
      : `<span class="chip">no spec</span>`;
    return `<a class="scan-item" href="#/scan/${s.id}">
      <img src="${s.thumb}" alt="" loading="lazy">
      <div><div class="t">${esc(s.style?.code || typeLabel(s.garment_type))}${s.size ? " · " + esc(s.size) : ""}</div>
        <div class="muted small">${esc(s.label || "")}${s.label ? " · " : ""}${new Date(s.created_at).toLocaleString()}</div>
        <div class="row" style="margin-top:6px">${chips}</div></div></a>`;
  };

  async function load(reset) {
    if (reset) { offset = 0; $("list").innerHTML = ""; }
    const q = new URLSearchParams({ limit: PAGE, offset });
    if (styleId) q.set("style_id", styleId);
    const rows = await api(`/api/scans?${q}`);
    offset += rows.length;
    if (reset && !rows.length) {
      $("list").innerHTML = `<p class="muted" style="padding:16px">No saved measurements yet. Measure a garment and tap <b>Save</b>.</p>`;
    } else {
      $("list").insertAdjacentHTML("beforeend", rows.map(item).join(""));
    }
    $("more").classList.toggle("hidden", rows.length < PAGE);
  }

  $("style").addEventListener("change", () => {
    styleId = $("style").value;
    remember("historyStyle", styleId);
    links();
    load(true);
  });
  $("more").addEventListener("click", () => load(false));
  links();
  await load(true);
}
