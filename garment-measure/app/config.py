"""Settings from environment variables, optionally loaded from a .env file next to run.sh."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _bool(v: str) -> bool:
    return v.strip().lower() in ("1", "true", "yes", "on")


@dataclass
class Settings:
    data_dir: Path
    host: str = "0.0.0.0"
    https_port: int = 8443
    http_port: int = 8080
    cert_dir: Path = ROOT / "certs"
    qwen_base_url: str = "http://127.0.0.1:8000/v1"
    qwen_api_key: str = ""
    qwen_model: str = ""
    qwen_timeout: float = 90.0
    qwen_enabled: bool = True
    app_pin: str = ""
    px_per_mm: float = 2.0
    draft_days: int = 2

    @property
    def cert_file(self) -> Path:
        return self.cert_dir / "server.crt"

    @property
    def key_file(self) -> Path:
        return self.cert_dir / "server.key"

    @property
    def ca_file(self) -> Path:
        return self.cert_dir / "ca.crt"


def load(env_file: Path | None = None) -> Settings:
    _load_env_file(env_file or ROOT / ".env")
    e = os.environ.get
    return Settings(
        data_dir=Path(e("DATA_DIR", str(ROOT / "data"))),
        host=e("HOST", "0.0.0.0"),
        https_port=int(e("HTTPS_PORT", "8443")),
        http_port=int(e("HTTP_PORT", "8080")),
        cert_dir=Path(e("CERT_DIR", str(ROOT / "certs"))),
        qwen_base_url=e("QWEN_BASE_URL", "http://127.0.0.1:8000/v1").rstrip("/"),
        qwen_api_key=e("QWEN_API_KEY", ""),
        qwen_model=e("QWEN_MODEL", ""),
        qwen_timeout=float(e("QWEN_TIMEOUT", "90")),
        qwen_enabled=_bool(e("QWEN_ENABLED", "true")),
        app_pin=e("APP_PIN", ""),
        px_per_mm=float(e("RECT_PX_PER_MM", "2.0")),
        draft_days=int(e("DRAFT_DAYS", "2")),
    )
