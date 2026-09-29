"""
tools/fetch_arxiv.py — build a REAL, un-memorizable benchmark corpus.

For each recent arXiv paper we download the published PDF *and* its LaTeX source
(flattening \\input/\\include into one file), so we get a real document with a
machine-readable ground-truth heading tree — no hand annotation.  Only papers
submitted AFTER a cutoff date are kept, so a model released before that date
cannot have memorised them: a win on these is real signal, not recall.

    python tools/fetch_arxiv.py --after 2026-05-01 --n 6 --category cs.LG

Politeness: sequential, with a delay between downloads, and a descriptive
User-Agent (arXiv asks for both).
"""

from __future__ import annotations

import argparse
import gzip
import io
import re
import sys
import tarfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

_API = "http://export.arxiv.org/api/query"
_UA = {"User-Agent": "structure-faithful-bench/0.1 (academic research; polite)"}
_CORPUS = Path("corpus")


def _get(url: str, timeout: int = 120) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=_UA), timeout=timeout) as r:
        return r.read()


def list_recent(category: str, after: str, want: int, scan: int) -> list[tuple[str, str, str]]:
    """[(arxiv_id, published_date, title)] submitted on/after `after` (YYYY-MM-DD)."""
    out: list[tuple[str, str, str]] = []
    start = 0
    while len(out) < scan and start < 400:
        q = urllib.parse.urlencode({
            "search_query": f"cat:{category}", "start": start, "max_results": 100,
            "sortBy": "submittedDate", "sortOrder": "descending"})
        xml = _get(f"{_API}?{q}", timeout=60).decode("utf-8", "ignore")
        entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
        if not entries:
            break
        for e in entries:
            idm = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", e)
            pub = re.search(r"<published>(\d{4}-\d{2}-\d{2})", e)
            ttl = re.search(r"<title>(.*?)</title>", e, re.S)
            if not (idm and pub):
                continue
            if pub.group(1) < after:                 # sorted desc → rest are older
                return out
            title = re.sub(r"\s+", " ", ttl.group(1)).strip() if ttl else ""
            out.append((idm.group(1).strip(), pub.group(1), title))
        start += 100
        time.sleep(3)
    return out


def _flatten(texs: dict[str, str]) -> str | None:
    """Inline \\input/\\include across a multi-file source into the main .tex."""
    main = next((c for c in texs.values()
                 if "\\documentclass" in c and "\\begin{document}" in c), None)
    if main is None:
        main = next((c for c in texs.values() if "\\begin{document}" in c), None)
    if main is None:
        return None

    by_base = {k.rsplit("/", 1)[-1]: v for k, v in texs.items()}

    def repl(m: re.Match) -> str:
        f = m.group(1).strip().lstrip("./")
        for cand in (f, f + ".tex"):
            if cand in texs:
                return texs[cand]
            if cand.rsplit("/", 1)[-1] in by_base:
                return by_base[cand.rsplit("/", 1)[-1]]
        return ""                                    # unknown include → drop

    out, prev = main, None
    for _ in range(12):
        if out == prev:
            break
        prev, out = out, re.sub(r"\\(?:input|include)\s*\{([^}]+)\}", repl, out)
    return out


def source_tex(arxiv_id: str) -> str | None:
    raw = _get(f"https://arxiv.org/e-print/{arxiv_id}")
    try:                                             # tar (.tar.gz / .tar)
        tf = tarfile.open(fileobj=io.BytesIO(raw), mode="r:*")
        texs = {m.name: tf.extractfile(m).read().decode("utf-8", "ignore")
                for m in tf.getmembers() if m.isfile() and m.name.endswith(".tex")}
        if texs:
            return _flatten(texs)
    except tarfile.TarError:
        pass
    for decoder in (lambda b: gzip.decompress(b), lambda b: b):  # single gz / plain
        try:
            s = decoder(raw).decode("utf-8", "ignore")
            if "\\documentclass" in s:
                return s
        except Exception:
            continue
    return None


def main() -> None:
    ap = argparse.ArgumentParser(prog="tools.fetch_arxiv")
    ap.add_argument("--after", required=True, help="keep papers submitted on/after YYYY-MM-DD")
    ap.add_argument("--n", type=int, default=6, help="how many usable papers to keep")
    ap.add_argument("--category", default="cs.LG")
    ap.add_argument("--max-pages", type=int, default=25, help="skip PDFs longer than this")
    ap.add_argument("--min-headings", type=int, default=4, help="skip docs with fewer truth headings")
    args = ap.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from bench.latex import parse_latex            # noqa: E402

    cand = list_recent(args.category, args.after, args.n, scan=max(args.n * 6, 40))
    print(f"[arxiv] {len(cand)} candidates submitted ≥ {args.after} in {args.category}")
    kept = 0
    for arxiv_id, pub, title in cand:
        if kept >= args.n:
            break
        safe = arxiv_id.replace("/", "_")
        d = _CORPUS / f"arxiv_{safe}"
        try:
            tex = source_tex(arxiv_id)
            time.sleep(3)
            if not tex or "\\begin{document}" not in tex:
                print(f"  - {arxiv_id}: no usable .tex source, skip"); continue
            d.mkdir(parents=True, exist_ok=True)
            tex_path = d / f"arxiv_{safe}.tex"
            tex_path.write_text(tex, encoding="utf-8")
            n_head = len(parse_latex(tex_path).all_nodes()) - 1
            if n_head < args.min_headings:
                print(f"  - {arxiv_id}: only {n_head} headings parsed, skip")
                tex_path.unlink(); d.rmdir(); continue
            pdf = _get(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
            time.sleep(3)
            (d / f"arxiv_{safe}.pdf").write_bytes(pdf)
            import pypdfium2 as pdfium               # noqa: E402
            pages = len(pdfium.PdfDocument(str(d / f"arxiv_{safe}.pdf")))
            if pages > args.max_pages:
                print(f"  - {arxiv_id}: {pages}pp > {args.max_pages}, skip")
                for f in d.iterdir():
                    f.unlink()
                d.rmdir(); continue
            import json                              # noqa: E402
            (d / "meta.json").write_text(json.dumps({
                "arxiv_id": arxiv_id, "category": args.category,
                "published": pub, "pages": pages, "headings": n_head,
                "title": title}, indent=2), encoding="utf-8")
            kept += 1
            print(f"  ✓ {arxiv_id}  {pub}  {pages}pp  {n_head} headings  | {title[:55]}")
        except Exception as ex:
            print(f"  ! {arxiv_id}: {type(ex).__name__}: {ex}")
            time.sleep(3)
    print(f"[arxiv] kept {kept} papers under corpus/")


if __name__ == "__main__":
    main()
