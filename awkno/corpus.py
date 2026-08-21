"""Load and query the offline corpus.

Pages are stored as JSON files under awkno/pages/. This module handles the
loading, searching, and formatting of those pages.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional


class NotFoundError(Exception):
    """Raised when a topic is not found."""

    pass


@dataclass
class AwknoPage:
    """A single man page."""

    topic: str
    category: str
    synopsis: str
    description: str
    adopt: Optional[str] = None
    status: Optional[str] = None
    see_also: Optional[list[str]] = None
    body: Optional[str] = None

    def render(self, plain: bool = False) -> str:
        """Render the page as text.

        Args:
            plain: If True, no ANSI codes. If False, use formatting (when TTY).

        Returns:
            The formatted page text.
        """
        lines = []
        lines.append("NAME")
        lines.append(f"    {self.topic} — {self.synopsis}")
        lines.append("")

        if self.adopt:
            lines.append("ADOPT")
            for line in self.adopt.split("\n"):
                lines.append(f"    {line}")
            lines.append("")

        if self.description:
            lines.append("DESCRIPTION")
            for line in self.description.split("\n"):
                lines.append(f"    {line}")
            lines.append("")

        if self.body:
            lines.append("DETAILS")
            for line in self.body.split("\n"):
                lines.append(f"    {line}")
            lines.append("")

        if self.status:
            lines.append("STATUS")
            lines.append(f"    {self.status}")
            lines.append("")

        if self.see_also:
            lines.append("SEE ALSO")
            for item in self.see_also:
                lines.append(f"    {item}")

        text = "\n".join(lines)

        if not plain:
            # Check if stdout is a TTY for formatting
            import sys

            if hasattr(sys.stdout, "isatty") and sys.stdout.isatty():
                # Apply ANSI formatting
                text = text.replace("NAME\n", "\033[1mNAME\033[0m\n")
                text = text.replace("ADOPT\n", "\033[1mADOPT\033[0m\n")
                text = text.replace("DESCRIPTION\n", "\033[1mDESCRIPTION\033[0m\n")
                text = text.replace("DETAILS\n", "\033[1mDETAILS\033[0m\n")
                text = text.replace("STATUS\n", "\033[1mSTATUS\033[0m\n")
                text = text.replace("SEE ALSO\n", "\033[1mSEE ALSO\033[0m\n")

        return text

    def to_dict(self) -> dict:
        """Convert to dict for JSON serialization."""
        return {
            "topic": self.topic,
            "category": self.category,
            "synopsis": self.synopsis,
            "description": self.description,
            "adopt": self.adopt,
            "status": self.status,
            "see_also": self.see_also,
            "body": self.body,
        }

    @classmethod
    def from_dict(cls, data: dict) -> AwknoPage:
        """Create from dict (JSON deserialization)."""
        return cls(**data)


class AwknoRegistry:
    """Load and query all pages."""

    def __init__(self):
        """Load all pages from the corpus directory."""
        self.pages: dict[str, AwknoPage] = {}
        self._load_pages()

    def _load_pages(self) -> None:
        """Load all JSON files from awkno/pages/."""
        pages_dir = Path(__file__).parent / "pages"

        if not pages_dir.exists():
            return

        for json_file in pages_dir.glob("*.json"):
            try:
                with open(json_file) as f:
                    data = json.load(f)
                    page = AwknoPage.from_dict(data)
                    self.pages[page.topic.lower()] = page
            except (json.JSONDecodeError, ValueError):
                pass

    def get(self, topic: str) -> AwknoPage:
        """Get a page by topic name.

        Args:
            topic: The topic name (case-insensitive).

        Returns:
            The AwknoPage.

        Raises:
            NotFoundError: If the topic is not found.
        """
        key = topic.lower()
        if key in self.pages:
            return self.pages[key]
        raise NotFoundError(f"Topic '{topic}' not found")

    def list_topics(self) -> list[str]:
        """List all available topics."""
        return sorted(self.pages.keys())

    def list_by_category(self, category: str) -> list[AwknoPage]:
        """List pages by category.

        Args:
            category: One of "brick", "stack", "law", "topic".

        Returns:
            List of pages in that category.
        """
        return [
            page for page in self.pages.values() if page.category == category
        ]

    def search(self, term: str) -> list[tuple[AwknoPage, float]]:
        """Search pages by keyword.

        Args:
            term: Search term (case-insensitive).

        Returns:
            List of (page, score) tuples sorted by score (highest first).
        """
        term_lower = term.lower()
        results = []

        for page in self.pages.values():
            # Score based on where the term appears
            score = 0.0

            if term_lower in page.topic.lower():
                score += 1.0

            if page.synopsis and term_lower in page.synopsis.lower():
                score += 0.8

            if page.description and term_lower in page.description.lower():
                score += 0.5

            if page.adopt and term_lower in page.adopt.lower():
                score += 0.3

            if page.body and term_lower in page.body.lower():
                score += 0.2

            # Use SequenceMatcher for fuzzy matching on topic
            ratio = SequenceMatcher(None, term_lower, page.topic.lower()).ratio()
            score += ratio * 0.5

            if score > 0:
                results.append((page, score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results
