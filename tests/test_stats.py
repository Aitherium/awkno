"""The counts the docs state come from the registry, and cannot drift from it.

Measured 2026-11-20: the published page advertised "36 tools ... 9 stacks, 18 laws"
while the registry held 97 bricks (71 public) and 29 stacks. Nothing compared the
two, so nothing could fail — the same defect the prune comment in generate.py
records for pages. These tests are the comparison.
"""
import json
import re
from pathlib import Path

import yaml

PKG = Path(__file__).resolve().parents[1]
MONOREPO = PKG.parents[2]
STATS = PKG / "awkno" / "pages" / "_stats.json"


def _expected():
    eco = yaml.safe_load((MONOREPO / "AitherOS" / "config" / "ecosystem.yaml")
                         .read_text(encoding="utf-8"))
    bricks = eco.get("bricks") or []
    return {
        "bricks": sum(1 for b in bricks if str(b.get("status") or "public") == "public"),
        "bricks_declared": len(bricks),
        "planned": sum(1 for b in bricks if b.get("status") == "planned"),
        "stacks": len(eco.get("stacks") or []),
    }


def test_committed_stats_match_the_registry():
    assert STATS.is_file(), "run python awkno/generate.py"
    got = json.loads(STATS.read_text(encoding="utf-8"))
    for key, want in _expected().items():
        assert got[key] == want, f"{key}: _stats.json says {got[key]}, registry says {want}"


def test_both_docs_state_the_same_numbers():
    got = json.loads(STATS.read_text(encoding="utf-8"))
    want = f"{got['bricks']} bricks · {got['stacks']} stacks · {got['laws']} laws"
    for doc in (PKG / "README.md", PKG / "docs" / "index.html"):
        text = doc.read_text(encoding="utf-8")
        blocks = re.findall(r"<!-- awkno:stats -->(.*?)<!-- /awkno:stats -->", text, re.S)
        assert blocks, f"{doc.name}: no generated stats block"
        assert want in blocks, f"{doc.name} states {blocks[0]!r}, expected {want!r}"


def test_every_listed_brick_exists_and_none_is_stale():
    text = (PKG / "README.md").read_text(encoding="utf-8")
    block = re.search(r"<!-- awkno:bricks -->(.*?)<!-- /awkno:bricks -->", text, re.S)
    assert block and block.group(1).strip(), "the bricks block was never filled"
    listed = set(re.findall(r"^- \*\*(.+?)\*\*", block.group(1), re.M))
    assert len(listed) == json.loads(STATS.read_text(encoding="utf-8"))["bricks"]
    for topic in listed:
        assert (PKG / "awkno" / "pages" / f"{topic.lower()}.json").is_file(), topic


def test_no_hand_typed_count_survives():
    for doc in (PKG / "README.md", PKG / "docs" / "index.html"):
        text = doc.read_text(encoding="utf-8")
        assert not re.search(r"\(\d+ (tools|collections|principles)\)", text), \
            f"{doc.name} still carries a hand-typed count"


def test_the_world_page_lists_owned_zones_and_public_surfaces():
    # Owner 2026-11-20: "does it include ... our domains/urls, index, a30.link?"
    # It did not. The page is generated from domains.json, tunnel-routes.yaml and
    # pages-cnames.yaml -- never typed -- and a demo mirror is left out.
    page = json.loads((PKG / "awkno" / "pages" / "world.json").read_text(encoding="utf-8"))
    body = page["body"]
    for zone in ("aitherium.com", "a30.link", "openaw.org"):
        assert zone in body, zone
    assert "https://index.aitherium.com" in body
    assert "demo." not in body
    assert "- https://" in body
