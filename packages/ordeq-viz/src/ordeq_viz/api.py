import importlib
from collections.abc import Callable
from pathlib import Path
from types import ModuleType
from typing import Any, Literal, overload

from ordeq.framework.nodes import get_node
from ordeq.framework.runner import (
    _gather_nodes_from_module,  # noqa: PLC2701 (private-member-access)
)

from ordeq_viz.gather import (
    gather_ios_from_module,
    gather_nodes_and_ios_from_package,
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

    Raises:
        TypeError: if runnables are not all modules, all package names,
            or all nodes
    """
    if all(isinstance(r, ModuleType) for r in runnables):
        module_types: tuple[ModuleType, ...] = runnables  # type: ignore[assignment]
        nodes = set()
        ios = {}
        for module in module_types:
            nodes.update(_gather_nodes_from_module(module))
            ios.update(gather_ios_from_module(module))
    elif all(isinstance(r, str) for r in runnables):
        package_names: tuple[str, ...] = runnables  # type: ignore[assignment]
        nodes = set()
        ios = {}
        for package in package_names:
            package_mod = importlib.import_module(package)
            nodes.update(_gather_nodes_from_module(package_mod))
            package_nodes, package_ios = gather_nodes_and_ios_from_package(
                package_mod
            )
            nodes.update(package_nodes)
            ios.update(package_ios)
    elif all(callable(r) for r in runnables):
        callables: tuple[Callable, ...] = runnables  # type: ignore[assignment]
        nodes = {get_node(func) for func in callables}
        ios = {}
        for node in nodes:
            mod = importlib.import_module(node.func.__module__)
            ios.update(gather_ios_from_module(mod))
    else:
        raise TypeError(
            "All objects provided must be either modules, package names,"
            " or nodes."
        )
    match fmt:
        case "kedro":
            pipeline_to_kedro_viz(
                nodes, ios, output_directory=output, **options
            )
        case "mermaid":
            result = pipeline_to_mermaid(nodes, ios, **options)
            output.write_text(result, encoding="utf8")
