"""ingest/pageindex_vendor.py — converter, page anchors, transport shim, and
an end-to-end vendored md_to_tree run (no LLM: summaries off)."""
import json
from pathlib import Path

import pytest

from ingest.pageindex_vendor import (
    QUOTA_ABORT, attach_page_anchors, heading_pages_from_blocks,
    install_transport, md_to_pageindex_structure, structure_to_node,
    _vendor_modules)


# ── structure_to_node ─────────────────────────────────────────────────────────

def test_structure_to_node_nesting_and_content():
    structure = [
        {"title": "Introduction", "node_id": "0000"},
        {"title": "Methods", "node_id": "0001", "nodes": [
            {"title": "Data", "node_id": "0002", "text": "we use data"},
        ]},
    ]
    root = structure_to_node(structure, "My Paper")
    assert root.title == "My Paper"
    assert [c.title for c in root.children] == ["Introduction", "Methods"]
    leaf = root.children[1].children[0]
    assert leaf.title == "Data"
    assert leaf.kind == "content" and leaf.content == "we use data"


def test_structure_to_node_lifts_doc_title_wrapper():
    structure = [{"title": "My  Paper", "nodes": [
        {"title": "Introduction"}, {"title": "Conclusion"}]}]
    root = structure_to_node(structure, "My Paper")
    assert [c.title for c in root.children] == ["Introduction", "Conclusion"]


def test_structure_to_node_keeps_non_title_single_top():
    structure = [{"title": "Part I", "nodes": [{"title": "Introduction"}]}]
    root = structure_to_node(structure, "My Paper")
    assert [c.title for c in root.children] == ["Part I"]


def test_structure_to_node_accepts_result_dict():
    res = {"doc_name": "x", "structure": [{"title": "A"}]}
    root = structure_to_node(res, "x")
    assert [c.title for c in root.children] == ["A"]


# ── page anchors ──────────────────────────────────────────────────────────────

def test_attach_page_anchors_ordered_duplicates():
    structure = [
        {"title": "Setup", "nodes": []},
        {"title": "Results", "nodes": [{"title": "Setup"}]},   # repeated title
    ]
    pages = [("setup", 2), ("results", 5), ("setup", 6)]
    attach_page_anchors(structure, pages)
    assert structure[0]["physical_index"] == 2
    assert structure[1]["physical_index"] == 5
    assert structure[1]["nodes"][0]["physical_index"] == 6


def test_heading_pages_from_blocks_is_one_based():
    class B:
        def __init__(self, label, text, page):
            self.label, self.text, self.page = label, text, page
    blocks = [B("doc_title", "My Paper", 0), B("text", "body", 0),
              B("paragraph_title", "Introduction", 1)]
    assert heading_pages_from_blocks(blocks) == [
        ("my paper", 1), ("introduction", 2)]


# ── transport shim ────────────────────────────────────────────────────────────

def test_transport_shim_patches_vendor_and_maps_finish_reason():
    calls = []

    def fake_chat(model, messages):
        calls.append((model, messages))
        return "REPLY", "length"

    install_transport(fake_chat)
    pi_utils, pi_pdf, _ = _vendor_modules()
    out, finish = pi_utils.llm_completion(
        "test-model", "hello", return_finish_reason=True)
    assert (out, finish) == ("REPLY", "max_output_reached")
    assert pi_pdf.llm_completion is pi_utils.llm_completion
    assert calls[0][0] == "test-model"
    # Gemma-dialect: the thought-suppression suffix rides on every prompt
    from ingest.pageindex_vendor import THINK_SUFFIX
    assert calls[0][1] == [{"role": "user", "content": "hello" + THINK_SUFFIX}]


def test_transport_shim_strips_thought_blocks():
    def chatty(model, messages):
        return "<thought>musing at length</thought>\n[1, 2]", "stop"

    install_transport(chatty)
    pi_utils, _, _ = _vendor_modules()
    assert pi_utils.llm_completion("m", "p") == "[1, 2]"


def test_transport_shim_shrinks_page_groups_idempotently():
    install_transport(lambda m, ms: ("x", "stop"))
    _, pi_pdf, _ = _vendor_modules()
    g1 = pi_pdf.page_list_to_group_text
    install_transport(lambda m, ms: ("x", "stop"))     # second install
    g2 = pi_pdf.page_list_to_group_text
    assert g1.__wrapped_orig__ is g2.__wrapped_orig__  # no wrapper stacking
    # 3 pages of ~2000 tokens each must split under the 4000-token group cap
    groups = g2(["a " * 2000] * 3, [2000] * 3)
    assert len(groups) > 1


def test_transport_shim_records_quota_abort():
    class DailyQuotaExhausted(RuntimeError):
        pass

    def quota_chat(model, messages):
        raise DailyQuotaExhausted("quota")

    install_transport(quota_chat)
    pi_utils, _, _ = _vendor_modules()
    QUOTA_ABORT.clear()
    with pytest.raises(DailyQuotaExhausted):
        pi_utils.llm_completion("m", "p")
    assert len(QUOTA_ABORT) == 1
    QUOTA_ABORT.clear()


# ── deliverable 3: our md → vendored md_to_tree ──────────────────────────────

MD = """# My Paper

intro preamble

## Introduction

some text here

## Methods

### Data

data text

```python
# not a heading
```

## Conclusion

done
"""


def test_md_to_pageindex_structure_end_to_end(tmp_path):
    md = tmp_path / "doc.md"
    md.write_text(MD, encoding="utf-8")
    res = md_to_pageindex_structure(md)               # no summaries → no LLM
    assert res["doc_name"] == "doc"
    top = res["structure"]
    assert [n["title"] for n in top] == ["My Paper"]
    lvl2 = [n["title"] for n in top[0]["nodes"]]
    assert lvl2 == ["Introduction", "Methods", "Conclusion"]
    methods = top[0]["nodes"][1]
    assert [n["title"] for n in methods.get("nodes", [])] == ["Data"]
    # node ids present, fenced pseudo-heading ignored, text carried
    assert all("node_id" in n for n in top[0]["nodes"])
    assert "data text" in methods["nodes"][0]["text"]

    # page anchors compose on top
    attach_page_anchors(top, [("my paper", 1), ("introduction", 1),
                              ("methods", 2), ("data", 2), ("conclusion", 3)])
    assert top[0]["physical_index"] == 1
    assert methods["physical_index"] == 2
    assert methods["nodes"][0]["physical_index"] == 2
    assert json.dumps(top)                             # stays JSON-serialisable
