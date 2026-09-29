"""
bench/offline.py — the model-assisted conditions, run by hand.

BASE-small, BASE-big and REFINE each need one model call per document. They
are run OFFLINE rather than through an API: the harness writes a prompt file
per document, a person pastes it into a chat model, and the reply is saved
next to the prompt. The harness then scores the saved replies.

That is not a workaround, it is a better instrument for this comparison:

  · The record IS the artifact. Every prompt and every reply sits in the
    repository as a readable file, so a reader can check what the baseline
    was actually asked and what it actually said, instead of trusting a
    cache keyed by a hash.
  · Re-scoring is free and offline. Changing a metric re-reads the same
    replies; no quota, no key, no rate limiter, no nondeterminism.
  · It removes the model tier as a hidden variable. Which model produced a
    reply is recorded explicitly in models.json rather than inferred from
    whatever .env happened to say at the time.

Layout under out1a/llm/:

    <cond>/<doc>.prompt.md   written by `run_1a.py prompts`
    <cond>/<doc>.reply.txt   pasted back by hand
    models.json              {"base_small": "...", ...} — which model, per
                             condition, and the settings it was run at

A missing reply parks its unit. Tier-major scheduling means every free
condition is already complete and reportable while these stay pending, which
is exactly the state the results table is designed to show.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
LLM_DIR = _ROOT / "out1a" / "llm"
MODELS_PATH = LLM_DIR / "models.json"


# ── reply parsing ──────────────────────────────────────────────────────────

def clean_llm_json(raw: str) -> str:
    """Best-effort JSON text from a chat reply.

    Drops reasoning blocks and markdown code fences, then returns the last
    OUTERMOST balanced {...} or [...] region — models put the answer last.
    "Outermost" is load-bearing: for '{"headings": [...]}' the whole dict is
    the answer, not the array nested inside it. An earlier version returned
    the nested array and silently broke every dict-with-array-value reply.
    """
    raw = re.sub(r"<thought>.*?(</thought>|$)", "", raw, flags=re.S)
    raw = re.sub(r"<thinking>.*?(</thinking>|$)", "", raw, flags=re.S)
    raw = re.sub(r"```(?:json)?", "", raw)
    spans = []
    for open_c, close_c in (("{", "}"), ("[", "]")):
        depth = 0
        start = None
        for i, ch in enumerate(raw):
            if ch == open_c:
                if depth == 0:
                    start = i
                depth += 1
            elif ch == close_c and depth:
                depth -= 1
                if depth == 0 and start is not None:
                    spans.append((start, i + 1))
    if not spans:
        return raw.strip()
    outer = [s for s in spans
             if not any(o[0] < s[0] and s[1] <= o[1] for o in spans if o != s)]
    start, end = max(outer, key=lambda s: (s[1], -s[0]))
    return raw[start:end]


# ── the prompt/reply store ─────────────────────────────────────────────────

def prompt_path(cond: str, doc: str) -> Path:
    return LLM_DIR / cond / f"{doc}.prompt.md"


def reply_path(cond: str, doc: str) -> Path:
    return LLM_DIR / cond / f"{doc}.reply.txt"


def write_prompt(cond: str, doc: str, prompt: str) -> Path:
    p = prompt_path(cond, doc)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(prompt, encoding="utf-8")
    return p


def read_reply(cond: str, doc: str) -> str | None:
    """The saved reply, or None if nobody has run this one yet."""
    p = reply_path(cond, doc)
    if not p.exists():
        return None
    text = p.read_text(encoding="utf-8").strip()
    return text or None


def models() -> dict[str, str]:
    """Which model answered each condition. Reported next to the results, so
    a table row can never be read without knowing what produced it."""
    if MODELS_PATH.exists():
        try:
            return json.loads(MODELS_PATH.read_text())
        except Exception:
            return {}
    return {}


def record_model(cond: str, model: str) -> None:
    LLM_DIR.mkdir(parents=True, exist_ok=True)
    current = models()
    current[cond] = model
    MODELS_PATH.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")


def status(conds: list[str], docs: list[str]) -> dict[str, dict]:
    """Per condition: how many prompts are written and how many answered."""
    out: dict[str, dict] = {}
    for c in conds:
        written = sum(1 for d in docs if prompt_path(c, d).exists())
        answered = sum(1 for d in docs if read_reply(c, d) is not None)
        out[c] = {"prompts": written, "replies": answered, "documents": len(docs),
                  "model": models().get(c)}
    return out


class ReplyMissing(RuntimeError):
    """No saved reply for this (document, condition) yet."""
