from typing import Any

from ordeq_viz.graph import IOData, NodeData
from ordeq_viz.to_mermaid import graph_to_mermaid


def graph_to_mermaid_md(
    graph: tuple[dict[str, list[NodeData]], dict[str | None, list[IOData]]],
    block_char: str = "`",
    **mermaid_options: Any,
) -> str:
    """Generate a mermaid diagram in markdown format.

    Args:
        graph: tuple of node and IO metadata.
        block_char: character to use for code block fencing
        mermaid_options: Additional options for the mermaid diagram.

    Returns:
        The mermaid diagram in markdown format.
    """
    mermaid_diagram = graph_to_mermaid(graph, **mermaid_options)
    return f"{block_char * 3}mermaid\n{mermaid_diagram}\n{block_char * 3}\n"
