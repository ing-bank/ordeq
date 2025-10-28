"""CLI tools for ordeq development."""

import argparse
import importlib
import logging
from typing import Final

from ordeq import run

logging.basicConfig(level=logging.INFO)

# Map command names to their module names
COMMAND_TO_MODULE: Final[dict[str, str]] = {
    "changed_packages": "list_changed_packages",
    "list_dependencies": "list_dependencies",
    "viz_tools": "viz_self",
    "compute_relevant_packages": "compute_relevant_packages",
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

    return parser


def main() -> None:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # Construct full module path with prefix
    module_path = f"ordeq_dev_tools.pipelines.{COMMAND_TO_MODULE[args.command]}"
    mod = importlib.import_module(module_path)
    run(mod)


if __name__ == "__main__":
    main()
