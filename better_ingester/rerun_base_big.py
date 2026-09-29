#!/usr/bin/env python3
"""Rerun the four selected BASE-big prompts as individual OpenRouter requests."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bench.offline import clean_llm_json

ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "out1a" / "llm" / "base_big"
OUTPUT_DIR = ROOT / "base_big_answers"
MODEL = "deepseek/deepseek-v4-pro-0813"
DOCUMENTS = (
    "arxiv_2608.17511v1",
    "arxiv_2607.20250v1",
    "arxiv_2607.21657v1",
    "arxiv_2607.23728v1",
)
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_TOKENS = 10000


def api_key() -> str:
    value = os.environ.get("OPENAI_API_KEY")
    if not value:
        raise RuntimeError(
            "OPENAI_API_KEY is not set; source .env before running this script"
        )
    return value


def request(prompt: str, key: str, timeout: float) -> dict:
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": MAX_TOKENS,
        "response_format": {"type": "json_object"},
        "reasoning": {"exclude": True},
    }
    req = Request(
        CHAT_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/effeemmeelle/BetterIngester",
            "X-Title": "BetterIngester BASE-big evaluation",
        },
        method="POST",
    )
    with urlopen(req, timeout=timeout) as response:
        result = json.loads(response.read().decode("utf-8"))
    if result.get("error") is not None:
        raise RuntimeError(f"model request failed: {result['error']}")
    try:
        content = result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("response did not contain message content") from exc
    if not isinstance(content, str):
        raise RuntimeError("response contained non-text message content")
    try:
        return json.loads(clean_llm_json(content))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"model response was not valid JSON: {exc}") from exc


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=float, default=600.0)
    args = parser.parse_args()
    try:
        key = api_key()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    failed = 0
    for document in DOCUMENTS:
        prompt_path = INPUT_DIR / f"{document}.prompt.md"
        output_path = OUTPUT_DIR / f"{document}.answer.md"
        try:
            prompt = prompt_path.read_text(encoding="utf-8")
            answer = request(prompt, key, args.timeout)
            output_path.write_text(
                json.dumps(answer, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            print(f"ok   {document}", flush=True)
        except (
            HTTPError,
            URLError,
            TimeoutError,
            OSError,
            RuntimeError,
            TypeError,
        ) as exc:
            print(f"FAIL {document}: {exc}", file=sys.stderr)
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
