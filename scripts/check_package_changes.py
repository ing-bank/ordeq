#!/usr/bin/env python3
"""Checks for commits between the latest tag and current state for each
package.

This script identifies all packages in the 'packages/' directory and, for
each package,
finds the latest tag in the format '[package]/vX.Y.Z' and lists all commits
that occurred between that tag and the current state.

Usage:
    uv run check_package_changes.py

"""

import json
import subprocess
from datetime import datetime
from pathlib import Path

REPO_ROOT: Path = Path(__file__).resolve().parent.parent


def run_command(command: list[str]) -> str:
    """Runs a shell command and returns its output.

    Args:
        command: List of command arguments

    Returns:
        Output of the command as a string
    """
    result = subprocess.run(
        command, capture_output=True, text=True, check=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()


def get_packages(packages_dir: Path) -> list[str]:
    """Gets a list of package names from the packages directory.

    Args:
        packages_dir: Path to the packages directory

    Returns:
        Package names
    """
    return [d.name for d in packages_dir.iterdir() if d.is_dir()]


def get_latest_tag(package: str) -> tuple[str, datetime] | None:
    """Gets the latest tag for a package in the format '[package]/vX.Y.Z'.

    Args:
        package: Name of the package

    Returns:
        Tuple of (tag, date) if found, None otherwise
    """
    try:
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

        # Get first (most recent) tag and parse
        latest_tag_line = tags_output.split("\n")[0]
        tag, date_str = latest_tag_line.split("|")
        # Get just the date part
        tag_date = datetime.fromisoformat(date_str.split()[0])

        return tag, tag_date
    except (subprocess.CalledProcessError, IndexError, ValueError):
        return None


def get_commits_since_tag(tag: str) -> list[str]:
    """Gets a list of commits between the specified tag and HEAD.

    Args:
        tag: Tag to compare against

    Returns:
        Commits with hash
    """
    try:
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
    except subprocess.CalledProcessError:
        return []


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
        try:
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
        except subprocess.CalledProcessError:  # noqa: PERF203
            # If there's an error checking the files, skip this commit
            continue

    return filtered_commits


def main() -> None:
    """Main function that checks each package for commits since its latest
    tag."""
    packages_dir = REPO_ROOT / "packages"
    packages = get_packages(packages_dir)

    result = {}

    for package in sorted(packages):
        latest_tag = get_latest_tag(package)
        if not latest_tag:
            continue

        tag, tag_date = latest_tag

        commits = get_commits_since_tag(tag)
        if not commits:
            continue

        # Filter commits to only include those that affect this package
        filtered_commits = filter_commits_by_package(commits, package)
        if not filtered_commits:
            continue

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

    # Print the result as a JSON string
    print(json.dumps(result, default=str, indent=4))


if __name__ == "__main__":
    main()
