"""Modular pipeline for generating release notes based on
git commits and PRs."""

import json
import operator
import typing
from typing import Any

from ordeq import node, Input, IO
from packaging.version import Version

from ordeq_dev_tools.utils import run_command

# Inputs and outputs for the modular pipeline
package = Input[str]()
release_notes = IO[str]()
new_tag = IO[str]()


@node(inputs=package)
def tags(package: str) -> list[str]:
    """Get all git tags for a given package.

    Args:
        package: The package name, e.g. 'ordeq'.

    Returns:
        A list of tags for the package.
    """
    result = run_command(["git", "tag", "--list", f"{package}/v*"])
    if not result:
        raise ValueError("No tags found for package")
    return result.splitlines()


def get_version_from_tag(tag: str) -> Version:
    """Extracts the version from a tag in the format '[package]/vX.Y.Z'.

    Args:
        tag: Tag string

    Returns:
        Version object
    """
    version_str = tag.split("/v")[-1]
    return Version(version_str)


@node(inputs=tags)
def latest_tag(tags: list[str]) -> str:
    """Gets the latest tag for a package in the format '[package]/vX.Y.Z'.

    Args:
        tags: package tags

    Returns:
        Tag if found, else None
    """
    if not tags:
        raise ValueError("No tags found for package")

    versions = {tag: get_version_from_tag(tag) for tag in tags}
    latest_tag, _ = max(versions.items(), key=operator.itemgetter(1))
    return latest_tag


@node(inputs=latest_tag)
def latest_version(tag: str) -> Version:
    """Gets the latest version from the latest tag.

    Args:
        tag: Latest tag

    Returns:
        Version if tag is provided, else None
    """
    return get_version_from_tag(tag)


@node(inputs=latest_tag)
def commits_since_tag(tag: str) -> dict[str, str]:
    """Gets a list of commits between the specified tag and HEAD.

    Args:
        tag: Tag to compare against

    Returns:
        Commits with hash
    """
    commits_output = run_command(
        [
            "git",
            "log",
            f"{tag}..HEAD",
            "--pretty=format:%h|%s",
            "--date=short",
        ]
    )

    if not commits_output:
        raise ValueError("No commits found since tag")

    commits = {}
    for line in commits_output.split("\n"):
        if line.strip():
            commit_hash, commit_message = line.strip().split("|", maxsplit=1)
            commits[commit_hash] = commit_message

    return commits


@node(inputs=commits_since_tag)
def commit_hashes(commits: dict[str, str]) -> list[str]:
    """Gets commit hashes for a list of commits.

    Args:
        commits: List of commits with hash and message

    Returns:
        List of commit hashes
    """
    return list(commits.keys())


@node(inputs=commit_hashes)
def commit_changed_files(
    commits: list[str],
) -> dict[str, list[str]]:
    """Gets the list of changed files for each commit.

    Args:
        commits: commit SHAs

    Returns:
        Mapping of commit hashes to their changed files
    """
    changes = {}
    for commit in commits:
        # Check if this commit modified files in the package directory
        # Get list of files changed in this commit
        changed_files = run_command(
            [
                "git",
                "diff-tree",
                "--no-commit-id",
                "--name-only",
                "-r",
                commit,
            ]
        )

        changes[commit] = [file for file in changed_files.split("\n") if file.strip()]
    return changes


@node(inputs=[commit_hashes, commit_changed_files, package])
def relevant_commits(
    commits: list[str], changes_per_commit: dict[str, list[str]], package: str
) -> list[str]:
    """Filters commits to only include those that have changes in the package.

    Args:
        commits: List of commit hashes
        changes_per_commit: List of commits to filter
        package: Package name to filter by

    Returns:
        Filtered list of commits with added 'changed_files' information
    """
    package_path = f"packages/{package}/"
    relevant_commits = []

    for commit in commits:
        changed_files = changes_per_commit[commit]
        # Check if this commit modified files in the package directory
        # Filter for files in the package directory
        package_files = [
            file.removeprefix("packages/")
            for file in changed_files
            if file.startswith(package_path)
            and not file.startswith(package_path + "tests/")
        ]

        if package_files:
            relevant_commits.append(commit)
    return relevant_commits


def get_github_pr_by_sha(commit: str) -> dict[str, Any] | None:
    """Get the GitHub PR URL associated with a commit SHA.

    Args:
        commit: Commit SHA

    Returns:
        PR URL if found, else None
    """
    linked_pr = run_command(
        [
            "gh",
            "pr",
            "list",
            "--search",
            commit,
            "--state",
            "merged",
            "--json",
            "number,labels,author",
            "--limit",
            "1",
        ]
    )
    if linked_pr:
        pr_data = json.loads(linked_pr)[0]
        return {
            "number": pr_data["number"],
            "author": pr_data["author"]["login"],
            "labels": [label["name"] for label in pr_data["labels"]],
        }
    return None


@node(inputs=[relevant_commits])
def relevant_prs(
    commits: list[str],
) -> dict[str, dict[str, Any]]:
    """Gets relevant PRs for each package based on filtered commits.

    Args:
        commits: Mapping of package names to their filtered commits

    Returns:
        Mapping of package names to their relevant PRs
    """
    prs = {}
    for commit in commits:
        pr_info = get_github_pr_by_sha(commit)
        if pr_info:
            prs[commit] = pr_info
    return prs


@node(inputs=relevant_prs)
def distinct_labels(prs):
    return sorted({label for pr in prs.values() for label in pr.get("labels", [])})


@node(inputs=distinct_labels)
def bump_type(
    labels: list[str],
) -> typing.Literal["major", "minor", "patch"] | None:
    """Compute the version bump type based on PR labels.

    Args:
        labels: List of PR labels

    Returns:
        Bump type if found, else None
    """
    if "breaking" in labels:
        return "major"
    if "change" in labels:
        return "minor"
    if "fix" in labels or "preview" in labels:
        return "patch"
    raise ValueError("No bump needed based on labels")


@node(inputs=[latest_version, bump_type])
def bump_version(
    version: Version, bump: typing.Literal["major", "minor", "patch"]
) -> str:
    """Bump the version based on the specified type.

    Args:
        version: the current version.
        bump: The type of bump to apply, one of 'major', 'minor', or 'patch'.

    Returns:
        A string representing the new version after the bump.

    Raises:
        ValueError: If the bump type is unknown.
    """

    if bump == "major":
        major, minor, micro = version.major + 1, 0, 0
    elif bump == "minor":
        major, minor, micro = version.major, version.minor + 1, 0
    elif bump == "patch":
        major, minor, micro = version.major, version.minor, version.micro + 1
    else:
        raise ValueError(f"Unknown bump type: {bump}")
    return f"v{major}.{minor}.{micro}"


@node(inputs=[package, bump_version], outputs=new_tag)
def get_new_tag(package: str, bumped_version: str) -> str:
    return f"{package}/{bumped_version}"


@node(inputs=[relevant_commits, commits_since_tag, relevant_prs])
def changes(commits, messages, prs):
    return {
        commit: {
            "message": messages[commit],
            **prs[commit],
        }
        for commit in commits
    }


@node(inputs=changes, outputs=release_notes)
def create_release_notes(changes: dict[str, dict[str, str | list[str]]]) -> str:
    """Generate release notes from a dictionary of changes.

    Args:
        changes: Dictionary mapping change identifiers to change information.

    Returns:
        Release notes as a string.
    """
    categories = {
        "breaking": "Breaking Changes",
        "change": "New Features",
        "preview": "Preview Features",
        "fix": "Bug Fixes or Improvements",
        "docs": "Documentation",
        "internal": "Other Changes",
    }

    def strip_prefix(message: str) -> str:
        """Strip prefix from commit message.

        Args:
            message: Commit message

        Returns:
            Stripped commit message

        Examples:
            "ordeq: Add new feature" -> "Add new feature"
            "Fix bug in module" -> "Fix bug in module"
            "`ordeq-manifest: Update docs" -> "Update docs"
        """
        if ": " in message:
            message = message.split(": ", 1)[1]
            return message[0].upper() + message[1:]
        return message

    groups = {key: [] for key in categories}
    for info in changes.values():
        contribution = strip_prefix(
            info["message"].removesuffix(f" (#{info['number']})")
        )
        author = info["author"]
        pr_id = info["number"]
        labels = info.get("labels", [])

        for label in labels:
            if label in categories:
                groups[label].append((contribution, author, pr_id))
                break

    release_notes = "# Release Notes\n\n"
    release_notes += "This release includes the following changes:\n\n"

    for key, title in categories.items():
        lines = groups.get(key, [])
        if lines:
            release_notes += f"## {title}\n\n"
            for contribution, author, pr_id in lines:
                release_notes += f"- {contribution} by @{author} in #{pr_id}\n"
            release_notes += "\n"

    return release_notes
