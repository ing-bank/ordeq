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
from ordeq_files import JSON, Text
from ordeq_toml import TOML

logging.basicConfig(level=logging.INFO)


ROOT_PATH = Path(__file__).parent.parent

lock_file = TOML(path=ROOT_PATH / "uv.lock")
dependencies = JSON(
    path=ROOT_PATH / "scripts" / "dependencies.json"
).with_save_options(indent=4)
diagram = Text(path=ROOT_PATH / "scripts" / "dependencies_diagram.mmd")


def _extract_package_name(pkg_entry: dict[str, Any]) -> str | None:
    """Extract ordeq package name from package entry.

    Args:
        pkg_entry: Package entry from uv.lock

    Returns:
        Package name if it's an ordeq package, None otherwise
    """
    source = pkg_entry.get("source", {})
    if not isinstance(source, dict):
        return None

    editable = source.get("editable", "")
    if not editable.startswith("packages/ordeq"):
        return None

    return editable[9:]  # Remove "packages/" prefix


def _extract_dependencies(metadata: dict[str, Any]) -> set[str]:
    """Extract ordeq dependencies from package metadata.

    Args:
        metadata: Package metadata from uv.lock

    Returns:
        Set of ordeq dependencies
    """
    deps = set()

    # Regular dependencies
    for dep in metadata.get("requires-dist", []):
        if isinstance(dep, dict):
            name = dep.get("name", "")
            if name and name.startswith("ordeq"):
                deps.add(name)

    # Test dependencies
    requires_dev = metadata.get("requires-dev", {})
    if isinstance(requires_dev, dict):
        for dep in requires_dev.get("test", []):
            if isinstance(dep, dict):
                name = dep.get("name", "")
                if name and name.startswith("ordeq"):
                    deps.add(name)

    return deps


@node(inputs=lock_file, outputs=dependencies)
def parse_dependencies(lock_data: dict[str, Any]) -> dict[str, list[str]]:
    """Parse dependencies from uv.lock.

    Args:
        lock_data: data from the uv.lock file

    Returns:
        A dictionary mapping package names to their dependencies
    """
    packages = lock_data.get("package", [])
    if not packages:
        return {}

    deps_by_package: dict[str, list[str]] = {}

    # Process all package entries
    for pkg_entry in packages:
        if not isinstance(pkg_entry, dict):
            continue

        pkg_name = _extract_package_name(pkg_entry)
        if not pkg_name:
            continue

        # Get package metadata
        metadata = pkg_entry.get("metadata")
        if not isinstance(metadata, dict):
            continue

        # Initialize empty list for new packages
        if pkg_name not in deps_by_package:
            deps_by_package[pkg_name] = []

        # Extract and store dependencies
        deps = _extract_dependencies(metadata)
        if deps:
            deps_by_package[pkg_name] = sorted(deps)

    return deps_by_package


@node(inputs=dependencies, outputs=diagram)
def generate_mermaid_diagram(deps_by_package: dict[str, list[str]]) -> str:
    """Generate a Mermaid diagram of package dependencies.

    Args:
        deps_by_package: mapping of package names to their dependencies

    Returns:
        The Mermaid diagram
    """
    lines = ["graph TD"]
    for pkg, deps in deps_by_package.items():
        lines.extend(f"    {pkg} --> {dep}" for dep in deps)
    return "\n".join(lines)


if __name__ == "__main__":
    run(__name__)
