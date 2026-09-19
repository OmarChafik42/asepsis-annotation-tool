#!/usr/bin/env bash
set -euo pipefail

DOC="${1:-}"
if [ -n "$DOC" ]; then
  git add "data/${DOC}/auto/sessions/"
else
  git add data/*/auto/sessions/
fi

git status --short -- data
if ! git diff --cached --quiet; then
  git commit -m "annotate: update approved sessions"
fi
