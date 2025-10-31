"""Automated release pipeline"""

import json
import logging
import operator
import typing
from typing import Any

from ordeq import IO, node
from ordeq_common import Literal
from ordeq_dev_tools.ios.github_release import GithubRelease
from ordeq_files import JSON
from packaging.version import Version

from ordeq_dev_tools.pipelines.shared import packages
from ordeq_dev_tools.paths import DATA_PATH, ROOT_PATH
from ordeq_dev_tools.utils import run_command


logger = logging.getLogger(__name__)


packages_dir = Literal(ROOT_PATH / "packages")
# TODO: use views
package_latest_tags = IO()
package_commits = IO()
commit_messages = IO()
commit_changes = IO()
package_relevant_commits = IO()
package_relevant_prs = IO()
changes = JSON(path=DATA_PATH / "change_report.json").with_save_options(
    default=str, indent=4
)


def get_tags(package: str) -> list[str] | None:
    """Get all git tags for a given package.

    Args:
        package: The package name, e.g. 'ordeq'.

    Returns:
        A list of tags for the package.
    """
    result = run_command(["git", "tag", "--list", f"{package}/v*"])
    if not result:
        return None
    return result.splitlines()


@node(inputs=packages)
def package_tags(packages: list[str]) -> dict[str, str]:
    """Gets all git tags for all packages.

    Args:
        packages: Package names

    Returns:
        Mapping package names to their tags
    """
    ptags = {}
    for package in sorted(packages):
        tags = get_tags(package)
        if tags is not None:
            ptags[package] = tags
    return ptags


def get_version_from_tag(tag: str) -> Version:
    """Extracts the version from a tag in the format '[package]/vX.Y.Z'.

    Args:
        tag: Tag string

    Returns:
        Version object
    """
    version_str = tag.split("/v")[-1]
    return Version(version_str)


def get_latest_tag(tags: list[str]) -> str | None:
    """Gets the latest tag for a package in the format '[package]/vX.Y.Z'.

    Args:
        tags: package tags

    Returns:
        Tag if found, else None
    """
    if not tags:
        return None

    versions = {tag: get_version_from_tag(tag) for tag in tags}
    latest_tag, _ = max(versions.items(), key=operator.itemgetter(1))
    return latest_tag


@node(inputs=package_tags, outputs=package_latest_tags)
def get_all_latest_tags(package_tags: dict[str, list[str]]) -> dict[str, str]:
    """Gets the latest tag for all packages.

    Args:
        package_tags: Mapping of package names to their tags

    Returns:
        Mapping of package names to their latest tag
    """
    package_latest_tags = {}
    for package, tags in package_tags.items():
        latest_tag = get_latest_tag(tags)
        if latest_tag is not None:
            package_latest_tags[package] = latest_tag
    return package_latest_tags


def get_commits_since_tag(tag: str) -> list[dict[str, str]]:
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
        return []

    commits = []
    for line in commits_output.split("\n"):
        if line.strip():
            commit_hash, commit_message = line.strip().split("|", maxsplit=1)
            commits.append({"hash": commit_hash, "message": commit_message})

    return commits


@node(inputs=package_latest_tags, outputs=[package_commits, commit_messages])
def get_all_commits(
    tags: dict[str, str],
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Gets all commits since the latest tag for all packages.

    Args:
        tags: Mapping of package names to their latest tag

    Returns:
        Mapping of package names to their commits and commit messages
    """
    package_commits = {}
    messages = {}
    for package, tag in tags.items():
        commits = get_commits_since_tag(tag)
        if commits:
            package_commits[package] = [commit["hash"] for commit in commits]
            for commit in commits:
                messages[commit["hash"]] = commit["message"]
    return package_commits, messages


@node(inputs=package_commits, outputs=commit_changes)
def get_commit_changed_files(
    commits_per_package: dict[str, list[str]],
) -> dict[str, list[str]]:
    """Gets the list of changed files for each commit.

    Args:
        commits_per_package: Mapping of package names to their commits

    Returns:
        Mapping of commit hashes to their changed files
    """
    changes = {}
    for commits in commits_per_package.values():
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

            changes[commit] = [
                file for file in changed_files.split("\n") if file.strip()
            ]
    return changes


def filter_commits_by_package(
    commits: list[str], changes_per_commit: dict[str, list[str]], package: str
) -> list[dict[str, str]]:
    """Filters commits to only include those that have changes in the package.

    Args:
        commits: List of commit hashes
        changes_per_commit: List of commits to filter
        package: Package name to filter by

    Returns:
        Filtered list of commits with added 'changed_files' information
    """
    package_path = f"packages/{package}/"
    filtered_commits = []

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
            commit_with_files = {
                "hash": commit,
                "changed_files": package_files,
            }
            filtered_commits.append(commit_with_files)

    return filtered_commits


@node(inputs=[package_commits, commit_changes], outputs=package_relevant_commits)
def filter_commits_by_package_node(
    commit_per_package: dict[str, list[str]],
    changes_per_commit: dict[str, list[str]],
) -> dict[str, list[dict[str, str]]]:
    """Filters commits for each package to only include those that have changes

    Args:
        commit_per_package: Mapping of package names to their commits
        changes_per_commit: Mapping of commit hashes to their changed files

    Returns:
        Mapping of package names to their filtered commits
    """
    package_filtered_commits = {}
    for package, commit_hashes in commit_per_package.items():
        filtered_commits = filter_commits_by_package(
            commit_hashes, changes_per_commit, package
        )
        if filtered_commits:
            package_filtered_commits[package] = filtered_commits
    return package_filtered_commits


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


@node(inputs=[package_relevant_commits], outputs=package_relevant_prs)
def get_relevant_prs(
    commits: dict[str, list[dict[str, str]]],
) -> dict[str, list[dict[str, Any]]]:
    """Gets relevant PRs for each package based on filtered commits.

    Args:
        commits: Mapping of package names to their filtered commits

    Returns:
        Mapping of package names to their relevant PRs
    """
    package_prs = {}
    for package, filtered_commits in commits.items():
        prs = {}
        for commit in filtered_commits:
            pr_info = get_github_pr_by_sha(commit["hash"])
            if pr_info:
                prs[commit["hash"]] = pr_info
        package_prs[package] = prs
    return package_prs


@node
def draft_releases() -> list[str]:
    """Get existing draft GitHub releases.

    Returns:
        List of tag names for draft releases
    """
    drafts_output = run_command(
        [
            "gh",
            "release",
            "list",
            "--json",
            "tagName,isDraft",
            "--jq",
            "[.[] | select(.isDraft == true) | .tagName]",
        ]
    )
    if drafts_output:
        return json.loads(drafts_output)
    return []


@node(
    inputs=[
        package_latest_tags,
        package_relevant_commits,
        package_relevant_prs,
        commit_messages,
    ],
    outputs=changes,
)
def compute_package_changes(
    tags: dict[str, str],
    commits: dict[str, list[dict[str, str]]],
    relevant_prs: dict[str, dict[str, dict[str, Any]]],
    messages,
) -> dict[str, object]:
    result = {}

    for package, filtered_commits in commits.items():
        # Extract just the hashes from filtered_commits
        commit_hashes = [commit["hash"] for commit in filtered_commits]

        # Create a set of all distinct files changed across all commits
        all_changed_files = set()
        for commit in filtered_commits:
            all_changed_files.update(commit.get("changed_files", []))

        # Convert the set back to a sorted list for the JSON output
        distinct_files = sorted(all_changed_files)

        distinct_labels = sorted(
            {
                label
                for pr in relevant_prs[package].values()
                for label in pr.get("labels", [])
            }
        )

        bump = compute_bump(distinct_labels)

        if bump:
            tag = tags[package]
            bumped_version = bump_version(get_version_from_tag(tag), bump)
            new_tag = f"{package}/{bumped_version}"

            changes = {
                commit: {
                    "message": messages[commit],
                    **relevant_prs[package][commit],
                }
                for commit in commit_hashes
            }

            release_notes = generate_release_notes(changes)

            result[package] = {
                "tag": tag,
                "new_tag": new_tag,
                "changes": changes,
                "release_type": bump,
                "release_notes": release_notes,
                "changed_files": distinct_files,
            }

    return result


@node(inputs=[changes, draft_releases])
def create_releases(changes: dict[str, dict[str, str]], releases: list[str]) -> None:
    """Create or update draft GitHub releases based on computed changes.

    Args:
        changes: Mapping of package names to their change info
        releases: List of existing draft release tags
    """
    for info in changes.values():
        new_tag = info["new_tag"]
        if new_tag in releases:
            releases.remove(new_tag)
            mode = "update"
        else:
            mode = "create"
        GithubRelease(tag=info["new_tag"]).save(info["release_notes"], mode=mode)

    if releases:
        logger.info("Deleting remaining outdated draft releases")
        for tag in releases:
            delete_draft_github_release(tag)


def compute_bump(
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
    if "fix" in labels:
        return "patch"
    return None


def bump_version(
    version: Version, bump: typing.Literal["major", "minor", "patch"]
) -> str:
    """Bump the version based on the specified type.

    Args:
        version: A tuple of integers representing the current version, e.g.
            (1, 2, 3).
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


def generate_release_notes(changes):
    categories = {
        "breaking": "Breaking Changes",
        "change": "New Features",
        "fix": "Bug Fixes",
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


def delete_draft_github_release(tag: str) -> None:
    """Delete a draft GitHub release for the given tag.

    Args:
        tag: Tag name
    """
    run_command(["gh", "release", "delete", tag, "--yes"])
    print(f"Deleted draft GitHub release for tag: {tag}")
