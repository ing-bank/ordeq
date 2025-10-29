"""Pipeline to visualize the development tools."""

from ordeq import node
from ordeq_files import Text
from ordeq_viz import viz

import ordeq_dev_tools
from ordeq_dev_tools.paths import DATA_PATH

ordeq_dev_tools_diagram = Text(path=DATA_PATH / "ordeq_dev_tools_diagram.mmd")


@node(outputs=ordeq_dev_tools_diagram)
def visualize_ordeq_dev_tools() -> str:
    """Visualize the development tools using a mermaid diagram.

    Returns:
        The mermaid diagram representation of the development tools.
    """
    return viz(ordeq_dev_tools, fmt="mermaid")
