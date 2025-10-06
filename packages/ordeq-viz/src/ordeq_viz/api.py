from collections.abc import Callable
from pathlib import Path
from types import ModuleType
from typing import Any, Literal, overload

from ordeq.framework._gather import (
    _collect_nodes_and_ios,  # noqa: PLC2701 (private-member-access)
)

from ordeq_viz.to_kedro_viz import pipeline_to_kedro_viz
from ordeq_viz.to_mermaid import pipeline_to_mermaid


@overload
def viz(
    *runnables: ModuleType,
    fmt: Literal["kedro", "mermaid"],
    output: Path,
    **options: Any,
) -> None: ...


@overload
def viz(
    *runnables: str,
    fmt: Literal["kedro", "mermaid"],
    output: Path,
    **options: Any,
) -> None: ...


@overload
def viz(
    *runnables: Callable,
    fmt: Literal["kedro", "mermaid"],
    output: Path,
    **options: Any,
) -> None: ...


def viz(
    *runnables: str | ModuleType | Callable,
    fmt: Literal["kedro", "mermaid"],
    output: Path,
    **options: Any,
) -> None:
    """Visualize the pipeline from the provided packages, modules, or nodes

    Args:
        runnables: Package names, modules, or node callables from which to
            gather nodes from.
        fmt: Format of the output visualization, ("kedro" or "mermaid").
        output: output file or directory where the viz will be saved.
        options: Additional options for the visualization functions.

    """

    nodes, ios = _collect_nodes_and_ios(*runnables)

    match fmt:
        case "kedro":
            pipeline_to_kedro_viz(
                nodes, ios, output_directory=output, **options
            )
        case "mermaid":
            result = pipeline_to_mermaid(nodes, ios, **options)
            output.write_text(result, encoding="utf8")
