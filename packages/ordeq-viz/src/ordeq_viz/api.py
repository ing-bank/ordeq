from pathlib import Path
from typing import Any, Literal, overload

from ordeq._resolve import (
    _resolve_runnables_to_nodes_and_ios,  # noqa: PLC2701 (private-member-access)
)
from ordeq._runner import Runnable

from ordeq_viz.to_kedro_viz import pipeline_to_kedro_viz
from ordeq_viz.to_mermaid import pipeline_to_mermaid


@overload
def viz(
    *runnables: Runnable,
    fmt: Literal["kedro-viz", "mermaid"],
    output: Path,
    **options: Any,
) -> None: ...


@overload
def viz(
    *runnables: Runnable,
    fmt: Literal["mermaid"],
    output: None = None,
    **options: Any,
) -> str: ...


def viz(
    *runnables: Runnable,
    fmt: Literal["kedro-viz", "mermaid"],
    output: Path | None = None,
    **options: Any,
) -> str | None:
    """Visualize the pipeline from the provided packages, modules, or nodes

    Args:
        runnables: Package names, modules, or node callables from which to
            gather nodes from.
        fmt: Format of the output visualization, ("kedro-viz" or "mermaid").
        output: output file or directory where the viz will be saved.
        options: Additional options for the visualization functions.

    Returns:
        If `fmt` is 'mermaid' and `output` is not provided, returns the mermaid
        diagram as a string. Otherwise, returns None.

    Raises:
        ValueError: If `fmt` is 'kedro-viz' and `output` is not provided.
    """

    nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)

    match fmt:
        case "kedro-viz":
            if not output:
                raise ValueError(
                    "`output` is required when `fmt` is 'kedro-viz'"
                )
            pipeline_to_kedro_viz(
                nodes, ios, output_directory=output, **options
            )
        case "mermaid":
            result = pipeline_to_mermaid(nodes, ios, **options)
            if output:
                output.write_text(result, encoding="utf8")
            return result
    return None
