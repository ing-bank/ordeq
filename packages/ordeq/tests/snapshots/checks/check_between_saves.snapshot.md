## Resource

```python
from typing import Any

import pandas as pd
from ordeq import IO, Input, node, run
from ordeq_viz import viz

txs = Input[pd.DataFrame](
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
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "IO"}
		io_type_1@{shape: rect, label: "Input"}
	end

	__main__:txs --> __main__:txs_agg
	__main__:txs_agg --> __main__:perform_check
	__main__:txs_agg --> __main__:print_agg

	__main__:txs_agg@{shape: subroutine, label: "txs_agg"}
	__main__:perform_check@{shape: subroutine, label: "perform_check"}
	__main__:print_agg@{shape: subroutine, label: "print_agg"}
	__main__:txs@{shape: rect, label: "txs"}

	class view_type,__main__:txs_agg,__main__:perform_check,__main__:print_agg view
	class io_type_0 io0
	class io_type_1,__main__:txs io1
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

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
    results = _run_node_func(node, args=args, hooks=hooks)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(
    ~~~~~~~~~~^
        graph, node_hooks=resolved_node_hooks, run_hooks=resolved_run_hooks
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

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
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Loading Input 'txs' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'txs' in module '__main__'
INFO	ordeq.runner	Running view 'txs_agg' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Loading IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
INFO	ordeq.runner	Running view 'perform_check' in module '__main__'

```