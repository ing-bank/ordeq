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

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
		L00@{shape: rect, label: "IO"}
		L01@{shape: rect, label: "Literal"}
	end

	IO0 --> __main__:txs_agg
	__main__:txs_agg --> __main__:print_agg
	__main__:txs_agg --> __main__:perform_check

	__main__:txs_agg@{shape: subroutine, label: "txs_agg"}
	__main__:print_agg@{shape: subroutine, label: "print_agg"}
	__main__:perform_check@{shape: subroutine, label: "perform_check"}
	IO0@{shape: rect, label: "txs"}

	class L0 node
	class L2,__main__:txs_agg,__main__:print_agg,__main__:perform_check view
	class L00 io0
	class L01,IO0 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

{"amount":{"BE":200,"NL":100,"US":300}}
AssertionError: Invalid countries found: US
  File "/packages/ordeq/tests/resources/checks/check_between_saves.py", line LINO, in perform_check
    assert len(countries) == 0, "Invalid countries found: " + ", ".join(
           ^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in inner
    return f(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    _run_node_func(node, args=_load_inputs(node.inputs), hooks=hooks),
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, node_hooks=node_hooks, run_hooks=run_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/checks/check_between_saves.py", line LINO, in <module>
    run(__name__)
    ~~~^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:txs_agg'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:perform_check'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:print_agg'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(   id  amount   to country
0   1     100   me      NL
1   2     200   me      BE
2   3     300  you      US)
INFO	ordeq.runner	Running view "txs_agg" in module "__main__"
INFO	ordeq.runner	Running view "print_agg" in module "__main__"
INFO	ordeq.runner	Running view "perform_check" in module "__main__"

```