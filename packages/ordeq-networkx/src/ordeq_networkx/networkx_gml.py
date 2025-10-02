from dataclasses import dataclass
from pathlib import Path
from typing import Any

import networkx as nx
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class NetworkxGML(IO[nx.Graph]):
    """IO to load from and save graph data using NetworkX's GML support.
    Calls `networkx.read_gml` and `networkx.write_gml` under the hood.

    Example usage:

    ```python
    >>> from pathlib import Path
    >>> import networkx as nx
    >>> from ordeq_networkx import NetworkxGML
    >>> random_graph = nx.erdos_renyi_graph(10, 0.5)
    >>> my_graph = NetworkxGML(
    ...     path=Path("graph.gml")
    ... )
    >>> my_graph.save(random_graph)  # doctest: +SKIP

    ```

    """

    path: Path

    def load(self, **load_options: Any) -> nx.Graph:
        return nx.read_gml(self.path, **load_options)

    def save(self, graph: nx.Graph, **save_options: Any) -> None:
        nx.write_gml(graph, self.path, **save_options)
