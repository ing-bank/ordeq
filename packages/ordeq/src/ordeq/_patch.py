from ordeq import Node
from ordeq._io import AnyIO


def _patch_nodes(
    *nodes: Node, patches: dict[AnyIO, AnyIO]
) -> tuple[Node, ...]:
    if patches:
        return tuple(node._patch_io(patches) for node in nodes)
    return nodes
