## Resource

```python
from typing import Any

import pandas as pd
from ordeq import IO, node, run
from ordeq_common import Literal
from ordeq_viz import viz

txs = IO[Any]()
txs_agg = IO[Any]()
threshold = Literal(100)


@node(inputs=[txs_agg, threshold], checks=txs_agg)
def perform_check(txs_agg: pd.DataFrame, t: int) -> None:
    assert txs_agg.count() > t


@node(inputs=txs, outputs=txs_agg)
def agg_txs(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupBy(...).agg(...)


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

	IO0 --> __main__:agg_txs
	__main__:agg_txs --> IO1
	IO1 --> __main__:perform_check
	IO2 --> __main__:perform_check

	__main__:agg_txs@{shape: rounded, label: "agg_txs"}
	__main__:perform_check@{shape: subroutine, label: "perform_check"}
	IO1@{shape: rect, label: "txs_agg"}
	IO0@{shape: rect, label: "txs"}
	IO2@{shape: rect, label: "threshold"}

	class L0,__main__:agg_txs node
	class L2,__main__:perform_check view
	class L00,IO1,IO0 io0
	class L01,IO2 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

IOException: Failed to load IO(id=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    data = cast("Input", input_dataset).load()

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/checks/check_after_load_inputs_and_checks.py", line LINO, in <module>
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
WARNING	ordeq.nodes	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:perform_check'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading IO(id=ID1)

```

## Typing

```text
packages/ordeq/tests/resources/checks/check_after_load_inputs_and_checks.py:20:12: error[call-non-callable] Object of type `Series[Any]` is not callable
Found 1 diagnostic

```