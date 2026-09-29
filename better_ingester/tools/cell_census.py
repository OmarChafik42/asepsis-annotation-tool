"""
tools/cell_census.py — prevalence census over arXiv layout x numbering cells.

Two jobs, one scan:

 1. EVIDENCE.  The corpus design drops two of the six layout x numbering cells
    (single-column roman/letter, two-column unnumbered) as too rare to
    populate.  "Too rare" is a claim about the world and needs a number
    attached, so this records EVERY paper it classifies — including ones it
    has no use for — and reports each cell's observed prevalence.  For a cell
    with zero observations the rule of three gives a 95% upper bound on its
    true prevalence of 3/N, which is the honest form of "we looked and did not
    find any".

 2. CANDIDATES.  Everything classified is banked, so the corpus builder can
    draw from the census instead of re-downloading sources.

The search is deliberately NOT a neutral sample.  A negative result is only
worth reporting if the search was aimed where the thing would be if it
existed, so the category list is weighted toward IEEEtran-heavy venues (where
a single-column roman paper would appear, via the onecolumn option) and toward
physics/maths venues using two-column REVTeX with starred sections (where a
two-column unnumbered paper would appear).

    python3 tools/cell_census.py --after 2026-06-01 --per-category 40
    python3 tools/cell_census.py --report        # pooled over every run so far

Re-runnable and cumulative: papers already seen are skipped, so repeated runs
grow N rather than repeating work.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.fetch_arxiv import list_recent, source_tex  # noqa: E402
from tools.corpus import CENSUS, classify, load, save   # noqa: E402


# Weighted toward where the two rare cells would live if they existed:
#   eess.SP / cs.IT / cs.NI / eess.SY  -> IEEEtran country (single-col roman)
#   astro-ph / cond-mat / quant-ph     -> REVTeX two-column (two-col unnumbered)
CATEGORIES = ["cs.LG", "math.NA", "q-bio.PE", "econ.GN", "eess.SP", "cs.IT",
              "cs.NI", "eess.SY", "astro-ph.GA", "cond-mat.stat-mech",
              "quant-ph", "stat.ME", "cs.CV", "cs.RO", "math.PR"]

ALL_CELLS = [("single", "arabic"), ("single", "roman"), ("single", "unnumbered"),
             ("two", "arabic"), ("two", "roman"), ("two", "unnumbered")]





def cmd_scan(args) -> None:
    seen = load()
    added = 0
    for cat in args.categories:
        try:
            cands = list_recent(cat, args.after, args.per_category,
                                scan=args.per_category * 3)
        except Exception as e:
            print(f"  ! {cat}: {type(e).__name__}: {e}", flush=True)
            continue
        print(f"[{cat}] {len(cands)} candidates since {args.after}", flush=True)
        n_cat = 0
        for aid, pub, title in cands:
            if n_cat >= args.per_category:
                break
            if aid in seen:
                continue
            try:
                tex = source_tex(aid)
                time.sleep(3)
            except Exception:
                continue
            if not tex or "\\begin{document}" not in tex:
                seen[aid] = {"cell": None, "reason": "no usable source",
                             "category": cat, "published": pub}
                continue
            col, num, cls = classify(tex)
            seen[aid] = {"cell": f"{col}_{num}", "columns": col,
                         "numbering": num, "documentclass": cls,
                         "category": cat, "published": pub,
                         "title": title[:80]}
            added += 1
            n_cat += 1
            if (col, num) in (("single", "roman"), ("two", "unnumbered")):
                print(f"   *** RARE CELL HIT: {aid} [{col}/{num}] {cls}",
                      flush=True)
            if added % 10 == 0:
                save(seen)
                print(f"   … {added} new, {len(seen)} total", flush=True)
    save(seen)
    print(f"[census] +{added} this run, {len(seen)} papers total")
    cmd_report(args)


def cmd_report(args) -> None:
    seen = load()
    usable = {k: v for k, v in seen.items() if v.get("cell")}
    n = len(usable)
    counts = Counter(v["cell"] for v in usable.values())
    print(f"\n[census] N = {n} papers with usable LaTeX source, "
          f"{len(seen) - n} unusable")
    print(f"  categories: {len(set(v['category'] for v in seen.values()))}\n")
    print("  cell                 n     prevalence   95% CI")
    print("  " + "-" * 55)
    for col, num in ALL_CELLS:
        cell = f"{col}_{num}"
        k = counts.get(cell, 0)
        if n == 0:
            continue
        p = k / n
        if k == 0:
            # rule of three: 0/n observed -> 95% upper bound 3/n
            ci = f"[0, {3 / n:.4f}]  (rule of three)"
        else:
            se = (p * (1 - p) / n) ** 0.5
            ci = f"[{max(0, p - 1.96 * se):.4f}, {min(1, p + 1.96 * se):.4f}]"
        print(f"  {cell:20s} {k:3d}   {p:8.4f}   {ci}")
    print()
    for cell in ("single_roman", "two_unnumbered"):
        k = counts.get(cell, 0)
        if k == 0 and n:
            print(f"  {cell}: 0 of {n}. At the 95% upper bound of {3/n:.4f}, "
                  f"populating a 15-document cell would require screening "
                  f"~{int(15 / (3 / n)):,} papers.")


def main() -> None:
    ap = argparse.ArgumentParser(prog="cell_census")
    ap.add_argument("--after", default="2026-06-01")
    ap.add_argument("--per-category", type=int, default=40)
    ap.add_argument("--categories", nargs="*", default=CATEGORIES)
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()
    cmd_report(args) if args.report else cmd_scan(args)


if __name__ == "__main__":
    main()
