#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "ordeq",
#     "ordeq-files",
#     "ordeq-common",
# ]
# ///
"""Checks for commits between the latest tag and current state for each
package.

This script identifies all packages in the 'packages/' directory and, for
each package,
finds the latest tag in the format '[package]/vX.Y.Z' and lists all commits
that occurred between that tag and the current state.

Usage:
    uv run check_package_changes.py

"""

import subprocess
from collections.abc import Generator, Iterable
from datetime import datetime
from pathlib import Path

from ordeq import IO, node, run
from ordeq_common import Literal
from ordeq_files import JSON

REPO_ROOT: Path = Path(__file__).resolve().parent.parent


packages_dir = Literal(REPO_ROOT / "packages")
packages = IO()
tags = IO()
commits = IO()
filtered_commits = IO()
changes = JSON(path=Path("change_report.json")).with_save_options(
    default=str, indent=4
)


def run_command(command: list[str]) -> str | None:
    """Runs a shell command and returns its output.

    Args:
        command: List of command arguments

    Returns:
        Output of the command as a string
    """
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, check=True, cwd=REPO_ROOT
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


@node(inputs=packages_dir, outputs=packages)
def get_packages(packages_dir: Path) -> list[str]:
    """Gets a list of package names from the packages directory.

    Args:
        packages_dir: Path to the packages directory

    Returns:
        Package names
    """
    return sorted([d.name for d in packages_dir.iterdir() if d.is_dir()])


def get_latest_tag(package: str) -> tuple[str, datetime] | None:
    """Gets the latest tag for a package in the format '[package]/vX.Y.Z'.

    Args:
        package: Name of the package

    Returns:
        Tuple of (tag, date) if found, None otherwise
    """
    # List tags with dates in ISO format for parsing
    tags_output = run_command([
        "git",
        "tag",
        "--list",
        f"{package}/v*",
        "--sort=-creatordate",
        "--format=%(refname:short)|%(creatordate:iso)",
    ])

    if not tags_output:
        return None

    try:
        # Get first (most recent) tag and parse
        latest_tag_line = tags_output.split("\n")[0]
        tag, date_str = latest_tag_line.split("|")
        # Get just the date part
        tag_date = datetime.fromisoformat(date_str.split()[0])

        return tag, tag_date
    except (IndexError, ValueError):
        return None


def get_commits_since_tag(tag: str) -> list[str]:
    """Gets a list of commits between the specified tag and HEAD.

    Args:
        tag: Tag to compare against

    Returns:
        Commits with hash
    """
    commits_output = run_command([
        "git",
        "log",
        f"{tag}..HEAD",
        "--pretty=format:%h",
        "--date=short",
    ])

    if not commits_output:
        return []

    return [
        line.strip() for line in commits_output.split("\n") if line.strip()
    ]


def filter_commits_by_package(
    commits: list[str], package: str
) -> list[dict[str, str]]:
    """Filters commits to only include those that have changes in the package.

    Args:
        commits: List of commits to filter
        package: Package name to filter by

    Returns:
        Filtered list of commits with added 'changed_files' information
    """
    package_path = f"packages/{package}/"
    filtered_commits = []

    for commit in commits:
        # Check if this commit modified files in the package directory
        # Get list of files changed in this commit
        changed_files = run_command([
            "git",
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "-r",
            commit,
        ])

        # Split the output into individual files
        changed_files_list = [
            file for file in changed_files.split("\n") if file.strip()
        ]

        # Filter for files in the package directory
        package_files = [
            file.removeprefix("packages/")
            for file in changed_files_list
            if file.startswith(package_path)
        ]

        if package_files:
            commit_with_files = {
                "hash": commit,
                "changed_files": package_files,
            }
            filtered_commits.append(commit_with_files)

    return filtered_commits


@node(inputs=packages, outputs=tags)
def get_latest_tags(
    packages: list[str],
) -> Generator[tuple[str, tuple[str, datetime]], None, None]:
    for package in sorted(packages):
        latest_tag = get_latest_tag(package)
        if latest_tag:
            yield package, latest_tag


@node(inputs=tags, outputs=commits)
def get_all_commits(
    tags: Iterable[tuple[str, tuple[str, datetime]]],
) -> Generator[tuple[str, tuple[str, datetime], list[str]], None, None]:
    for package, (tag, tag_date) in sorted(tags):
        commits = get_commits_since_tag(tag)
        if commits:
            yield package, (tag, tag_date), commits


@node(inputs=commits, outputs=filtered_commits)
def filter_commits_by_package_node(
    commits: Iterable[tuple[str, tuple[str, datetime], list[str]]],
) -> Generator[
    tuple[str, tuple[str, datetime], list[dict[str, str]]], None, None
]:
    for package, (tag, tag_date), commit_hashes in sorted(commits):
        filtered_commits = filter_commits_by_package(commit_hashes, package)
        if filtered_commits:
            yield package, (tag, tag_date), filtered_commits


@node(inputs=filtered_commits, outputs=changes)
def compute_package_changes(tags: list[str]) -> dict[str, object]:
    result = {}

    for package, (tag, tag_date), filtered_commits in sorted(tags):
        # Extract just the hashes from filtered_commits
        commit_hashes = [commit["hash"] for commit in filtered_commits]

        # Create a set of all distinct files changed across all commits
        all_changed_files = set()
        for commit in filtered_commits:
            all_changed_files.update(commit.get("changed_files", []))

        # Convert the set back to a sorted list for the JSON output
        distinct_files = sorted(all_changed_files)

        result[package] = {
            "tag": tag,
            "date": tag_date,
            "commits": commit_hashes,
            "changed_files": distinct_files,
        }

    return result


if __name__ == "__main__":
    # run all nodes
    run(__name__)
