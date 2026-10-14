// End-to-end: a phone-sized Chromium whose camera "sees" a synthetic sweater photo.
// Usage: node tests/e2e/phone_flow.cjs <base-url> <fake-camera.mjpeg> <screenshot-dir>
// Needs the app running (with the fake Qwen) and Playwright with Chromium installed.
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const [base, camFile, outDir] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const shot = (page, name) => page.screenshot({ path: path.join(outDir, name + ".png"), fullPage: true });
const check = (cond, msg) => { if (!cond) throw new Error("CHECK FAILED: " + msg); console.log("ok -", msg); };

(async () => {
  // Seed a style with a spec (sleeve spec deliberately 1.5 cm short so one point fails).
  const spec = [["chest", 520], ["body_length", 660], ["sleeve_length", 585], ["hem", 496], ["across_shoulder", 440],
    ["sleeve_opening", 95]].map(([key, t]) => ({ size: "M", key, target_mm: t, tol_minus_mm: 10, tol_plus_mm: 10 }));
  const r = await fetch(base + "/api/styles", { method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code: "KN-2291", name: "Crew neck sweater", customer: "Demo brand", garment_type: "sweater",
      sizes: ["S", "M", "L"], spec }) });
  check(r.ok, "style created via API");

  const browser = await chromium.launch({
    args: ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream",
      `--use-file-for-fake-video-capture=${camFile}`],
  });
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true,
    hasTouch: true, acceptDownloads: true, permissions: ["camera"] });
  const page = await ctx.newPage();
  const errors = [];
  page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
  page.on("pageerror", (e) => errors.push(String(e)));

  await page.goto(base + "/#/scan");
  await page.waitForSelector("#style");
  await page.selectOption("#style", { label: "KN-2291 · Crew neck sweater" });
  await page.selectOption("#size", "M");
  await page.fill("#label", "PO-2291 #3");
  await shot(page, "1-scan");

  await page.click("#live");
  await page.waitForSelector(".cam .status.ready", { timeout: 30000 });
  await page.screenshot({ path: path.join(outDir, "2-live-camera.png") });
  check(true, "live preview found the sheet and the garment");

  await page.waitForURL(/#\/scan\/[a-z0-9]+$/, { timeout: 60000 });
  await page.waitForSelector("table.meas tbody tr");
  check(true, "auto-capture measured the garment");
  await page.waitForFunction(() => /Qwen|Flash/.test(document.querySelector("#ai")?.textContent || ""), null, { timeout: 30000 });
  await shot(page, "3-result");

  const rows = await page.$$eval("table.meas tbody tr", (trs) => trs.map((tr) => ({
    k: tr.dataset.k, cls: tr.className, actual: tr.children[2].textContent.trim() })));
  const val = (k) => parseFloat(rows.find((x) => x.k === k).actual);
  console.log(rows.map((x) => `${x.k}=${x.actual}`).join("  "));
  check(Math.abs(val("chest") - 52.0) <= 0.6, `chest ${val("chest")} cm ≈ 52.0`);
  check(Math.abs(val("body_length") - 66.0) <= 0.6, `body length ${val("body_length")} cm ≈ 66.0`);
  check(rows.find((x) => x.k === "sleeve_length.l").cls.includes("fail"), "sleeve length flagged against the short spec");
  const banner = await page.textContent("#banner");
  check(/FAIL/.test(banner), "banner shows FAIL");

  // Drag the left cuff point 1.5 cm back toward the shoulder (on screen) and check the number follows.
  const before = val("sleeve_length.l");
  const g = await page.$('g.lm[data-n="cuff_top_l"]');
  const sp = await (await page.$('g.lm[data-n="sp_l"]')).boundingBox();
  const b = await g.boundingBox();
  const cx = b.x + b.width / 2, cy = b.y + b.height / 2;
  const vx = sp.x + sp.width / 2 - cx, vy = sp.y + sp.height / 2 - cy, n = Math.hypot(vx, vy);
  const pxPerCm = n / before;
  await page.mouse.move(cx, cy);
  await page.mouse.down();
  for (let i = 1; i <= 8; i++) await page.mouse.move(cx + vx / n * pxPerCm * 1.5 * i / 8, cy + vy / n * pxPerCm * 1.5 * i / 8);
  await shot(page, "4-dragging");
  await page.mouse.up();
  const after = parseFloat(await page.$eval('tr[data-k="sleeve_length.l"] td:nth-child(3)', (td) => td.textContent));
  check(Math.abs(before - after - 1.5) < 0.3, `drag changed sleeve L from ${before} to ${after}`);

  await page.click("#save");
  await page.waitForFunction(() => /Saved/.test(document.querySelector("#banner").textContent));
  check(true, "saved");

  await page.goto(base + "/#/history");
  await page.waitForSelector(".scan-item");
  await shot(page, "5-history");
  const [dl] = await Promise.all([page.waitForEvent("download"), page.click("#xlsx")]);
  const file = path.join(outDir, "export.xlsx");
  await dl.saveAs(file);
  check(fs.statSync(file).size > 3000, "Excel export downloaded");

  await page.goto(base + "/#/styles");
  await page.click("text=KN-2291");
  await page.waitForSelector("table.spec");
  await shot(page, "6-style-spec");

  await page.goto(base + "/#/settings");
  await page.waitForSelector("#aiInfo b");
  await shot(page, "7-settings");

  await page.goto(base + "/onboarding");
  await page.waitForSelector(".qr");
  await shot(page, "8-setup-page");

  check(errors.length === 0, "no browser console errors" + (errors.length ? ": " + errors.join(" | ") : ""));
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
