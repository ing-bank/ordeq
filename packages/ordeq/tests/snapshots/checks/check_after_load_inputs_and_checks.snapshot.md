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
txs_agg = IO[Any]()
threshold = Input[int](100)


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
		L01@{shape: rect, label: "Input"}
	end

	__main__:txs --> __main__:agg_txs
	__main__:agg_txs --> __main__:txs_agg
	__main__:txs_agg --> __main__:perform_check
	__main__:threshold --> __main__:perform_check

	__main__:agg_txs@{shape: rounded, label: "agg_txs"}
	__main__:perform_check@{shape: subroutine, label: "perform_check"}
	__main__:txs_agg@{shape: rect, label: "txs_agg"}
	__main__:threshold@{shape: rect, label: "threshold"}
	__main__:txs@{shape: rect, label: "txs"}

	class L0,__main__:agg_txs node
	class L2,__main__:perform_check view
	class L00,__main__:txs_agg io0
	class L01,__main__:threshold,__main__:txs io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62


```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID2)
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
DEBUG	ordeq.io	Loading cached data for 'txs' in module '__main__'
INFO	ordeq.runner	Running node 'agg_txs' in module '__main__'
DEBUG	ordeq.io	Persisting data for 'txs_agg' in module '__main__'
DEBUG	ordeq.io	Loading cached data for 'txs_agg' in module '__main__'
DEBUG	ordeq.io	Loading cached data for 'threshold' in module '__main__'
INFO	ordeq.runner	Running view 'perform_check' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for 'txs_agg' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```