"""
bench/ledger.py — one row per (document, condition) unit of work.

The executor schedules against this table, which is what makes a long run
interruptible at any point without losing anything: a unit is the atom that
succeeds, fails or is parked, so a document that breaks one condition still
carries its results for every other.  It also means every reported table can
state its own n and its own completeness, instead of a partial run silently
overwriting a report card that looks complete.
"""

from __future__ import annotations

import json
import sqlite3
import threading
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = _ROOT / "out1a" / "ledger.db"

PENDING, DONE, FAILED, PARKED, SKIPPED = "pending", "done", "failed", "parked", "skipped"

_local = threading.local()


def _conn() -> sqlite3.Connection:
    c = getattr(_local, "conn", None)
    if c is None:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        c = sqlite3.connect(DB_PATH, timeout=60.0)
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("""CREATE TABLE IF NOT EXISTS unit (
                        doc TEXT NOT NULL, cond TEXT NOT NULL,
                        tier INTEGER NOT NULL, status TEXT NOT NULL,
                        attempts INTEGER NOT NULL DEFAULT 0,
                        updated_at REAL, seconds REAL,
                        error TEXT, payload TEXT,
                        PRIMARY KEY (doc, cond))""")
        c.commit()
        _local.conn = c
    return c


def plan(doc: str, cond: str, tier: int) -> None:
    _conn().execute(
        "INSERT OR IGNORE INTO unit (doc,cond,tier,status,updated_at) "
        "VALUES (?,?,?,?,?)", (doc, cond, tier, PENDING, time.time()))
    _conn().commit()


def finish(doc: str, cond: str, status: str, payload: dict | None = None,
           error: str | None = None, seconds: float | None = None) -> None:
    c = _conn()
    c.execute("""UPDATE unit SET status=?, attempts=attempts+1, updated_at=?,
                        seconds=?, error=?, payload=?
                 WHERE doc=? AND cond=?""",
              (status, time.time(), seconds, error,
               json.dumps(payload, default=str) if payload else None, doc, cond))
    c.commit()


def pending(tier: int | None = None, conds: list[str] | None = None) -> list[tuple]:
    """Units still to do, ordered tier-major then document — the ordering that
    guarantees an interruption leaves every cheaper tier complete."""
    q = ("SELECT doc, cond, tier FROM unit WHERE status IN (?,?,?)",
         [PENDING, FAILED, PARKED])
    sql, args = q[0], list(q[1])
    if tier is not None:
        sql += " AND tier=?"
        args.append(tier)
    if conds:
        sql += f" AND cond IN ({','.join('?' * len(conds))})"
        args += conds
    sql += " ORDER BY tier, doc, cond"
    return _conn().execute(sql, args).fetchall()


def results(cond: str | None = None) -> list[dict]:
    sql = "SELECT doc, cond, payload FROM unit WHERE status='done'"
    args: list = []
    if cond:
        sql += " AND cond=?"
        args.append(cond)
    out = []
    for doc, c, payload in _conn().execute(sql + " ORDER BY doc", args):
        d = json.loads(payload) if payload else {}
        d["doc"], d["cond"] = doc, c
        out.append(d)
    return out


def summary() -> dict:
    rows = _conn().execute(
        "SELECT cond, tier, status, COUNT(*) FROM unit GROUP BY cond, tier, status"
    ).fetchall()
    out: dict = {}
    for cond, tier, status, n in rows:
        out.setdefault(cond, {"tier": tier})[status] = n
    return out


def redo(tier: int | None = None, conds: list[str] | None = None,
         docs: list[str] | None = None) -> int:
    """Mark matching units pending again so a changed pipeline is re-scored."""
    sql, args = "UPDATE unit SET status=?", [PENDING]
    where, wargs = [], []
    if tier is not None:
        where.append("tier=?"); wargs.append(tier)
    if conds:
        where.append(f"cond IN ({','.join('?' * len(conds))})"); wargs += conds
    if docs:
        where.append(f"doc IN ({','.join('?' * len(docs))})"); wargs += docs
    if where:
        sql += " WHERE " + " AND ".join(where)
    c = _conn()
    n = c.execute(sql, args + wargs).rowcount
    c.commit()
    return n


def prune(known: list[str]) -> int:
    """Drop units for conditions that no longer exist.

    A retired condition leaves rows behind that would otherwise keep showing
    up in the completeness table and the CSV as work that is somehow never
    done. Called by `plan`, so retiring a condition is one edit to the
    registry."""
    c = _conn()
    n = c.execute(f"DELETE FROM unit WHERE cond NOT IN "
                  f"({','.join('?' * len(known))})", known).rowcount
    c.commit()
    return n
