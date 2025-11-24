from collections.abc import Callable
from typing import Annotated, TypeAlias

from ordeq import Node
from ordeq.preview import preview


def _collect_views(*nodes: Node) -> tuple[Node, ...]:
    # Views are granted an "unknown" FQN for consistency with other nodes.
    # TODO: see if the view appears in the scanned modules,
    #  and assign the correct FQN.
    all_nodes: dict[Node, None] = {}

    def _collect(*nodes_: Node) -> None:
        for node in nodes_:
            all_nodes[node] = None
            for view in node.views:
                _collect(view)

    _collect(*nodes)
    return tuple(all_nodes.keys())


NodeFilter: TypeAlias = Annotated[
    Callable[[Node], bool],
    """Method for filtering nodes. The method should take `ordeq.Node` as
only argument and return `bool`.

Examples:

>>> def filter_daily(node: Node) -> bool:
...     # Filters all nodes with `@node(..., frequency="daily")`
...     return node.attributes.get("frequency", None) == "daily"

>>> def filter_spark_iceberg(node: Node) -> bool:
...     # Filters all nodes that have use SparkIcebergTable
...     return (
...         SparkIcebergTable in {
...             type(t) for t in [*node.inputs, *node.outputs]
...         }
...     )

>>> def filter_ml(node: Node) -> bool:
...     # Filters all nodes with `@node(..., group="ml")`
...     return node.attributes.get("group", None) == "ml"

""",
]


def _filter_nodes(
    *nodes: Node, node_filter: NodeFilter | None = None
) -> tuple[Node, ...]:
    if not node_filter:
        return nodes

    preview(
        "Node filters are in preview mode and may change "
        "without notice in future releases."
    )
    return tuple(node for node in nodes if node_filter(node))


def _validate_nodes(*nodes: Node) -> None:
    for node in nodes:
        node.validate()


def _process_nodes(
    *nodes: Node, node_filter: NodeFilter | None = None
) -> tuple[Node, ...]:
    filtered_nodes = _filter_nodes(*nodes, node_filter=node_filter)
    return tuple(_collect_views(*filtered_nodes))
