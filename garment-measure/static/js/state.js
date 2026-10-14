import { api } from "./api.js";

export const state = { catalogue: null, settings: null, styles: [], status: null };

export async function loadBasics() {
  const [catalogue, settings, styles] = await Promise.all([
    api("/api/catalogue"), api("/api/settings"), api("/api/styles"),
  ]);
  Object.assign(state, { catalogue, settings, styles });
}

export async function refreshStyles() {
  state.styles = await api("/api/styles");
  return state.styles;
}

export const unit = () => state.settings?.unit || "cm";

export function typeLabel(t) {
  return state.catalogue?.types?.[t]?.label || t;
}

export function remember(key, value) {
  try { localStorage.setItem("gm." + key, JSON.stringify(value)); } catch { /* private mode */ }
}
export function recall(key, fallback = null) {
  try { const v = localStorage.getItem("gm." + key); return v == null ? fallback : JSON.parse(v); } catch { return fallback; }
}
