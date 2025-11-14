#!/bin/bash
cd /tmp/kavia/workspace/code-generation/secure-notes-117-126/notes_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

