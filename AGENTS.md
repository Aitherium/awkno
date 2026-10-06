# awkno for agents

Read this if you are an agent (or a human) editing this package. Short on
purpose: the commands, the traps that cost a session, and where the rest lives.
Nothing here is read at runtime — it is for you.

## What this is

PyPI distribution **`awkno`** (version in `pyproject.toml`), import package
`awkno`, Python >= 3.10. The man page for the Aither World: every brick, stack
and law, offline — a generated corpus of committed JSON pages plus the CLI and
API that read it.

This repository is a **synced mirror** of the AitherOS monorepo (lane
`.github/workflows/sync-awkno.yml`). Hand edits made here are overwritten on
the next sync — change the source and let the lane publish.

## Build, test, verify

```bash
python -m pytest tests -q        # the suite: 25 tests, green at v0.2.6
python awkno/generate.py         # regenerate the committed corpus (158 pages)
pip install -e .                 # editable install for developing against it
```

The suite was run from a source checkout with no prior install. The publish
lane (`publish-brick.yml`) additionally builds the wheel, installs it and
imports it — a tree that tests green can still ship a broken wheel.

## Rules that keep this useful

- **The corpus is GENERATED and COMMITTED.** Pages under `awkno/pages/` come
  from the ecosystem registry and the law files (`python awkno/generate.py`).
  After ANY change to a registry entry or a law, regenerate before committing
  — a page is public the moment it is generated, and the registry-drift check
  fails the lane when the committed pages lag a fresh render.
- **A page is a public artifact; the leak gate is real.** `LOCAL_PATH_RE`
  (in `awkno/generate.py`, imported by the tests rather than restated) refuses
  any page text carrying a local path shape or a monorepo tree name. It has
  already caught a real leak: an `install:` line that spelled out a monorepo
  path. Keep registry prose free of paths.
- **The registry drives the public surface.** This repo's README header,
  `llms.txt` and `aither-manifest.json` are generated from the ecosystem
  registry (one yaml in the AitherOS monorepo) and rewritten on every sync.
  Change the registry; do not hand-edit the generated blocks.
- **The install line is a measured claim.** `check_ecosystem_install_lines`
  asserts the advertised `pip install` channel is real and ours. A rename or
  a move lands with the registry entry in the same change.

## Read next

- `llms.txt` — the install/use card written for an agent to execute
- `README.md` — the human front door, including the corpus generation story
- `docs/` — the generated docs site source
