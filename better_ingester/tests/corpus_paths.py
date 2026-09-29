"""Locate corpus documents for tests, without encoding the corpus layout.

Tests must use documents the repository actually ships. The frozen manifest
names those, so it is the lookup of record: the retired pilot set is not
tracked, and a test anchored to it passes here and fails on a fresh clone.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_CORPUS = _ROOT / "corpus"
_MANIFEST = _ROOT / "corpus_manifest.json"


def doc_path(name: str, suffix: str = ".pdf") -> str:
    """corpus/<name>/<name><suffix>, at either nesting depth."""
    direct = _CORPUS / name / f"{name}{suffix}"
    if direct.exists():
        return str(direct)
    if _CORPUS.exists():
        for group in sorted(p for p in _CORPUS.iterdir() if p.is_dir()):
            cand = group / name / f"{name}{suffix}"
            if cand.exists():
                return str(cand)
    return str(direct)          # let the caller fail with a clear path


@lru_cache(maxsize=1)
def frozen_names() -> list[str]:
    if not _MANIFEST.exists():
        return []
    return [d["name"] for d in json.loads(_MANIFEST.read_text())["documents"]]


@lru_cache(maxsize=1)
def a_corpus_pdf() -> str:
    """Any tracked corpus PDF — for tests that need a real file to open but
    do not care which document it is."""
    for name in frozen_names():
        p = doc_path(name, ".pdf")
        if Path(p).exists():
            return p
    raise RuntimeError("no frozen corpus document found on disk")
