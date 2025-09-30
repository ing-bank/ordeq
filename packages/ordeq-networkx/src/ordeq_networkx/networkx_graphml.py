from dataclasses import dataclass
from pathlib import Path

import networkx as nx
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class NetworkxGraphML(IO[nx.Graph]):
    """IO to load from and save graph data using NetworkX's GraphML support.
    Calls `networkx.read_graphml` and `networkx.write_graphml` under the hood.

    Example usage:

    ```python
    >>> from pathlib import Path
    >>> from ordeq_networkx import NetworkxGraphML
    >>> MyGraph = NetworkxGraphML(
    ...     path=Path("path/to.graphml")
    ... )

    ```

    """

    path: Path

    def load(self, **load_options) -> nx.Graph:
        return nx.read_graphml(self.path, **load_options)

    def save(self, graph: nx.Graph, **save_options) -> None:
        nx.write_graphml(graph, self.path, **save_options)
