// Live camera: shows the phone camera full screen, sends a small frame to the server a few times
// a second, draws where it found the reference sheet and the garment, and takes the full-resolution
// photo when everything is ready and steady (or when the shutter is tapped).
import { api } from "./api.js";

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export function liveCameraSupported() {
  return window.isSecureContext && !!navigator.mediaDevices?.getUserMedia;
}

export class LiveCamera {
  constructor({ autoCapture = true, onCapture, onClose }) {
    this.auto = autoCapture;
    this.onCapture = onCapture;
    this.onClose = onClose;
    this.running = false;
    this.stable = 0;
    this.last = null;
  }

  async open() {
    const el = document.createElement("div");
    el.className = "cam";
    el.innerHTML = `
      <video playsinline muted autoplay></video>
      <canvas></canvas>
      <div class="status">Starting camera…</div>
      <select class="hidden" aria-label="Camera"></select>
      <div class="controls">
        <button class="ctl left" data-act="close" type="button">Cancel</button>
        <button class="shutter" data-act="shoot" type="button" aria-label="Take photo"></button>
        <button class="ctl right ${this.auto ? "on" : ""}" data-act="auto" type="button">Auto</button>
      </div>`;
    document.body.appendChild(el);
    this.el = el;
    this.video = el.querySelector("video");
    this.canvas = el.querySelector("canvas");
    this.statusEl = el.querySelector(".status");
    this.shutter = el.querySelector(".shutter");
    this.select = el.querySelector("select");
    el.addEventListener("click", (e) => {
      const act = e.target.closest("[data-act]")?.dataset.act;
      if (act === "close") this.close(true);
      if (act === "shoot") this.capture();
      if (act === "auto") {
        this.auto = !this.auto;
        e.target.classList.toggle("on", this.auto);
      }
    });
    this.select.addEventListener("change", () => {
      localStorage.setItem("gm.camera", this.select.value);
      this.start(this.select.value);
    });
    try {
      await this.start(localStorage.getItem("gm.camera"));
    } catch (e) {
      this.setStatus(`Camera not available: ${e.message || e.name}`);
      return;
    }
    this.running = true;
    this.loop();
  }

  async start(deviceId) {
    this.stream?.getTracks().forEach((t) => t.stop());
    const size = { width: { ideal: 3840 }, height: { ideal: 2160 } };
    const video = deviceId ? { deviceId: { exact: deviceId }, ...size } : { facingMode: { ideal: "environment" }, ...size };
    try {
      this.stream = await navigator.mediaDevices.getUserMedia({ audio: false, video });
    } catch (e) {
      if (!deviceId) throw e;
      localStorage.removeItem("gm.camera");
      this.stream = await navigator.mediaDevices.getUserMedia({ audio: false, video: { facingMode: { ideal: "environment" }, ...size } });
    }
    this.track = this.stream.getVideoTracks()[0];
    this.video.srcObject = this.stream;
    await this.video.play().catch(() => {});
    const devices = (await navigator.mediaDevices.enumerateDevices()).filter((d) => d.kind === "videoinput");
    if (devices.length > 1) {
      const cur = this.track.getSettings().deviceId;
      this.select.innerHTML = devices.map((d, i) =>
        `<option value="${d.deviceId}" ${d.deviceId === cur ? "selected" : ""}>${d.label || "Camera " + (i + 1)}</option>`).join("");
      this.select.classList.remove("hidden");
    }
  }

  async frame(maxW, quality) {
    const vw = this.video.videoWidth, vh = this.video.videoHeight;
    const k = Math.min(1, maxW / vw);
    const c = document.createElement("canvas");
    c.width = Math.round(vw * k);
    c.height = Math.round(vh * k);
    c.getContext("2d").drawImage(this.video, 0, 0, c.width, c.height);
    const blob = await new Promise((r) => c.toBlob(r, "image/jpeg", quality));
    return { blob, w: c.width, h: c.height };
  }

  async loop() {
    while (this.running) {
      if (this.video.readyState >= 2 && this.video.videoWidth) {
        try {
          const { blob, w, h } = await this.frame(1280, 0.6);
          if (!this.running) break;
          const res = await api("/api/preview", { method: "POST", body: blob, headers: { "Content-Type": "image/jpeg" } });
          if (!this.running) break;
          this.draw(res, w, h);
          this.update(res, w, h);
        } catch (e) {
          this.setStatus("Cannot reach the server – check the Wi-Fi");
          await sleep(800);
        }
      }
      await sleep(150);
    }
  }

  setStatus(text, ready = false) {
    this.statusEl.textContent = text;
    this.statusEl.classList.toggle("ready", ready);
  }

  draw(res, w, h) {
    const c = this.canvas, dpr = window.devicePixelRatio || 1;
    const cw = c.clientWidth, ch = c.clientHeight;
    c.width = cw * dpr;
    c.height = ch * dpr;
    const ctx = c.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const s = Math.min(cw / w, ch / h), ox = (cw - w * s) / 2, oy = (ch - h * s) / 2;
    const P = ([x, y]) => [ox + x * s, oy + y * s];
    const poly = (pts, stroke, fill) => {
      if (!pts.length) return;
      ctx.beginPath();
      pts.forEach((p, i) => { const [x, y] = P(p); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); });
      ctx.closePath();
      if (fill) { ctx.fillStyle = fill; ctx.fill(); }
      ctx.lineWidth = 3;
      ctx.strokeStyle = stroke;
      ctx.stroke();
    };
    for (const q of res.markers || []) poly(q, "#38d6ff", "rgba(56,214,255,.25)");
    const ready = res.status === "READY";
    poly(res.outline || [], ready ? "#4fcb83" : "#ffb547", ready ? "rgba(79,203,131,.18)" : "rgba(255,181,71,.15)");
  }

  update(res, w, h) {
    const ready = res.status === "READY";
    if (ready && res.outline?.length) {
      const xs = res.outline.map((p) => p[0]), ys = res.outline.map((p) => p[1]);
      const box = [Math.min(...xs) / w, Math.min(...ys) / h, Math.max(...xs) / w, Math.max(...ys) / h];
      const moved = this.last ? Math.max(...box.map((v, i) => Math.abs(v - this.last[i]))) : 1;
      this.stable = moved < 0.015 ? this.stable + 1 : 1;
      this.last = box;
    } else {
      this.stable = 0;
      this.last = null;
    }
    this.shutter.classList.toggle("armed", ready && this.auto);
    if (ready) {
      this.setStatus(this.auto ? (this.stable >= 3 ? "Taking photo…" : "Ready – hold still") : "Ready – tap the button", true);
      if (res.low_contrast) this.setStatus("Ready – but low contrast: a plainer background is better", true);
      if (this.auto && this.stable >= 3) this.capture();
    } else {
      this.setStatus(res.message || res.status);
    }
  }

  async capture() {
    if (this.capturing) return;
    this.capturing = true;
    this.running = false;
    this.setStatus("Taking photo…", true);
    let blob = null;
    if ("ImageCapture" in window && this.track) {
      try {
        const ic = new ImageCapture(this.track);
        let opts = {};
        try {
          const caps = await ic.getPhotoCapabilities();
          if (caps.imageWidth?.max) opts = { imageWidth: caps.imageWidth.max, imageHeight: caps.imageHeight.max };
        } catch { /* keep defaults */ }
        blob = await ic.takePhoto(opts);
      } catch { blob = null; }
    }
    if (!blob || blob.size < 1000) blob = (await this.frame(100000, 0.93)).blob;
    this.close(false);
    this.onCapture?.(blob);
  }

  close(user) {
    this.running = false;
    this.stream?.getTracks().forEach((t) => t.stop());
    this.el?.remove();
    if (user) this.onClose?.();
  }
}
