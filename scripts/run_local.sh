#!/usr/bin/env bash
# Start this lessons 1-6 copy locally on http://localhost:8001
# Usage: scripts/run_local.sh [--ingest]   (--ingest rebuilds this copy's Qdrant collections)
set -euo pipefail
cd "$(dirname "$0")/.."

VENV=".venv"
if [[ ! -x "$VENV/bin/python" ]]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q -r requirements.txt
fi
PY="$VENV/bin/python"

if ! curl -s -o /dev/null http://127.0.0.1:6333; then
  if docker ps -a --format '{{.Names}}' | grep -qx qdrant; then
    docker start qdrant >/dev/null
  else
    docker run -d --name qdrant -p 127.0.0.1:6333:6333 -v qdrant_storage:/qdrant/storage qdrant/qdrant:v1.16.3 >/dev/null
  fi
  sleep 3
fi

if [[ "${1:-}" == "--ingest" ]]; then
  "$PY" -m rag.ingest
fi

exec "$PY" -u -m uvicorn backend.app:app --host 127.0.0.1 --port 8001
