"""
bench/cache_db.py — the LLM call cache, as one SQLite file.

Every call is keyed by a hash of (kind, model, payload) at temperature 0, so
a re-run costs nothing. One SQLite file rather than thousands of loose ones,
which is what makes committing the cache as a checkpoint survive a
60-document corpus.

Used only by bench/transport.py, and therefore only by the unscored paths —
see that module's header.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = _ROOT / "out1a" / "cache.db"

_local = threading.local()


def key_hash(kind: str, model: str, payload: str) -> str:
    """kind is 'api' (single prompt) or 'chat' (message list), matching the
    legacy prefixes exactly so migrated entries are found by new lookups."""
    return hashlib.sha256(f"{kind}\0{model}\0{payload}".encode()).hexdigest()


def _conn() -> sqlite3.Connection:
    c = getattr(_local, "conn", None)
    if c is None:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        c = sqlite3.connect(DB_PATH, timeout=60.0)
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("""CREATE TABLE IF NOT EXISTS calls (
                        key_hash   TEXT PRIMARY KEY,
                        payload    TEXT NOT NULL,
                        usage_json TEXT,
                        created_at REAL NOT NULL)""")
        c.execute("""CREATE TABLE IF NOT EXISTS budget (
                        bucket TEXT NOT NULL,
                        day    TEXT NOT NULL,
                        calls  INTEGER NOT NULL DEFAULT 0,
                        PRIMARY KEY (bucket, day))""")
        c.commit()
        _local.conn = c
    return c


def get(kh: str) -> str | None:
    row = _conn().execute("SELECT payload FROM calls WHERE key_hash=?",
                          (kh,)).fetchone()
    return row[0] if row else None


def put(kh: str, payload: str, usage=None) -> None:
    uj = None
    if usage is not None:
        uj = json.dumps({"prompt": getattr(usage, "prompt_tokens", None),
                         "completion": getattr(usage, "completion_tokens", None),
                         "total": getattr(usage, "total_tokens", None)})
    c = _conn()
    c.execute("INSERT OR REPLACE INTO calls VALUES (?,?,?,?)",
              (kh, payload, uj, time.time()))
    c.commit()


# ── daily budget accounting ────────────────────────────────────────────────

def note_call(bucket: str) -> int:
    """Record one live call against today's budget; returns the running count.
    Persisted, so the count survives a resume within the same UTC day."""
    day = time.strftime("%Y-%m-%d", time.gmtime())
    c = _conn()
    c.execute("""INSERT INTO budget (bucket, day, calls) VALUES (?,?,1)
                 ON CONFLICT(bucket, day) DO UPDATE SET calls = calls + 1""",
              (bucket, day))
    c.commit()
    return c.execute("SELECT calls FROM budget WHERE bucket=? AND day=?",
                     (bucket, day)).fetchone()[0]


def calls_today(bucket: str) -> int:
    day = time.strftime("%Y-%m-%d", time.gmtime())
    row = _conn().execute("SELECT calls FROM budget WHERE bucket=? AND day=?",
                          (bucket, day)).fetchone()
    return row[0] if row else 0


def stats() -> dict:
    c = _conn()
    n = c.execute("SELECT COUNT(*) FROM calls").fetchone()[0]
    nu = c.execute("SELECT COUNT(*) FROM calls WHERE usage_json IS NOT NULL"
                   ).fetchone()[0]
    return {"entries": n, "with_usage": nu, "db": str(DB_PATH)}
