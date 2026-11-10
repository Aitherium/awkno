# Changelog

Releases before 0.2.8 are on PyPI and in the git history; this file starts at 0.2.8.

## [0.2.9] - 2026-11-10

### Fixed

- **pages**: the public corpus no longer carries internal design-tree paths (`.AITHEROS/`, `.AITHERIUM/`). The generator drops a backticked span or a parenthetical that holds one, then any sentence that still cites one, so no "map: ." stub is left. Three pages (aws, inference-commons, set-and-forget) had shipped them, and the Veil leak check blocked every publish until this fix. Their source texts in `config/ecosystem.yaml` no longer cite the design docs.

## [0.2.8] - 2026-11-08

### Added

- **pages**: the offline corpus now carries every brick in the registry (174 pages, up from 168), so `awkno <brick>` answers for every registered brick and stack
