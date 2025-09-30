from dataclasses import dataclass
from pathlib import Path

import networkx as nx
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class NetworkxGML(IO[nx.Graph]):
    """IO to load from and save graph data using NetworkX's GML support.
    Calls `networkx.read_gml` and `networkx.write_gml` under the hood.

    Example usage:

    ```python
    >>> from pathlib import Path
    >>> from ordeq_networkx import NetworkxGML
    >>> MyGraph = NetworkxGML(
    ...     path=Path("path/to.gml")
    ... )

    ```

    """

    path: Path

    def load(self, **load_options) -> nx.Graph:
        return nx.read_gml(self.path, **load_options)

    def save(self, graph: nx.Graph, **save_options) -> None:
        nx.write_gml(graph, self.path, **save_options)
