import importlib
from pathlib import Path
from types import ModuleType
from typing import Any, Literal, overload

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
    *modules: ModuleType,
    fmt: Literal["kedro", "mermaid"],
    output: Path,
    **options: Any,
) -> None: ...


@overload
def viz(
    *modules: str,
    fmt: Literal["kedro", "mermaid"],
    output: Path,
    **options: Any,
) -> None: ...


def viz(
    *modules: str | ModuleType,
    fmt: Literal["kedro", "mermaid"],
    output: Path,
    **options: Any,
) -> None:
    """Visualize the pipeline from the provided packages or modules

    Args:
        modules: Package names or modules from which to gather nodes from.
        fmt: Format of the output visualization, ("kedro" or "mermaid").
        output: output file or directory where the viz will be saved.
        options: Additional options for the visualization functions.

    Raises:
        TypeError: if modules are not all modules or all package names
    """
    if all(isinstance(r, ModuleType) for r in modules):
        module_types: tuple[ModuleType, ...] = modules  # type: ignore[assignment]
        nodes = set()
        ios = {}
        for module in module_types:
            nodes.update(_gather_nodes_from_module(module))
            ios.update(gather_ios_from_module(module))
    elif all(isinstance(r, str) for r in modules):
        package_names: tuple[str, ...] = modules  # type: ignore[assignment]
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
    else:
        raise TypeError(
            "All objects provided must be either modules or package names."
        )
    match fmt:
        case "kedro":
            pipeline_to_kedro_viz(
                nodes, ios, output_directory=output, **options
            )
        case "mermaid":
            result = pipeline_to_mermaid(nodes, ios, **options)
            output.write_text(result, encoding="utf8")
