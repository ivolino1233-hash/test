// Small fetch wrapper: JSON in/out, readable errors, and the optional shared PIN.

let pinPrompt = null;

function askPin() {
  if (pinPrompt) return pinPrompt;
  pinPrompt = new Promise((resolve) => {
    const bg = document.createElement("div");
    bg.className = "modal-bg";
    bg.innerHTML = `<form class="modal stack">
        <h2>Enter PIN</h2>
        <p class="muted small">This app is protected with a shared PIN.</p>
        <input type="password" inputmode="numeric" autocomplete="current-password" name="pin" required>
        <p class="small" style="color:var(--fail)" hidden></p>
        <button class="btn primary block" type="submit">Unlock</button>
      </form>`;
    document.body.appendChild(bg);
    const form = bg.querySelector("form");
    const err = bg.querySelector("p[hidden]");
    form.pin.focus();
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const r = await fetch("/api/login", { method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin: form.pin.value }) });
      if (r.ok) { bg.remove(); pinPrompt = null; resolve(); }
      else { err.hidden = false; err.textContent = "Wrong PIN"; form.pin.select(); }
    });
  });
  return pinPrompt;
}

export async function api(path, opts = {}) {
  const init = { credentials: "same-origin", method: opts.method || (opts.json || opts.body ? "POST" : "GET"),
    headers: { ...(opts.headers || {}) } };
  if (opts.json !== undefined) {
    init.headers["Content-Type"] = "application/json";
    init.body = JSON.stringify(opts.json);
  } else if (opts.body !== undefined) init.body = opts.body;
  if (opts.signal) init.signal = opts.signal;
  const r = await fetch(path, init);
  if (r.status === 401 && path !== "/api/login") {
    await askPin();
    return api(path, opts);
  }
  const ct = r.headers.get("content-type") || "";
  const data = ct.includes("json") ? await r.json() : null;
  if (!r.ok) {
    const msg = data?.error?.message || (typeof data?.detail === "string" ? data.detail : null) || `Request failed (${r.status})`;
    const e = new Error(msg);
    e.status = r.status;
    e.data = data;
    throw e;
  }
  return data ?? r;
}

export function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}

let toastTimer;
export function toast(msg, ms = 2600) {
  const t = document.getElementById("toast");
  t.textContent = msg;
  t.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove("show"), ms);
}
