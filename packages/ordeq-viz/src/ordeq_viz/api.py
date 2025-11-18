from pathlib import Path
from types import ModuleType
from typing import Any, Literal, TypeAlias, overload

from ordeq._fqn import ModuleRef
from ordeq._resolve import _resolve_runnables_to_nodes_and_ios

from ordeq_viz.to_kedro_viz import pipeline_to_kedro_viz
from ordeq_viz.to_mermaid import pipeline_to_mermaid
from ordeq_viz.to_mermaid_md import pipeline_to_mermaid_md

Vizzable: TypeAlias = ModuleRef | ModuleType


@overload
def viz(
    *vizzables: Vizzable,
    fmt: Literal["kedro-viz", "mermaid", "mermaid-md"],
    output: Path,
    **options: Any,
) -> None: ...


@overload
def viz(
    *vizzables: Vizzable,
    fmt: Literal["mermaid", "mermaid-md"],
    output: None = None,
    **options: Any,
) -> str: ...


def viz(
    *vizzables: Vizzable,
    fmt: Literal["kedro-viz", "mermaid", "mermaid-md"],
    output: Path | None = None,
    **options: Any,
) -> str | None:
    """Visualize the pipeline from the provided packages, modules, or nodes

    Args:
        vizzables: modules or references to modules to visualize.
        fmt: Format of the output visualization, ("kedro-viz" or "mermaid").
        output: output file or directory where the viz will be saved.
        options: Additional options for the visualization functions.

    Returns:
        If `fmt` is 'mermaid' and `output` is not provided, returns the mermaid
        diagram as a string. Otherwise, returns None.

    Raises:
        TypeError: If any of the `vizzables` are not modules or module
            references.
        ValueError: If `fmt` is 'kedro-viz' and `output` is not provided.
    """

    if not all(isinstance(v, (ModuleType, str)) for v in vizzables):
        raise TypeError(
            "All vizzables must be modules or references to modules."
        )

    nodes, ios = _resolve_runnables_to_nodes_and_ios(*vizzables)
    # TODO: Propagate FQNs to viz
    nodes_ = [node for _, _, node in nodes]
    match fmt:
        case "kedro-viz":
            if not output:
                raise ValueError(
                    "`output` is required when `fmt` is 'kedro-viz'"
                )
            pipeline_to_kedro_viz(
                nodes_, ios, output_directory=output, **options
            )
        case "mermaid":
            result = pipeline_to_mermaid(nodes_, ios, **options)
            if output:
                output.write_text(result, encoding="utf8")
                return None
            return result
        case "mermaid-md":
            result = pipeline_to_mermaid_md(nodes_, ios, **options)
            if output:
                output.write_text(result, encoding="utf8")
                return None
            return result
    return None
