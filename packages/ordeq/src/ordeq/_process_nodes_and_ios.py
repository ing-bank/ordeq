import inspect
from collections import defaultdict
from types import ModuleType
from typing import TYPE_CHECKING

from ordeq._fqn import FQN
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
from ordeq._scan import IOFQNs, _scan_fqns
from ordeq._static import _select_canonical_fqn_using_imports

if TYPE_CHECKING:
    from ordeq._io import AnyIO


def _get_missing_io_fqns_from_parameters(
    io_fqns: IOFQNs, nodes_to_process: tuple[Node, ...]
) -> IOFQNs:
    io_param_fqns: defaultdict[AnyIO, list[FQN]] = defaultdict(list)
    for node in nodes_to_process:
        func = node.func
        sig = inspect.signature(func)

        for io, param in zip(
            node.inputs, sig.parameters.values(), strict=True
        ):
            if io not in io_fqns and node.is_fq:
                fqn = FQN(node.module, f"{node.name}:{param.name}")  # type: ignore[arg-type]
                io_param_fqns[io].append(fqn)
    io_fqns.update(io_param_fqns)
    return io_fqns


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

    nodes_processed = _process_nodes(
        *nodes_to_process, node_filter=node_filter, node_fqns=node_fqns
    )

    io_fqns = _select_canonical_fqn_using_imports(io_fqns)
    io_fqns = _get_missing_io_fqns_from_parameters(io_fqns, nodes_processed)

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
