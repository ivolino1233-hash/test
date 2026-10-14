"""LAN addresses of this machine, for the phone URL, the QR code and the HTTPS certificate."""
from __future__ import annotations

import socket


def lan_ips() -> list[str]:
    ips = []
    try:  # the address used for outbound traffic (no packet is sent for UDP connect)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1))
        ips.append(s.getsockname()[0])
        s.close()
    except OSError:
        pass
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            ips.append(info[4][0])
    except OSError:
        pass
    seen = []
    for ip in ips:
        if ip not in seen and not ip.startswith("127."):
            seen.append(ip)
    return seen


def hostname() -> str:
    return socket.gethostname()
