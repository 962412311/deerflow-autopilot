#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-dev}"

if [[ -n "${DEER_FLOW_FRONTEND_TIMEOUT:-}" ]]; then
    printf '%s\n' "$DEER_FLOW_FRONTEND_TIMEOUT"
    exit 0
fi

case "$MODE" in
    dev)
        printf '%s\n' "${DEER_FLOW_FRONTEND_TIMEOUT_DEV:-120}"
        ;;
    prod)
        printf '%s\n' "${DEER_FLOW_FRONTEND_TIMEOUT_PROD:-600}"
        ;;
    *)
        echo "Unknown frontend startup mode: $MODE" >&2
        echo "Usage: $0 [dev|prod]" >&2
        exit 1
        ;;
esac
