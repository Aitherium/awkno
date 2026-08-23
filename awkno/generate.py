"""Generate the awkno corpus from sources.

Run this script to regenerate the offline man-page corpus from ecosystem.yaml
and the laws in awknowledge/laws/. The output is committed as JSON files
under awkno/pages/ so the installed package is fully offline.

    python awkno/generate.py

Output files are deterministically ordered and formatted for reproducible
corpus generation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required for generate.py")
    print("Install with: pip install PyYAML")
    exit(1)


class AwknoGenerator:
    """Generate the corpus from sources."""

    def __init__(self, repo_root: str | None = None,
                 output_dir: str | Path | None = None):
        """Initialize the generator.

        Args:
            repo_root: Path to repo root (auto-detected if not provided).
            output_dir: Where to write the corpus. Defaults to the committed
                `pages/` beside this file. A caller passes a temp dir to ask
                "is what is committed what I would generate now?" -- a question
                that cannot be answered by a run that overwrites the answer.
        """
        if repo_root is None:
            # Auto-detect: walk up from this file to find the repo root
            current = Path(__file__).parent
            while current != current.parent:
                if (current / "AitherOS" / "config" / "ecosystem.yaml").exists():
                    repo_root = str(current / "AitherOS")
                    break
                if (current / "config" / "ecosystem.yaml").exists():
                    repo_root = str(current)
                    break
                current = current.parent

        if repo_root is None:
            raise ValueError("Could not find repo root. Pass repo_root explicitly.")

        self.repo_root = Path(repo_root)
        self.ecosystem_file = self.repo_root / "config" / "ecosystem.yaml"
        self.laws_dir = self.repo_root.parent / "awknowledge" / "laws"
        # The PUBLIC shelf. Deliberately not `AitherOS/config/pack_shelf.yaml`:
        # that file is the internal backlog and its hold reasons name internal
        # services and debt ids. A public corpus that reads it and filters is
        # one unanticipated reason away from publishing one; a public corpus
        # that never reads it cannot fail that way.
        self.shelf_dir = self.repo_root.parent / "awpack" / "packs"
        self.output_dir = (Path(output_dir) if output_dir
                           else Path(__file__).parent / "pages")

        if not self.ecosystem_file.exists():
            raise FileNotFoundError(f"ecosystem.yaml not found at {self.ecosystem_file}")

    def generate(self) -> dict[str, Any]:
        """Generate the full corpus.

        Returns:
            A dict mapping page keys to their content (for testing).
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        pages = {}

        # Load ecosystem
        # encoding is NOT optional here. Python's default is the platform's
        # preferred encoding, which is cp1252 on Windows — so every em dash in
        # the registry decoded to three junk characters. It never LOOKED wrong,
        # because the writer below escaped non-ASCII on the way out, turning the
        # damage into `â€”` inside the JSON where no text search
        # for a mojibake sequence would ever match it.
        with open(self.ecosystem_file, encoding="utf-8") as f:
            ecosystem = yaml.safe_load(f)

        # Generate brick pages
        if "bricks" in ecosystem:
            for brick in ecosystem["bricks"]:
                page = self._make_brick_page(brick)
                pages[page["topic"].lower()] = page

        # Generate stack pages
        if "stacks" in ecosystem:
            for stack in ecosystem["stacks"]:
                page = self._make_stack_page(stack)
                pages[page["topic"].lower()] = page

        # Generate a page per pack ON THE SHELF. Held packs are absent by
        # design -- see _make_pack_page.
        if self.shelf_dir.exists():
            for manifest in sorted(self.shelf_dir.glob("*/pack.yaml")):
                page = self._make_pack_page(manifest)
                if page is not None:
                    pages[page["topic"].lower()] = page

        # Generate law pages
        if self.laws_dir.exists():
            for law_file in sorted(self.laws_dir.glob("*.md")):
                page = self._make_law_page(law_file)
                pages[page["topic"].lower()] = page

        # Write all pages to JSON
        for topic_key, page_data in pages.items():
            output_file = self.output_dir / f"{topic_key}.json"
            # ensure_ascii=False keeps real characters in the file. With the
            # default (True) any encoding damage upstream is escaped into
            # \uXXXX and becomes invisible to inspection — the corpus reads as
            # clean ASCII while rendering as garbage in the terminal.
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(page_data, f, indent=2, sort_keys=True, ensure_ascii=False)

        # PRUNE. Writing without deleting makes this a write-ONLY mirror: a brick
        # retired from the registry keeps its page here forever, and `awkno <it>`
        # then answers a stranger, offline, about something that does not exist --
        # which reads exactly like the brick existing. Found live 2026-08-22:
        # `awflow` and `awroll` had been shipping as `status: planned` stubs while
        # appearing in no registry entry and no package. The generator had run
        # correctly every time; nothing it wrote was wrong, and the corpus was
        # still wrong, because the defect was in what it DIDN'T write.
        #
        # Safe because `pages` above is the complete corpus -- bricks, stacks AND
        # laws -- so anything on disk it does not name is by definition stale.
        # Asserted from the other side upstream: the registry's own gate compares
        # this committed corpus against it and fails on drift in EITHER direction,
        # so a regression here cannot pass silently.
        keep = {f"{k}.json" for k in pages}
        removed = []
        for stale in sorted(self.output_dir.glob("*.json")):
            if stale.name not in keep:
                stale.unlink()
                removed.append(stale.stem)
        if removed:
            print(f"[PRUNED] {len(removed)} stale page(s): {', '.join(removed)}")

        return pages

    def _scrub_internal_refs(self, text: str) -> str:
        """Remove internal references from text.

        Removes debt IDs (D-NNNN), rule codes (PQ, EC, SEC, etc), and other
        internal identifiers that should not appear in public documentation.

        Args:
            text: Text to scrub.

        Returns:
            Text with internal references removed.
        """
        import re

        if not text:
            return text

        # Issue-tracker row ids, bare and bracketed.
        text = re.sub(r"\(\s*D-\d+\s*\)", "", text)
        text = re.sub(r"\[\s*D-\d+\s*\]", "", text)
        text = re.sub(r"\bD-\d+\b", "", text)

        # Quality-gate rule codes.
        text = re.sub(
            r"\b(?:PQ|EC|SEC|ONB|MRP|SHW|NX|RB|TP|DAW|SAE|CX|MR|AC|ACG|AWM|AWP|QCP|QIC)"
            r"\d{3,4}\b",
            "",
            text,
        )
        text = re.sub(r"gate\s+\d+[a-z]*", "", text)

        # Names of internal gate scripts. These reach the corpus through the LAW
        # TEXT itself, which cites the checker that caught each defect -- so the
        # two rules above, which only look for ids, passed them straight through.
        # A law keeps all of its force as "a gate that asserted entry points";
        # the filename is internal vocabulary and carries none of the lesson.
        # The replacement must stay a valid FILENAME, because these names appear
        # inside runnable code blocks as well as in prose. Substituting a phrase
        # ("an internal gate") reads fine in a sentence, but inside a shell
        # example it turns a runnable command into an unrunnable one presented
        # as runnable — a worse defect than the disclosure it was fixing. A
        # placeholder FILENAME reads correctly in both places and is obviously a
        # placeholder.
        text = re.sub(r"\bcheck_[a-z0-9_]+\.py\b", "your_checker.py", text)

        # Collapse whitespace left behind by the removals above, so a scrubbed
        # sentence does not read as though a word is missing.
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r" ([,.;:)])", r"\1", text)

        return text

    def _make_brick_page(self, brick: dict) -> dict[str, Any]:
        """Create a page for a brick.

        Args:
            brick: A brick entry from ecosystem.yaml.

        Returns:
            A page dict ready for JSON serialization.
        """
        brick_id = brick.get("id", "unknown")
        tagline = brick.get("tagline", "")
        synopsis = tagline.split(" — ")[0] if " — " in tagline else tagline

        adopt = self._scrub_internal_refs(brick.get("adopt", ""))
        status = brick.get("status", "unknown")
        install = brick.get("install", "")
        problem = self._scrub_internal_refs(brick.get("problem", ""))
        kind = brick.get("kind", "tool")

        description = f"Kind: {kind}\n"
        if problem:
            description += f"\nProblem\n{problem}\n"
        if install:
            description += f"\nInstall\n{install}"

        see_also = []
        if brick.get("pairs_with"):
            see_also.extend(brick["pairs_with"])
        if brick.get("includes"):
            see_also.extend(brick["includes"])

        return {
            "adopt": adopt if adopt else None,
            "category": "brick",
            "description": description.strip(),
            "see_also": see_also if see_also else None,
            "status": status,
            "synopsis": synopsis,
            "topic": brick_id,
        }

    def _make_pack_page(self, manifest: Path) -> dict[str, Any] | None:
        """Create a page for one pack on the shelf, or None to skip it.

        Returns None for a manifest that will not parse or that declares
        `status: internal` — an internal pack must be ABSENT from a public
        corpus, not present and marked. A reader offline cannot tell a marked
        page from an available one at a glance, and a name is already a
        disclosure.
        """
        try:
            with open(manifest, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
        except (OSError, yaml.YAMLError):
            # A manifest we cannot read is skipped, not half-rendered. The
            # shelf's own gate (check_packs.py) is what makes this loud.
            return None

        pack_id = data.get("id") or manifest.parent.name
        status = data.get("status", "unknown")
        if status == "internal":
            return None

        summary = " ".join(str(data.get("summary", "")).split())
        synopsis = summary.split(". ")[0] if summary else pack_id

        runtime = data.get("runtime", "")
        extras = data.get("extras") or []
        needs = data.get("needs") or []
        tools = data.get("tools") or []

        description = "Kind: pack\n"
        if summary:
            description += f"\nWhat it does\n{summary}\n"
        if runtime:
            # The install line a reader can actually type. A pack is not
            # installed on its own — it runs inside a runtime, which is exactly
            # why a pack is not a brick (a brick's `adopt` may not name one).
            description += f"\nRuntime\n{runtime}"
            if extras:
                description += f" with extras: {', '.join(extras)}"
            description += "\n"
        if needs:
            description += f"\nNeeds\n{', '.join(needs)}\n"
        if tools:
            description += "\nTools\n" + "\n".join(f"  {t}" for t in tools) + "\n"

        see_also = ["awdk", "awpack"]
        if "memory" in extras:
            see_also.append("awm")

        # ADOPT is the command a reader TYPES. Repeating the summary here (as
        # the first version did) fills the section with what NAME already said,
        # which reads as a page that has nothing to tell you.
        install = str(data.get("install", "")).strip()
        return {
            "adopt": install or None,
            "category": "pack",
            "description": description.strip(),
            "see_also": see_also,
            "status": status,
            "synopsis": synopsis,
            "topic": pack_id,
        }

    def _make_stack_page(self, stack: dict) -> dict[str, Any]:
        """Create a page for a stack.

        Args:
            stack: A stack entry from ecosystem.yaml.

        Returns:
            A page dict ready for JSON serialization.
        """
        stack_id = stack.get("id", "unknown")
        name = stack.get("name", "")
        what = stack.get("what", "")
        status = stack.get("status", "unknown")
        bricks = stack.get("bricks", [])

        synopsis = name if name else stack_id

        # Clean internal references from what field
        description = self._scrub_internal_refs(what)
        description = description + "\n\n"
        if bricks:
            description += f"Includes: {', '.join(bricks)}"

        return {
            "adopt": None,
            "category": "stack",
            "description": description.strip(),
            "see_also": bricks if bricks else None,
            "status": status,
            "synopsis": synopsis,
            "topic": stack_id,
        }

    def _make_law_page(self, law_file: Path) -> dict[str, Any]:
        """Create a page for a law.

        Args:
            law_file: Path to a law markdown file.

        Returns:
            A page dict ready for JSON serialization.
        """
        # Extract law number and slug from filename: 01-rule-name.md
        stem = law_file.stem
        parts = stem.split("-", 1)
        law_num = int(parts[0])
        law_slug = parts[1] if len(parts) > 1 else ""

        # Read the file, and SCRUB IT — the law bodies are the longest prose in
        # this corpus and the only source that cites internal gate scripts by
        # name. Brick and stack pages were scrubbed from the start; this call
        # site was missed, so a correct sanitiser shipped internal identifiers
        # from three law pages while every other page was clean.
        content = self._scrub_internal_refs(law_file.read_text(encoding="utf-8"))

        # Extract the title (first line, usually # heading)
        lines = content.strip().split("\n")
        title = ""
        description = ""

        for i, line in enumerate(lines):
            if line.startswith("# "):
                title = line[2:].strip()
                description = "\n".join(lines[i + 1 :]).strip()
                break

        # Use the title as the synopsis
        synopsis = title if title else law_slug.replace("-", " ").title()

        # Create topic key as "law-01" for law 1
        topic_key = f"law-{law_num:02d}"

        return {
            "adopt": None,
            "body": description if description else None,
            "category": "law",
            "description": f"Law #{law_num}",
            "see_also": None,
            "status": "published",
            "synopsis": synopsis,
            "topic": topic_key,
            # The filename slug. `awkno law <N|SLUG>` advertised this lookup
            # while the value was computed here and thrown away, so no slug
            # ever resolved -- a documented invocation that could not work.
            "slug": law_slug or None,
        }


def main() -> None:
    """CLI entry point for corpus generation."""
    import sys

    # --out DIR writes elsewhere, leaving the committed corpus untouched. Parsed by
    # hand rather than with argparse to keep the positional repo_root working exactly
    # as it did -- this is a published module, and a CLI that changes shape under a
    # caller is a breakage nobody attributes to a "docs" change.
    argv = sys.argv[1:]
    out_dir = None
    if "--out" in argv:
        i = argv.index("--out")
        if i + 1 >= len(argv):
            print("ERROR: --out needs a directory")
            exit(2)
        out_dir = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]

    try:
        # Allow repo root to be passed as first argument
        repo_root = argv[0] if argv else None
        generator = AwknoGenerator(repo_root, output_dir=out_dir)
        pages = generator.generate()
        print(f"[OK] Generated corpus with {len(pages)} pages")
        print(f"     Output: {generator.output_dir}")

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        exit(1)
    except ValueError as e:
        print(f"ERROR: {e}")
        print("\nUsage: python awkno/generate.py [repo_root]")
        print("\nIf repo_root is not provided, auto-detects from ecosystem.yaml location")
        exit(1)


if __name__ == "__main__":
    main()
