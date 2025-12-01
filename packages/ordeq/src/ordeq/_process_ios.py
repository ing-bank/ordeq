from itertools import chain

from ordeq._nodes import Node
from ordeq._scan import IOFQNs


def _assign_io_fqns(*nodes: Node, io_fqns: IOFQNs) -> None:
    for node in nodes:
        for io in chain(node.inputs, node.outputs):
            if io in io_fqns:
                if len(io_fqns[io]) == 1:  # type: ignore[index]
                    io._set_fqn(io_fqns[io][0])  # type: ignore[index]
                elif len(io_fqns[io]) > 1:  # type: ignore[index]
                    io._set_name(io_fqns[io][0].name)  # type: ignore[index]


def _process_ios(
    *nodes: Node, io_fqns: IOFQNs | None = None
) -> tuple[Node, ...]:
    if io_fqns:
        _assign_io_fqns(*nodes, io_fqns=io_fqns)
    return nodes
