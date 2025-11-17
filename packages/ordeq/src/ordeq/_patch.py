from ordeq import Node
from ordeq._io import AnyIO
from ordeq._nodes import View


def _patch_nodes(
    *nodes: Node, patches: dict[AnyIO, AnyIO]
) -> tuple[Node, ...]:
    if patches:
        return tuple(
            node._patch_io(patches)  # type: ignore[arg-type] # noqa: SLF001 (private access)
            for node in nodes
        )
    return nodes


def _patch_view_inputs(*nodes: Node) -> tuple[Node, ...]:
    # Patches view inputs to the view's sentinel IOs.
    # TODO: Can we do this when creating the node?
    view_patches: dict[AnyIO | View, AnyIO] = {}
    for view in [view for view in nodes if isinstance(view, View)]:
        view_patches[view] = view.outputs[0]
    return _patch_nodes(*nodes, patches=view_patches)  # type: ignore[arg-type]
