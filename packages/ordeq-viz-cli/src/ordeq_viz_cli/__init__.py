from argparse import ArgumentParser, Namespace
from pathlib import Path

from ordeq_viz.api import viz


def _create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        "packages",
        metavar="package.subpackage package2",
        nargs="+",
        help=(
            "Point to the Python package(s) for which to gather the nodes "
            "for the pipeline."
        ),
    )
    parser.add_argument(
        "--output",
        "-o",
        metavar="path/to/output",
        help="Output file or directory to write the visualizations to. ",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "--fmt",
        "-fmt",
        metavar="FORMAT",
        help=(
            "Output format for the visualization. "
            "Supported formats: kedro, mermaid."
        ),
        choices=("kedro", "mermaid", "mermaid_md"),
        default="mermaid",
    )
    # Allow any options as --option key=value
    parser.add_argument(
        "--option",
        metavar="KEY=VALUE",
        help=(
            "Additional options for the visualization functions, "
            "specified as key=value pairs."
        ),
        action="append",
        default=[],
    )
    return parser


def parse_args(args: tuple[str, ...] | None = None) -> Namespace:
    """Function to parse the command line arguments.

    Args:
        args: optional arguments

    Returns:
        parsed args namespace
    """

    parser = _create_parser()
    known_args, _ = parser.parse_known_args(args=args)
    return known_args


def main() -> None:
    """Main function for the CLI. Parses arguments and runs the viz."""

    args = parse_args()
    extra_options = {}
    for option in args.option:
        key, value = option.split("=", 1)
        extra_options[key] = value

    viz(*args.packages, fmt=args.fmt, output=args.output, **extra_options)
