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

    ```pycon
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
        """Load a graph from the GML file at the specified path.

        Args:
            **load_options: Additional keyword arguments passed to
                `networkx.read_gml`. These can be used to control how the
                GML file is parsed (e.g., `label`, `destringizer`).

        Returns:
            The loaded NetworkX graph.
        """
        return nx.read_gml(self.path, **load_options)

    def save(self, graph: nx.Graph, **save_options: Any) -> None:
        """Save a NetworkX graph to the GML file at the specified path.

        Args:
            graph: The NetworkX graph to save.
            **save_options: Additional keyword arguments passed to
                `networkx.write_gml`. These can be used to control how the
                GML file is written (e.g., `stringizer`, `prettyprint`).

        """
        nx.write_gml(graph, self.path, **save_options)
