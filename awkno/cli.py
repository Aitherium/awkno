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
import re
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


def slugify(text: str) -> str:
    """Reduce a synopsis to a comparable slug."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def resolve_law_key(registry: "AwknoRegistry", law_id: str) -> str | None:
    """Map `5` or `design-for-the-silence` onto a law page key.

    A slug matches when it prefixes the slugified synopsis of exactly ONE law.
    Ambiguous prefixes return None rather than the first hit: a prefix matcher
    that guesses is how `get("nemotron")` came to answer for a model nobody
    registered.
    """
    if law_id.isdigit():
        return f"law-{int(law_id):02d}"

    want = slugify(law_id)
    if not want:
        return None

    laws = [t for t in registry.list_topics() if t.startswith("law-")]

    # The law's OWN slug first. Exact, and it survives a retitle -- the
    # synopsis fallback below does not.
    for topic in laws:
        if slugify(registry.pages[topic].slug or "") == want:
            return topic

    # Fall back to a unique prefix of the synopsis, for a corpus generated
    # before slugs were carried. Unique or nothing: a prefix matcher that
    # answers with its first hit is fail-open, and returns a confident wrong
    # law for a slug nobody registered.
    hits = [
        topic
        for topic in laws
        if slugify(registry.pages[topic].synopsis).startswith(want)
    ]
    return hits[0] if len(hits) == 1 else None


def _build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser.

    Separate from main() so the self-test can assert that every form printed
    in the SYNOPSIS actually parses.
    """
    parser = argparse.ArgumentParser(
        description="The man page for the Aither World",
        add_help=False,
        usage="awkno [TOPIC] or awkno COMMAND [OPTIONS]",
    )

    # nargs="*", not "?": the SYNOPSIS advertises `awkno law 5` and
    # `awkno search TERM`, both of which argparse rejected as
    # "unrecognized arguments" under nargs="?" -- only the quoted
    # `awkno "law 5"` worked, which nobody would type.
    parser.add_argument(
        "topic", nargs="*", help="Topic, brick, stack, law, or command"
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

    return parser


def main() -> None:
    """Main CLI entry point."""
    parser = _build_parser()
    args = parser.parse_args()
    topic = " ".join(args.topic).strip()

    if args.self_test:
        _self_test()
        return

    registry = AwknoRegistry()

    if not topic and not args.search:
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

    topic_lower = topic.lower()

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
        parts = topic.split()
        if len(parts) < 2:
            print("Usage: awkno law <N|SLUG>")
            return
        law_id = parts[1]
        law_key = resolve_law_key(registry, law_id)
        if law_key is None:
            print(
                f"Law '{law_id}' not found or ambiguous. "
                "Try: awkno law 5, awkno law design-for-the-silence"
            )
            return
        try:
            page = registry.get(law_key)
        except NotFoundError:
            print(f"Law '{law_id}' not found. Try: awkno law 1, awkno law 5, etc.")
            return
    else:
        try:
            page = registry.get(topic)
        except NotFoundError:
            print(f"Topic '{topic}' not found")
            print(f"Try: awkno list, awkno -k '{topic}'")
            return

    if args.json:
        print(json.dumps(page.to_dict()))
    else:
        text = page.render(plain=args.plain)
        pager_render(text)


def _self_test() -> None:
    """Run self-test (pure, no external service needed)."""
    from awkno.corpus import AwknoPage, AwknoRegistry

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

    # --- the SYNOPSIS is a promise; assert it ------------------------------
    #
    # This block exists because every two-word form printed in this tool's own
    # SYNOPSIS -- `awkno law 5`, `awkno search TERM` -- was rejected by argparse
    # as "unrecognized arguments" in a SHIPPED release on PyPI, and `<N|SLUG>`
    # advertised a slug lookup the generator computed and discarded, so no slug
    # ever resolved. The self-test above could not see any of it: it asserted
    # that a dataclass renders. A tool that documents an invocation it cannot
    # perform is a broken tool that reads as an authoritative one.
    parser = _build_parser()

    for argv in (["law", "5"], ["search", "silence"], ["list"], ["awdk"]):
        try:
            parsed = parser.parse_args(argv)
        except SystemExit:  # argparse exits rather than raising
            raise AssertionError(
                f"SYNOPSIS form `awkno {' '.join(argv)}` was REJECTED by the parser"
            ) from None
        joined = " ".join(parsed.topic).strip()
        assert joined == " ".join(argv), f"SYNOPSIS form {argv} did not parse"

    # the quoted form callers may already be using must keep working
    assert " ".join(parser.parse_args(["law 5"]).topic).strip() == "law 5"

    registry = AwknoRegistry()

    # numeric and slug lookups both resolve, and to the SAME law
    by_num = resolve_law_key(registry, "5")
    by_slug = resolve_law_key(registry, "design-for-the-silence")
    assert by_num == "law-05", f"numeric law lookup gave {by_num}"
    assert by_slug == "law-05", f"slug law lookup gave {by_slug}"
    assert registry.get(by_num).synopsis

    # every law is reachable by BOTH spellings -- a resolver that answers for
    # law 5 and nothing else passes a single-case test while being useless
    law_topics = [t for t in registry.list_topics() if t.startswith("law-")]
    assert len(law_topics) >= 19, f"only {len(law_topics)} laws in the corpus"
    for topic in law_topics:
        number = topic.split("-", 1)[1].lstrip("0") or "0"
        assert resolve_law_key(registry, number) == topic, f"{topic} not reachable by number"
        slug = slugify(registry.pages[topic].synopsis)
        assert resolve_law_key(registry, slug) == topic, f"{topic} not reachable by slug"
        own = registry.pages[topic].slug
        assert own, f"{topic} carries no slug -- regenerate the corpus"
        assert resolve_law_key(registry, own) == topic, f"{topic} not reachable by its own slug"

    # A RETITLED law: slug and synopsis diverge, which is the only case the
    # exact-slug branch exists for. Without this the branch is dead weight --
    # every current law's filename slug happens to prefix its own synopsis, so
    # deleting the branch leaves the suite green and the lookup silently
    # dependent on a coincidence that a single retitle ends.
    registry.pages["law-99"] = AwknoPage(
        topic="law-99",
        category="law",
        synopsis="Completely different words after a retitle",
        description="Law #99",
        slug="the-original-filename-slug",
    )
    try:
        assert resolve_law_key(registry, "the-original-filename-slug") == "law-99", (
            "a retitled law is unreachable by its own slug"
        )
        assert resolve_law_key(registry, "completely-different-words") == "law-99"
    finally:
        del registry.pages["law-99"]

    # fail closed: nonsense and ambiguity resolve to nothing, never to law 1.
    # An ambiguous prefix returning its first hit is the trap that made a
    # licence lookup answer for models nobody had registered.
    assert resolve_law_key(registry, "no-such-law-anywhere") is None
    assert resolve_law_key(registry, "") is None
    assert resolve_law_key(registry, "a") is None, "bare prefix must be ambiguous, not law-01"

    print(f"[OK] awkno self-test passed ({len(law_topics)} laws, both spellings)")


if __name__ == "__main__":
    main()
