from typing import TYPE_CHECKING

from ordeq._nodes import Node, View
from ordeq._process_ios import _process_ios
from ordeq._process_nodes import NodeFilter, _process_nodes, _validate_nodes
from ordeq._resolve import (
    Catalog,
    Runnable,
    _resolve_modules_to_nodes,
    _resolve_runnable_refs_to_runnables,
    _validate_runnables,
)
from ordeq._scan import _scan_fqns

if TYPE_CHECKING:
    from ordeq._io import AnyIO


def process_nodes_and_ios(
    *runnables: Runnable,
    context: list[Runnable],
    node_filter: NodeFilter | None = None,
) -> tuple[Node, ...]:
    _validate_runnables(*runnables)
    modules, nodes = _resolve_runnable_refs_to_runnables(*runnables)
    nodes += _resolve_modules_to_nodes(*modules)
    node_fqns, io_fqns = _scan_fqns(*context, *modules)
    nodes_processed = _process_nodes(
        *nodes, node_filter=node_filter, node_fqns=node_fqns
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
