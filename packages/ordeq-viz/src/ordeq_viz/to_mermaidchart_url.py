import base64
import json
import zlib
from typing import Any

from ordeq_viz.graph import IOData, NodeData
from ordeq_viz.to_mermaid import graph_to_mermaid


def _encode_pako(code: str, config=None) -> str:
    if config is None:
        config = {}
    graph = {"code": code, "mermaid": config}
    compress = zlib.compressobj(
        9, zlib.DEFLATED, 15, 8, zlib.Z_DEFAULT_STRATEGY
    )
    compressed_data = (
        compress.compress(bytes(json.dumps(graph), "ascii")) + compress.flush()
    )
    return "#pako:" + base64.b64encode(compressed_data).decode(
        "ascii"
    ).replace("+", "-").replace("/", "_")


def graph_to_mermaidchart_url(
    graph: tuple[dict[str, list[NodeData]], dict[str | None, list[IOData]]],
    base_url: str = "https://www.mermaidchart.com/play",
    **mermaid_options: Any,
) -> str:
    """Generate a mermaidchart.com URL for the given graph.
    Take in mind that this is an external service and your graph data will be
    sent to their server.

    Args:
        graph: tuple of node and IO metadata.
        base_url: Base URL for mermaidchart.com
        mermaid_options: Additional options for the mermaid diagram.

    Returns:
        The mermaidchart.com URL.

    """
    mermaid_diagram = graph_to_mermaid(graph, **mermaid_options)
    encoded_diagram = _encode_pako(mermaid_diagram)
    return base_url + encoded_diagram
