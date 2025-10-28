"""CLI tools for ordeq development."""

import argparse
import logging
import os
from pathlib import Path
from typing import Final

from ordeq import run

logging.basicConfig(level=logging.INFO)

# Map command names to their module names
COMMAND_TO_MODULE: Final[dict[str, str]] = {
    "changed_packages": "list_changed_packages",
    "list_dependencies": "list_dependencies",
    "viz_tools": "viz_self",
    "compute_relevant_packages": "relevant_packages",
    "generate_draft_releases": "generate_draft_releases",
    "docs_contributing_just": "docs_update_just",
    "docs_package_overview": "docs_package_overview",
}


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser for the CLI.

    Returns:
        Configured argument parser
    """

    parser = argparse.ArgumentParser(description="ordeq development tools")
    parser.add_argument(
        "command",
        choices=list(COMMAND_TO_MODULE.keys()),
        help="Sub-command to run",
    )
    parser.add_argument("repo_path", type=Path, help="Path to the ordeq repository")

    return parser


def main() -> None:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # Construct full module path with prefix
    module_path = f"ordeq_dev_tools.pipelines.{COMMAND_TO_MODULE[args.command]}"
    os.environ["REPOSITORY_ROOT"] = str(args.repo_path.resolve())
    run(module_path)


if __name__ == "__main__":
    main()
