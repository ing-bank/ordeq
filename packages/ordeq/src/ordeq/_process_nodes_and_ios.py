from types import ModuleType
from typing import TYPE_CHECKING

from ordeq._nodes import Node, View
from ordeq._process_ios import _process_ios
from ordeq._process_nodes import NodeFilter, _process_nodes, _validate_nodes
from ordeq._resolve import (
    Catalog,
    Runnable,
    RunnableRef,
    _deduplicate_modules,
    _resolve_modules_to_nodes,
    _resolve_packages_to_modules,
    _resolve_runnable_refs_to_modules,
    _resolve_runnable_refs_to_nodes,
    _validate_runnables,
)
from ordeq._scan import _scan_fqns
from ordeq._static import _select_canonical_fqn_using_imports

if TYPE_CHECKING:
    from ordeq._io import AnyIO


def process_nodes_and_ios(
    *runnables: Runnable | RunnableRef,
    context: list[ModuleType],
    node_filter: NodeFilter | None = None,
) -> tuple[Node, ...]:
    _validate_runnables(*runnables)
    modules_to_process = _resolve_runnable_refs_to_modules(*runnables)
    nodes_to_process = _resolve_runnable_refs_to_nodes(*runnables)
    nodes_to_process += _resolve_modules_to_nodes(*modules_to_process)
    submodules_to_process = _resolve_packages_to_modules(*modules_to_process)
    submodules_to_process = _deduplicate_modules(*submodules_to_process)
    submodules_context = _resolve_packages_to_modules(*context)
    node_fqns, io_fqns = _scan_fqns(
        *submodules_context, *submodules_to_process
    )
    node_fqns = _select_canonical_fqn_using_imports(node_fqns)
    io_fqns = _select_canonical_fqn_using_imports(io_fqns)

    nodes_processed = _process_nodes(
        *nodes_to_process, node_filter=node_filter, node_fqns=node_fqns
    )
    nodes_processed = _process_ios(*nodes_processed, io_fqns=io_fqns)
    _validate_nodes(*nodes_processed)
    return nodes_processed


def _check_missing_ios(nodes: set[Node], ios: Catalog) -> None:
    missing_ios: set[AnyIO | View] = set()
    for node in nodes:
        for inp in node.inputs:
            if inp not in ios.values():
                missing_ios.add(inp)
        for out in node.outputs:
            if out not in ios.values():
                missing_ios.add(out)

    if missing_ios:
        raise ValueError(
            f"The following IOs are used by nodes but not defined: "
            f"{missing_ios}. Please include the module defining them in "
            f"the runnables."
        )
