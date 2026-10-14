"""`./run.sh doctor`: check everything the app needs and say what to fix."""
from __future__ import annotations

import asyncio
import socket
import sys
import time

import cv2
import numpy as np

from . import netinfo
from .config import load
from .qwen import QwenClient

OK, WARN, BAD = "  OK ", " WARN", " FAIL"


def line(tag, msg):
    print(f"[{tag}] {msg}")


def port_free(host, port) -> bool:
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((host, port))
            return True
        except OSError:
            return False


async def main() -> int:
    st = load()
    bad = 0
    line(OK, f"Python {sys.version.split()[0]}, OpenCV {cv2.__version__}, NumPy {np.__version__}")
    if not hasattr(cv2.aruco, "CharucoDetector"):
        line(BAD, "OpenCV has no ChArUco detector - install opencv-python-headless>=4.10")
        bad += 1

    ips = netinfo.lan_ips()
    line(OK if ips else WARN, f"LAN address(es): {', '.join(ips) or 'none found'}")
    if st.cert_file.exists():
        san = (st.cert_dir / "server.san").read_text() if (st.cert_dir / "server.san").exists() else ""
        missing = [ip for ip in ips if f"IP:{ip}" not in san]
        line(WARN if missing else OK, "HTTPS certificate present" +
             (f" but not valid for {', '.join(missing)} - run scripts/make_cert.sh" if missing else ""))
    else:
        line(WARN, "No HTTPS certificate: live camera unavailable until you run scripts/make_cert.sh")
    for port in (st.https_port, st.http_port):
        line(OK if port_free(st.host, port) else WARN,
             f"Port {port} {'is free' if port_free(st.host, port) else 'is in use (app already running?)'}")

    if not st.qwen_enabled:
        line(WARN, "Qwen disabled (QWEN_ENABLED=false) - measuring works, AI checks are off")
        return bad
    q = QwenClient(st.qwen_base_url, st.qwen_api_key, st.qwen_model, st.qwen_timeout)
    s = await q.status()
    if not s["reachable"]:
        line(BAD, f"Cannot reach vLLM at {st.qwen_base_url}: {s['error']}")
        line(WARN, "Check that vLLM is running and QWEN_BASE_URL in .env points to it (…/v1)")
        await q.close()
        return bad + 1
    line(OK if s["ok"] else BAD, f"vLLM at {st.qwen_base_url} serves: {', '.join(s['models'])}; using '{s['model']}'"
         + (f" - {s['error']}" if s["error"] else ""))
    img = np.full((256, 384, 3), 200, np.uint8)
    cv2.rectangle(img, (90, 40), (290, 230), (60, 60, 170), -1)
    jpeg = cv2.imencode(".jpg", img)[1].tobytes()
    t = time.time()
    try:
        r = await q.photo_check(jpeg, "Sweater")
        line(OK, f"Image request answered in {time.time() - t:.1f}s (structured output: "
                 f"{'yes' if q.supports_schema else 'no, using text fallback'}): {r.get('notes', '')[:80]}")
    except Exception as e:  # noqa: BLE001
        line(BAD, f"Image request failed: {e}")
        line(WARN, "Is the served model multimodal and was vLLM started with image input allowed?")
        bad += 1
    await q.close()
    return bad


if __name__ == "__main__":
    sys.exit(1 if asyncio.run(main()) else 0)
