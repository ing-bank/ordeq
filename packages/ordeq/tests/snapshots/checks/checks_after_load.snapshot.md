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
    })
)
txs_agg = IO[Any]()


@node(inputs=txs, checks=txs)
def perform_check(txs: pd.DataFrame) -> None:
    assert txs.count(axis=0)["id"] > 2


@node(inputs=txs)
def txs_agg(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupby("to").agg({"amount": "sum"})


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

	IO0 --> __main__:perform_check
	__main__:txs_agg --> __main__:print_agg
	IO0 --> __main__:txs_agg

	__main__:perform_check@{shape: subroutine, label: "perform_check"}
	__main__:print_agg@{shape: subroutine, label: "print_agg"}
	__main__:txs_agg@{shape: subroutine, label: "txs_agg"}
	IO0@{shape: rect, label: "txs"}

	class L0 node
	class L2,__main__:perform_check,__main__:print_agg,__main__:txs_agg view
	class L00 io0
	class L01,IO0 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

{"amount":{"me":300,"you":300}}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:perform_check'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:txs_agg'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:print_agg'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(   id  amount   to
0   1     100   me
1   2     200   me
2   3     300  you)
INFO	ordeq.runner	Running view "perform_check" in module "__main__"
INFO	ordeq.runner	Running view "txs_agg" in module "__main__"
INFO	ordeq.runner	Running view "print_agg" in module "__main__"

```