"""Private design-tree paths never reach a published page.

The site's deploy leak check refuses `.AITHEROS/` / `.AITHERIUM/` paths, and three pages
carrying them blocked every Veil deploy (2026-11-10).
"""
import json
from pathlib import Path

from awkno.generate import AwknoGenerator

PAGES = Path(__file__).resolve().parents[1] / "awkno" / "pages"


def _scrub(text: str) -> str:
    return AwknoGenerator.__new__(AwknoGenerator)._scrub_internal_refs(text)


def test_backticked_path_sentence_goes_and_the_rest_stays():
    out = _scrub("Packs are never baked in. Design and the map: `.AITHEROS/43-X.md`.")
    assert out == "Packs are never baked in."


def test_parenthetical_citation_goes_whole():
    out = _scrub("Named 2026-09-18 (plan.AITHEROS/39) because every member exists.")
    assert out == "Named 2026-09-18 because every member exists."


def test_bare_path_sentence_goes_without_a_stray_tail():
    out = _scrub("Settled in .AITHEROS/35-Y.md (Phase 4). Phasing follows.")
    assert out == "Phasing follows."


def test_other_lines_and_plain_text_are_untouched():
    assert _scrub("Nothing internal. Second.") == "Nothing internal. Second."
    out = _scrub("See .AITHERIUM/p/00.md for why.\nNext line stays.")
    assert out.strip() == "Next line stays."


def test_no_committed_page_carries_a_private_tree_path():
    bad = [p.name for p in sorted(PAGES.glob("*.json"))
           if ".AITHEROS/" in p.read_text(encoding="utf-8")
           or ".AITHERIUM/" in p.read_text(encoding="utf-8")]
    assert not bad, f"pages leak private design-tree paths: {bad}"
    assert any(PAGES.glob("*.json")), "no pages found -- the check would pass vacuously"
    json.loads((sorted(PAGES.glob("*.json"))[0]).read_text(encoding="utf-8"))
