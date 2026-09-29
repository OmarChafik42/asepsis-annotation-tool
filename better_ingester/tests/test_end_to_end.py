# Run: python3 -m pytest tests/test_end_to_end.py -v
"""One real document, all the way through: PDF -> pipeline -> scored row -> CSV.

Every other test file exercises one module against synthetic blocks. Nothing
checked that the pieces still compose on a real PDF, which is the failure a
refactor actually produces. These use the frozen corpus and the committed OCR
cache, so they are fast and need no models.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

from bench import conditions as C
from bench.report import CSV_COLUMNS, write_csv
from bench.score import score_unit
from tests.corpus_paths import doc_path, frozen_names

_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def ctx():
    """The first frozen-corpus document whose OCR blocks are already cached."""
    from ingest.ocr import OcrConfig, _cache_path
    for name in frozen_names():
        pdf = Path(doc_path(name, ".pdf"))
        tex = Path(doc_path(name, ".tex"))
        if not (pdf.exists() and tex.exists()):
            continue
        if _cache_path(pdf, OcrConfig(ocr_scale=C.OCR_SCALE),
                       _ROOT / ".ocr_cache").exists():
            return C.load_ctx(name, tex, pdf)
    pytest.skip("no frozen corpus document with cached OCR blocks")


class TestPipelineEndToEnd:
    def test_ours_produces_every_measure(self, ctx, tmp_path):
        row = score_unit("ours", ctx, tmp_path, {})
        # the eight measures of bench/score.py, all present on a real document
        for key in ("title_f1", "depth_acc", "edge_f1", "order_tau",
                    "asset_f1", "reach_f1", "content_f1", "coverage"):
            assert key in row, f"{key} missing from the OURS row"

    def test_coverage_decomposition_sums_to_one(self, ctx, tmp_path):
        # The property that makes `unaccounted` mean anything at all.
        row = score_unit("ours", ctx, tmp_path, {})
        total = sum(row[k] for k in
                    ("coverage", "excluded_rate", "asset_rate",
                     "furniture_rate", "unaccounted_rate"))
        assert total == pytest.approx(1.0, abs=0.005)

    def test_markdown_and_tree_agree_on_the_headings(self, ctx, tmp_path):
        from ingest.betteringest import BetterIngest
        doc = BetterIngest(out_dir=tmp_path).ingest(ctx.pdf)
        assert doc.markdown.startswith("#")
        assert Path(doc.md_path).exists()
        for heading in [n.title for n in doc.tree.all_nodes()[1:]
                        if n.kind == "heading"]:
            assert heading in doc.markdown

    def test_every_asset_has_a_crop_on_disk(self, ctx, tmp_path):
        from ingest.betteringest import BetterIngest
        doc = BetterIngest(out_dir=tmp_path).ingest(ctx.pdf)
        for a in doc.assets:
            assert Path(a.image).exists(), f"{a.asset_id} has no crop"
            assert a.type in ("figure", "table")
            assert a.page >= 1                     # 1-based, PageIndex convention

    def test_ladder_ablation_holds_detection_fixed(self, ctx, tmp_path):
        # The check the ablation rests on: each row differs from the one above
        # by exactly one stage, so detection must not move across them.
        rows = {c: score_unit(c, ctx, tmp_path, {})
                for c in ("ladder0", "ladder1", "ladder2")}
        detections = {r["title_f1"] for r in rows.values()}
        assert len(detections) == 1, f"detection moved across rungs: {rows}"

    def test_ceiling_bounds_content_recall(self, ctx, tmp_path):
        # A ceiling below the pipeline it bounds is ill-posed — two earlier
        # designs of this condition failed exactly that way.
        ours = score_unit("ours", ctx, tmp_path, {})
        ceiling = score_unit("ceiling", ctx, tmp_path, {})
        if ours.get("content_r") is not None:
            assert ceiling["floor_recall"] >= ours["content_r"] - 1e-9


class TestCsvContract:
    def test_row_fills_declared_columns_and_no_others(self, ctx, tmp_path):
        row = {**score_unit("ours", ctx, tmp_path, {}),
               "doc": ctx.name, "cond": "ours"}
        manifest = json.loads((_ROOT / "corpus_manifest.json").read_text())
        out = tmp_path / "results.csv"
        write_csv(out, [row], manifest, ["ours"])

        got = list(csv.DictReader(open(out)))
        assert len(got) == 1
        assert list(got[0]) == CSV_COLUMNS
        assert got[0]["doc"] == ctx.name
        assert got[0]["condition_label"] == "OURS"
        assert got[0]["tier"] == "0"
        assert got[0]["cell"]                       # covariates joined in

    def test_rows_sort_by_cell_then_document_then_registry_order(self, tmp_path):
        manifest = {"documents": [
            {"name": "b", "cell": "single_arabic"},
            {"name": "a", "cell": "two_roman"}]}
        rows = [{"doc": "a", "cond": "ceiling"}, {"doc": "a", "cond": "ours"},
                {"doc": "b", "cond": "ours"}]
        out = tmp_path / "r.csv"
        write_csv(out, rows, manifest, ["ours", "ceiling"])
        got = [(r["doc"], r["cond"]) for r in csv.DictReader(open(out))]
        assert got == [("b", "ours"), ("a", "ours"), ("a", "ceiling")]
