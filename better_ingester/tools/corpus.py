"""
tools/corpus.py — build and freeze the stratified corpus.

The corpus is stratified on the two variables the pipeline actually reacts
to — column count (must reading order be reconstructed across columns?) and
numbering scheme (which level decoder fires?) — rather than on subject
category, which the pipeline never sees. Category is balanced WITHIN cells,
so it is controlled rather than ignored.

The workflow, in order:

    python3 tools/corpus.py status              where every cell stands
    python3 tools/corpus.py scan --after DATE   sweep arXiv for deficit cells
    python3 tools/corpus.py select              seeded, category-balanced pick
    python3 tools/corpus.py download            PDFs + LaTeX sources
    python3 tools/corpus.py freeze --after DATE hash, verify, write manifest
    python3 tools/corpus.py topup               refill cells the render moved

Freezing makes corpus_manifest.json AUTHORITATIVE: the runner then ignores
anything in corpus/ the manifest does not name, so an exploratory download
can never silently widen the corpus the paper reports on.

Column count is decided from the RENDER, not the source. Source-only
classification was wrong on 15% of the pilot: a conference style file can
call \\twocolumn from a plain \\documentclass{article} with nothing
detectable in the source at all. Since the pipeline consumes the render, the
render is what the stratification has to be true of — so `freeze` re-verifies
every document and `topup` exists because that verification moves documents
between cells.

Scanning is deliberately not a neutral sample of arXiv. Unnumbered sectioning
is roughly 1% of it and tracks journal templates rather than any subject, so
the deficit categories below aim where a missing cell would be if it existed.
A negative result is only worth reporting if the search was aimed properly;
tools/cell_census.py records the prevalence evidence that makes the two rare
cells a measured claim rather than an assumption.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import random
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.fetch_arxiv import _get, list_recent, source_tex

CORPUS = Path("corpus")
MANIFEST = Path("corpus_manifest.json")
SEED = 20260702

TARGET = {"single_arabic": 12, "single_roman": 6, "single_unnumbered": 12,
          "two_arabic": 12, "two_roman": 12, "two_unnumbered": 6}


DEFICIT_CATEGORIES = {
    "single_unnumbered": ["q-bio.PE", "q-bio.QM", "q-bio.NC", "econ.EM", "econ.GN",
                          "stat.AP", "stat.ME", "math.PR", "math.ST", "q-fin.ST",
                          "physics.med-ph", "physics.soc-ph", "cs.CY", "cs.DL"],
    "two_unnumbered": ["cond-mat.soft", "cond-mat.stat-mech", "physics.bio-ph",
                       "astro-ph.GA", "astro-ph.CO", "quant-ph", "q-bio.PE",
                       "physics.optics", "physics.flu-dyn", "nlin.AO"],
    "two_arabic": ["cs.CY", "cs.HC", "cs.SE", "cs.DB", "cond-mat.mtrl-sci",
                   "astro-ph.SR", "physics.comp-ph"],
    "single_arabic": ["cs.LG", "math.NA", "econ.GN", "stat.ML"],
    "single_roman": ["eess.SP", "cs.IT", "eess.SY", "cs.NI"],
    "two_roman": ["eess.SP", "cs.IT", "cs.NI", "eess.SY"],
}


PLAN = Path("out1a/corpus_plan.json")


# ── the candidate bank ───────────────────────────────────────────────────
#
# Every paper ever classified, banked so a rescan grows N rather than
# repeating work, and so the corpus builder draws from the census instead
# of re-downloading sources. tools/cell_census.py reports over the same
# file — the prevalence evidence and the candidate pool are one dataset.

CENSUS = Path("out1a/cell_census.json")


def load() -> dict:
    if CENSUS.exists():
        return json.loads(CENSUS.read_text())
    return {}


def save(d: dict) -> None:
    CENSUS.parent.mkdir(parents=True, exist_ok=True)
    CENSUS.write_text(json.dumps(d, indent=1))


# ── source classification ────────────────────────────────────────────────

_COMMENT = re.compile(r"(?<!\\)%.*")          # strip LaTeX comments, keep \%

_CLASS = re.compile(r"\\documentclass\s*(\[[^\]]*\])?\s*\{([^}]+)\}")

_TWOCOL_CMD = re.compile(r"^\s*\\twocolumn\b", re.M)

_MULTICOLS = re.compile(r"\\begin\{multicols\}\s*\{\s*[2-9]")

_SEC = re.compile(r"\\(?:sub)*section(\*?)\s*[\{\[]")

_SECNUMDEPTH = re.compile(r"\\setcounter\s*\{secnumdepth\}\s*\{\s*(-?\d+)\s*\}")


# classes whose default sectioning is roman section / letter subsection
_ROMAN_CLASSES = ("ieeetran", "ieeeconf", "ieeeojs")

# Classes that render two columns by default, with no option required.
_TWOCOL_CLASSES = ("ieeetran", "ieeeconf", "sig-alternate", "aa",
                   "emulateapj", "aastex6", "aastex61", "mnras")


def classify(tex: str) -> tuple[str, str, str]:
    """(columns, numbering, documentclass) from the LaTeX source.

    This is a PRE-FILTER, not the final answer for column count. Verified
    against renders on the 47-document pilot, source-only classification was
    wrong on 7 (15%): commented-out class lines, `\\twocolumn` issued as a
    command, revtex `reprint`, two-column-by-default classes, and — not fixable
    in principle — conference style files that call `\\twocolumn` internally
    from a plain `\\documentclass{article}`. There is no bounded list of those,
    so `bench.layout_verify` decides the column count at freeze time and this
    function only decides what is worth downloading.

    Numbering stays source-derived: it follows from the class and its counters,
    which the source does state reliably."""
    tex = _COMMENT.sub("", tex)          # a commented-out \documentclass is not the class
    m = _CLASS.search(tex)
    opts = (m.group(1) or "").lower() if m else ""
    cls = (m.group(2) or "").strip().lower() if m else "unknown"

    columns = "single"
    if "twocolumn" in opts or any(c in cls for c in _TWOCOL_CLASSES):
        columns = "two"
    if "acmart" in cls and ("sigconf" in opts or "sigplan" in opts):
        columns = "two"
    if "revtex" in cls and "twocolumn" in opts:
        columns = "two"
    if "reprint" in opts and "revtex" in cls:      # revtex reprint = two columns
        columns = "two"
    if _TWOCOL_CMD.search(tex) or _MULTICOLS.search(tex):
        columns = "two"
    if "onecolumn" in opts:                        # explicit override wins
        columns = "single"

    secs = _SEC.findall(tex)
    starred = sum(1 for s in secs if s == "*")
    depth = _SECNUMDEPTH.search(tex)
    numbering = "arabic"
    if any(c in cls for c in _ROMAN_CLASSES):
        numbering = "roman"
    if (depth and int(depth.group(1)) < 1) or (secs and starred / len(secs) > 0.6):
        numbering = "unnumbered"
    return columns, numbering, cls


# ── the cell bank ────────────────────────────────────────────────────────

def _doc_dir(cell: str, safe_id: str) -> Path:
    """Where a document lives. Grouped by cell when the corpus is organised
    that way, flat otherwise, so both layouts keep working."""
    name = f"arxiv_{safe_id}"
    flat = CORPUS / name
    if flat.exists():
        return flat
    grouped = CORPUS / cell / name
    if grouped.exists() or (CORPUS / cell).exists():
        return grouped
    return flat


def counts(bank: dict) -> collections.Counter:
    return collections.Counter(v["cell"] for v in bank.values() if v.get("cell"))


def deficits(bank: dict) -> dict[str, int]:
    c = counts(bank)
    return {k: t - c.get(k, 0) for k, t in TARGET.items() if c.get(k, 0) < t}


def _all_doc_dirs(root: Path):
    """Every document directory, at either nesting depth. A directory is a
    document iff it directly contains a .tex file."""
    if not root.exists():
        return
    for sub in sorted(p for p in root.iterdir() if p.is_dir()):
        if any(sub.glob("*.tex")):
            yield sub
        else:
            yield from (d for d in sorted(sub.iterdir())
                        if d.is_dir() and any(d.glob("*.tex")))


# ── commands ─────────────────────────────────────────────────────────────

def cmd_status(args) -> None:
    """Where every cell stands, against its target."""
    bank = load()
    c = counts(bank)
    print(f"bank: {len(bank)} scanned, {sum(c.values())} classified\n")
    print(f"  {'cell':22s} {'have':>5s} {'target':>7s} {'short':>6s}")
    for k, t in TARGET.items():
        have = c.get(k, 0)
        print(f"  {k:22s} {have:5d} {t:7d} {max(0, t - have):6d}")
    d = deficits(bank)
    print(f"\n  cells short: {len(d)}  ({sum(d.values())} documents)"
          if d else "\n  ALL CELLS FULL — run `select`")
    if MANIFEST.exists():
        docs = json.loads(MANIFEST.read_text()).get("documents", [])
        print(f"\n  frozen manifest: {len(docs)} documents "
              f"({collections.Counter(d['cell'] for d in docs)})")


def cmd_scan(args) -> None:
    bank = load()
    scanned_this_run = 0
    t_start = time.time()
    while (d := deficits(bank)) and scanned_this_run < args.budget:
        cats = []
        for cell in d:
            cats += DEFICIT_CATEGORIES.get(cell, [])
        seen_cats = list(dict.fromkeys(cats))
        print(f"[fill] short: { {k: v for k, v in d.items()} }  "
              f"sweeping {len(seen_cats)} categories", flush=True)
        progressed = False
        for cat in seen_cats:
            if scanned_this_run >= args.budget or not deficits(bank):
                break
            try:
                cands = list_recent(cat, args.after, args.per_category,
                                    scan=args.per_category * 4)
            except Exception as e:
                print(f"  ! {cat}: {type(e).__name__}", flush=True)
                continue
            new_here = 0
            for aid, pub, title in cands:
                if aid in bank or new_here >= args.per_category:
                    continue
                if scanned_this_run >= args.budget:
                    break
                try:
                    tex = source_tex(aid)
                    time.sleep(3)
                except Exception:
                    continue
                scanned_this_run += 1
                new_here += 1
                progressed = True
                if not tex or "\\begin{document}" not in tex:
                    bank[aid] = {"cell": None, "category": cat, "published": pub}
                    continue
                col, num, cls = classify(tex)
                cell = f"{col}_{num}"
                bank[aid] = {"cell": cell, "columns": col, "numbering": num,
                             "documentclass": cls, "category": cat,
                             "published": pub, "title": title[:80]}
                if cell in d:
                    print(f"   + {cell:18s} {aid}  {cls}", flush=True)
                if scanned_this_run % 25 == 0:
                    save(bank)
                    print(f"   … {scanned_this_run} scanned this run "
                          f"({time.time()-t_start:.0f}s), short="
                          f"{sum(deficits(bank).values())}", flush=True)
        save(bank)
        if not progressed:
            print("[fill] no new candidates from any deficit category — "
                  "widen --after or raise --per-category", flush=True)
            break
    save(bank)
    cmd_status(args)


def cmd_select(args) -> None:
    """Pick the corpus, seeded and frozen, balancing categories within cells."""
    bank = load()
    rng = random.Random(SEED)
    chosen: dict[str, list] = {}
    for cell, target in TARGET.items():
        pool = [dict(v, arxiv_id=k) for k, v in bank.items() if v.get("cell") == cell]
        # balance categories within the cell: round-robin over category buckets
        buckets: dict[str, list] = {}
        for p in pool:
            buckets.setdefault(p.get("category") or "?", []).append(p)
        for b in buckets.values():
            rng.shuffle(b)
        order = sorted(buckets, key=lambda k: -len(buckets[k]))
        picked = []
        while len(picked) < target and any(buckets[k] for k in order):
            for k in order:
                if buckets[k] and len(picked) < target:
                    picked.append(buckets[k].pop())
        chosen[cell] = picked
        print(f"  {cell:22s} {len(picked):2d}/{target}  "
              f"categories={len({p.get('category') for p in picked})}")
    PLAN.parent.mkdir(parents=True, exist_ok=True)
    PLAN.write_text(json.dumps(chosen, indent=2))
    total = sum(len(v) for v in chosen.values())
    print(f"\n[select] {total} documents → {PLAN}")


def cmd_download(args) -> None:
    plan = json.loads(PLAN.read_text())
    kept = failed = 0
    for cell, items in plan.items():
        for it in items:
            aid = it["arxiv_id"]
            safe = aid.replace("/", "_")
            d = _doc_dir(cell, safe)
            if (d / f"arxiv_{safe}.pdf").exists():
                continue
            try:
                tex = source_tex(aid)
                time.sleep(3)
                if not tex:
                    failed += 1
                    continue
                d.mkdir(parents=True, exist_ok=True)
                (d / f"arxiv_{safe}.tex").write_text(tex, encoding="utf-8")
                (d / f"arxiv_{safe}.pdf").write_bytes(
                    _get(f"https://arxiv.org/pdf/{aid}.pdf"))
                time.sleep(3)
                (d / "meta.json").write_text(
                    json.dumps({**it, "cell": cell}, indent=2))
                kept += 1
                print(f"  ✓ {cell:18s} {aid}", flush=True)
            except Exception as e:
                failed += 1
                print(f"  ! {aid}: {type(e).__name__}: {str(e)[:70]}", flush=True)
    print(f"\n[download] {kept} fetched, {failed} failed")


def cmd_freeze(args) -> None:
    """Hash every PDF, verify its column count from the RENDER, and write the
    manifest that makes the corpus authoritative.

    Two modes, because they answer different questions:

    · With no manifest yet, this SELECTS: it verifies every downloaded
      document and trims each cell to its target, seeded, so a corpus built
      from scratch is reproducible. Trimming is needed because `topup`
      deliberately over-pulls — render verification moves documents between
      cells, so more are fetched than are kept.

    · With a manifest already frozen, this RE-VERIFIES exactly the documents
      it names and nothing else. The frozen corpus is the artifact every
      reported number is computed over, so re-running freeze must not
      silently reselect it; `--refreeze` is the explicit way to rebuild.
    """
    from bench.latex import parse_latex
    from bench.layout_verify import verify
    import pypdfium2 as pdfium

    existing = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else None
    if existing and not args.refreeze:
        keep = {d["name"] for d in existing["documents"]}
        print(f"[freeze] re-verifying the {len(keep)} frozen documents. "
              f"Pass --refreeze to reselect the corpus from the plan.")
    else:
        keep = None
        if PLAN.exists():
            plan = json.loads(PLAN.read_text())
            keep = {f"arxiv_{i['arxiv_id'].replace('/', '_')}"
                    for items in plan.values() for i in items}
            print(f"[freeze] selecting from the {len(keep)} planned documents")

    docs, flagged = [], []
    for sub in _all_doc_dirs(CORPUS):
        if keep is not None and sub.name not in keep:
            continue
        tex = next(iter(sorted(sub.glob("*.tex"))), None)
        pdf = sub / f"{tex.stem}.pdf" if tex else None
        if not (tex and pdf and pdf.exists()):
            continue
        meta = json.loads((sub / "meta.json").read_text()) \
            if (sub / "meta.json").exists() else {}
        col_src, num, cls = classify(
            tex.read_text(encoding="utf-8", errors="ignore"))
        # The render is authoritative; the source pre-filter only decided this
        # document was worth fetching.
        v = verify(pdf)
        col = v.columns if v.columns in ("single", "two") else col_src
        if v.columns != col_src:
            flagged.append((sub.name, col_src, v.columns, v.span_ratio))
        docs.append({
            "name": sub.name,
            "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
            "cell": f"{col}_{num}", "columns": col, "numbering": num,
            "columns_source": col_src, "columns_render": v.columns,
            "span_ratio": round(v.span_ratio, 3), "documentclass": cls,
            "category": meta.get("category"), "published": meta.get("published"),
            "pages": len(pdfium.PdfDocument(str(pdf))),
            "gt_headings": len(parse_latex(tex).all_nodes()) - 1,
        })

    verified = len(docs)
    if existing and not args.refreeze:
        missing = {d["name"] for d in existing["documents"]} - {d["name"] for d in docs}
        if missing:
            raise SystemExit(
                f"[freeze] {len(missing)} frozen document(s) are missing from "
                f"corpus/: {', '.join(sorted(missing)[:5])}...\n"
                "The manifest is authoritative — restore them, or --refreeze "
                "to rebuild the corpus (which changes every reported number).")
        trimmed_from = existing.get("trimmed_from")
        date_gate = existing.get("date_gate", args.after)
    else:
        docs = _trim_to_targets(docs)
        trimmed_from = verified if len(docs) != verified else None
        date_gate = args.after

    out = {
        "frozen_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "seed": SEED,
        "date_gate": date_gate,
        "date_gate_source": (existing or {}).get(
            "date_gate_source",
            "TODO: record the pinned model's published training cutoff and "
            "where it was stated"),
        "cells": dict(TARGET),
        "trimmed_from": trimmed_from,
        "documents": sorted(docs, key=lambda d: d["name"]),
    }
    MANIFEST.write_text(json.dumps(out, indent=2))
    print(f"[freeze] {len(docs)} documents → {MANIFEST}")
    if flagged:
        print(f"\n  {len(flagged)} document(s) where the render disagreed with "
              f"the source — the render won; review the ambiguous ones:")
        for name, cs, cr, sr in flagged:
            mark = "  <-- AMBIGUOUS" if cr not in ("single", "two") else ""
            print(f"    {name:28s} source={cs:7s} render={cr:9s} "
                  f"span={sr:.2f}{mark}")
    print("  cells:", dict(collections.Counter(d["cell"] for d in docs)))
    print("  categories:",
          dict(collections.Counter(str(d["category"]) for d in docs)))


def _trim_to_targets(docs: list[dict]) -> list[dict]:
    """Cut each cell down to its target count, seeded and category-balanced.

    `topup` over-pulls on purpose, so a freshly built corpus holds more
    documents than the design calls for. Trimming here rather than at download
    time is deliberate: which cell a document belongs to is only known after
    the render is verified, so the selection cannot be made any earlier.

    Balanced the same way `select` is — round-robin over category buckets —
    so trimming does not concentrate a cell on whichever category happened to
    be easiest to find.
    """
    by_cell: dict[str, list[dict]] = {}
    for d in docs:
        by_cell.setdefault(d["cell"], []).append(d)

    kept: list[dict] = []
    for cell, group in sorted(by_cell.items()):
        target = TARGET.get(cell)
        if target is None or len(group) <= target:
            kept += group
            continue
        rng = random.Random(f"{SEED}:{cell}")
        buckets: dict[str, list[dict]] = {}
        for d in sorted(group, key=lambda x: x["name"]):
            buckets.setdefault(str(d.get("category")), []).append(d)
        for b in buckets.values():
            rng.shuffle(b)
        order = sorted(buckets, key=lambda k: (-len(buckets[k]), k))
        picked: list[dict] = []
        while len(picked) < target and any(buckets[k] for k in order):
            for k in order:
                if buckets[k] and len(picked) < target:
                    picked.append(buckets[k].pop())
        print(f"  {cell:22s} trimmed {len(group)} -> {len(picked)}")
        kept += picked
    return kept


def cmd_topup(args) -> None:
    """Top up cells that fell short AFTER render verification.

    Selection draws on the census bank, whose cell labels come from the source
    pre-filter. The render is authoritative and can disagree — a paper the
    source calls single-column may render two-column — so the cells that
    actually hold 12 documents are only known once the manifest is frozen.
    This reads the frozen manifest, finds the real deficits, and pulls more
    candidates for those cells. Run freeze again afterwards; repeat until
    every cell is full, since topped-up documents can themselves land
    elsewhere."""

    man = MANIFEST
    if not man.exists():
        print("[topup] no frozen manifest — run `corpus.py freeze` first")
        return
    docs = json.loads(man.read_text())["documents"]
    have = collections.Counter(d["cell"] for d in docs)
    deficits = {k: t - have.get(k, 0) for k, t in TARGET.items()
                if have.get(k, 0) < t}
    if not deficits:
        print("[topup] every cell is full after render verification")
        return
    print(f"[topup] render-verified deficits: {deficits}")

    bank = load()
    on_disk = {d["name"] for d in docs}
    plan = json.loads(PLAN.read_text()) if PLAN.exists() else {}
    planned = {i["arxiv_id"] for items in plan.values() for i in items}
    rng = random.Random(SEED + args.round)

    picked = []
    for cell, short in deficits.items():
        pool = [dict(v, arxiv_id=k) for k, v in bank.items()
                if v.get("cell") == cell and k not in planned]
        rng.shuffle(pool)
        # over-pull: some will land in a different cell once rendered
        want = min(len(pool), short * args.overpull)
        picked += [(cell, p) for p in pool[:want]]
        print(f"   {cell:20s} short {short}, pulling {want} candidate(s)")
    if not picked:
        print("[topup] bank exhausted for the short cells — run `scan` again")
        return

    kept = 0
    for cell, it in picked:
        aid = it["arxiv_id"]
        safe = aid.replace("/", "_")
        d = _doc_dir(cell, safe)
        if (d / f"arxiv_{safe}.pdf").exists():
            continue
        try:
            tex = source_tex(aid)
            time.sleep(3)
            if not tex:
                continue
            d.mkdir(parents=True, exist_ok=True)
            (d / f"arxiv_{safe}.tex").write_text(tex, encoding="utf-8")
            (d / f"arxiv_{safe}.pdf").write_bytes(
                _get(f"https://arxiv.org/pdf/{aid}.pdf"))
            time.sleep(3)
            (d / "meta.json").write_text(json.dumps({**it, "cell": cell}, indent=2))
            plan.setdefault(cell, []).append(it)
            kept += 1
            print(f"  + {cell:20s} {aid}", flush=True)
        except Exception as e:
            print(f"  ! {aid}: {type(e).__name__}", flush=True)
    PLAN.write_text(json.dumps(plan, indent=2))
    print(f"\n[topup] fetched {kept}; re-run "
          f"`python3 tools/corpus.py freeze` to re-verify")


def main() -> None:
    ap = argparse.ArgumentParser(
        prog="corpus", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn, help_ in (
            ("status", cmd_status, "where every cell stands"),
            ("scan", cmd_scan, "sweep arXiv for the cells that are short"),
            ("select", cmd_select, "seeded, category-balanced pick of the corpus"),
            ("download", cmd_download, "fetch PDFs and LaTeX sources"),
            ("freeze", cmd_freeze, "hash, render-verify, write the manifest"),
            ("topup", cmd_topup, "refill cells the render verification moved")):
        s = sub.add_parser(name, help=help_)
        s.add_argument("--after", default="2026-01-01",
                       help="submission date gate (memorisation control)")
        s.add_argument("--per-category", type=int, default=30)
        s.add_argument("--budget", type=int, default=1200,
                       help="max papers to scan this run")
        s.add_argument("--overpull", type=int, default=3,
                       help="candidates to pull per missing document")
        s.add_argument("--round", type=int, default=0,
                       help="reseed across topup rounds")
        s.add_argument("--refreeze", action="store_true",
                       help="rebuild the corpus from the plan instead of "
                            "re-verifying the frozen one (changes results)")
        s.set_defaults(fn=fn)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
