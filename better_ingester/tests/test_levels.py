# Run: python3 -m pytest tests/test_levels.py -v
# The ladder's leveling core: marker-schema induction (rung 1'), typography
# calibration (rung 2), the confidence gate (rung 3), and the outline gate
# (rung 0).  Cases mirror the executable failure probes F1-F4 — each was a
# confirmed failure of the old closed-grammar heuristic.
from __future__ import annotations

from ingest.levels import (Leveled, calibrate_typography, classify_marker,
                           gate, induce_levels)
from ingest.outline import OutlineEntry, validate_outline
from ingest.ocr import Block


def levels_of(heads):
    return [l.level for l in induce_levels(heads)]


class TestOpenVocabulary:
    def test_word_prefixes_classify(self):                      # F1
        for h in ["Section 3: Hand Hygiene", "Chapter 2 Prevention",
                  "Annex B Cleaning", "Appendix C Details", "Step 1: Assess"]:
            assert classify_marker(h) is not None, h

    def test_letterdotted_classifies(self):                     # F1
        m = classify_marker("A.1 Data Collection")
        assert m is not None and m.kind == "letterdotted"

    def test_lowercase_paren(self):                             # F1
        assert classify_marker("a) Hand washing").kind == "paren_alpha"
        assert classify_marker("(i) Scope").kind == "paren_roman"


class TestInducedMapping:
    def test_lettered_top_level_doc(self):                      # F2
        assert levels_of(["A. Scope", "B. Definitions", "C. Requirements"]) == [1, 1, 1]

    def test_paren_top_level_doc(self):                         # F2
        assert levels_of(["1) Purpose", "2) Scope", "3) Responsibilities"]) == [1, 1, 1]

    def test_mixed_mode_keeps_numbered_levels(self):            # F3
        got = levels_of(["1 Introduction", "Background", "2 Methods",
                         "Participants", "3 Results"])
        assert got == [1, None, 1, None, 1]

    def test_ieee_mapping_is_induced(self):
        got = levels_of(["I. Introduction", "II. Related Work", "A. Edge",
                         "B. Sched", "III. Methodology", "A. Problem",
                         "1) Detail", "2) More", "B. Sub", "IV. Experiments",
                         "V. Conclusion"])
        assert got == [1, 1, 2, 2, 1, 2, 3, 3, 2, 1, 1]

    def test_roman_after_letter_gap(self):                      # F4
        got = levels_of(["I. Intro", "A. Setup", "B. Data", "C. Models",
                         "D. Eval", "V. Results"])
        assert got == [1, 2, 2, 2, 2, 1]

    def test_dotted_unchanged(self):
        assert levels_of(["1 Intro", "1.1 Sub", "1.2.3 Deep", "2 Next"]) == [1, 2, 3, 1]

    def test_guideline_grammar(self):                           # F1+F2 combined
        got = levels_of(["Section 1: Scope", "Section 2: Hand Hygiene",
                         "Annex A Cleaning", "A.1 Surfaces", "A.2 Devices"])
        assert got == [1, 1, 1, 2, 2]


class TestTypographyCalibration:
    def test_unnumbered_cluster_adopts_numbered_level(self):    # F3 completion
        leveled = [Leveled("1 Intro", 1, "high", "dotted"),
                   Leveled("Background", None, "none", "unnumbered"),
                   Leveled("1.1 Setup", 2, "high", "dotted")]
        sigs = [(14.0, 700), (12.0, 700), (12.0, 700)]
        out = calibrate_typography(leveled, sigs)
        assert out[1].level == 2 and out[1].signal == "typography"

    def test_fully_unnumbered_ranked_by_cluster(self):
        leveled = [Leveled(t, None, "none", "unnumbered") for t in "ABCD"]
        sigs = [(14.0, 700), (12.0, 700), (12.0, 700), (14.0, 700)]
        assert [l.level for l in calibrate_typography(leveled, sigs)] == [1, 2, 2, 1]

    def test_same_size_bold_flat_not_fabricated(self):          # F11 honest floor
        leveled = [Leveled(t, None, "none", "unnumbered") for t in "ABC"]
        sigs = [(12.0, 700)] * 3
        assert [l.level for l in calibrate_typography(leveled, sigs)] == [1, 1, 1]


class TestGate:
    def test_high_confidence_ships(self):
        ok, share = gate([Leveled("x", 1, "high", "dotted")] * 5)
        assert ok and share == 1.0

    def test_low_confidence_escalates(self):
        ok, _ = gate([Leveled("x", 1, "low", "typography")] * 5)
        assert not ok


def _tb(label, text, page=0):
    return Block(label=label, text=text, page=page, bbox=(0, 0, 10, 10))


class TestOutlineGate:
    BLOCKS = [_tb("paragraph_title", "1 Introduction"),
              _tb("paragraph_title", "2 Methods", 1),
              _tb("paragraph_title", "3 Results", 2)]

    def test_faithful_outline_full_trust(self):
        entries = [OutlineEntry("Introduction", 0, 0),
                   OutlineEntry("Methods", 0, 1),
                   OutlineEntry("Results", 0, 2)]
        v = validate_outline(entries, self.BLOCKS)
        assert v.verdict in ("full", "titles_only") and v.match_rate == 1.0

    def test_service_entries_pruned_not_fatal(self):            # O3
        entries = [OutlineEntry("Abstract", 0, 0),
                   OutlineEntry("Introduction", 0, 0),
                   OutlineEntry("Methods", 0, 1),
                   OutlineEntry("Results", 0, 2)]
        v = validate_outline(entries, self.BLOCKS)
        assert v.verdict != "reject"
        assert all(e.title != "Abstract" for e in v.entries)

    def test_page_anchor_garbage_rejected(self):                # O8
        entries = [OutlineEntry(f"Page {i}", 0, i) for i in range(6)]
        assert validate_outline(entries, self.BLOCKS).verdict == "reject"

    def test_absent_rejected(self):                             # O1
        assert validate_outline([], self.BLOCKS).verdict == "reject"

    def test_unmatched_entries_pruned(self):                    # O5
        entries = [OutlineEntry("Introduction", 0, 0),
                   OutlineEntry("Methods", 0, 1),
                   OutlineEntry("Results", 0, 2),
                   OutlineEntry("Some run-in paragraph", 1, 1)]
        v = validate_outline(entries, self.BLOCKS)
        assert v.verdict != "reject" and len(v.entries) == 3


# ── rung 0b: the outline gap fill (closed numbering grammar) ────────────────
#
# These pin the leveller that fires when rung 0 accepts an outline that does
# not name every detected heading. It is a closed grammar on purpose — see
# ingest/levels.py's header for why it is kept alongside induce_levels.

from ingest.levels import assign_levels


class TestGapFillDottedArabic:
    def test_levels(self):
        assert assign_levels(
            ["1 Intro", "1.1 Sub", "1.2.3 Deep", "2 Next"]) == [1, 2, 3, 1]


class TestGapFillIEEE:
    def test_ieeetran_titlecase_sections(self):
        # IEEEtran renders sections in Title Case, so the capitalisation
        # signal is gone: single I and V must still read as sections, resolved
        # by the roman sequence rather than by case.
        heads = ["I. Introduction", "II. Related Work", "A. Edge", "B. Sched",
                 "III. Methodology", "A. Problem", "IV. Experiments",
                 "V. Conclusion"]
        assert assign_levels(heads) == [1, 1, 2, 2, 1, 2, 1, 1]

    def test_roman_valued_letters_are_subsections(self):
        # C and D are valid roman numerals but here continue the letter run
        heads = ["I. Intro", "A. a", "B. b", "C. c", "D. d", "II. Next"]
        assert assign_levels(heads) == [1, 2, 2, 2, 2, 1]

    def test_paren_subsubsection(self):
        heads = ["III. Sec", "A. Sub", "1) one", "2) two", "B. Sub2"]
        assert assign_levels(heads) == [1, 2, 3, 3, 2]


class TestGapFillUnnumbered:
    def test_flat_no_signal(self):
        assert assign_levels(["Preface", "Body", "End"]) == [1, 1, 1]

    def test_font_ranking_when_unnumbered(self):
        heads = ["Foundations", "Type Systems", "Monads", "Maybe"]
        assert assign_levels(heads, [14.5, 12.0, 12.0, 11.0]) == [1, 2, 2, 3]

    def test_uniform_font_is_flat(self):
        assert assign_levels(["A", "B", "C"], [12.0, 12.0, 12.0]) == [1, 1, 1]

    def test_numbering_beats_font(self):
        # font size inverts on IEEE small caps, so a numbered document must
        # never reach the font branch
        assert assign_levels(["1 A", "1.1 B", "2 C"],
                             [10.0, 20.0, 10.0]) == [1, 2, 1]
