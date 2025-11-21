from ordeq import Node
from ordeq._fqn import FQ
from ordeq._io import AnyIO


def _patch_nodes(
    *nodes: FQ[Node], patches: dict[AnyIO, AnyIO]
) -> tuple[FQ[Node], ...]:
    if patches:
        return tuple((fqn, node._patch_io(patches)) for fqn, node in nodes)
    return nodes
