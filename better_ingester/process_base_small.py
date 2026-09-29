#!/usr/bin/env python3
"""Submit and retrieve BASE-small answers through OpenRouter's Batch API."""

from __future__ import annotations

import process_base_big as batch_runner


batch_runner.DEFAULT_INPUT = batch_runner.ROOT / "out1a" / "llm" / "base_small"
batch_runner.DEFAULT_OUTPUT = batch_runner.ROOT / "base_small_answers"
batch_runner.DEFAULT_MODEL = "google/gemma-4-31b-it"


if __name__ == "__main__":
    raise SystemExit(batch_runner.main())
