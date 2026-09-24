#!/usr/bin/env bash
# The CI check, step for step; stops at the first failure. A rebuild must leave the
# generated pages unchanged (on a clean checkout this equals `git diff --exit-code`).
# --freshness also runs the advisory scripts/freshness.py, which never fails the check.
set -euo pipefail
cd "$(dirname "$0")/.."
generated=(reports decisions/README.md docs/client-fixes.md)
snapshot() { find "${generated[@]}" -type f -exec shasum -a 256 {} + | sort; }

uv sync --locked
uv run --locked trace-interop verify
uv run --locked python -m unittest discover -s tests -v
uv run --locked python scripts/check_schema.py
before=$(snapshot)
uv run --locked python scripts/build_reports.py
if [ "$(snapshot)" != "$before" ]; then
  echo 'Generated reports are stale: commit the output of scripts/build_reports.py.' >&2
  diff <(echo "$before") <(snapshot) >&2 || true
  exit 1
fi
if [ "${1:-}" = --freshness ]; then
  uv run --locked python scripts/freshness.py || echo 'Freshness warnings are advisory.' >&2
fi
