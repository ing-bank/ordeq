"""Pipeline to list changed packages compared to main branch."""

import sys
from pathlib import Path

from ordeq import node
from ordeq_files import JSON

from ordeq_dev_tools.paths import DATA_PATH
from ordeq_dev_tools.utils import run_command

packages = JSON(path=DATA_PATH / "changed_packages.json").with_save_options(indent=4)


@node
def changed_files() -> list[str]:
    """Get list of changed files compared to main branch.

    Returns:
        List of changed file paths relative to repo root
    """
    cmd = ["git", "diff", "--name-only", "origin/main", "HEAD"]
    result = run_command(cmd)
    if result is None:
        print("Error running git diff", file=sys.stderr)
        sys.exit(1)
    return result.splitlines()


@node(inputs=changed_files, outputs=packages)
def extract_changed_packages(changed_files: list[str]) -> list[str]:
    """Extract unique package names from changed files.

    Args:
        changed_files: List of changed file paths

    Returns:
        List of package names that have changes
    """
    packages = set()
    for file_path in changed_files:
        parts = Path(file_path).parts
        # Look for files under packages/ordeq*
        if len(parts) >= 2 and parts[0] == "packages" and parts[1].startswith("ordeq"):
            packages.add(parts[1])
    return sorted(packages)
