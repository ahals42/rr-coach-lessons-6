#!/usr/bin/env bash
# Start this lessons 1-6 copy locally on http://localhost:8001
# Usage: scripts/run_local.sh [--ingest]   (--ingest rebuilds this copy's Qdrant collections)
set -euo pipefail
cd "$(dirname "$0")/.."

PY="${PYTHON:-$HOME/Documents/rr-coach-venv/bin/python}"

if ! curl -s -o /dev/null http://127.0.0.1:6333; then
  docker start qdrant >/dev/null
  sleep 3
fi

if [[ "${1:-}" == "--ingest" ]]; then
  "$PY" -m rag.ingest
fi

exec "$PY" -u -m uvicorn backend.app:app --host 127.0.0.1 --port 8001
