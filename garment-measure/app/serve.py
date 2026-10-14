"""Start the app: HTTPS (live camera) and plain HTTP (setup page, photo mode) on the LAN."""
from __future__ import annotations

import asyncio
import sys

import uvicorn

from . import netinfo
from .config import load
from .main import create_app


def _qr_ascii(text: str) -> str:
    try:
        import qrcode

        q = qrcode.QRCode(border=1)
        q.add_data(text)
        q.make()
        lines = []
        m = q.get_matrix()
        for y in range(0, len(m), 2):
            row = ""
            for x in range(len(m[0])):
                top, bot = m[y][x], m[y + 1][x] if y + 1 < len(m) else False
                row += "█" if top and bot else "▀" if top else "▄" if bot else " "
            lines.append(row)
        return "\n".join(lines)
    except Exception:  # noqa: BLE001
        return ""


async def main() -> None:
    st = load()
    app = create_app(st)
    https = st.cert_file.exists() and st.key_file.exists()
    servers = []
    if https:
        servers.append(uvicorn.Server(uvicorn.Config(app, host=st.host, port=st.https_port, ssl_certfile=str(st.cert_file),
                                                     ssl_keyfile=str(st.key_file), log_level="warning")))
    servers.append(uvicorn.Server(uvicorn.Config(app, host=st.host, port=st.http_port, log_level="warning",
                                                 lifespan="off" if https else "on")))

    ips = netinfo.lan_ips() or ["<this-computer-ip>"]
    first = f"https://{ips[0]}:{st.https_port}" if https else f"http://{ips[0]}:{st.http_port}"
    setup = f"http://{ips[0]}:{st.http_port}/onboarding"
    print("\n  Garment Measure is running.\n")
    for ip in ips:
        if https:
            print(f"   Phone app (live camera):  https://{ip}:{st.https_port}")
        print(f"   Setup page / photo mode:  http://{ip}:{st.http_port}/onboarding")
    if not https:
        print("\n   No HTTPS certificate yet: run scripts/make_cert.sh for the live camera mode.")
    print(f"\n   Qwen: {st.qwen_base_url} ({'on' if st.qwen_enabled else 'off'})")
    print("\n   First time on a phone? Scan this to open the setup page:\n")
    print(_qr_ascii(setup))
    print(f"\n   Then open {first}\n   Press Ctrl+C to stop.\n")

    tasks = [asyncio.create_task(s.serve()) for s in servers]
    _, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for s in servers:
        s.should_exit = True
    await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
