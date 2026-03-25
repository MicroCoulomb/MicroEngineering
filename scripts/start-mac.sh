#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

docker build -t microprelegal "${REPO_ROOT}"
docker rm -f microprelegal >/dev/null 2>&1 || true
docker run -d --name microprelegal -p 8000:8000 microprelegal
