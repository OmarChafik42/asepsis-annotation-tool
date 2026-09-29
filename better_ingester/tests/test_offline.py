# Run: python3 -m pytest tests/test_offline.py -v
"""The offline model conditions: reply salvage and the prompt/reply store."""
from __future__ import annotations

import pytest

from bench import offline
from bench.conditions import baseline_prompt, parse_headings, refine_prompt
from bench.offline import clean_llm_json


@pytest.fixture
def store(tmp_path, monkeypatch):
    monkeypatch.setattr(offline, "LLM_DIR", tmp_path)
    monkeypatch.setattr(offline, "MODELS_PATH", tmp_path / "models.json")
    return offline


# ── salvaging JSON out of a chat reply ─────────────────────────────────────

class TestCleanLlmJson:
    def test_dict_with_array_value_returns_the_whole_dict(self):
        # The regression this function exists for: returning the nested array
        # instead of the dict silently broke every reply of this shape.
        assert clean_llm_json('{"headings": [1, 2]}') == '{"headings": [1, 2]}'

    def test_bare_array_reply(self):
        assert clean_llm_json("[1, 2, 3]") == "[1, 2, 3]"

    def test_prose_around_the_answer_is_dropped(self):
        raw = 'Sure! Here it is:\n{"headings": []}\nLet me know if that helps.'
        assert clean_llm_json(raw) == '{"headings": []}'

    def test_code_fences_are_stripped(self):
        assert clean_llm_json('```json\n{"a": 1}\n```') == '{"a": 1}'

    def test_reasoning_blocks_are_stripped(self):
        assert clean_llm_json(
            '<thinking>{"wrong": 1}</thinking>{"right": 2}') == '{"right": 2}'

    def test_answer_last_wins(self):
        assert clean_llm_json('{"draft": 1} then {"final": 2}') == '{"final": 2}'

    def test_no_json_falls_back_to_stripped_text(self):
        assert clean_llm_json("  I cannot do that.  ") == "I cannot do that."


# ── reply shapes different models actually return ──────────────────────────

class TestParseHeadings:
    def test_canonical_shape(self):
        h, l = parse_headings('{"headings":[{"title":"A","level":1},'
                              '{"title":"B","level":2}]}')
        assert h == ["A", "B"] and l == [1, 2]

    def test_nested_children_are_flattened_with_depth(self):
        h, l = parse_headings(
            '{"sections":[{"title":"A","children":[{"title":"A1"}]}]}')
        assert h == ["A", "A1"] and l == [1, 2]

    def test_bare_list_of_strings(self):
        h, l = parse_headings('["A", "B"]')
        assert h == ["A", "B"] and l == [1, 1]

    def test_garbage_returns_empty_rather_than_raising(self):
        assert parse_headings("not json at all") == ([], [])

    def test_levels_are_floored_at_one(self):
        _, l = parse_headings('{"headings":[{"title":"A","level":0}]}')
        assert l == [1]


# ── the prompt/reply store ─────────────────────────────────────────────────

class TestStore:
    def test_missing_reply_reads_as_none(self, store):
        assert store.read_reply("base_small", "doc1") is None

    def test_roundtrip(self, store):
        store.write_prompt("base_small", "doc1", "PROMPT")
        assert store.prompt_path("base_small", "doc1").read_text() == "PROMPT"
        store.reply_path("base_small", "doc1").write_text('{"headings":[]}')
        assert store.read_reply("base_small", "doc1") == '{"headings":[]}'

    def test_empty_reply_counts_as_unanswered(self, store):
        store.write_prompt("base_small", "doc1", "P")
        store.reply_path("base_small", "doc1").write_text("   \n")
        assert store.read_reply("base_small", "doc1") is None

    def test_model_is_recorded_per_condition(self, store):
        store.record_model("base_small", "some-small-model")
        store.record_model("base_big", "some-big-model")
        assert store.models() == {"base_small": "some-small-model",
                                  "base_big": "some-big-model"}

    def test_status_counts_prompts_and_replies(self, store):
        store.write_prompt("base_small", "d1", "P")
        store.write_prompt("base_small", "d2", "P")
        store.reply_path("base_small", "d1").write_text("{}")
        st = store.status(["base_small"], ["d1", "d2"])["base_small"]
        assert st == {"prompts": 2, "replies": 1, "documents": 2, "model": None}


# ── the prompts themselves ─────────────────────────────────────────────────

class TestPrompts:
    def test_baseline_prompt_carries_the_document_and_asks_for_json(self):
        p = baseline_prompt("# flat markdown text")
        assert "flat markdown text" in p and '"headings"' in p

    def test_baseline_prompt_does_not_leak_the_answer(self):
        # It must not hint at the metric, the corpus, or how many headings to
        # expect — any of which would make the baseline easier than the one a
        # real deployment runs.
        p = baseline_prompt("x").lower()
        for leak in ("f1", "ground truth", "latex", "arxiv", "score"):
            assert leak not in p

    def test_refine_prompt_invites_additions_not_only_deletions(self):
        # A prompt that only invited deletions would decide REFINE's answer in
        # advance.
        p = refine_prompt([("A", 1)], "body").lower()
        assert "missed" in p and "wrong nesting level" in p

    def test_refine_prompt_truncates_the_document(self):
        from bench.conditions import REFINE_TEXT_CHARS
        p = refine_prompt([("A", 1)], "@" * (REFINE_TEXT_CHARS * 3))
        assert p.count("@") == REFINE_TEXT_CHARS
