from typing import Any

from ordeq import Node
from ordeq._resolve import Catalog

from ordeq_viz.to_mermaid import pipeline_to_mermaid


def pipeline_to_mermaid_md(
    nodes: set[Node],
    ios: Catalog,
    block_char: str = "`",
    **mermaid_options: Any,
) -> str:
    """Generate a mermaid diagram in markdown format.

    Args:
        nodes: nodes
        ios: ios
        block_char: character to use for code block fencing
        mermaid_options: Additional options for the mermaid diagram.

    Returns:
        The mermaid diagram in markdown format.
    """
    mermaid_diagram = pipeline_to_mermaid(nodes, ios, **mermaid_options)
    return f"{block_char * 3}mermaid\n{mermaid_diagram}\n{block_char * 3}\n"
