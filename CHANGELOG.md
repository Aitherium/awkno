# Changelog

Releases before 0.2.8 are on PyPI and in the git history; this file starts at 0.2.8.

## [0.3.0] - 2026-11-20

### Fixed

- **docs**: README and the site page were hand-typed — "36 tools, 9 stacks, 18 laws" against a registry holding 97 bricks (71 public) and 29 stacks. `generate.py` now writes `awkno/pages/_stats.json`, stamps the counts between `<!-- awkno:stats -->` markers, and renders the bricks, stacks and laws lists between `<!-- awkno:bricks|stacks|laws -->` markers from the committed corpus. `tests/test_stats.py` fails on drift in either direction, and on a hand-typed count surviving anywhere.
- **corpus**: `AwknoPage` did not carry a stack's `bricks` list, so every stack page failed to load (`unexpected keyword argument 'bricks'`) and 15 tests were red on develop. `from_dict` also ignores keys a newer corpus carries and this build does not.
- **registry**: `_stats.json` is bookkeeping, not a page; the loader skips `_`-prefixed files.
- **generate `--out`**: a run into a temp directory no longer stamps the real README/site (a one-brick test fixture had rewritten them to "1 bricks · 0 stacks · 0 laws").

## [0.2.9] - 2026-11-10

### Fixed

- **pages**: the public corpus no longer carries internal design-tree paths (`.AITHEROS/`, `.AITHERIUM/`). The generator drops a backticked span or a parenthetical that holds one, then any sentence that still cites one, so no "map: ." stub is left. Three pages (aws, inference-commons, set-and-forget) had shipped them, and the Veil leak check blocked every publish until this fix. Their source texts in `config/ecosystem.yaml` no longer cite the design docs.

## [0.2.8] - 2026-11-08

### Added

- **pages**: the offline corpus now carries every brick in the registry (174 pages, up from 168), so `awkno <brick>` answers for every registered brick and stack
