import logging
from pathlib import Path
from types import ModuleType
from typing import Any, Literal, TypeAlias, overload

from ordeq._fqn import ModuleName
from ordeq._process_nodes_and_ios import process_nodes_and_ios
from ordeq._resolve import _resolve_module_name_to_module
from ordeq._runner import NodeFilter

from ordeq_viz.graph import _gather_graph
from ordeq_viz.to_kedro_viz import graph_to_kedro_viz
from ordeq_viz.to_mermaid import graph_to_mermaid
from ordeq_viz.to_mermaid_md import graph_to_mermaid_md

Vizzable: TypeAlias = ModuleName | ModuleType


logger = logging.getLogger("ordeq.viz")


@overload
def viz(
    *vizzables: Vizzable,
    fmt: Literal["kedro-viz", "mermaid", "mermaid-md"],
    output: Path,
    node_filter: NodeFilter | None = None,
    context: ModuleType | ModuleName | None = None,
    **options: Any,
) -> None: ...


@overload
def viz(
    *vizzables: Vizzable,
    fmt: Literal["mermaid", "mermaid-md"],
    output: None = None,
    node_filter: NodeFilter | None = None,
    context: ModuleType | ModuleName | None = None,
    **options: Any,
) -> str: ...


def viz(
    *vizzables: Vizzable,
    fmt: Literal["kedro-viz", "mermaid", "mermaid-md"],
    output: Path | None = None,
    node_filter: NodeFilter | None = None,
    context: ModuleType | ModuleName | None = None,
    **options: Any,
) -> str | None:
    """Visualize the pipeline from the provided packages, modules, or nodes

    Args:
        vizzables: modules or references to modules to visualize.
        fmt: Format of the output visualization, ("kedro-viz" or "mermaid").
        output: output file or directory where the viz will be saved.
        node_filter: Optional filter to apply to nodes before visualization.
        context: additional modules or references to modules to use as
            context for resolving nodes and IOs.
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

    context_ = [_resolve_module_name_to_module(context)] if context else []
    nodes = process_nodes_and_ios(
        *vizzables, context=context_, node_filter=node_filter
    )

    graph = _gather_graph(nodes, {})

    match fmt:
        case "kedro-viz":
            if not output:
                raise ValueError(
                    "`output` is required when `fmt` is 'kedro-viz'"
                )
            graph_to_kedro_viz(graph, output_directory=output, **options)
        case "mermaid":
            result = graph_to_mermaid(graph, **options)
            if output:
                output.write_text(result, encoding="utf8")
                return None
            return result
        case "mermaid-md":
            result = graph_to_mermaid_md(graph, **options)
            if output:
                output.write_text(result, encoding="utf8")
                return None
            return result
    return None
