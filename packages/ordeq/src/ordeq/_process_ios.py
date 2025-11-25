from itertools import chain

from ordeq._nodes import Node
from ordeq._scan import IOFQNs


def _assign_io_fqns(*nodes: Node, io_fqns: IOFQNs) -> None:
    for node in nodes:
        for io in chain(node.inputs, node.outputs):
            io_id = id(io)
            if io_id in io_fqns and len(io_fqns[io_id]) == 1:
                io._set_fqn(io_fqns[io_id][0])  # type: ignore[attr-defined]


def _process_ios(
    *nodes: Node, io_fqns: IOFQNs | None = None
) -> tuple[Node, ...]:
    if io_fqns:
        _assign_io_fqns(*nodes, io_fqns=io_fqns)
    return nodes
