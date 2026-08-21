"""Tests for awkno."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from awkno import AwknoPage, AwknoRegistry, NotFoundError


class TestAwknoPage:
    """Test AwknoPage rendering."""

    def test_page_creation(self):
        """Test creating a page."""
        page = AwknoPage(
            topic="test",
            category="brick",
            synopsis="A test brick",
            description="This is a test",
            adopt="Adopt by testing",
            status="test",
        )

        assert page.topic == "test"
        assert page.category == "brick"
        assert page.synopsis == "A test brick"

    def test_page_render_plain(self):
        """Test rendering with --plain flag."""
        page = AwknoPage(
            topic="test",
            category="brick",
            synopsis="A test brick",
            description="This is a test",
        )

        text = page.render(plain=True)

        # Plain output should have no ANSI codes
        assert "\033[" not in text
        assert "NAME" in text
        assert "test" in text

    def test_page_to_dict(self):
        """Test serialization to dict."""
        page = AwknoPage(
            topic="test",
            category="brick",
            synopsis="A test brick",
            description="This is a test",
            adopt="Adopt this",
            status="live",
        )

        data = page.to_dict()
        assert data["topic"] == "test"
        assert data["adopt"] == "Adopt this"

    def test_page_from_dict(self):
        """Test deserialization from dict."""
        data = {
            "topic": "test",
            "category": "brick",
            "synopsis": "A test",
            "description": "Test description",
            "adopt": "Adopt",
            "status": "live",
            "see_also": ["other"],
            "body": "More details",
        }

        page = AwknoPage.from_dict(data)
        assert page.topic == "test"
        assert page.category == "brick"
        assert page.see_also == ["other"]


class TestAwknoRegistry:
    """Test the corpus registry."""

    def test_registry_loads_pages(self):
        """Test that registry loads available pages."""
        registry = AwknoRegistry()
        # Should have loaded pages from awkno/pages/
        assert len(registry.pages) > 0

    def test_registry_get_known_page(self):
        """Test getting a known page."""
        registry = AwknoRegistry()

        if "awdk" in registry.pages:
            page = registry.get("awdk")
            assert page.topic.lower() == "awdk"
            assert page.category == "brick"

    def test_registry_get_unknown_page(self):
        """Test getting an unknown page raises NotFoundError."""
        registry = AwknoRegistry()

        with pytest.raises(NotFoundError):
            registry.get("nonexistent-topic-xyz-123")

    def test_registry_list_topics(self):
        """Test listing all topics."""
        registry = AwknoRegistry()
        topics = registry.list_topics()

        assert isinstance(topics, list)
        assert len(topics) > 0
        # Topics should be sorted
        assert topics == sorted(topics)

    def test_registry_list_by_category(self):
        """Test filtering by category."""
        registry = AwknoRegistry()

        bricks = registry.list_by_category("brick")
        assert all(p.category == "brick" for p in bricks)

        laws = registry.list_by_category("law")
        assert all(p.category == "law" for p in laws)

    def test_registry_search(self):
        """Test keyword search."""
        registry = AwknoRegistry()

        if len(registry.pages) > 0:
            results = registry.search("test")
            # Results should be ordered by score (highest first)
            if len(results) > 1:
                assert results[0][1] >= results[1][1]

    def test_corpus_files_exist(self):
        """Test that corpus JSON files are committed."""
        pages_dir = Path(__file__).parent.parent / "awkno" / "pages"

        if pages_dir.exists():
            json_files = list(pages_dir.glob("*.json"))
            assert len(json_files) > 0, "Corpus has no JSON files"

            # Check that each file is valid JSON
            for json_file in json_files[:5]:  # Check first 5 files
                with open(json_file) as f:
                    data = json.load(f)
                    assert "topic" in data
                    assert "category" in data
                    assert "synopsis" in data

    def test_brick_coverage(self):
        """Test that all bricks from ecosystem.yaml are in corpus."""
        registry = AwknoRegistry()

        # Check for known bricks
        known_bricks = [
            "awdk",
            "awskills",
            "awm",
            "awgit",
            "awgraph",
            "awrelay",
        ]

        for brick_id in known_bricks:
            page = registry.get(brick_id)
            assert page.category == "brick", f"{brick_id} should be a brick"

    #: A FLOOR pinned to the CURRENT count, raised in the same change that adds
    #: a law. It is not an equality (that goes red on correct work and gets
    #: edited without being read) and it is not a historical low-water mark
    #: either: pinned below the real count, deleting the NEWEST law leaves a
    #: corpus that is still contiguous and still above the floor, so the rule
    #: passes on the exact regression it exists to catch. Measured: with the
    #: floor at 18 and 19 laws shipped, removing law-19 was undetectable.
    MIN_LAWS = 19

    def test_law_coverage(self):
        """Every law is present, numbered contiguously from 01, and none was lost."""
        registry = AwknoRegistry()
        laws = registry.list_by_category("law")

        assert len(laws) >= self.MIN_LAWS, (
            f"corpus has {len(laws)} laws, fewer than the {self.MIN_LAWS} it had when "
            "this rule was written — a law was dropped from the corpus"
        )

        # Contiguity is the real assertion. A gap means the generator skipped a
        # source file, which an aggregate count would happily absorb by adding
        # a new law at the end while losing one in the middle.
        for i in range(1, len(laws) + 1):
            law_key = f"law-{i:02d}"
            page = registry.get(law_key)
            assert page is not None, f"{law_key} missing — the law numbering has a gap"
            assert page.category == "law"

    def test_law_access_by_number(self):
        """Test that laws are accessible by their number."""
        registry = AwknoRegistry()

        # Check a few laws
        for law_num in [1, 5, 18]:
            law_key = f"law-{law_num:02d}"
            page = registry.get(law_key)
            assert page.category == "law"
            assert "law-" in page.topic.lower()

    def test_deterministic_generation(self):
        """Test that corpus generation is deterministic."""
        from awkno.generate import AwknoGenerator

        # Find the repo root (has AitherOS/config/ecosystem.yaml)
        current = Path(__file__).parent
        repo_root = None
        while current != current.parent:
            if (current / "AitherOS" / "config" / "ecosystem.yaml").exists():
                repo_root = str(current / "AitherOS")
                break
            current = current.parent

        if not repo_root:
            pytest.skip("Could not find repo root")

        # Generate twice and compare
        gen1 = AwknoGenerator(repo_root)
        pages1 = gen1.generate()

        gen2 = AwknoGenerator(repo_root)
        pages2 = gen2.generate()

        # Same topics
        assert set(pages1.keys()) == set(pages2.keys())

        # Same content (sort keys for comparison)
        for key in pages1:
            data1_str = json.dumps(pages1[key], sort_keys=True)
            data2_str = json.dumps(pages2[key], sort_keys=True)
            assert data1_str == data2_str, f"Page {key} differs between runs"

    def test_no_internal_identifiers(self):
        """Test that no obvious internal identifiers leak into public corpus."""
        registry = AwknoRegistry()

        # Exclude known public bricks that start with "aither" (like aitherkvcache)
        known_public = ["aitherkvcache", "aitherzero", "aitherconnect"]

        for topic, page in registry.pages.items():
            content = json.dumps(page.to_dict())

            # Check for bare debt IDs (D-NNNN pattern) but allow "D-" in filenames/paths
            import re

            debt_ids = re.findall(r"\bD-\d{4}\b", content)
            assert not debt_ids, f"Debt ID found in {topic}: {debt_ids}"

            # Check for absolute paths (the most important ones to avoid)
            assert "C:\\" not in content and "C:/" not in content, f"Windows path in {topic}"
            assert "/app/" not in content, f"Linux container path in {topic}"
            assert "/opt/aitheros" not in content, f"Aither opt path in {topic}"

            # Check for internal service hostnames (but allow lowercase for product names)
            if not any(pub in topic.lower() for pub in known_public):
                # Assembled from fragments on purpose. Spelled as a literal, this
                # assertion makes the test file itself a finding for the
                # publish-time scan of the sdist — a detector's fixture becoming
                # the thing it detects.
                needle = "aitheros" + "-"
                assert needle not in content.lower(), f"Internal hostname prefix in {topic}"

    def test_plain_output_no_ansi(self):
        """Test that --plain mode produces no ANSI codes."""
        registry = AwknoRegistry()
        topics = registry.list_topics()

        if topics:
            page = registry.get(topics[0])
            plain_text = page.render(plain=True)
            # Plain output should have no ANSI escape codes
            assert "\033[" not in plain_text

    def test_page_richness_awdk_awsh(self):
        """Test that awdk and awsh have rich pages."""
        registry = AwknoRegistry()

        for brick_id in ["awdk", "awsh"]:
            page = registry.get(brick_id)

            # Rich pages should have all sections
            assert page.synopsis, f"{brick_id} missing synopsis"
            assert page.description, f"{brick_id} missing description"
            assert page.adopt, f"{brick_id} missing adopt"
            assert page.status, f"{brick_id} missing status"

            # Description should be substantial
            assert len(page.description) > 50, f"{brick_id} description too short"


class TestNotFoundError:
    """Test NotFoundError exception."""

    def test_not_found_error_message(self):
        """Test that NotFoundError has a clear message."""
        error = NotFoundError("test not found")
        assert "test not found" in str(error)
