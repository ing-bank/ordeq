#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ordeq-files",
#     "ordeq-toml",
# ]
# ///

"""Script to parse uv.lock and find dependencies of all ordeq packages."""

import logging
from pathlib import Path
from typing import Any

from ordeq import node, run
from ordeq_files import JSON

logging.basicConfig(level=logging.INFO)


ROOT_PATH = Path(__file__).parent.parent

affected_dependencies = JSON(
    path=ROOT_PATH / "scripts" / "affected_dependencies.json"
)
packages = JSON(
    path=Path(__file__).parent / "changed_packages.json"
)
relevant_packages = JSON(
    path=Path(__file__).parent / "relevant_packages.json"
)


@node(inputs=[packages, affected_dependencies], outputs=relevant_packages)
def extract_relevant_packages(
    changed_packages: list[str], affected_deps: dict[str, Any]
) -> list[str]:
    """Extract relevant ordeq packages based on changed packages and affected
    dependencies.

    Args:
        changed_packages: List of changed package names.
        affected_deps: Dictionary mapping package names to their affected
            dependencies.

    Returns:
        List of relevant package names.
    """
    relevant = set(changed_packages)
    for pkg in changed_packages:
        deps = affected_deps.get(pkg, [])
        relevant.update(deps)

    return sorted(relevant)


if __name__ == "__main__":
    run(__name__)
