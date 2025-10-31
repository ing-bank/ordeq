from dataclasses import dataclass

from ordeq import Output
from typing import Literal
from ordeq_dev_tools.utils import run_command


def _create_draft_github_release(new_tag: str, release_notes: str) -> None:
    """Create a draft GitHub release for the new tag.

    Args:
        new_tag: New tag name
        release_notes: Changes dictionary
    """
    run_command(
        [
            "gh",
            "release",
            "create",
            new_tag,
            "--draft",
            "--title",
            new_tag,
            "--notes",
            release_notes,
            "--latest=false" if not new_tag.startswith("ordeq/") else "--latest",
        ]
    )


def _update_release_notes(existing_tag: str, release_notes: str) -> None:
    """Update the release notes for an existing GitHub release.

    Args:
        existing_tag: Existing tag name
        release_notes: New release notes
    """
    run_command(
        [
            "gh",
            "release",
            "edit",
            existing_tag,
            "--draft",
            "--notes",
            release_notes,
        ]
    )


@dataclass
class GithubRelease(Output):
    tag: str

    def save(
        self, release_notes: str, mode: Literal["create", "update"] = "create"
    ) -> None:
        """Save the release notes to the GitHub release identified by the tag.

        Args:
            release_notes: The release notes content to be saved.
            mode: Mode of operation, either "create" to create a new draft release
                      or "update" to update an existing release's notes.
        """
        if mode == "create":
            _create_draft_github_release(self.tag, release_notes)
        else:
            _update_release_notes(self.tag, release_notes)
