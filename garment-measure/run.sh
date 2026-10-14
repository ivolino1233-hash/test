#!/usr/bin/env bash
# Start Garment Measure on this computer (the DGX). First run installs everything it needs.
#   ./run.sh            start the app
#   ./run.sh test       run the test suite
#   ./run.sh doctor     check OpenCV, certificate, network and the connection to Qwen
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
if [[ ! -x .venv/bin/python ]]; then
  echo "Creating Python environment (.venv)…"
  "$PY" -m venv .venv
fi
REQ_HASH="$(sha256sum requirements.txt requirements-dev.txt | sha256sum | cut -c1-16)"
if [[ ! -f .venv/.req-$REQ_HASH ]]; then
  echo "Installing Python packages…"
  .venv/bin/pip install -q --upgrade pip
  .venv/bin/pip install -q -r requirements-dev.txt
  rm -f .venv/.req-* && touch ".venv/.req-$REQ_HASH"
fi

[[ -f .env ]] || cp .env.example .env

# (Re)issue the HTTPS certificate when missing or when this machine's IP changed.
need_cert=0
if [[ ! -f certs/server.crt ]]; then
  need_cert=1
else
  for ip in $(hostname -I 2>/dev/null || true); do
    [[ "$ip" == *:* ]] && continue
    grep -q "IP:${ip}\b" certs/server.san 2>/dev/null || need_cert=1
  done
fi
if [[ $need_cert == 1 ]]; then
  if command -v openssl >/dev/null; then
    bash scripts/make_cert.sh
  else
    echo "openssl not found: running without HTTPS (photo mode only)."
  fi
fi

case "${1:-start}" in
  test)   exec .venv/bin/python -m pytest -q tests ;;
  doctor) exec .venv/bin/python -m app.doctor ;;
  *)      exec .venv/bin/python -m app.serve ;;
esac
