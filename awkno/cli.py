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
        import contextlib
        with contextlib.suppress(BrokenPipeError):
            # the reader quit the pager mid-stream — that is the pager working
            proc.stdin.write(text)
            proc.stdin.close()
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
    awkno guide [N]
    awkno open [TOPIC]
    awkno search TERM
    awkno -k TERM
    awkno --plain
    awkno --json

DESCRIPTION
    awkno is an offline reference for the Aither World ecosystem. Every brick
    (standalone tool), stack (curated set), law (learned principle) and every
    chapter of the Aither World Guide lives here — no browser, no internet
    connection needed. `awkno open` renders any page to a local HTML file and
    opens it in your browser, still offline.

    The registry is built from ecosystem.yaml and the laws corpus at build time
    and committed as data files. After install, the pages are always there.

QUICK START
    awkno awdk                 Show the awdk brick
    awkno awsh                 Show the awsh brick
    awkno law 5                Show law 5
    awkno guide                The Aither World Guide: the chapters, in order
    awkno guide 2              Chapter 2 (your first local brain), in the pager
    awkno open guide 2         The same chapter, in your web browser, offline
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


def resolve_topic_key(registry: "AwknoRegistry", text: str) -> str | None:
    """`guide` / `guide 2` / `law 5` / `awdk` -> the corpus key, or None."""
    parts = text.strip().split()
    if not parts:
        return None
    head = parts[0].lower()
    if head == "guide":
        if len(parts) == 1:
            return "guide" if "guide" in registry.pages else None
        n = parts[1]
        if n.isdigit():
            key = f"guide-{int(n):02d}"
            return key if key in registry.pages else None
        # a chapter slug (02-first-brain / first-brain)
        for key, page in registry.pages.items():
            if page.category == "guide" and page.slug and (
                    page.slug == n or page.slug.endswith("-" + n)):
                return key
        return None
    if head == "law" and len(parts) > 1:
        return resolve_law_key(registry, parts[1])
    key = text.strip().lower()
    return key if key in registry.pages else None


_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} - awkno</title>
<style>
body{{margin:0;background:#0a0f1e;color:#e6ecf5;font:16px/1.6 Inter,system-ui,sans-serif}}
main{{max-width:880px;margin:0 auto;padding:2rem 1.25rem 4rem}}
h1{{font-size:1.8rem;margin:.2rem 0 .4rem}}
.syn{{opacity:.8;margin:0 0 1.5rem;white-space:pre-wrap}}
pre{{white-space:pre-wrap;background:#111a33;border:1px solid #22305a;
  border-radius:10px;padding:1rem;line-height:1.5}}
nav a{{color:#7fdbea;margin-right:1rem}}
.k{{font:13px JetBrains Mono,monospace;letter-spacing:.08em;text-transform:uppercase;opacity:.6}}
footer{{opacity:.6;font-size:.85rem;margin-top:2rem}}
</style></head><body><main>
<nav>{nav}</nav>
<p class="k">{category} &middot; awkno, offline</p>
<h1>{title}</h1>
<p class="syn">{synopsis}</p>
<pre>{body}</pre>
<footer>Rendered by <code>awkno open</code> from the committed corpus. The same page online:
<a href="{online}">{online}</a></footer>
</main></body></html>
"""


def write_html(registry: "AwknoRegistry", key: str):
    """Render one page to ~/.aither/awkno/<key>.html and return the path."""
    import html as _html
    from pathlib import Path

    page = registry.get(key)
    out_dir = Path.home() / ".aither" / "awkno"
    out_dir.mkdir(parents=True, exist_ok=True)
    nav = []
    if page.category == "guide":
        nav.append('<a href="guide.html">The Guide</a>')
        for sib in page.see_also or []:
            if sib.startswith("guide-"):
                nav.append(f'<a href="{sib}.html">next: {sib}</a>')
    if page.category == "guide":
        online = "https://aitherium.github.io/awknowledge/" + (
            f"path/{page.slug}.html" if page.slug else "")
    else:
        online = "https://aitherium.github.io/awknowledge/man/" + (
            f"{page.topic}.html" if page.category == "brick" else "index.html")
    body = page.render(plain=True)
    text = _HTML.format(
        title=_html.escape(page.synopsis or page.topic),
        synopsis=_html.escape(page.description or ""),
        category=_html.escape(page.category),
        body=_html.escape(body),
        nav=" ".join(nav),
        online=online,
    )
    path = out_dir / f"{key}.html"
    path.write_text(text, encoding="utf-8")
    # Sibling pages the nav links to, so "next" works offline too.
    if page.category == "guide":
        for sib in page.see_also or []:
            if sib.startswith("guide-") and not (out_dir / f"{sib}.html").exists():
                write_html(registry, sib)
        if key != "guide" and not (out_dir / "guide.html").exists():
            write_html(registry, "guide")
    return path


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
    # GENERATED doctor intercept (gen_aw_doctor.py) -- do not edit
    _dv = locals().get("argv")
    if (_dv if _dv is not None else __import__("sys").argv[1:])[:1] == ["doctor"]:
        from ._doctor import report
        return report()
    # GENERATED repo-state intercept (gen_aw_doctor.py) -- do not edit
    try:
        from awgit import state as _aw_state
    except Exception:
        _aw_state = None
    if _aw_state is not None:
        _sv = locals().get("argv")
        if _aw_state.cli_banner(_sv if _sv is not None else __import__("sys").argv[1:]):
            return 0
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
            "guide": [],
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
        for cat in ["guide", "brick", "stack", "law", "topic"]:
            if categories[cat]:
                print(f"{cat.upper()}S ({len(categories[cat])})")
                for name in sorted(categories[cat]):
                    page = registry.pages[name]
                    print(f"    {name:<20} {page.synopsis}")
                print()
        return

    # `awkno open [TOPIC]` -- the same page, rendered to a local HTML file and
    # opened in the default browser. Offline: nothing is fetched.
    if topic_lower == "open" or topic_lower.startswith("open "):
        rest = topic[4:].strip() or "guide"
        key = resolve_topic_key(registry, rest)
        if key is None:
            print(f"Topic '{rest}' not found. Try: awkno open guide, awkno open guide 2")
            return
        path = write_html(registry, key)
        print(f"wrote {path}")
        import webbrowser

        if not webbrowser.open(path.as_uri()):
            print("(could not launch a browser - open the file above by hand)")
        return

    if topic_lower == "guide" or topic_lower.startswith("guide "):
        key = resolve_topic_key(registry, topic)
        if key is None:
            print("Usage: awkno guide [N]    (N = chapter number, e.g. awkno guide 2)")
            return
        page = registry.get(key)
        if args.json:
            print(json.dumps(page.to_dict()))
        else:
            pager_render(page.render(plain=args.plain))
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

    for argv in (["law", "5"], ["search", "silence"], ["list"], ["awdk"],
                 ["guide"], ["guide", "2"], ["open", "guide", "2"]):
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

    # --- the guide is in the corpus and resolvable every way the SYNOPSIS says
    reg = AwknoRegistry()
    assert "guide" in reg.pages, "corpus has no `guide` index page - regenerate"
    assert resolve_topic_key(reg, "guide") == "guide"
    assert resolve_topic_key(reg, "guide 2") == "guide-02", "guide N must resolve"
    assert resolve_topic_key(reg, "guide first-brain") == "guide-02", "slug must resolve"
    assert resolve_topic_key(reg, "guide 99") is None
    chapters = reg.list_by_category("guide")
    assert len(chapters) >= 10, f"expected the full journey, got {len(chapters)}"
    two = reg.get("guide-02")
    assert "adk quickstart-local" in (two.body or ""), "chapter 2 lost its DO steps"
    assert "D-" not in (two.body or ""), "internal ref leaked into the guide corpus"

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
