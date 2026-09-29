"""
bench/transport.py — the governed LLM transport.

NOT used by the intrinsic evaluation. The scored conditions are either
deterministic (tier 0) or run offline by hand (tier 1, bench/offline.py), so
nothing in the report card depends on this file or on an API key.

It exists for the two paths that genuinely need a live model and are not
scored: the PageIndex seam (ingest/pageindex_vendor.py, deferred) and
BetterIngest.describe_assets. Both are optional.

What it provides: temperature 0, a cache keyed by (kind, model, payload) so a
re-run is free, pacing on a rolling token budget rather than a request count,
a per-bucket circuit breaker so one dead serving stack cannot stall the rest,
and a persisted daily budget so a run stops before the wall instead of
discovering it mid-document.
"""

from __future__ import annotations

import json
import os
import re
import threading
import time
from pathlib import Path

from bench import cache_db

_ROOT = Path(__file__).resolve().parents[1]

# Free-tier limits READ FROM THE AI STUDIO DASHBOARD (not documented publicly;
# they are per-project and can change, so they are recorded in the frozen
# manifest as a run parameter).  Measured 2026-08-25 for gemma-4-31b-it:
#   RPM 30 · TPM 16,000 · RPD 14,400
#
# TPM is the binding constraint by a wide margin, and pacing on REQUESTS gets
# it wrong: 4.2 s between 4k-token calls is ~57k tokens/min, 3.5x over the
# ceiling.  Sustained overshoot is what the July 500-storms actually were.
# So the governor paces on a rolling 60-second TOKEN budget, with RPM as a
# secondary floor.
RPM: dict[str, float] = {"small": 30, "big": 30}
TPM: dict[str, float] = {"small": 16_000, "big": 16_000}
RPD: dict[str, float] = {"small": 14_400, "big": 14_400}
DEFAULT_RPM, DEFAULT_TPM = 30.0, 16_000.0
TPM_HEADROOM = 0.85            # aim under the ceiling; estimates are approximate
CHARS_PER_TOKEN = 4.0          # standard rough estimate for budgeting only

MAX_ATTEMPTS = 5
BREAKER_THRESHOLD = 6          # consecutive transient failures before parking
BREAKER_COOLDOWN = 900.0       # seconds a parked bucket stays parked

_lock = threading.Lock()
_last_call: dict[str, float] = {}
_breaker: dict[str, dict] = {}
_token_log: dict[str, list[tuple[float, float]]] = {}   # bucket -> [(t, tokens)]


def est_tokens(text: str) -> float:
    return len(text) / CHARS_PER_TOKEN


class DailyQuotaExhausted(RuntimeError):
    """Per-day request cap hit — the run is resumable from cache tomorrow."""


class BucketParked(RuntimeError):
    """This model bucket is in circuit-breaker cooldown; try other work."""


def load_env(path: Path = _ROOT / ".env") -> dict[str, str]:
    env: dict[str, str] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("BIG_LLM_API_KEY", "BIG_LLM_BASE_URL", "BIG_LLM_MODEL",
              "SMALL_LLM_MODEL"):
        env.setdefault(k, os.environ.get(k, ""))
    return env


# ── circuit breaker ────────────────────────────────────────────────────────

def _breaker_state(bucket: str) -> dict:
    return _breaker.setdefault(bucket, {"fails": 0, "open_until": 0.0})


def check_bucket(bucket: str) -> None:
    st = _breaker_state(bucket)
    if st["open_until"] > time.time():
        left = st["open_until"] - time.time()
        raise BucketParked(f"[{bucket}] parked for another {left:.0f}s "
                           f"after {st['fails']} consecutive failures")


def _record_failure(bucket: str) -> None:
    st = _breaker_state(bucket)
    st["fails"] += 1
    if st["fails"] >= BREAKER_THRESHOLD:
        st["open_until"] = time.time() + BREAKER_COOLDOWN
        print(f"    [{bucket}] circuit breaker OPEN — parking "
              f"{BREAKER_COOLDOWN / 60:.0f} min", flush=True)


def _record_success(bucket: str) -> None:
    _breaker_state(bucket).update(fails=0, open_until=0.0)


# ── rate limiting: acquire, compute, RELEASE, then sleep ───────────────────

def _pace(bucket: str, tokens: float = 0.0) -> None:
    """Block until this call fits both the token/minute and request/minute
    budgets.  The wait is COMPUTED under the lock and SLEPT outside it, so a
    slow or failing call never freezes other buckets."""
    deadline = 0.0
    with _lock:
        now = time.time()
        log = _token_log.setdefault(bucket, [])
        log[:] = [(t, n) for t, n in log if now - t < 60.0]

        cap = TPM.get(bucket, DEFAULT_TPM) * TPM_HEADROOM
        used = sum(n for _, n in log)
        if used + tokens > cap and log:
            # wait until enough of the oldest tokens age out of the window
            need = used + tokens - cap
            freed = 0.0
            for t, n in log:
                freed += n
                if freed >= need:
                    deadline = max(deadline, t + 60.0)
                    break
            else:
                deadline = max(deadline, log[-1][0] + 60.0)

        rpm_gap = 60.0 / max(RPM.get(bucket, DEFAULT_RPM), 1.0)
        deadline = max(deadline, _last_call.get(bucket, 0.0) + rpm_gap)

        start = max(deadline, now)
        _last_call[bucket] = start
        log.append((start, tokens))          # reserve before releasing

    wait = start - time.time()
    if wait > 0:
        if wait > 5:
            print(f"    [{bucket}] token budget — waiting {wait:.0f}s "
                  f"({tokens:.0f} tok)", flush=True)
        time.sleep(wait)


def _classify(msg: str) -> str:
    if re.search(r"per.?day|daily|PerDay", msg, re.I):
        return "quota_day"
    if "429" in msg or "RESOURCE_EXHAUSTED" in msg or "quota" in msg.lower():
        return "rate"
    if any(c in msg.lower() for c in
           ("500", "502", "503", "internal", "unavailable",
            "timed out", "timeout", "connection")):
        return "transient"
    return "fatal"


def _retry_delay(kind: str, attempt: int, msg: str) -> float:
    if kind == "rate":
        m = re.search(r"retry.{0,20}?(\d+(?:\.\d+)?)\s*s", msg, re.I)
        return float(m.group(1)) + 2.0 if m else 20.0 * (attempt + 1)
    return 10.0 * (attempt + 1)


def _client(timeout: float):
    env = load_env()
    if not env.get("BIG_LLM_API_KEY"):
        return None
    from openai import OpenAI
    return OpenAI(api_key=env["BIG_LLM_API_KEY"],
                  base_url=env.get("BIG_LLM_BASE_URL") or None,
                  max_retries=0, timeout=timeout)


def _call(kind: str, model: str, bucket: str, payload_key: str,
          make_request, decode, timeout: float, tokens: float = 0.0):
    """Shared cache/pace/retry/breaker loop for both call shapes."""
    if not model:
        return None
    kh = cache_db.key_hash(kind, model, payload_key)
    hit = cache_db.get(kh)
    if hit is not None:
        return decode(hit)

    check_bucket(bucket)
    try:
        client = _client(timeout)
    except Exception as e:
        print(f"    [{kind}/{bucket}] sdk unavailable: {e}", flush=True)
        return None
    if client is None:
        print(f"    [{kind}/{bucket}] no API key — skipping", flush=True)
        return None

    for attempt in range(MAX_ATTEMPTS):
        _pace(bucket, tokens)
        try:
            resp = make_request(client)
            cache_db.note_call(bucket)
            payload, value = resp
            cache_db.put(kh, payload, getattr(value, "usage", None))
            _record_success(bucket)
            return decode(payload)
        except Exception as e:
            err = e
        # everything below runs with no lock held
        msg = str(err)
        kindf = _classify(msg)
        if kindf == "quota_day":
            raise DailyQuotaExhausted(f"[{kind}/{bucket}] daily quota: {msg[:160]}")
        if kindf == "fatal":
            print(f"    [{kind}/{bucket}] failed: {msg[:160]}", flush=True)
            _record_failure(bucket)
            return None
        _record_failure(bucket)
        try:
            check_bucket(bucket)
        except BucketParked:
            raise
        delay = _retry_delay(kindf, attempt, msg)
        print(f"    [{kind}/{bucket}] {kindf} ({msg[:60]}) — "
              f"retry in {delay:.0f}s", flush=True)
        time.sleep(delay)
    print(f"    [{kind}/{bucket}] gave up after {MAX_ATTEMPTS} attempts",
          flush=True)
    return None


def api_chat(model: str, messages: list[dict],
             bucket: str) -> tuple[str, str] | None:
    """Chat-message variant for the vendored PageIndex transport: returns
    (content, finish_reason).  No max_tokens cap — the vendored code expects
    model-limit replies and hard-fails on truncation.  480 s timeout: its long
    TOC prompts legitimately take a small model minutes."""
    key = json.dumps(messages, ensure_ascii=False, sort_keys=True)

    def make_request(client):
        r = client.chat.completions.create(
            model=model, temperature=0, messages=messages)
        env = {"content": r.choices[0].message.content or "",
               "finish_reason": r.choices[0].finish_reason or "stop"}
        return json.dumps(env, ensure_ascii=False), r

    def decode(payload: str) -> tuple[str, str]:
        d = json.loads(payload)
        return d["content"], d.get("finish_reason", "stop")

    return _call("chat", model, bucket, key, make_request, decode,
                 timeout=480.0, tokens=est_tokens(key))
