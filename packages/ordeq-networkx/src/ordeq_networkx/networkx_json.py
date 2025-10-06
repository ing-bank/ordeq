import json
from dataclasses import dataclass
from typing import Any

import networkx as nx
from ordeq import IO
from ordeq.types import PathLike


@dataclass(frozen=True, kw_only=True)
class NetworkxJSON(IO[nx.Graph]):
    """IO to load from and save graph data using NetworkX's JSON support.
    Calls `networkx.node_link_graph` and `networkx.node_link_data`
    under the hood.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> import networkx as nx
    >>> from ordeq_networkx import NetworkxJSON
    >>> random_graph = nx.erdos_renyi_graph(10, 0.5)
    >>> my_graph = NetworkxJSON(
    ...     path=Path("graph.json")
    ... )
    >>> my_graph.save(random_graph)  # doctest: +SKIP
    ```

    """

    path: PathLike

    def load(self, **load_options: Any) -> nx.Graph:
        """Load a NetworkX graph from a JSON file using node-link format.

        Args:
            **load_options: Additional keyword arguments passed to `json.load`.
                These can be used to control JSON decoding options.

        Returns:
            The loaded NetworkX graph.
        """
        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f, **load_options)
        return nx.node_link_graph(data)

    def save(self, graph: nx.Graph, **save_options: Any) -> None:
        """Save a NetworkX graph to a JSON file using node-link format.

        Args:
            graph: The NetworkX graph to save.
            **save_options: Additional keyword arguments passed to `json.dump`.
                These can be used to control JSON encoding options.

        """
        data = nx.node_link_data(graph)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, **save_options)
