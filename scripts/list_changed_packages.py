#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "ordeq",
#   "ordeq-files",
# ]
# ///

"""Script to extract changed packages from git PR diff."""

import sys
from pathlib import Path

from ordeq import IO, node, run
from ordeq_files import JSON
from utils import run_command  # ty: ignore[unresolved-import]

packages = JSON(path=Path(__file__).parent / "changed_packages.json")
# TODO: replace with view once ordeq/v1.3.0 is released
cf = IO()


@node(outputs=cf)
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


@node(inputs=cf, outputs=packages)
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
        if (
            len(parts) >= 2
            and parts[0] == "packages"
            and parts[1].startswith("ordeq")
        ):
            packages.add(parts[1])
    return sorted(packages)


if __name__ == "__main__":
    run(__name__)
