#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
ENV_FILE="$ROOT/deploy/compose/.env"

if [ ! -f "$ENV_FILE" ]; then
    echo "Қате: .env файлы табылмады"
    exit 1
fi

set -a
source "$ENV_FILE"
set +a

if [ -z "${DITTO_PASSWORD:-}" ]; then
    echo "Қате: DITTO_PASSWORD орнатылмаған"
    exit 1
fi

cd "$ROOT/team/kachar-mine/web"

echo "Kachar Mine Dashboard: http://localhost:8766/"
python3 -u server.py
