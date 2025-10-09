from argparse import ArgumentParser, Namespace
from typing import get_args

from ordeq._runner import SaveMode  # noqa: PLC2701 (private-member-access)

from ordeq_cli_runner.runner import run_node_refs, run_pipeline_ref


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
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--nodes",
        dest="nodes",
        help="list of nodes, e.g. domain_A:node_A domain_B:node_B ...",
        nargs="*",
    )
    group.add_argument(
        "--pipeline",
        dest="pipeline",
        help="pipeline, e.g. domain_A:pipeline_A",
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
    """Main function for the CLI. Parses arguments and runs the provided
    nodes."""
    args = parse_args()
    if args.nodes:
        run_node_refs(
            node_refs=args.nodes, hook_refs=args.hooks, save=args.save
        )
    else:
        run_pipeline_ref(
            pipeline_ref=args.pipeline, hook_refs=args.hooks, save=args.save
        )


if __name__ == "__main__":
    main()
