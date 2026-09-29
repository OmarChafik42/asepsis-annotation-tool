"""BetterIngest — the PageIndex-facing ingestion class (offline: cached OCR,
no LLM; the multimodal step is tested with a fake transport)."""

from tests.corpus_paths import doc_path
import json
from pathlib import Path

import pytest

from ingest.betteringest import Asset, BetterIngest, _ladder_levels

ROOT = Path(__file__).resolve().parents[1]
# A frozen-corpus document with many figures and a deep heading tree, so the
# asset and enrichment assertions below have something to bite on. It must be
# a document the repository actually ships: the retired pilot set is not
# tracked, and a fixture anchored there skips silently on a fresh clone.
DOC = "arxiv_2608.17312v1"
PDF = Path(doc_path(DOC, ".pdf"))

pytestmark = pytest.mark.skipif(not PDF.exists(), reason="corpus doc missing")


@pytest.fixture(scope="module")
def ingested(tmp_path_factory):
    bi = BetterIngest(out_dir=tmp_path_factory.mktemp("bi_out"))
    return bi.ingest(PDF)


def test_markdown_written_with_structure(ingested):
    assert Path(ingested.md_path).exists()
    lines = ingested.markdown.splitlines()
    assert lines[0].startswith("# ")                     # doc title H1
    assert any(l.startswith("## ") for l in lines)       # sections H2
    assert ingested.title and ingested.title != DOC


def test_assets_managed(ingested):
    assert len(ingested.assets) >= 10
    a = ingested.assets[0]
    assert a.asset_id and a.type in ("figure", "table")
    assert Path(a.image).exists()                        # crop saved
    assert a.page >= 1                                   # 1-based position
    assert a.caption
    ids = [x.asset_id for x in ingested.assets]
    assert len(ids) == len(set(ids))                     # stable unique ids
    assert any(a.sections for a in ingested.assets)      # reachability wired
    # markdown embeds the linked crops
    assert "![" in ingested.markdown


def test_to_pageindex_enriched(ingested):
    res = ingested.to_pageindex()                        # no LLM
    top = res["structure"]
    assert isinstance(top, list) and top

    flat: list[dict] = []

    def walk(nodes):
        for d in nodes:
            flat.append(d)
            walk(d.get("nodes") or [])
    walk(top)

    assert all("node_id" in d for d in flat)             # PageIndex schema
    assert any(d.get("physical_index") for d in flat)    # page anchors
    paras = [p for d in flat for p in d.get("paragraphs", [])]
    assert paras                                         # paragraph indexes
    idxs = [p["paragraph_index"] for p in paras]
    assert idxs == sorted(idxs) and len(idxs) == len(set(idxs))
    assert all("local_index" in p and p["text"] for p in paras)
    assert any(d.get("assets") for d in flat)            # assets attached
    assert res["assets"] and isinstance(res["unplaced_assets"], list)
    json.dumps(res)                                      # serialisable


def test_describe_assets_fake_transport(ingested):
    calls = []

    def fake_chat(messages):
        calls.append(messages)
        assert messages[0]["content"][1]["type"] == "image_url"
        return "<thought>hm</thought> A bar chart of daily power usage.", "stop"

    bi = BetterIngest()
    bi.describe_assets(ingested, model="fake", chat=fake_chat)
    assert all(a.description == "A bar chart of daily power usage."
               for a in ingested.assets)
    assert len(calls) == len(ingested.assets)
    # idempotent: described assets are not re-called
    bi.describe_assets(ingested, model="fake", chat=fake_chat)
    assert len(calls) == len(ingested.assets)


def test_ladder_levels_positional_and_outline():
    # rungs 1-5: positional
    diag = {"rung": 1, "headings": [("A", 1, "high", "induced"),
                                    ("B", 2, "high", "induced")]}
    assert _ladder_levels(diag, ["A", "B"]) == [1, 2]
    # rung 0: title-matched, order-consuming for duplicates
    diag = {"rung": 0, "headings": [("Setup", 1, "high", "outline"),
                                    ("Results", 1, "high", "outline"),
                                    ("Setup", 2, "high", "outline")]}
    assert _ladder_levels(diag, ["Setup", "Results", "Setup"]) == [1, 1, 2]
    # unmatched heading → no mapping, so the caller falls back to rung 0b
    assert _ladder_levels(diag, ["Nowhere"]) is None
