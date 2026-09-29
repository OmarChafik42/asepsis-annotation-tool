"""
bench/latex.py — LaTeX source → ground-truth heading tree.

Levels are RELATIVE: whichever sectioning commands actually appear are ranked
in canonical order (part < chapter < section < subsection < …), so a document
that only uses \\section/\\subsection is two levels deep regardless of absolute
LaTeX semantics.  \\printbibliography / \\bibliography count as a References
section.  The root node is the \\title (or the file stem).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .tree import Node, normalise_title, normalize_to_leaves

# Block-level sectioning only.  \paragraph / \subparagraph are deliberately
# excluded: they render *run-in* (inline, not a separate heading block), so they
# have no visual heading representation for any layout/OCR method to detect, and
# counting them would penalise every condition for the undetectable.
_COMMAND_ORDER = ["part", "chapter", "section", "subsection", "subsubsection"]

_HEADING_RE = re.compile(
    r"\\(part|chapter|section|subsection|subsubsection)\*?\s*\{")
_PRINTBIB_RE = re.compile(r"\\printbibliography\b|\\bibliography\s*\{[^}]*\}")
_COMMENT_RE = re.compile(r"(?<!\\)%[^\n]*")


# ---------------------------------------------------------------------------
# Minimal LaTeX → text (for heading/title strings)
# ---------------------------------------------------------------------------

_WRAP = re.compile(r"\\(?:textbf|emph|textit|texttt|textsc|textrm|textsf|text|mbox)\s*\{")
_DROP_ARG = re.compile(r"\\(?:cite[a-z]*|ref|label|footnote|index)\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}")
_MATH = re.compile(r"\$[^$]*\$")
_CMD = re.compile(r"\\[a-zA-Z]+\*?")


def _extract_braced(s: str, open_pos: int) -> tuple[str, int]:
    """(content, end) for the {...} whose '{' is at open_pos (handles nesting)."""
    depth = 0
    for i in range(open_pos, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[open_pos + 1:i], i + 1
    return s[open_pos + 1:], len(s)


def clean_latex(s: str) -> str:
    """Strip LaTeX markup from a short string (heading/title) → reading text."""
    s = _COMMENT_RE.sub("", s)
    s = s.replace(r"\textbackslash", "\x00").replace(r"\&", "&").replace(r"\%", "%")
    s = s.replace(r"\_", "_").replace(r"\#", "#").replace(r"\{", "(").replace(r"\}", ")")
    s = _DROP_ARG.sub("", s)
    s = _MATH.sub("", s)
    # expand wrap commands (\textbf{x} → x), innermost-first
    prev = None
    while prev != s:
        prev = s
        m = _WRAP.search(s)
        if m:
            inner, end = _extract_braced(s, m.end() - 1)
            s = s[:m.start()] + inner + s[end:]
    s = _CMD.sub("", s)
    s = s.replace("{", "").replace("}", "").replace("\x00", "\\")
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------------------
# Parse
# ---------------------------------------------------------------------------

def _find_title(tex: str) -> str | None:
    m = re.search(r"\\title\s*\{", tex)
    if not m:
        return None
    content, _ = _extract_braced(tex, m.end() - 1)
    return clean_latex(content) or None


def _body(tex: str) -> str:
    m = re.search(r"\\begin\s*\{document\}", tex)
    if not m:
        return tex
    start = m.end()
    m2 = re.search(r"\\end\s*\{document\}", tex[start:])
    return tex[start: start + m2.start()] if m2 else tex[start:]


@dataclass
class Heading:
    """One sectioning event in the source.

    `start` is where the command begins and `body_start` where its argument
    ends — i.e. where the section's own prose begins, which is what the
    content-carrying parse needs and the heading-only parse ignores."""
    start: int
    body_start: int
    level: int
    title: str


def _headings(body: str) -> list[Heading]:
    """Every sectioning event in document order, with RELATIVE levels.

    Whichever sectioning commands actually appear are ranked in canonical
    order, so a paper using only \\section/\\subsection is two levels deep
    regardless of what those commands mean in some other document. This is
    the single heading walk: both `parse_latex` (structure only) and
    `parse_doc` (structure + text + assets) are built on it, so the ruler
    cannot disagree with itself about what a heading is."""
    used = {m.group(1) for m in _HEADING_RE.finditer(body)}
    level_of = {c: i + 1 for i, c in
                enumerate(c for c in _COMMAND_ORDER if c in used)}
    bib_level = level_of.get("section", 1)

    out: list[Heading] = []
    for m in _HEADING_RE.finditer(body):
        content, end = _extract_braced(body, m.end() - 1)
        out.append(Heading(m.start(), end, level_of[m.group(1)],
                           clean_latex(content)))
    for m in _PRINTBIB_RE.finditer(body):
        out.append(Heading(m.start(), m.end(), bib_level, "References"))

    out.sort(key=lambda h: h.start)
    return out


def _nest(root: Node, nodes: list[tuple[int, Node]]) -> Node:
    """Attach (level, node) pairs under `root` by relative depth.

    The one place the ruler turns a flat level sequence into a tree. Depth in
    the resulting tree IS the level — no integer is stored on a node, because
    storing it once bit us with the two drifting apart."""
    stack: list[tuple[int, Node]] = [(0, root)]
    for level, node in nodes:
        while stack and stack[-1][0] >= level:
            stack.pop()
        (stack[-1] if stack else (0, root))[1].children.append(node)
        stack.append((level, node))
    return root


def parse_latex(tex_path: Path) -> Node:
    """Parse a .tex file into the ground-truth heading tree.

    The abstract is included as a first-level node when the document declares
    one. It is not a sectioning command, so a purely syntactic reading would
    omit it — but it renders as a headed block, a PDF-side pipeline can and
    should detect it, and for a retrieval tree it is a node worth routing to.
    Recording it here keeps the heading tree consistent with `parse_doc`, which
    carries the abstract's text as a leaf."""
    tex = tex_path.read_text(encoding="utf-8")
    title = _find_title(tex) or tex_path.stem
    body = _body(_COMMENT_RE.sub("", tex))
    root = _nest(Node(title=title),
                 [(h.level, Node(title=h.title))
                  for h in _headings(body) if h.title])
    if _abstract_of(body):
        root.children.insert(0, Node(title="Abstract"))
    return root


# ---------------------------------------------------------------------------
# Phase 3 — asset-aware document ground truth
# ---------------------------------------------------------------------------

_ASSET_ENV_RE = re.compile(r"\\begin\{(figure|table)\*?\}(.*?)\\end\{\1\*?\}", re.S)
_CAPTION_RE = re.compile(r"\\caption(?:of\{[^}]*\})?\s*\{")
_LABEL_RE = re.compile(r"\\label\s*\{([^}]*)\}")
# \ref / \cref / \autoref / \eqref … → the label(s) of what a leaf points at
_REF_RE = re.compile(r"\\(?:auto|eq|v|labelc|c|C)?ref\*?\s*\{([^}]*)\}")
# strip a float env + its body from prose content (so a section's text excludes its figures)
_FLOAT_BLOCK_RE = re.compile(r"\\begin\{(figure|table)\*?\}.*?\\end\{\1\*?\}", re.S)


@dataclass
class DocGT:
    """Normalised ground truth: a content-at-leaves tree + the asset inventory."""
    tree: Node
    assets: list[Node] = field(default_factory=list)

    def reachability(self) -> set[tuple[str, str]]:
        """{(normalised leaf title, asset label)} — a content leaf is linked to an
        asset iff its text contains a \\ref to that asset's \\label."""
        asset_labels = {a.label for a in self.assets if a.label}
        out: set[tuple[str, str]] = set()
        for leaf in self.tree.content_leaves():
            for r in leaf.refs:
                if r in asset_labels:
                    out.add((normalise_title(leaf.title), r))
        return out

    def asset_numbers(self) -> dict[str, tuple[str, int]]:
        """label → (type, rendered number).  Figures/tables are numbered 1,2,… in
        source order, which is the rendered "Figure N" the prose cites."""
        count = {"figure": 0, "table": 0}
        nums: dict[str, tuple[str, int]] = {}
        for a in self.assets:
            count[a.asset_type] += 1
            nums[a.label] = (a.asset_type, count[a.asset_type])
        return nums

    def reach_keys(self) -> set[tuple[str, str, int]]:
        """Reachability as (heading, type, number) — the key shared with the
        recovered side, which can only cite assets by their rendered number."""
        nums = self.asset_numbers()
        return {(leaf, *nums[label]) for leaf, label in self.reachability()
                if label in nums}


# \begin{abstract}...\end{abstract}, or the \abstract{...} command form.
_ABSTRACT_ENV = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.S)
_ABSTRACT_CMD = re.compile(r"\\abstract\s*\{", re.S)


def _abstract_of(body: str) -> str:
    """The abstract as the author declared it, or '' if there is none."""
    m = _ABSTRACT_ENV.search(body)
    if m:
        return _clean_body(m.group(1))
    m = _ABSTRACT_CMD.search(body)
    if m:
        inner, _ = _extract_braced(body, m.end() - 1)
        return _clean_body(inner)
    return ""


def _refs_in(span: str) -> list[str]:
    out: list[str] = []
    for m in _REF_RE.finditer(span):
        out += [x.strip() for x in m.group(1).split(",") if x.strip()]
    return out


def _clean_body(span: str) -> str:
    """Light prose cleaner for a section's body text (floats/refs/math/commands out)."""
    s = _FLOAT_BLOCK_RE.sub(" ", span)
    s = _REF_RE.sub(" ", s)
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", s)   # \cmd[..]{..}
    s = s.replace("{", " ").replace("}", " ")
    return re.sub(r"\s+", " ", s).strip()


def _parse_assets(body: str) -> tuple[list[Node], dict[str, Node]]:
    assets: list[Node] = []
    count = {"figure": 0, "table": 0}
    for m in _ASSET_ENV_RE.finditer(body):
        env, inner = m.group(1), m.group(2)
        cap = ""
        cm = _CAPTION_RE.search(inner)
        if cm:
            cap, _ = _extract_braced(inner, cm.end() - 1)
            cap = clean_latex(cap)
        lm = _LABEL_RE.search(inner)
        count[env] += 1
        label = lm.group(1).strip() if lm else f"__{env}{count[env]}"
        assets.append(Node(title=cap, kind="asset", asset_type=env,
                           label=label))
    return assets, {a.label: a for a in assets}


def parse_doc(tex_path: Path) -> DocGT:
    """Full GT: content-at-leaves tree (with per-leaf \\ref labels) + assets."""
    tex = _COMMENT_RE.sub("", tex_path.read_text(encoding="utf-8"))
    title = _find_title(tex_path.read_text(encoding="utf-8")) or tex_path.stem
    body = _body(tex)
    assets, _ = _parse_assets(body)

    events = _headings(body)

    root = Node(title=title)
    if not events:                          # no sections at all → whole doc is one leaf
        root.content, root.refs = _clean_body(body), _refs_in(body)
    else:
        # Pre-section frontmatter is dropped — title block, authors,
        # affiliations, template boilerplate — with ONE exception. The abstract
        # is body content, not metadata: for a retrieval substrate it is often
        # the single most valuable passage in the paper, and the author declares
        # it explicitly, so the source states it as unambiguously as it states a
        # section. Dropping it here would make its absence from a pipeline's
        # output undetectable, because the ruler would share the omission.
        abs_text = _abstract_of(body)
        if abs_text:
            root.children.append(Node(title="Abstract", content=abs_text,
                                      refs=_refs_in(abs_text)))

    nodes: list[tuple[int, Node]] = []
    for i, h in enumerate(events):
        end = events[i + 1].start if i + 1 < len(events) else len(body)
        span = body[h.body_start:end]
        nodes.append((h.level, Node(title=h.title, content=_clean_body(span),
                                    refs=_refs_in(span))))
    _nest(root, nodes)

    normalize_to_leaves(root)
    return DocGT(tree=root, assets=assets)
