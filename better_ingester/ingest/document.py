"""
ingest/document.py — assemble headings + body text into the document tree,
and render it as markdown.

The invariant this module enforces is the one the whole project is built on:
**text lives only in leaves**. A section that has both subsections and its own
introductory prose has that prose pushed into its own leaf, so an internal
node is pure structure. That is what makes the tree a *segmentation* — the
property §sec:method-2 needs for two retrieval systems to be comparable at
all — and it mirrors how the LaTeX ruler builds ground truth, so the two are
comparable leaf for leaf.
"""

from __future__ import annotations

from bench.tree import Node, normalise_title, normalize_to_leaves
from ingest.ocr import Block
from ingest.order import SECTION_TITLE, reading_order
from ingest.text import PageText


def build_content_tree(blocks: list[Block], doc_title: str = "", pdf_path=None,
                       ocr_scale: float = 2.0,
                       levels: list[int | None] | None = None) -> Node:
    """Content-at-leaves tree: heading hierarchy with body text anchored under
    the deepest open heading, then normalised so content lives only in leaves.

    `levels` carries one entry per detected heading, in reading order — the
    seam that lets the escalation ladder's hierarchy drive the content
    partition. A None entry DEMOTES that heading to body text, which is how a
    validated outline disowns a pseudo-heading ('Abstract', a running head).
    Passing None for the whole list is not supported: the caller owns the
    levelling decision, so that it is made in one place.
    """
    ordered = reading_order(blocks)
    heads = [b for b in ordered if b.label == SECTION_TITLE]
    if levels is None:
        raise ValueError("levels is required — level the headings via the ladder")
    if len(levels) != len(heads):
        raise ValueError(f"levels: expected {len(heads)} entries, got {len(levels)}")
    level_of = {id(b): lv for b, lv in zip(heads, levels)}
    kept = [b for b in heads if level_of[id(b)] is not None]

    # Page-0 title/author band: column-aware order can sort a right-column
    # author block AFTER a left-column heading, bleeding it into that section.
    # Anything above the topmost heading on page 0 is frontmatter — drop it.
    first_page_heads = [b.bbox[1] for b in kept if b.page == 0]
    frontmatter_y = min(first_page_heads) if first_page_heads else -1.0

    pages = PageText(pdf_path, ocr_scale) if pdf_path else None

    def text_of(b: Block) -> str:
        return pages.of(b) if pages is not None else ""

    root = Node(title=doc_title)

    # The abstract is body content, not frontmatter. The layout detector gives
    # it its own label, so it can be kept precisely without readmitting the
    # title/author band around it. It becomes the document's first leaf,
    # mirroring how the LaTeX ruler records it — the symmetry that made the
    # abstract's omission visible to the metrics at all.
    abstract = [b for b in ordered if b.label == "abstract"]
    if abstract:
        text = " ".join(t for t in (text_of(b) for b in abstract) if t).strip()
        if text:
            root.children.append(Node(title="Abstract", kind="content",
                                      content=text))

    stack: list[tuple[int, Node]] = [(0, root)]
    for b in ordered:
        is_heading = b.label == SECTION_TITLE and level_of.get(id(b)) is not None
        if is_heading:
            node = Node(title=b.text)
            level = level_of[id(b)]
            while stack and stack[-1][0] >= level:
                stack.pop()
            (stack[-1] if stack else (0, root))[1].children.append(node)
            stack.append((level, node))
            continue
        # body text, plus any heading the levelling demoted to body text
        if not (b.label == "text" or (b.label == SECTION_TITLE and id(b) in level_of)):
            continue
        current = stack[-1][1]
        # Pre-first-heading text is frontmatter → drop, mirroring the ruler.
        # But a document with NO headings at all (a memo, a notice) is one
        # leaf in ground truth, so its text anchors to the root instead.
        if current is root and kept:
            continue
        if b.page == 0 and b.bbox[1] < frontmatter_y:      # title/author band
            continue
        text = text_of(b)
        if text:
            current.content = (current.content + " " + text).strip()

    normalize_to_leaves(root)
    _prune_empty(root)
    return root


def _prune_empty(node: Node) -> None:
    """Drop heading nodes left with no content and no children — e.g. an
    'Abstract' heading whose body was dropped as frontmatter."""
    for c in node.children:
        _prune_empty(c)
    node.children = [c for c in node.children
                     if c.kind == "content" or c.children or c.content.strip()]


def to_markdown(root: Node, assets_at: dict[str, list[str]] | None = None) -> str:
    """Render the content-at-leaves tree as markdown.

    Artificial leaves (title == parent, created by the leaf normalisation)
    emit their text with no heading of their own, so the markdown reads as the
    document does rather than repeating a heading. Asset links are placed
    under the sections that cite them, each once; anything cited nowhere goes
    to a trailing section rather than being dropped.
    """
    assets_at = assets_at or {}
    lines: list[str] = [f"# {root.title}\n"] if root.title else []
    placed: set[str] = set()

    # An unheaded document: the leaf normalisation turned the root itself into
    # the single content leaf, so there are no children to walk.
    if root.kind == "content" and root.content:
        lines.append(root.content + "\n")

    def emit(node: Node, depth: int) -> None:
        for c in node.children:
            hashes = "#" * min(depth, 6)
            if c.kind != "content":
                lines.append(f"{hashes} {c.title}\n")
                emit(c, depth + 1)
                continue
            if normalise_title(c.title) != normalise_title(node.title):
                lines.append(f"{hashes} {c.title}\n")
            if c.content:
                lines.append(c.content + "\n")
            for img in assets_at.get(normalise_title(c.title), []):
                if img not in placed:
                    lines.append(img + "\n")
                    placed.add(img)

    emit(root, 2)                                   # doc title is H1, sections H2
    leftover = [img for imgs in assets_at.values() for img in imgs
                if img not in placed]
    if leftover:
        lines.append("## Figures and Tables\n")
        lines += [img + "\n" for img in dict.fromkeys(leftover)]
    return "\n".join(lines)
