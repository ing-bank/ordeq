## Resource

```python
from typing import Any

import pandas as pd
from ordeq import IO, node, run
from ordeq_common import Literal
from ordeq_viz import viz

txs = Literal(
    pd.DataFrame({
        "id": [1, 2, 3],
        "amount": [100, 200, 300],
        "to": ["me", "me", "you"],
        "country": ["NL", "BE", "US"],
    })
)
txs_agg_invalid = IO[Any]()


@node(inputs=txs)
def txs_agg(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupby("country").agg({"amount": "sum"})


@node(inputs=txs_agg, checks=txs_agg)
def perform_check(txs_agg: pd.DataFrame) -> None:
    countries = set(txs_agg.index.values) - {"NL", "BE"}
    assert len(countries) == 0, "Invalid countries found: " + ", ".join(
        countries
    )


@node(inputs=txs_agg)
def print_agg(txs_agg: pd.DataFrame) -> None:
    print(txs_agg.to_json())


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)

```

## Exception

```text
AttributeError: 'function' object has no attribute '_resource'
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    resource = Resource(check._resource)
                        ^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(NodeResourceGraph.from_nodes(nodes))
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/graph.py", line LINO, in _gather_graph
    node_graph = NodeGraph.from_nodes(nodes_and_views)

  File "/packages/ordeq-viz/src/ordeq_viz/to_mermaid.py", line LINO, in pipeline_to_mermaid
    node_modules, io_modules = _gather_graph(nodes, ios)
                               ~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/api.py", line LINO, in viz
    result = pipeline_to_mermaid(nodes, ios, **options)

  File "/packages/ordeq/tests/resources/checks/check_between_saves.py", line LINO, in <module>
    print(viz(__name__, fmt="mermaid"))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:txs_agg'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:perform_check'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:print_agg'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```