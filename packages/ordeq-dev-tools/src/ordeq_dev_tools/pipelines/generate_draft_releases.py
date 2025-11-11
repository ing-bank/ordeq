"""Automated release pipeline"""

import json
import logging

from ordeq import node, run
from ordeq_common import Literal

from ordeq_dev_tools.ios.github_release import GithubRelease
from ordeq_dev_tools.pipelines import generate_release_notes
from ordeq_dev_tools.pipelines.shared import packages
from ordeq_dev_tools.utils import run_command


logger = logging.getLogger(__name__)


def delete_draft_github_release(tag: str) -> None:
    """Delete a draft GitHub release for the given tag.

    Args:
        tag: Tag name
    """
    run_command(["gh", "release", "delete", tag, "--yes"])
    print(f"Deleted draft GitHub release for tag: {tag}")


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


@node(inputs=[packages])
def new_releases(package_names):
    new_release_data = {}
    for p in package_names:
        try:
            run(generate_release_notes, io={generate_release_notes.package: Literal(p)})
            tag = generate_release_notes.new_tag.load()
            notes = generate_release_notes.release_notes.load()
            new_release_data[tag] = notes
        except ValueError:
            print(f"No new release for package {p}")
    return new_release_data


@node(inputs=[new_releases, draft_releases])
def create_releases(changes: dict[str, str], releases: list[str]) -> None:
    """Create or update draft GitHub releases based on computed changes.

    Args:
        changes: Mapping of package names to their change info
        releases: List of existing draft release tags
    """
    for new_tag, release_notes in changes.items():
        if new_tag in releases:
            releases.remove(new_tag)
            mode = "update"
        else:
            mode = "create"
        GithubRelease(tag=new_tag).save(release_notes, mode=mode)

    if releases:
        logger.info("Deleting remaining outdated draft releases")
        for tag in releases:
            delete_draft_github_release(tag)


if __name__ == "__main__":
    run(__name__)
