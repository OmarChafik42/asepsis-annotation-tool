"""Tests for the 1(a) harness infrastructure: ledger, cache, report, transport."""
import json
import threading

import pytest

from bench import cache_db, ledger, report as R
from bench.conditions import parse_headings
from bench.transport import _classify, _retry_delay


@pytest.fixture
def fresh_ledger(tmp_path, monkeypatch):
    monkeypatch.setattr(ledger, "DB_PATH", tmp_path / "ledger.db")
    monkeypatch.setattr(ledger, "_local", threading.local())
    return ledger


@pytest.fixture
def fresh_cache(tmp_path, monkeypatch):
    monkeypatch.setattr(cache_db, "DB_PATH", tmp_path / "cache.db")
    monkeypatch.setattr(cache_db, "_local", threading.local())
    return cache_db


# ── ledger ─────────────────────────────────────────────────────────────────

def test_pending_is_tier_major(fresh_ledger):
    """The scheduling property the whole design rests on: every document is
    exhausted at a cheap tier before any expensive unit runs, so an interruption
    always leaves the cheaper tiers complete."""
    L = fresh_ledger
    for doc in ("b_doc", "a_doc"):
        L.plan(doc, "expensive", 2)
        L.plan(doc, "cheap", 0)
        L.plan(doc, "medium", 1)
    tiers = [t for _, _, t in L.pending()]
    assert tiers == sorted(tiers), "pending() must yield tier-major order"
    assert tiers[:2] == [0, 0] and tiers[-2:] == [2, 2]


def test_plan_is_idempotent(fresh_ledger):
    fresh_ledger.plan("d", "ours", 0)
    fresh_ledger.plan("d", "ours", 0)
    assert len(fresh_ledger.pending()) == 1


def test_done_units_leave_the_queue(fresh_ledger):
    L = fresh_ledger
    L.plan("d", "ours", 0)
    L.finish("d", "ours", L.DONE, payload={"edge_f1": 0.9})
    assert L.pending() == []
    assert L.results("ours")[0]["edge_f1"] == 0.9


def test_failed_and_parked_units_are_retried(fresh_ledger):
    L = fresh_ledger
    L.plan("d1", "c", 1)
    L.plan("d2", "c", 1)
    L.finish("d1", "c", L.FAILED, error="boom")
    L.finish("d2", "c", L.PARKED, error="bucket down")
    assert {d for d, _, _ in L.pending()} == {"d1", "d2"}


def test_one_failing_unit_does_not_take_the_document_with_it(fresh_ledger):
    """A document that breaks one condition keeps its results for the others."""
    L = fresh_ledger
    L.plan("d", "ours", 0)
    L.plan("d", "refine", 1)
    L.finish("d", "ours", L.DONE, payload={"edge_f1": 0.8})
    L.finish("d", "refine", L.FAILED, error="no reply")
    assert len(L.results("ours")) == 1
    assert L.summary()["refine"]["failed"] == 1


def test_redo_scopes_to_selection(fresh_ledger):
    L = fresh_ledger
    for c, t in (("ours", 0), ("ceiling", 0), ("refine", 1)):
        L.plan("d", c, t)
        L.finish("d", c, L.DONE, payload={})
    assert L.redo(conds=["ours"]) == 1
    assert [c for _, c, _ in L.pending()] == ["ours"]
    assert L.redo(tier=0) == 2


# ── cache ──────────────────────────────────────────────────────────────────

def test_cache_roundtrip_and_miss(fresh_cache):
    k = fresh_cache.key_hash("api", "m", "prompt")
    assert fresh_cache.get(k) is None
    fresh_cache.put(k, "reply")
    assert fresh_cache.get(k) == "reply"


def test_cache_key_is_stable_and_scheme_compatible(fresh_cache):
    """Migration imported legacy entries by filename, which was
    sha256("kind\\0model\\0payload") — the derivation must not drift or every
    migrated entry silently becomes a miss and gets re-paid for."""
    import hashlib
    expect = hashlib.sha256(b"api\x00gpt\x00hello").hexdigest()
    assert fresh_cache.key_hash("api", "gpt", "hello") == expect


def test_cache_key_separates_models_and_kinds(fresh_cache):
    a = fresh_cache.key_hash("api", "m1", "p")
    assert len({a, fresh_cache.key_hash("api", "m2", "p"),
                fresh_cache.key_hash("chat", "m1", "p")}) == 3


def test_budget_counter_accumulates(fresh_cache):
    assert fresh_cache.calls_today("big") == 0
    fresh_cache.note_call("big")
    fresh_cache.note_call("big")
    assert fresh_cache.calls_today("big") == 2
    assert fresh_cache.calls_today("small") == 0


# ── report aggregation ─────────────────────────────────────────────────────

def test_asset_means_exclude_documents_with_no_ground_truth_asset():
    """The empty-set convention scores a figure-free document 1.0, which is
    right per document and inflates a corpus mean. Guarded metrics must drop
    those rows rather than average them in."""
    rows = [{"doc": "has", "asset_f1": 0.5, "asset_n_truth": 4},
            {"doc": "none", "asset_f1": 1.0, "asset_n_truth": 0}]
    agg = R.aggregate({"ours": rows})["ours"]
    assert agg["asset_f1"]["n"] == 1
    assert agg["asset_f1"]["mean"] == pytest.approx(0.5)


def test_unguarded_metric_keeps_every_row():
    rows = [{"doc": "a", "edge_f1": 0.4}, {"doc": "b", "edge_f1": 0.6}]
    agg = R.aggregate({"ours": rows})["ours"]
    assert agg["edge_f1"]["n"] == 2 and agg["edge_f1"]["mean"] == pytest.approx(0.5)


def test_aggregate_skips_missing_and_non_numeric():
    rows = [{"doc": "a", "edge_f1": 0.4}, {"doc": "b"},
            {"doc": "c", "edge_f1": None}, {"doc": "d", "edge_f1": True}]
    assert R.aggregate({"ours": rows})["ours"]["edge_f1"]["n"] == 1


def test_latex_macro_names_are_letters_only():
    """TeX control sequences cannot contain digits or underscores."""
    summary = {"ours": {"edge_f1": {"mean": 0.8, "sd": 0.1, "n": 5,
                                    "ci_lo": 0.7, "ci_hi": 0.9}}}
    out = R.latex_numbers(summary, [], {}, 5)
    import re
    for name in re.findall(r"\\newcommand\{\\(\w+)\}", out):
        assert name.isalpha(), f"invalid TeX macro name: {name}"
    assert "\\resOursEdgeFOne" in out


def test_latex_numbers_reports_n_alongside_every_value():
    summary = {"ours": {"edge_f1": {"mean": 0.8, "sd": 0.1, "n": 42,
                                    "ci_lo": 0.7, "ci_hi": 0.9}}}
    out = R.latex_numbers(summary, [], {}, 42)
    assert "\\resOursEdgeFOneN}{42}" in out


# ── transport error classification ─────────────────────────────────────────

@pytest.mark.parametrize("msg,kind", [
    ("429 RESOURCE_EXHAUSTED quota", "rate"),
    ("Error code: 500 - internal", "transient"),
    ("Request timed out.", "transient"),
    ("503 Service Unavailable", "transient"),
    ("You exceeded your quota PerDay limit", "quota_day"),
    ("invalid api key", "fatal"),
])
def test_error_classification(msg, kind):
    assert _classify(msg) == kind


def test_daily_quota_wins_over_generic_rate_wording():
    """A per-day exhaustion must abort the run, not trigger an endless backoff."""
    assert _classify("429 quota exceeded: PerDay limit reached") == "quota_day"


def test_retry_delay_honours_server_hint():
    assert _retry_delay("rate", 0, "please retry in 7s") == pytest.approx(9.0)
    assert _retry_delay("transient", 2, "boom") == pytest.approx(30.0)


# ── LLM reply parsing ──────────────────────────────────────────────────────

@pytest.mark.parametrize("raw", [
    '{"headings":[{"title":"Intro","level":1}]}',
    '{"sections":[{"name":"Intro","level":1}]}',
    '[{"title":"Intro","level":1}]',
    '["Intro"]',
])
def test_parse_headings_tolerates_schema_drift(raw):
    heads, lvls = parse_headings(raw)
    assert heads == ["Intro"] and lvls == [1]


def test_parse_headings_flattens_nested_children():
    heads, lvls = parse_headings(
        '{"headings":[{"title":"A","level":1,'
        '"children":[{"title":"A1","level":2}]}]}')
    assert heads == ["A", "A1"] and lvls == [1, 2]


def test_parse_headings_returns_empty_on_garbage():
    assert parse_headings("not json at all") == ([], [])
    assert parse_headings("{}") == ([], [])


# ── OpenKB's dispatch threshold ────────────────────────────────────────────
#
# OpenKB reads a document under 20 pages in one call after converting it with
# markitdown, which is what BASE reproduces, but routes a longer one to
# PageIndex instead. The report has to say where BASE is faithful and where it
# is extrapolated, or a reader will assume the first everywhere.

def test_page_groups_split_at_the_threshold():
    rows = [{"doc": "a"}, {"doc": "b"}, {"doc": "c"}]
    pages = {"a": 19, "b": 20, "c": 77}
    g = R.page_groups(rows, pages)
    assert [r["doc"] for r in g["under"]] == ["a"]
    assert [r["doc"] for r in g["over"]] == ["b", "c"]


def test_page_groups_ignores_documents_with_no_page_count():
    g = R.page_groups([{"doc": "a"}, {"doc": "ghost"}], {"a": 5})
    assert len(g["under"]) == 1 and not g["over"]


def test_openkb_section_is_absent_until_base_rows_exist():
    assert R.openkb_fidelity({"ours": [{"doc": "a", "title_f1": 0.9}]},
                             {"a": 5}, ["ours", "base_small"]) == []


def test_openkb_section_reports_both_subsets_with_their_n():
    rows = {"base_small": [
        {"doc": "a", "title_f1": 0.80, "edge_f1": 0.70, "depth_acc": 0.9},
        {"doc": "b", "title_f1": 0.60, "edge_f1": 0.50, "depth_acc": 0.8},
    ]}
    out = "\n".join(R.openkb_fidelity(rows, {"a": 10, "b": 40},
                                      ["base_small"]))
    assert "faithful" in out and "extrapolated" in out
    assert "0.800" in out and "0.600" in out


def test_openkb_section_omits_an_empty_subset():
    """A corpus with no long documents should not print an empty row."""
    rows = {"base_small": [{"doc": "a", "title_f1": 0.8, "edge_f1": 0.7,
                            "depth_acc": 0.9}]}
    out = "\n".join(R.openkb_fidelity(rows, {"a": 10}, ["base_small"]))
    assert "faithful" in out and "extrapolated" not in out
