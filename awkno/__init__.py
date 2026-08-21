"""awkno — The man page for the Aither World.

    from awkno import AwknoRegistry

    registry = AwknoRegistry()
    page = registry.get("awdk")
    print(page.render())

Every brick, stack and law in your terminal, offline. No external dependencies,
no network required. Pages are generated from ecosystem.yaml and the laws corpus,
committed as data files.
"""

from __future__ import annotations

from awkno.corpus import AwknoPage, AwknoRegistry, NotFoundError

__version__ = "0.1.0"

__all__ = [
    "AwknoRegistry",
    "AwknoPage",
    "NotFoundError",
    "__version__",
]
