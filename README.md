# awkno — The man page for the Aither World

**Every brick, stack, and law in your terminal, offline.**

awkno is a standalone reference for the Aither World ecosystem — the set of portable, composable tools and principles that make agent automation reproducible and auditable. No browser, no internet connection, no external dependencies needed.

## Why

Agent systems need documented principles. The Aither World is built on 18 laws derived from real failures on production systems — lessons about gates, silence, atomicity, and delivery that apply to every agent work you build.

The ecosystem itself is ~36 portable tools (bricks) organized into thematic stacks. awkno brings them all into your terminal: any brick's purpose and adoption path, any law's principle and reasoning, any stack's composition and status — all offline, all fast, queryable by keyword, and open to reading and redistribution.

## Quick Start

### Install

```bash
pip install awkno
```

### Use

```bash
# Show a brick
awkno awdk
awkno awsh

# Show a law
awkno law 5

# List everything
awkno list

# Search for a term
awkno search agent
awkno -k silence

# Raw output for piping
awkno awdk --plain
awkno --json awdk
```

### No Arguments

```bash
awkno
```

Shows the overview: command summary, quick start examples, and how to explore further.

## What's Inside

### Bricks (36 tools)

Portable, single-purpose tools that do one job well and compose with others:

- **awdk** — Build AI agent fleets (3 lines, any backend)
- **awskills** — Portable agent skills (self-contained procedures)
- **awm** — Scoped agent memory (tenant:user:project boundaries)
- **awgit** — Semantic version control (edit-ops, leases)
- **awgraph** — Code graph for agents (AST, call graphs)
- **awrelay** — Agent messaging (findings, alerts, coordination)
- **awmail** — Email for agents (send and receive)
- **And 29 more...**

Each has an "adopt" sentence: the smallest useful thing you can do with it alone, without adopting anything else.

### Stacks (9 collections)

Curated sets of bricks that work together:

- **agent-vm** — The bare agent VM
- **agent-senses** — Perception (search, pages)
- **shared-worktree** — Many agents, one repo
- **the-front-door** — Identity, authority, record
- **And 5 more...**

### Laws (18 principles)

Lessons learned in production, written down so they don't have to be re-derived:

1. A rule nothing asserts is a suggestion
2. Make it a check, not a ticket
3. Watch your gate fail
4. Mutate the test, not just the code
5. Design for the silence
6. A check that cannot run must not pass
7. The symptom names the innocent
8. A checker in the wrong place found nothing
9. Detection without delivery is not detection
10. A gate that floods gets switched off
11. Open green; ratchet down
12. Measure it again
13. Written is not deployed
14. You wrote it; that does not mean it ships
15. Generate, never copy
16. The defect lives in the union
17. Fail closed, then prove the happy path
18. Never trust the caller

## Architecture

### Offline-First Design

The corpus is **generated once** from `ecosystem.yaml` and `awskills/codex/laws/`, then **committed as JSON data files** under `awkno/pages/`. After install, the package needs no external files or network.

This means:
- No runtime generation (fast startup)
- No external dependencies beyond stdlib
- Reproducible across machines and time
- Auditable: every page is in the repo

### CLI Features

- **Pager support**: Automatic pagination on TTY (via `$PAGER` or system default)
- **TTY-aware formatting**: ANSI bold headers only when connected to a terminal
- **Multiple output modes**:
  - `--plain` — No ANSI codes (safe for piping to other tools)
  - `--json` — Structured output for scripting
  - Default — Man-page-style formatted text
- **Fuzzy search**: Type something close, get ranked results
- **Command shortcuts**:
  - `awkno list` — Show all topics grouped by category
  - `awkno law N` — Show law by number
  - `awkno -k TERM` / `awkno --apropos TERM` — Search (like `man -k`)

### No Internal Leakage

This package is built for public distribution, and the corpus is GENERATED from
an internal registry -- so the generator strips, and the build then re-checks,
every category of internal detail: infrastructure hostnames, absolute paths from
the build machine, issue-tracker and quality-gate identifiers, and imports that
only resolve inside a private monorepo.

The point of scanning the *generated* corpus rather than the generator is that a
sanitiser is only as good as its last pattern. A page that slips through reads as
ordinary prose, so nothing downstream would ever notice.

## Development

### Regenerate the Corpus

```bash
python awkno/generate.py
```

The generator reads:
- `ecosystem.yaml` — The brick and stack registry
- `awskills/codex/laws/*.md` — The 18 laws

And writes JSON to `awkno/pages/`.

### Test Locally

```bash
pip install -e .
pytest

# Or run the CLI directly
python -m awkno.cli awdk
```

### Build and Publish

```bash
pip install build
python -m build

# Publish to PyPI
twine upload dist/*
```

## Integration

### In Your Own Code

```python
from awkno import AwknoRegistry

registry = AwknoRegistry()
page = registry.get("awdk")
print(page.render())

# Search
results = registry.search("agent memory")
for page, score in results[:5]:
    print(f"{page.topic}: {page.synopsis}")

# List by category
bricks = registry.list_by_category("brick")
laws = registry.list_by_category("law")
```

### As a Dependency

awkno has zero runtime dependencies (PyYAML is dev-only, for corpus generation).

```toml
[project]
dependencies = [
    "awkno",
]
```

## Contributing

Read a law, apply it, send a pull request. The package itself is small and well-documented.

Pages are generated from `ecosystem.yaml` and law files — edits to those files flow into awkno on the next generation.

## License

Apache 2.0. See [LICENSE](LICENSE).

## Further Reading

- Ecosystem registry: https://github.com/Aitherium/ecosystem
- Laws and codex: https://github.com/Aitherium/awskills
- AitherWorld reference: https://aitherium.com

---

**awkno** — read the principles once, apply them everywhere.
