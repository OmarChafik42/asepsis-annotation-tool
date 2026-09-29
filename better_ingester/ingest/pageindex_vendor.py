"""
ingest/pageindex_vendor.py — drive the REAL vendored PageIndex
(vendor/pageindex, commit in vendor/pageindex/PINNED_COMMIT) through our
cached, rate-limited LLM transport.

Two jobs:

1. PDF baseline (report-card PAGEINDEX columns): `pdf_to_pageindex_structure`
   runs the verbatim `page_index()` recipe — PyPDF2 page text,
   <physical_index_N> markers, TOC detect/extract/align prompts, chunked
   no-TOC fallback — with the LLM swapped for the configured local-proxy
   model.  Nothing of PageIndex's logic is reimplemented; only the transport
   (`llm_completion` / `llm_acompletion`) is replaced, so calls are cached by
   (model, messages) at temperature 0 and rate-limited like every other
   column.

2. Deliverable 3 (our ingestion → PageIndex): `md_to_pageindex_structure`
   feeds our pipeline's markdown to the vendored `md_to_tree`, yielding
   PageIndex's own {title, node_id, nodes, ...} JSON tree; `attach_page_anchors`
   then adds PDF-style physical_index fields from our layout blocks (the md
   path has no page concept — line_num only — but our blocks know pages).
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from bench.tree import Node, normalise_title

_ROOT = Path(__file__).resolve().parents[1]
_VENDOR = _ROOT / "vendor" / "pageindex"

# set when the transport raises DailyQuotaExhausted inside vendor code that
# might swallow exceptions (thread pools / gather): callers re-check this.
QUOTA_ABORT: list[BaseException] = []

# ── Gemma-dialect accommodations (transport-level, logged deviations) ─────────
# The vendored prompts are verbatim; these adapt the MODEL, not the recipe.
# 1. Gemma 4 opens <thought> blocks and, on the long PageIndex prompts, reasons
#    until the output budget dies before any JSON appears.  Every other column
#    in this repo appends the same suppression line; without it the verbatim
#    prompts are unanswerable for this family (probe 2026-07-09: 14.9k chars of
#    thought, finish=length, zero JSON).  Replies also get <thought> stripped —
#    the vendor's extract_json has no concept of them.
THINK_SUFFIX = ("\n\nCRITICAL: Keep your thinking process inside "
                "<thought>...</thought> tags extremely short and brief (under "
                "5 sentences), then output the final answer.")
_THOUGHT_RE = None  # compiled lazily

# 2. AI Studio's Gemma serving 500s instantly on the vendored 20 000-token page
#    groups (probe: 9 pages ≈ 10k tokens → HTTP 500 in 0-1 s; 4 pages fine).
#    page_list_to_group_text's max_tokens is re-defaulted to this — the same
#    knob the vendor exposes, sized for the serving stack.
GROUP_MAX_TOKENS = 4000


def _vendor_modules():
    if str(_VENDOR) not in sys.path:
        sys.path.insert(0, str(_VENDOR))
    import importlib
    # NB: pageindex/__init__.py re-exports a function named `page_index`,
    # shadowing the submodule as a package attribute — go via sys.modules.
    importlib.import_module("pageindex.page_index")
    importlib.import_module("pageindex.page_index_md")
    importlib.import_module("pageindex.utils")
    return (sys.modules["pageindex.utils"],
            sys.modules["pageindex.page_index"],
            sys.modules["pageindex.page_index_md"])


_installed = False


def install_transport(chat_fn=None) -> None:
    """Replace the vendored llm_completion/llm_acompletion (litellm) with
    `chat_fn(model, messages) -> (content, finish_reason)`.  Defaults to
    bench.transport.api_chat (cached, rate-limited, quota-aborting).  Patched in
    every vendor module namespace (they `from .utils import *`)."""
    global _installed
    pi_utils, pi_pdf, pi_md = _vendor_modules()

    if chat_fn is None:
        from bench.transport import api_chat as _api_chat

        def chat_fn(model, messages):
            r = _api_chat(model, messages, bucket=model)
            if r is None:
                raise RuntimeError(
                    f"LLM transport returned nothing for model {model!r} "
                    "(missing key / persistent failure)")
            return r

    import re
    thought_re = re.compile(r"<thought>.*?(</thought>|$)", re.S)

    def llm_completion(model, prompt, chat_history=None,
                       return_finish_reason=False):
        messages = (list(chat_history) if chat_history else []) + [
            {"role": "user", "content": prompt + THINK_SUFFIX}]
        try:
            content, finish = chat_fn(model, messages)
        except BaseException as e:                       # noqa: record + re-raise
            if type(e).__name__ == "DailyQuotaExhausted":
                QUOTA_ABORT.append(e)
            raise
        content = thought_re.sub("", content or "").strip()
        if return_finish_reason:
            return content, ("max_output_reached" if finish == "length"
                             else "finished")
        return content

    async def llm_acompletion(model, prompt):
        return await asyncio.to_thread(llm_completion, model, prompt)

    # serving-stack-sized page groups (see GROUP_MAX_TOKENS above)
    orig_group = pi_pdf.page_list_to_group_text
    while hasattr(orig_group, "__wrapped_orig__"):       # idempotent re-install
        orig_group = orig_group.__wrapped_orig__

    def grouped(page_contents, token_lengths,
                max_tokens=GROUP_MAX_TOKENS, overlap_page=1):
        return orig_group(page_contents, token_lengths,
                          max_tokens=max_tokens, overlap_page=overlap_page)
    grouped.__wrapped_orig__ = orig_group
    pi_pdf.page_list_to_group_text = grouped

    for mod in (pi_utils, pi_pdf, pi_md):
        mod.llm_completion = llm_completion
        mod.llm_acompletion = llm_acompletion
    _installed = True


def reraise_quota_abort() -> None:
    """Vendor code runs calls in thread pools / gathers that can swallow our
    DailyQuotaExhausted; call this after a vendor invocation to surface it."""
    if QUOTA_ABORT:
        exc = QUOTA_ABORT[-1]
        QUOTA_ABORT.clear()
        raise exc


# ── 1 · PDF path: the real PageIndex as a report-card column ─────────────────

def pdf_to_pageindex_structure(pdf: Path | str, model: str,
                               add_node_text: str = "no") -> dict:
    """Verbatim `page_index()` on a PDF with the given model; summaries and
    doc description off (structure benchmark; also 10× fewer calls)."""
    install_transport()
    _, pi_pdf, _ = _vendor_modules()
    try:
        result = pi_pdf.page_index(
            str(pdf), model=model,
            if_add_node_id="yes", if_add_node_summary="no",
            if_add_doc_description="no", if_add_node_text=add_node_text)
    finally:
        reraise_quota_abort()
    return result


def structure_to_node(structure: list | dict, root_title: str = "") -> Node:
    """PageIndex structure JSON → bench Node tree for scoring.

    If the whole document is wrapped in a single top node whose title matches
    the document title, its children are lifted to the root — the GT tree
    keeps the title on the root, not as a section (same relative-nesting
    convention every other column uses via build_tree)."""
    if isinstance(structure, dict):
        structure = structure.get("structure", structure.get("nodes", []))

    def conv(d: dict) -> Node:
        n = Node(title=str(d.get("title", "")))
        n.children = [conv(c) for c in d.get("nodes") or []]
        text = d.get("text") or ""
        if text and not n.children:
            n.kind, n.content = "content", text
        return n

    root = Node(title=root_title)
    kids = [conv(d) for d in structure]
    if (len(kids) == 1 and root_title and kids[0].children
            and normalise_title(kids[0].title) == normalise_title(root_title)):
        kids = kids[0].children
    root.children = kids
    return root


# ── 2 · Deliverable 3: our markdown → PageIndex's own tree format ────────────

def md_to_pageindex_structure(md_path: Path | str, *, model: str | None = None,
                              add_summaries: bool = False,
                              add_node_text: str = "yes",
                              summary_token_threshold: int = 200) -> dict:
    """Vendored `md_to_tree` on a markdown file (ours or anyone's): returns
    PageIndex's {doc_name, structure: [{title, node_id, line_num, ...}]}.
    Summaries need `model` and cost LLM calls; off by default."""
    if add_summaries:
        install_transport()
    _, _, pi_md = _vendor_modules()
    try:
        return asyncio.run(pi_md.md_to_tree(
            str(md_path),
            if_add_node_summary="yes" if add_summaries else "no",
            summary_token_threshold=summary_token_threshold,
            model=model,
            if_add_node_text=add_node_text,
            if_add_node_id="yes"))
    finally:
        reraise_quota_abort()


def heading_pages_from_blocks(blocks) -> list[tuple[str, int]]:
    """(normalised heading, 1-based page) in reading order, from our layout
    blocks — the page source for attach_page_anchors."""
    out = []
    for b in blocks:
        if b.label in ("doc_title", "paragraph_title") and b.text.strip():
            out.append((normalise_title(b.text), int(b.page) + 1))
    return out


def attach_page_anchors(structure: list[dict],
                        heading_pages: list[tuple[str, int]]) -> list[dict]:
    """Add PDF-style `physical_index` to an md-path tree in place.

    Nodes are visited in document (pre-)order and matched against the ordered
    heading/page list; each match consumes the queue up to that heading, so
    repeated titles resolve by position, not just name."""
    queue = list(heading_pages)

    def walk(nodes: list[dict]) -> None:
        for d in nodes:
            t = normalise_title(str(d.get("title", "")))
            for i, (ht, pg) in enumerate(queue):
                if ht == t:
                    d["physical_index"] = pg
                    del queue[:i + 1]
                    break
            walk(d.get("nodes") or [])

    walk(structure)
    return structure
