#!/usr/bin/env bash
# Create a small local certificate authority (once) and a server certificate for this
# computer's LAN addresses, so phones can open the app over HTTPS (needed for the live camera).
#
# Phones install certs/ca.crt once (see the setup page). When the computer's IP changes, run this
# again: only the server certificate is re-issued, phones keep trusting the same CA.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p certs
cd certs

if [[ ! -f ca.key || ! -f ca.crt ]]; then
  echo "Creating local certificate authority (certs/ca.crt)…"
  openssl req -x509 -newkey rsa:2048 -nodes -sha256 -days 3650 \
    -keyout ca.key -out ca.crt -subj "/CN=Garment Measure Local CA/O=Garment Measure" \
    -addext "basicConstraints=critical,CA:TRUE,pathlen:0" \
    -addext "keyUsage=critical,keyCertSign,cRLSign" \
    -addext "subjectKeyIdentifier=hash" 2>/dev/null
  chmod 600 ca.key
fi

HOST="$(hostname)"
IPS="$(hostname -I 2>/dev/null || true)"
if [[ -z "${IPS// }" ]]; then
  IPS="$(ip -4 -o addr show scope global 2>/dev/null | awk '{print $4}' | cut -d/ -f1 | tr '\n' ' ')"
fi
SAN="DNS:localhost,DNS:${HOST},DNS:${HOST}.local,IP:127.0.0.1"
for ip in $IPS; do
  [[ "$ip" == *:* ]] && continue      # skip IPv6
  SAN="${SAN},IP:${ip}"
done
for extra in ${EXTRA_SAN:-}; do       # e.g. EXTRA_SAN="IP:10.0.0.9 DNS:measure.lan"
  SAN="${SAN},${extra}"
done

echo "Issuing server certificate for: ${SAN}"
openssl req -newkey rsa:2048 -nodes -sha256 -keyout server.key -out server.csr -subj "/CN=${HOST}" 2>/dev/null
cat > server.ext <<EOF
basicConstraints=CA:FALSE
keyUsage=critical,digitalSignature,keyEncipherment
extendedKeyUsage=serverAuth
subjectAltName=${SAN}
EOF
# 825 days is the longest validity iPhones accept for a server certificate.
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 825 \
  -sha256 -extfile server.ext 2>/dev/null
rm -f server.csr server.ext
chmod 600 server.key
echo "$SAN" > server.san
echo "Done: certs/server.crt (phones trust it after installing certs/ca.crt)"
