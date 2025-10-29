"""Pipeline that extracts relevant ordeq packages based on changed packages and
affected dependencies."""

from typing import Any

from ordeq import node
from ordeq_files import JSON

from ordeq_dev_tools.paths import DATA_PATH

affected_dependencies = JSON(
    path=DATA_PATH / "affected_dependencies.json"
).with_save_options(indent=4)
packages = JSON(path=DATA_PATH / "changed_packages.json").with_save_options(indent=4)
relevant_packages = JSON(path=DATA_PATH / "relevant_packages.json")


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
