"""awkno CLI.

    awkno awdk
    awkno awsh
    awkno law 5
    awkno list
    awkno search design-for-the-silence
    awkno -k silence
    awkno --plain

Type awkno with no args to show an overview.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from awkno.corpus import AwknoRegistry, NotFoundError


def pager_render(text: str) -> None:
    """Render text through $PAGER if available, else stdout."""
    pager = os.environ.get("PAGER", "less" if sys.platform != "win32" else "more")

    if not sys.stdout.isatty():
        print(text)
        return

    try:
        import subprocess

        proc = subprocess.Popen(
            pager, stdin=subprocess.PIPE, text=True, bufsize=1024
        )
        try:
            proc.stdin.write(text)
            proc.stdin.close()
        except BrokenPipeError:
            pass
        proc.wait()
    except (FileNotFoundError, OSError):
        print(text)


def show_overview() -> None:
    """Show the overview page."""
    text = """NAME
    awkno — The man page for the Aither World

SYNOPSIS
    awkno [TOPIC]
    awkno list
    awkno law <N|SLUG>
    awkno search TERM
    awkno -k TERM
    awkno --plain
    awkno --json

DESCRIPTION
    awkno is an offline reference for the Aither World ecosystem. Every brick
    (standalone tool), stack (curated set), and law (learned principle) lives
    here — no browser, no internet connection needed.

    The registry is built from ecosystem.yaml and the laws corpus at build time
    and committed as data files. After install, the pages are always there.

QUICK START
    awkno awdk                 Show the awdk brick
    awkno awsh                 Show the awsh brick
    awkno law 5                Show law 5
    awkno list                 List all topics
    awkno search kubernetes    Search for "kubernetes"

OPTIONS
    --plain              No ANSI formatting
    --json               JSON output (for piping)
    -k, --apropos TERM   Search for TERM (like man -k)

SEE ALSO
    For the full ecosystem, visit https://github.com/Aitherium/awkno
"""
    pager_render(text)


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="The man page for the Aither World",
        add_help=False,
        usage="awkno [TOPIC] or awkno COMMAND [OPTIONS]",
    )

    parser.add_argument(
        "topic", nargs="?", help="Topic, brick, stack, law, or command"
    )
    parser.add_argument(
        "--plain", action="store_true", help="Plain text, no ANSI formatting"
    )
    parser.add_argument(
        "--json", action="store_true", help="JSON output for piping"
    )
    parser.add_argument(
        "-k", "--apropos", dest="search", help="Search for term (like man -k)"
    )
    parser.add_argument(
        "--self-test", action="store_true", help="Run self-test"
    )

    args = parser.parse_args()

    if args.self_test:
        _self_test()
        return

    registry = AwknoRegistry()

    if not args.topic and not args.search:
        show_overview()
        return

    if args.search:
        results = registry.search(args.search)
        if not results:
            print(f"No matches for '{args.search}'")
            return
        if args.json:
            output = [
                {"topic": page.topic, "score": score}
                for page, score in results[:10]
            ]
            print(json.dumps(output))
        else:
            print(f"\n[{args.search}]\n")
            for page, score in results[:10]:
                print(f"    {page.topic:<20} {page.synopsis}")
        return

    topic_lower = args.topic.lower()

    if topic_lower == "list":
        topics = registry.list_topics()
        categories = {
            "brick": [],
            "stack": [],
            "law": [],
            "topic": [],
        }
        for t in topics:
            page = registry.pages[t]
            if page.category not in categories:
                categories[page.category] = []
            categories[page.category].append(t)

        print()
        for cat in ["brick", "stack", "law", "topic"]:
            if categories[cat]:
                print(f"{cat.upper()}S ({len(categories[cat])})")
                for name in sorted(categories[cat]):
                    page = registry.pages[name]
                    print(f"    {name:<20} {page.synopsis}")
                print()
        return

    if topic_lower.startswith("law"):
        parts = args.topic.split()
        if len(parts) < 2:
            print("Usage: awkno law <N|SLUG>")
            return
        law_id = parts[1]
        try:
            if law_id.isdigit():
                law_key = f"law-{int(law_id):02d}"
            else:
                law_key = f"law-{law_id}"
            page = registry.get(law_key)
        except NotFoundError:
            print(f"Law '{law_id}' not found. Try: awkno law 1, awkno law 5, etc.")
            return
    else:
        try:
            page = registry.get(args.topic)
        except NotFoundError:
            print(f"Topic '{args.topic}' not found")
            print(f"Try: awkno list, awkno -k '{args.topic}'")
            return

    if args.json:
        print(json.dumps(page.to_dict()))
    else:
        text = page.render(plain=args.plain)
        pager_render(text)


def _self_test() -> None:
    """Run self-test (pure, no external service needed)."""
    from awkno.corpus import AwknoPage

    page = AwknoPage(
        topic="test",
        category="topic",
        synopsis="A test page",
        description="This is a test",
        adopt="Adopt this test",
        status="test",
    )

    assert page.topic == "test"
    assert page.render()
    assert page.to_dict()

    print("[OK] awkno self-test passed")


if __name__ == "__main__":
    main()
