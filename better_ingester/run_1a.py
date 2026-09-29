#!/usr/bin/env python3
"""
run_1a.py — the intrinsic evaluation of the ingestion pipeline.

    python3 run_1a.py plan       # enumerate the (document x condition) units
    python3 run_1a.py run        # score them, cheapest tier first
    python3 run_1a.py prompts    # write the tier-1 prompts for offline running
    python3 run_1a.py report     # ledger -> report card, CSV, LaTeX numbers
    python3 run_1a.py status     # what is done, what is left

Scheduling is TIER-MAJOR: every document is scored on the zero-cost
conditions before any condition that needs a model call. An interruption
therefore always leaves a complete, reportable result set for every tier
cheaper than the one that stalled.

Each (document, condition) is an independently resumable unit in a SQLite
ledger, so one failing pair parks one pair rather than the document.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(_ROOT))

from bench import conditions as C, ledger, offline
from bench.conditions import ALL_CONDS, COMPARISONS, REGISTRY, TIER1
from bench.offline import ReplyMissing
from bench.score import score_unit

CORPUS_DIR = _ROOT / "corpus"
OUT_DIR = _ROOT / "out1a"
MANIFEST = _ROOT / "corpus_manifest.json"

# The measure printed per unit while a run is in flight — the one that says
# most about whether that condition did its job.
HEADLINE = {"ours": "edge_f1", "ceiling": "floor_recall"}


# ── terminal narration ─────────────────────────────────────────────────────

def say(msg: str = "") -> None:
    print(msg, flush=True)


def rule(title: str = "") -> None:
    say("─" * 78 if not title else f"── {title} " + "─" * max(0, 74 - len(title)))


# ── corpus ─────────────────────────────────────────────────────────────────

def manifest() -> dict:
    """The frozen manifest, or {} if the corpus has not been frozen yet."""
    if MANIFEST.exists():
        d = json.loads(MANIFEST.read_text())
        if isinstance(d, dict) and "documents" in d:
            return d
    return {}


def scored_names() -> set[str] | None:
    """Documents carrying claims. Once frozen, the manifest is AUTHORITATIVE:
    anything else left in corpus/ is ignored rather than silently widening the
    corpus the paper reports on. None means nothing is frozen yet."""
    m = manifest()
    return {d["name"] for d in m["documents"]} if m else None


def cell_of() -> dict[str, str]:
    return {d["name"]: d.get("cell", "?") for d in manifest().get("documents", [])}


def doc_dirs(root: Path) -> list[Path]:
    """Every document directory under `root`, at either nesting.

    A directory is a document iff it directly contains a .tex file, which
    distinguishes it from a stratification-cell folder without this needing to
    know the cell names."""
    out = []
    for sub in sorted(p for p in root.iterdir() if p.is_dir()):
        if any(sub.glob("*.tex")):
            out.append(sub)
        else:
            out.extend(sorted(d for d in sub.iterdir()
                              if d.is_dir() and any(d.glob("*.tex"))))
    return out


def discover() -> list[tuple[str, Path, Path]]:
    """(name, tex, pdf) for every document in the frozen corpus."""
    if not CORPUS_DIR.exists():
        return []
    keep = scored_names()
    docs = []
    for sub in doc_dirs(CORPUS_DIR):
        if keep is not None and sub.name not in keep:
            continue
        tex = next(iter(sorted(sub.glob("*.tex"))), None)
        if not tex:
            continue
        pdf = sub / f"{tex.stem}.pdf"
        if pdf.exists():
            docs.append((sub.name, tex, pdf))
    return docs


def selected_conds(args) -> list[str]:
    conds = list(args.only) if args.only else ALL_CONDS
    unknown = [c for c in conds if c not in REGISTRY]
    if unknown:
        raise SystemExit(f"unknown condition(s): {', '.join(unknown)}\n"
                         f"known: {', '.join(ALL_CONDS)}")
    if args.tier is not None:
        conds = [c for c in conds if REGISTRY[c].tier == args.tier]
    return conds


# ── commands ───────────────────────────────────────────────────────────────

def cmd_plan(args) -> int:
    docs = discover()
    conds = selected_conds(args)
    rule("plan")
    if not docs:
        say("No documents found. corpus_manifest.json is authoritative once "
            "frozen; check that corpus/ holds the documents it names.")
        return 1
    say(f"Corpus: {len(docs)} documents"
        f"{' (frozen manifest)' if scored_names() else ' (unfrozen)'}")
    say(f"Conditions: {len(conds)}")
    say("")
    for tier in sorted({REGISTRY[c].tier for c in conds}):
        cost = ("no model calls — runs unattended" if tier == 0
                else "one model call per document, supplied offline")
        say(f"  tier {tier}  ({cost})")
        for c in conds:
            if REGISTRY[c].tier == tier:
                say(f"      {REGISTRY[c].label:<12} {REGISTRY[c].note}")
        say("")
    retired = ledger.prune(ALL_CONDS)
    if retired:
        say(f"Dropped {retired} unit(s) for conditions that no longer exist.")
        say("")
    for name, _, _ in docs:
        for c in conds:
            ledger.plan(name, c, REGISTRY[c].tier)
    say(f"{len(docs)} x {len(conds)} = {len(docs) * len(conds)} units in the "
        f"ledger. Run them with `run_1a.py run`.")
    return 0


def cmd_prompts(args) -> int:
    """Write the tier-1 prompts for offline running."""
    docs = {n: (t, p) for n, t, p in discover()}
    conds = [c for c in selected_conds(args) if c in TIER1]
    rule("prompts")
    if not conds:
        say("Nothing to write: the tier-1 conditions are "
            f"{', '.join(TIER1)}.")
        return 0
    say("These conditions need one model call per document. This writes the "
        "prompt files; you paste each into a chat model and save the reply "
        "beside it.")
    say("")
    if args.doc:
        docs = {n: v for n, v in docs.items() if n in set(args.doc)}
    written = 0
    for name in sorted(docs):
        tex, pdf = docs[name]
        ctx = None
        for cond in conds:
            path = offline.prompt_path(cond, name)
            if path.exists() and not args.redo:
                continue
            if ctx is None:
                ctx = C.load_ctx(name, tex, pdf)
            if cond == "refine":
                from ingest.betteringest import BetterIngest, heading_skeleton
                d = BetterIngest(out_dir=OUT_DIR).ingest(ctx.pdf)
                prompt = C.build_refine_prompt(
                    ctx, heading_skeleton(d.tree, ctx.title))
            else:
                prompt = C.build_baseline_prompt(ctx)
            offline.write_prompt(cond, name, prompt)
            written += 1
    say(f"Wrote {written} prompt file(s) under out1a/llm/<condition>/.")
    say("")
    say("To answer them:")
    say("  1. Open   out1a/llm/<condition>/<document>.prompt.md")
    say("  2. Paste it into one chat model, at temperature 0 if you can set it.")
    say("  3. Save the reply verbatim to <document>.reply.txt beside it.")
    say("  4. Record which model you used:")
    say("       python3 run_1a.py status --model base_small=<model-name>")
    say("  5. Re-run `run_1a.py run --tier 1` to score the replies.")
    say("")
    say("BASE-small and BASE-big are the same prompt at two model tiers, so a "
        "reply is only comparable if the model that produced it is recorded. "
        "REFINE consumes our own output, so its prompts go stale if the "
        "pipeline changes — regenerate with `prompts --redo --only refine`.")
    return 0


def cmd_run(args) -> int:
    conds = selected_conds(args)
    if args.redo:
        n = ledger.redo(tier=args.tier, conds=conds,
                        docs=list(args.doc) if args.doc else None)
        say(f"--redo: {n} unit(s) reset to pending")
    units = [u for u in ledger.pending(tier=args.tier, conds=conds)]
    if args.doc:
        units = [u for u in units if u[0] in set(args.doc)]
    if not units:
        say("Nothing pending. Run `run_1a.py plan` first, or `run --redo` to "
            "re-score units that are already done.")
        return 0

    docs = {n: (t, p) for n, t, p in discover()}
    rule("run")
    say(f"{len(units)} unit(s) pending, in tier-major order: every document is "
        "scored on the free conditions before any that costs a model call.")
    say("")
    say("Each line below is one (document, condition). The number is that "
        "condition's headline measure — nesting F1 for the pipeline and the "
        "ablation rows, content recall for the ceiling.")
    say("")
    OUT_DIR.mkdir(exist_ok=True)

    ctx_cache: dict[str, C.DocCtx] = {}
    shared: dict[str, dict] = {}
    done = failed = parked = 0
    tier_seen = None

    for doc, cond, tier in units:
        if tier != tier_seen:
            tier_seen = tier
            say("")
            rule(f"tier {tier}")
        if doc not in docs:
            ledger.finish(doc, cond, ledger.SKIPPED, error="not in corpus")
            continue
        t0 = time.time()
        label = REGISTRY[cond].label
        try:
            if doc not in ctx_cache:
                ctx_cache.clear()              # one document's blocks at a time
                tex, pdf = docs[doc]
                ctx_cache[doc] = C.load_ctx(doc, tex, pdf)
                shared[doc] = {}
            row = score_unit(cond, ctx_cache[doc], OUT_DIR,
                             shared.setdefault(doc, {}))
            ledger.finish(doc, cond, ledger.DONE, payload=row,
                          seconds=round(time.time() - t0, 2))
            done += 1
            key = HEADLINE.get(cond, "edge_f1")
            val = row.get(key)
            shown = f"{key} {val:.3f}" if isinstance(val, float) else str(val)
            say(f"  ok    {doc:<28} {label:<12} {shown}")
        except ReplyMissing:
            ledger.finish(doc, cond, ledger.PARKED,
                          error="awaiting an offline reply",
                          seconds=round(time.time() - t0, 2))
            parked += 1
            say(f"  wait  {doc:<28} {label:<12} no reply saved yet")
        except Exception as e:
            ledger.finish(doc, cond, ledger.FAILED,
                          error=f"{type(e).__name__}: {e}"[:300],
                          seconds=round(time.time() - t0, 2))
            failed += 1
            say(f"  FAIL  {doc:<28} {label:<12} "
                f"{type(e).__name__}: {str(e)[:60]}")

    say("")
    say(f"Scored {done}, failed {failed}, awaiting a reply {parked}.")
    if parked:
        say("Units awaiting a reply are a schedule state, not a failure: write "
            "their prompts with `run_1a.py prompts`, answer them, and re-run.")
    say("")
    return cmd_report(args)


def cmd_report(args) -> int:
    """Write every artifact together so they can never disagree."""
    from bench import report as R

    OUT_DIR.mkdir(exist_ok=True)
    all_rows = ledger.results()
    by_cond: dict[str, list[dict]] = {}
    for r in all_rows:
        by_cond.setdefault(r["cond"], []).append(r)

    cell_map = cell_of()
    cells: dict[str, list[dict]] = {}
    for r in by_cond.get("ours", []):
        cells.setdefault(cell_map.get(r["doc"], "unassigned"), []).append(r)
    if set(cells) == {"unassigned"}:
        cells = {}

    docs = [n for n, _, _ in discover()]
    summary = R.aggregate(by_cond)
    comps = R.comparisons(by_cond, COMPARISONS)
    led = ledger.summary()
    llm = offline.status(TIER1, docs)

    pages_of = {d['name']: d.get('pages') for d in manifest().get('documents', [])}
    md = R.markdown(summary, by_cond, cells, comps, led, len(docs),
                    ALL_CONDS, pages_of, llm)
    (OUT_DIR / "report_card.md").write_text(md + "\n", encoding="utf-8")
    (OUT_DIR / "summary.json").write_text(json.dumps(
        {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
         "corpus_n": len(docs), "conditions": summary, "comparisons": comps,
         "cells": {k: len(v) for k, v in cells.items()},
         "completeness": led, "offline_models": offline.models()},
        indent=2), encoding="utf-8")
    (OUT_DIR / "results.json").write_text(
        json.dumps(all_rows, indent=2, default=str), encoding="utf-8")
    n_csv = R.write_csv(OUT_DIR / "results.csv", all_rows, manifest(), ALL_CONDS)
    (OUT_DIR / "numbers.tex").write_text(
        R.latex_numbers(summary, comps, cells, len(docs)), encoding="utf-8")
    (OUT_DIR / "tables.tex").write_text(
        R.latex_tables(summary, cells, ALL_CONDS), encoding="utf-8")

    say(md)
    say("")
    rule("artifacts")
    for f, what in (
            ("results.csv", f"{n_csv} rows, one per (document, condition), "
                            "every measure in a fixed column order"),
            ("report_card.md", "the tables above, as a standalone document"),
            ("summary.json", "the same aggregates, machine-readable"),
            ("results.json", "the per-document rows the aggregates come from"),
            ("numbers.tex", "one \\newcommand per number — \\input it so the "
                            "paper never holds a hand-copied figure"),
            ("tables.tex", "ready-to-paste tabular environments")):
        say(f"  out1a/{f:<16} {what}")
    return 0


def cmd_status(args) -> int:
    docs = [n for n, _, _ in discover()]
    if args.model:
        for pair in args.model:
            cond, _, name = pair.partition("=")
            if cond not in REGISTRY or not name:
                raise SystemExit(f"expected <condition>=<model>, got {pair!r}")
            offline.record_model(cond, name)
            say(f"Recorded: {REGISTRY[cond].label} was answered by {name}")
        return 0

    rule("status")
    say(f"Corpus: {len(docs)} documents.")
    say("")
    say("| condition | tier | done | failed | awaiting | pending |")
    for cond, st in sorted(ledger.summary().items(),
                           key=lambda kv: (kv[1]["tier"], kv[0])):
        label = REGISTRY[cond].label if cond in REGISTRY else cond
        say(f"  {label:<12} {st['tier']:<5} {st.get('done', 0):<6} "
            f"{st.get('failed', 0):<8} {st.get('parked', 0):<10} "
            f"{st.get('pending', 0)}")
    say("")
    say("Offline conditions (prompts written / replies saved):")
    for cond, st in offline.status(TIER1, docs).items():
        say(f"  {REGISTRY[cond].label:<12} {st['prompts']:>3} / "
            f"{st['replies']:>3} of {st['documents']}"
            f"   model: {st.get('model') or 'not recorded'}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="run_1a", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn, help_ in (
            ("plan", cmd_plan, "enumerate the units to score"),
            ("run", cmd_run, "score pending units, cheapest tier first"),
            ("prompts", cmd_prompts, "write the tier-1 prompts"),
            ("report", cmd_report, "regenerate every reporting artifact"),
            ("status", cmd_status, "what is done and what is left")):
        s = sub.add_parser(name, help=help_)
        s.add_argument("--tier", type=int, default=None,
                       help="restrict to one cost tier")
        s.add_argument("--only", nargs="*", default=None,
                       help="restrict to named conditions")
        s.add_argument("--doc", nargs="*", default=None,
                       help="restrict to named documents")
        s.add_argument("--redo", action="store_true",
                       help="recompute matching units instead of skipping them")
        s.add_argument("--model", nargs="*", default=None,
                       help="record which model answered a condition, "
                            "e.g. --model base_small=claude-haiku-4-5")
        s.set_defaults(fn=fn)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
