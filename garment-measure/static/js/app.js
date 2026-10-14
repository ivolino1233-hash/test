import { api, esc } from "./api.js";
import { loadBasics, state } from "./state.js";
import { scanView } from "./views/scan.js";
import { resultView } from "./views/result.js";
import { historyView } from "./views/history.js";
import { stylesView, styleEditView } from "./views/styles.js";
import { settingsView } from "./views/settings.js";

const view = document.getElementById("view");
let cleanup = null;

const routes = [
  [/^#\/scan$/, "scan", () => scanView(view)],
  [/^#\/scan\/([a-z0-9]+)$/, "scan", (m) => resultView(view, m[1])],
  [/^#\/history$/, "history", () => historyView(view)],
  [/^#\/styles$/, "styles", () => stylesView(view)],
  [/^#\/styles\/(new|\d+)$/, "styles", (m) => styleEditView(view, m[1])],
  [/^#\/settings$/, "settings", () => settingsView(view)],
];

async function route() {
  const hash = location.hash || "#/scan";
  if (typeof cleanup === "function") cleanup();
  cleanup = null;
  for (const [re, tab, fn] of routes) {
    const m = hash.match(re);
    if (m) {
      document.querySelectorAll(".tabs a").forEach((a) => a.classList.toggle("active", a.dataset.tab === tab));
      window.scrollTo(0, 0);
      try {
        cleanup = await fn(m);
      } catch (e) {
        view.innerHTML = `<div class="card"><h2>Something went wrong</h2><p class="muted">${esc(e.message)}</p></div>`;
      }
      return;
    }
  }
  location.hash = "#/scan";
}

async function aiDot() {
  const dot = document.getElementById("ai-dot");
  try {
    state.status = await api("/api/status");
    const q = state.status.qwen;
    dot.className = "ai-dot " + (!q.enabled ? "" : q.ok ? "ok" : "bad");
    dot.textContent = !q.enabled ? "AI off" : q.ok ? "AI ready" : "AI offline";
    dot.title = q.enabled ? `${q.model || "no model"} @ ${q.base_url}${q.error ? " – " + q.error : ""}` : "AI checks disabled";
  } catch {
    dot.className = "ai-dot bad";
    dot.textContent = "Offline";
  }
}

document.getElementById("ai-dot").addEventListener("click", () => { location.hash = "#/settings"; });
window.addEventListener("hashchange", route);

(async () => {
  try {
    await loadBasics();
  } catch (e) {
    view.innerHTML = `<div class="card"><h2>Cannot reach the server</h2><p class="muted">${esc(e.message)}</p></div>`;
    return;
  }
  aiDot();
  setInterval(aiDot, 30000);
  route();
})();
