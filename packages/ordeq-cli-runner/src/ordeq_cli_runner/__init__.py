from argparse import ArgumentParser, Namespace
from typing import get_args

from ordeq import run
from ordeq._runner import SaveMode  # noqa: PLC2701 (private-member-access)


def _create_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="ordeq", description="Framework for data pipeline development"
    )
    parser.add_argument(
        "action",
        help="action to execute (only 'run' is supported)",
        default="run",
        choices=("run",),
    )
    parser.add_argument(
        dest="runnables",
        help="runnables (package, module, or node references)",
        nargs="+",
    )
    parser.add_argument(
        "--hooks",
        dest="hooks",
        help="list of hooks, e.g. domain_A:LogHook domain_B:SparkHook ...",
        nargs="*",
        default=[],
    )
    parser.add_argument(
        "--save",
        choices=get_args(SaveMode),
        help="Which outputs to save: all, or only sinks (outputs with "
        "no successor node)",
        default="all",
    )
    return parser


def parse_args(args: tuple[str, ...] | None = None) -> Namespace:
    """Function to parse the command line arguments

    Args:
        args: optional arguments

    Returns:
        parsed args namespace
    """

    parser = _create_parser()
    known_args, _ = parser.parse_known_args(args=args)
    return known_args


def main() -> None:
    """Main function for the CLI. Parses arguments and triggers the run."""
    args = parse_args()
    run(*args.runnables, hooks=args.hooks, save=args.save)


if __name__ == "__main__":
    main()
