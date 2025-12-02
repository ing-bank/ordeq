import warnings
from collections.abc import Callable, Generator
from dataclasses import replace
from typing import Annotated, TypeAlias

from ordeq import Node
from ordeq._scan import NodeFQNs
from ordeq.preview import preview


def _collect_views(*nodes: Node) -> tuple[Node, ...]:
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


def _assign_node_fqns(*nodes: Node, node_fqns: NodeFQNs) -> Generator[Node]:
    for node in nodes:
        if not node.is_fq and node in node_fqns and len(node_fqns[node]) == 1:
            fqn = node_fqns[node][0]
            yield replace(node, name=fqn.name, module=fqn.module)
        else:
            yield node


def _deduplicate_nodes(*nodes: Node) -> Generator[Node]:
    seen: set[Node] = set()
    for node in nodes:
        if node in seen:
            warnings.warn(
                f"{str(node).capitalize()} was provided more than once. "
                f"Duplicates are ignored.",
                stacklevel=2,
            )
        seen.add(node)
        yield node


def _process_nodes(
    *nodes: Node,
    node_filter: NodeFilter | None = None,
    node_fqns: NodeFQNs | None = None,
) -> tuple[Node, ...]:
    nodes_deduplicated = _deduplicate_nodes(*nodes)
    filtered_nodes = _filter_nodes(
        *nodes_deduplicated, node_filter=node_filter
    )
    nodes_and_views = _collect_views(*filtered_nodes)
    if node_fqns:
        nodes_and_views = tuple(
            _assign_node_fqns(*nodes_and_views, node_fqns=node_fqns)
        )
    return nodes_and_views
