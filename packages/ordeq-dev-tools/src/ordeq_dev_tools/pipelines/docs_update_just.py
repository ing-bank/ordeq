"""Pipeline to update documentation with the latest `just` command list."""

from ordeq import node, run
from ordeq_files import Text

from ordeq_dev_tools.paths import ROOT_PATH
from ordeq_dev_tools.utils import run_command

docs_file = Text(path=ROOT_PATH / "docs" / "CONTRIBUTING.md")
# TODO: write to self after https://github.com/ing-bank/ordeq/pull/191
updated_docs_file = Text(path=ROOT_PATH / "docs" / "CONTRIBUTING_NEW.md")


@node
def just_output() -> str:
    """Run `just --list` command and return its output as a string.

    Returns:
            Output of `just --list` command.
    """
    return run_command(["just"]) or ""


@node(inputs=just_output)
def docs_just_section(content: str) -> str:
    return f"""```text
    {content}
    ```"""


@node(inputs=[docs_file, docs_just_section], outputs=updated_docs_file)
def update_docs_with_just_section(docs_file: str, just_section: str) -> str:
    """Update the documentation file with the latest `just` command list.

    Args:
        docs_file: The current content of the documentation file.
        just_section: The formatted `just` command list section.

    Returns:
        The updated documentation content.
    """
    start_marker = "<!-- auto-generated justfile commands start -->"
    end_marker = "<!-- auto-generated justfile commands end -->"

    before = docs_file.split(start_marker, maxsplit=1)[0]
    after = docs_file.rsplit(end_marker, maxsplit=1)[-1]

    return before + start_marker + "\n\n" + just_section + "\n\n" + end_marker + after


if __name__ == "__main__":
    run(__name__)
