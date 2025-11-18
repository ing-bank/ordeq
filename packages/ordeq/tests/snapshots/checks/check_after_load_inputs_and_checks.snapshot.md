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
txs_agg = IO[Any]()
threshold = Literal(100)


@node(inputs=[txs_agg, threshold], checks=txs_agg)
def perform_check(txs_agg: pd.DataFrame, t: int) -> None:
    assert (txs_agg.count() < t).all()


@node(inputs=txs, outputs=txs_agg)
def agg_txs(txs: pd.DataFrame) -> pd.DataFrame:
    return txs.groupby("country").agg({"amount": "sum"})


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
	class L00,IO1 io0
	class L01,IO0,IO2 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62


```

## Logging

```text
WARNING	ordeq.nodes	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:perform_check'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(   id  amount   to country
0   1     100   me      NL
1   2     200   me      BE
2   3     300  you      US)
INFO	ordeq.runner	Running node "agg_txs" in module "__main__"
INFO	ordeq.io	Loading Literal(100)
INFO	ordeq.runner	Running view "perform_check" in module "__main__"

```