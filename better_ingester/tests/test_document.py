# Run: python3 -m pytest tests/test_document.py -v
"""The content-at-leaves tree and its markdown rendering."""
from __future__ import annotations

from bench.tree import Node
from ingest.document import build_content_tree, to_markdown
from ingest.ocr import Block
from tests.corpus_paths import a_corpus_pdf


def _block(label, text="", page=0, bbox=(0, 0, 10, 10)):
    return Block(label=label, text=text, page=page, bbox=bbox)


class TestDegenerateDocuments:
    """A document with no headings at all is one leaf in ground truth, so the
    recovered side must not drop its body as frontmatter."""

    def test_unheaded_content_anchors_to_root(self, monkeypatch):
        monkeypatch.setattr("ingest.text.block_text",
                            lambda b, tp, ph, s=2.0: "memo body text")
        tree = build_content_tree([_block("text")], "Memo",
                                  pdf_path=a_corpus_pdf(), levels=[])
        assert tree.kind == "content"
        assert "memo body text" in tree.content

    def test_headed_doc_still_drops_pre_heading_frontmatter(self, monkeypatch):
        # Regression guard: the unheaded fix must not disable the frontmatter
        # drop for headed documents (title blocks, author bands).
        monkeypatch.setattr("ingest.text.block_text",
                            lambda b, tp, ph, s=2.0: "some text")
        blocks = [_block("text", bbox=(0, 0, 10, 5)),
                  _block("paragraph_title", "1 Intro", bbox=(0, 10, 10, 12)),
                  _block("text", bbox=(0, 20, 10, 30))]
        tree = build_content_tree(blocks, "Doc", pdf_path=a_corpus_pdf(),
                                  levels=[1])
        leaves = tree.content_leaves()
        assert len(leaves) == 1 and leaves[0].title == "1 Intro"


class TestLevellingIsTheCallersJob:
    def test_missing_levels_is_an_error_not_a_guess(self):
        # build_content_tree used to level headings itself, which meant depth
        # was decided in two places. It now refuses rather than guessing.
        import pytest
        with pytest.raises(ValueError):
            build_content_tree([_block("paragraph_title", "1 A")], "Doc",
                               pdf_path=a_corpus_pdf(), levels=None)

    def test_wrong_length_is_rejected(self):
        import pytest
        with pytest.raises(ValueError):
            build_content_tree([_block("paragraph_title", "1 A")], "Doc",
                               pdf_path=a_corpus_pdf(), levels=[1, 2])

    def test_none_level_demotes_a_heading_to_body_text(self, monkeypatch):
        # How a validated outline disowns a pseudo-heading.
        monkeypatch.setattr("ingest.text.block_text",
                            lambda b, tp, ph, s=2.0: "prose")
        blocks = [_block("paragraph_title", "1 Real", bbox=(0, 0, 10, 2)),
                  _block("paragraph_title", "Contributions.", bbox=(0, 5, 10, 7))]
        tree = build_content_tree(blocks, "Doc", pdf_path=a_corpus_pdf(),
                                  levels=[1, None])
        assert [c.title for c in tree.children] == ["1 Real"]


class TestMarkdown:
    def test_emits_root_content_leaf(self):
        root = Node(title="Memo", kind="content", content="the whole body")
        assert "the whole body" in to_markdown(root)

    def test_nesting_becomes_heading_depth(self):
        root = Node("Doc", [Node("A", [Node("A1", kind="content",
                                            content="text")])])
        md = to_markdown(root)
        assert "## A" in md and "### A1" in md

    def test_artificial_leaf_emits_no_repeated_heading(self):
        # A leaf titled after its parent is the leaf-normalisation artifact,
        # not a heading the author wrote.
        root = Node("Doc", [Node("A", [
            Node("A", kind="content", content="intro prose"),
            Node("A1", kind="content", content="sub prose")])])
        md = to_markdown(root)
        assert md.count("A\n") >= 1 and "intro prose" in md
        assert "### A\n" not in md

    def test_unplaced_assets_reach_the_leftover_section(self):
        # A single-asset document has no headings and no reachability links;
        # the sentinel key must route crops to the trailing section.
        md = to_markdown(Node(title="Sheet"),
                         {"\x00unplaced": ["![figure 1](assets/figure_1.png)"]})
        assert "Figures and Tables" in md and "figure_1.png" in md
