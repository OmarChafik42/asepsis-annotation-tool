#!/usr/bin/env python3
"""Submit and retrieve BASE-big answers through OpenRouter's Batch API."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bench.offline import clean_llm_json

ROOT = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "out1a" / "llm" / "base_big"
DEFAULT_OUTPUT = ROOT / "base_big_answers"
BATCH_URL = "https://openrouter.ai/api/beta/batches"
DEFAULT_MODEL = "deepseek/deepseek-v4-pro-0813:batch"
MAX_TOKENS = 2048


def load_api_key() -> str:
    """Read only OPENAI_API_KEY at runtime; never print or persist its value."""
    value = os.environ.get("OPENAI_API_KEY")
    if value:
        return value
    env_path = ROOT / ".env"
    if not env_path.exists():
        raise RuntimeError("OPENAI_API_KEY is not set and .env was not found")
    for line in env_path.read_text(encoding="utf-8").splitlines():
        assignment = line.strip()
        for prefix in ("export ", "source "):
            if assignment.startswith(prefix):
                assignment = assignment[len(prefix):].lstrip()
        if assignment.startswith("OPENAI_API_KEY="):
            value = assignment.split("=", 1)[1].strip().strip('"').strip("'")
            if value:
                return value
    raise RuntimeError("OPENAI_API_KEY was not found in .env")


def api_request(url: str, api_key: str, method: str, payload: object | None,
                timeout: float) -> dict:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(url, data=data, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/effeemmeelle/BetterIngester",
        "X-Title": "BetterIngester BASE-big evaluation",
    }, method=method)
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def answer_path(output_dir: Path, prompt_path: Path) -> Path:
    name = prompt_path.name.removesuffix(".prompt.md")
    return output_dir / f"{name}.answer.md"


def extract_answer(result: dict) -> object:
    if result.get("error") is not None:
        raise RuntimeError(f"model request failed: {result['error']}")
    try:
        content = result["response"]["body"]["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("batch result did not contain message content") from exc
    if not isinstance(content, str):
        raise RuntimeError("batch result contained non-text message content")
    try:
        return json.loads(clean_llm_json(content))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"model response was not valid JSON: {exc}") from exc


def submit(args, api_key: str, prompts: list[Path]) -> int:
    requests = [{
        "custom_id": prompt.name,
        "body": {
            "messages": [{"role": "user",
                          "content": prompt.read_text(encoding="utf-8")}],
            "temperature": 0,
            "max_tokens": MAX_TOKENS,
            "response_format": {"type": "json_object"},
            "reasoning": {"exclude": True},
        },
    } for prompt in prompts]
    body = {"endpoint": "/v1/chat/completions", "model": args.model,
            "requests": requests}
    try:
        batch = api_request(BATCH_URL, api_key, "POST", body, args.timeout)
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        print(f"ERROR submitting batch: {exc}", file=sys.stderr)
        return 1
    metadata = args.output / "batch.json"
    metadata.write_text(json.dumps(batch, indent=2) + "\n", encoding="utf-8")
    print(f"Submitted {len(prompts)} prompt(s).")
    print(f"Batch ID: {batch.get('id', 'unknown')}")
    print(f"Status: {batch.get('status', 'unknown')}")
    print(f"Metadata: {metadata}")
    return 0


def retrieve(args, api_key: str, prompts: list[Path]) -> int:
    if args.batch_id:
        batch_id = args.batch_id
    else:
        try:
            batch_id = json.loads(
                (args.output / "batch.json").read_text(encoding="utf-8"))["id"]
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            print("ERROR: provide --batch-id or run submit first",
                  file=sys.stderr)
            return 2
    try:
        batch = api_request(f"{BATCH_URL}/{batch_id}", api_key, "GET",
                            None, args.timeout)
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        print(f"ERROR retrieving batch: {exc}", file=sys.stderr)
        return 1
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "batch.json").write_text(
        json.dumps(batch, indent=2) + "\n", encoding="utf-8")
    status = batch.get("status")
    print(f"Batch {batch_id}: {status}")
    if status != "completed":
        counts = batch.get("request_counts", {})
        print(f"Completed {counts.get('completed', 0)} of "
              f"{counts.get('total', len(prompts))}; retrieve again later.")
        return 0 if status in {"validating", "in_progress", "finalizing"} else 1
    prompt_names = {p.name: p for p in prompts}
    failed = 0
    for result in batch.get("results", []):
        prompt = prompt_names.get(result.get("custom_id"))
        if prompt is None:
            print(f"FAIL unknown custom_id: {result.get('custom_id')}",
                  file=sys.stderr)
            failed += 1
            continue
        try:
            answer_path(args.output, prompt).write_text(
                json.dumps(extract_answer(result), ensure_ascii=False, indent=2)
                + "\n", encoding="utf-8")
            print(f"ok   {prompt.name}", flush=True)
        except (RuntimeError, OSError, TypeError) as exc:
            print(f"FAIL {prompt.name}: {exc}", file=sys.stderr)
            failed += 1
    print(f"Retrieved {len(batch.get('results', [])) - failed}, failed {failed}.")
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("submit", "retrieve"),
                        nargs="?", default="submit")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--batch-id")
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--redo", action="store_true")
    args = parser.parse_args()
    try:
        api_key = load_api_key()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    prompts = sorted(args.input.glob("*.prompt.md"))
    if not prompts:
        print(f"ERROR: no prompt files found in {args.input}", file=sys.stderr)
        return 2
    args.output.mkdir(parents=True, exist_ok=True)
    if args.action == "submit":
        prompts = [p for p in prompts
                   if args.redo or not answer_path(args.output, p).exists()]
        return submit(args, api_key, prompts) if prompts else 0
    return retrieve(args, api_key, prompts)


if __name__ == "__main__":
    raise SystemExit(main())
