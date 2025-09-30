import json
from dataclasses import dataclass

import networkx as nx
from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class NetworkxJSON(IO[nx.Graph]):
    """IO to load from and save graph data using NetworkX's JSON support.
    Calls `networkx.node_link_graph` and `networkx.node_link_data`
    under the hood.

    Example usage:

    ```python
    >>> from pathlib import Path
    >>> from ordeq_networkx import NetworkxJSON
    >>> MyGraph = NetworkxJSON(
    ...     path=Path("path/to.json")
    ... )

    ```

    """

    path: PathLike

    def load(self, **load_options) -> nx.Graph:
        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f, **load_options)
        return nx.node_link_graph(data)

    def save(self, graph: nx.Graph, **save_options) -> None:
        data = nx.node_link_data(graph)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, **save_options)
