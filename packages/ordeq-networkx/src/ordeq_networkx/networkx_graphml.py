from dataclasses import dataclass
from pathlib import Path
from typing import Any

import networkx as nx
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class NetworkxGraphML(IO[nx.Graph]):
    """IO to load from and save graph data using NetworkX's GraphML support.
    Calls `networkx.read_graphml` and `networkx.write_graphml` under the hood.

    Example usage:

    ```python
    >>> from pathlib import Path
    >>> import networkx as nx
    >>> from ordeq_networkx import NetworkxGraphML
    >>> random_graph = nx.erdos_renyi_graph(10, 0.5)
    >>> my_graph = NetworkxGraphML(
    ...     path=Path("graph.graphml")
    ... )
    >>> my_graph.save(random_graph)  # doctest: +SKIP
    ```

    """

    path: Path

    def load(self, **load_options: Any) -> nx.Graph:
        return nx.read_graphml(self.path, **load_options)

    def save(self, graph: nx.Graph, **save_options: Any) -> None:
        nx.write_graphml(graph, self.path, **save_options)
