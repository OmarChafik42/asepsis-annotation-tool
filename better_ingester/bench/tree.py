"""
bench/tree.py — the shared heading tree, title normalisation, and scoring.

The whole benchmark compares two trees: the LaTeX ground truth and a recovered
tree from some ingestion path.  A tree is just nested Nodes; depth IS the level
(no stored integers — that bit us before).  The root is the document title.

Scoring is deliberately small and interpretable, on *relative* structure:
  - title_f1        : are the right headings present (position-independent)?
  - parent_child_f1 : are the right nestings present (structure + identity)?

Both use `normalise_title`, which folds away the two evaluation-schema artifacts
we learned the hard way: rendered section numbering ("I." / "A." / "1)") and
markdown emphasis ("**bold**"), neither of which is part of the author's heading.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field


@dataclass
class Node:
    title: str
    children: list["Node"] = field(default_factory=list)
    # Phase-3 additions (default to the old heading-only behaviour):
    kind: str = "heading"          # "heading" (internal) | "content" (leaf) | "asset"
    content: str = ""              # body text — content leaves only
    asset_type: str = ""           # "figure" | "table" — asset nodes only
    label: str = ""                # \label key — asset nodes (target of \ref)
    refs: list[str] = field(default_factory=list)  # content leaves: \label keys referenced

    def all_nodes(self) -> list["Node"]:
        out = [self]
        for c in self.children:
            out.extend(c.all_nodes())
        return out

    def content_leaves(self) -> list["Node"]:
        return [n for n in self.all_nodes() if n.kind == "content"]


def normalize_to_leaves(node: "Node") -> "Node":
    """Enforce: content lives only in leaves.  Any node that has children *and*
    its own content gets that content pushed into a synthetic leaf child (titled
    after the node), so internal nodes are pure structure and every piece of text
    is addressable as a leaf.  Mutates and returns the tree."""
    for c in node.children:
        normalize_to_leaves(c)
    if node.children:                              # internal node → structure only
        if node.content.strip() or node.refs:
            node.children.insert(0, Node(
                title=node.title, kind="content",
                content=node.content, refs=list(node.refs)))
        node.content, node.refs, node.kind = "", [], "heading"
    elif node.content.strip() or node.refs:        # leaf with text → content leaf
        node.kind = "content"
    return node


def build_tree(root_title: str, headings: list[str],
               levels: list[int]) -> Node:
    """An ordered (heading, level) list -> a tree, nested by relative level.

    Used for any condition whose output is a flat list with depths attached:
    a model's reconstruction, or the ladder's leveled headings. Levels are
    relative, so a reply that starts at level 3 still yields a top-level
    child rather than three phantom ancestors."""
    root = Node(title=root_title)
    stack: list[tuple[int, Node]] = [(0, root)]
    for title, level in zip(headings, levels):
        node = Node(title=str(title))
        lvl = max(1, int(level))
        while stack and stack[-1][0] >= lvl:
            stack.pop()
        (stack[-1] if stack else (0, root))[1].children.append(node)
        stack.append((lvl, node))
    return root


# ---------------------------------------------------------------------------
# Title normalisation (evaluation-schema fixes)
# ---------------------------------------------------------------------------

_MD_EMPHASIS = re.compile(r"[*`]+")
# Fold Unicode punctuation variants to ASCII so a heading isn't counted as both a
# miss and a false positive purely because an OCR/LLM emitted a smart quote
# ("Google's" vs "Google's") — an evaluation-schema artifact, not a content
# difference.
_PUNCT_FOLD = str.maketrans({
    "’": "'", "‘": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", "‐": "-", " ": " ",
})
# Appendix sections render with an auto letter ("A PEEU Prompt", "B AHC057 …")
# while the LaTeX truth is just "PEEU Prompt".  Strip a leading single capital
# letter followed by a CAPITAL or digit (so the appendix marker goes) — but never
# when the next char is lowercase, so a real "A problem"/"An overview" survives.
# Runs on the original-case string, before lower-casing.
_APPENDIX_PREFIX = re.compile(r"^[A-Z]\s+(?=[A-Z0-9])")
# IEEE-style compound bookmark prefixes from embedded PDF outlines: "II Datacenter
# architecture", "I-A Related research", "III-B2 Details".  Multi-char roman
# (optionally dash-joined sub-tokens), followed by a capitalised/digit word —
# the same next-word guard as the appendix rule, so "I am legend" survives.
# Runs on the original-case string, before lower-casing.
_OUTLINE_PREFIX = re.compile(r"^[IVXLCDM]{2,7}(?:-[A-Z][0-9]*)*\s+(?=[A-Z0-9])"
                             r"|^[IVXLCDM]{1,7}(?:-[A-Z][0-9]*)+\s+(?=[A-Z0-9])")
# leading rendered numbering. Digit numbering needs no trailing separator
# ("1 Introduction", "1.1 Background"); letter/roman numbering requires a "." or
# ")" so a real article like "A problem" is never stripped.  Letter-dotted-digit
# compounds ("A.1 Data") are appendix subsections and are stripped.
_ENUM_PREFIX = re.compile(
    r"^(?:\d+(?:\.\d+)*[.)]?|[ivxlcdm]+[.)]|[a-z][.)]|[a-z]\.\d+(?:\.\d+)*[.)]?)\s+")


def normalise_title(text: str) -> str:
    """Canonical form for comparing headings across LaTeX vs recovered markdown."""
    text = text.translate(_PUNCT_FOLD).strip()
    text = _OUTLINE_PREFIX.sub("", text)
    text = _APPENDIX_PREFIX.sub("", text)
    text = _MD_EMPHASIS.sub("", text.lower())
    text = " ".join(text.split())
    text = _ENUM_PREFIX.sub("", text)
    return text.strip(" .,:;-–—#")


# Rendered caption label ("Figure 1.", "Table 2:", "Fig. 3") — present in OCR'd
# captions but NOT in the LaTeX \caption{} source; strip it so the two compare.
_CAPTION_LABEL = re.compile(
    r"^\s*(?:figure|fig\.?|table|tab\.?|algorithm|alg\.?)\s*\d*[a-z]?\s*[.:)–-]?\s*",
    re.I)


def normalise_caption(text: str) -> str:
    return normalise_title(_CAPTION_LABEL.sub("", text))


# ---------------------------------------------------------------------------
# Edge / node extraction
# ---------------------------------------------------------------------------

def section_titles(root: Node) -> list[str]:
    """Normalised titles of every node except the root, in pre-order."""
    return [normalise_title(n.title) for n in root.all_nodes()[1:]]


def parent_child_edges(root: Node) -> Counter:
    """Multiset of (parent_title, child_title) normalised pairs."""
    edges: Counter = Counter()

    def walk(n: Node) -> None:
        for c in n.children:
            edges[(normalise_title(n.title), normalise_title(c.title))] += 1
            walk(c)

    walk(root)
    return edges


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def _prf(truth: Counter, recovered: Counter) -> tuple[float, float, float]:
    overlap = sum((truth & recovered).values())
    nt, nr = sum(truth.values()), sum(recovered.values())
    precision = overlap / nr if nr else (1.0 if nt == 0 else 0.0)
    recall    = overlap / nt if nt else (1.0 if nr == 0 else 0.0)
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    return precision, recall, f1


@dataclass
class Score:
    title_p: float
    title_r: float
    title_f1: float
    edge_p: float
    edge_r: float
    edge_f1: float
    n_truth: int
    n_recovered: int

    def row(self) -> dict[str, float | int]:
        return {
            "title_p": round(self.title_p, 3), "title_r": round(self.title_r, 3),
            "title_f1": round(self.title_f1, 3),
            "edge_p": round(self.edge_p, 3), "edge_r": round(self.edge_r, 3),
            "edge_f1": round(self.edge_f1, 3),
            "n_truth": self.n_truth, "n_recovered": self.n_recovered,
        }


def score(truth: Node, recovered: Node) -> Score:
    """Compare a recovered tree against the truth tree."""
    t_titles = Counter(section_titles(truth))
    r_titles = Counter(section_titles(recovered))
    tp, tr, tf = _prf(t_titles, r_titles)

    ep, er, ef = _prf(parent_child_edges(truth), parent_child_edges(recovered))

    return Score(
        title_p=tp, title_r=tr, title_f1=tf,
        edge_p=ep, edge_r=er, edge_f1=ef,
        n_truth=len(truth.all_nodes()) - 1,
        n_recovered=len(recovered.all_nodes()) - 1,
    )


# ---------------------------------------------------------------------------
# Asset detection scoring (Phase 3a) — match by normalised caption
# ---------------------------------------------------------------------------

@dataclass
class AssetScore:
    precision: float
    recall: float
    f1: float
    type_acc: float                 # of matched assets, fraction with correct figure/table
    n_truth: int
    n_recovered: int
    matched: list[str]
    missed: list[str]               # in truth, not recovered
    extra: list[str]                # recovered, not in truth (false positives)


def _cap_words(s: str) -> set[str]:
    return {w for w in s.split() if len(w) >= 3}


def _overlap_coeff(a: set[str], b: set[str]) -> float:
    return len(a & b) / min(len(a), len(b)) if a and b else 0.0


@dataclass
class ContentScore:
    leaf_match: float       # fraction of GT content leaves with a same-title recovered leaf
    content_f1: float       # mean content-word F1 over MATCHED leaves (text fidelity)
    content_f2: float       # the same, weighting recall higher (sec:metrics)
    overall: float          # mean over ALL GT leaves (missed leaf scores 0)
    n_gt: int
    n_rec: int
    n_matched: int


def score_content(gt_root: Node, rec_root: Node) -> ContentScore:
    """Body-text fidelity per leaf: match leaves by heading title, compare their
    text by content-word F1.  Catches assembly errors (mis-anchored / bled
    content), not just characters.  GT text is LaTeX-cleaned and recovered text is
    the rendered text layer, so math/symbols differ — hence overlap, not exact."""
    from bench.metrics import content_words          # one definition, shared

    def by_title(root: Node) -> dict[str, str]:
        d: dict[str, str] = {}
        for leaf in root.content_leaves():
            k = normalise_title(leaf.title)
            d[k] = (d.get(k, "") + " " + leaf.content).strip()
        return d

    g, r = by_title(gt_root), by_title(rec_root)
    f1s: list[float] = []
    f2s: list[float] = []
    overall: list[float] = []
    matched = 0
    for title, gtext in g.items():
        gw = content_words(gtext)
        if title in r:
            matched += 1
            rw = content_words(r[title])
            inter = len(gw & rw)
            p = inter / len(rw) if rw else 0.0
            rec = inter / len(gw) if gw else 0.0
            f1 = (2 * p * rec / (p + rec)) if (p + rec) else 0.0
            f1s.append(f1)
            f2s.append((5 * p * rec / (4 * p + rec)) if (4 * p + rec) else 0.0)
            overall.append(f1)
        else:
            overall.append(0.0)
    return ContentScore(
        leaf_match=(matched / len(g) if g else 1.0),
        content_f1=(sum(f1s) / len(f1s) if f1s else 0.0),
        content_f2=(sum(f2s) / len(f2s) if f2s else 0.0),
        overall=(sum(overall) / len(overall) if overall else 1.0),
        n_gt=len(g), n_rec=len(r), n_matched=matched,
    )


def score_assets(truth: list[Node], recovered: list[Node],
                 thresh: float = 0.6) -> AssetScore:
    """Detection score over asset captions, matched by content-word **overlap**
    rather than exact text — GT captions lose inline math/\\ref/macros that the
    OCR'd caption keeps, so an exact match would punish the ruler, not the
    pipeline.  Greedy best-overlap assignment, each recovered caption used once."""
    T = [(normalise_caption(a.title), a) for a in truth if normalise_caption(a.title)]
    R = [(_cap_words(normalise_caption(a.title)), a) for a in recovered
         if normalise_caption(a.title)]
    used: set[int] = set()
    matched: list[str] = []
    type_ok = 0
    for cap, ta in T:
        tw = _cap_words(cap)
        best, best_j = -1, 0.0
        for i, (rw, _) in enumerate(R):
            if i in used:
                continue
            j = _overlap_coeff(tw, rw)
            if j > best_j:
                best, best_j = i, j
        if best >= 0 and best_j >= thresh:
            used.add(best)
            matched.append(cap)
            if ta.asset_type == R[best][1].asset_type:
                type_ok += 1
    nt, nr, m = len(T), len(R), len(matched)
    rec = m / nt if nt else (1.0 if not nr else 0.0)
    p = m / nr if nr else (1.0 if not nt else 0.0)
    f1 = (2 * p * rec / (p + rec)) if (p + rec) else 0.0
    extra = [" ".join(sorted(rw))[:60] for i, (rw, _) in enumerate(R) if i not in used]
    return AssetScore(
        precision=p, recall=rec, f1=f1,
        type_acc=(type_ok / m if m else 0.0),
        n_truth=nt, n_recovered=nr,
        matched=sorted(matched),
        missed=sorted(c for c, _ in T if c not in matched),
        extra=sorted(extra),
    )
