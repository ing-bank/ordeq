## Resource

```python
import pandas as pd
from ordeq import Input, node, run
from ordeq_viz import viz

txs = Input[pd.DataFrame](
    pd.DataFrame({
        "id": [1, 2, 3],
        "amount": [100, 200, 300],
        "to": ["me", "me", "you"],
    })
)


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
		L01@{shape: rect, label: "Input"}
	end

	__main__:txs --> __main__:perform_check
	__main__:txs --> __main__:txs_agg
	unknown_2 --> __main__:print_agg

	__main__:perform_check@{shape: subroutine, label: "perform_check"}
	__main__:txs_agg@{shape: subroutine, label: "txs_agg"}
	__main__:print_agg@{shape: subroutine, label: "print_agg"}
	__main__:txs@{shape: rect, label: "txs"}
	unknown_2@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0 node
	class L2,__main__:perform_check,__main__:txs_agg,__main__:print_agg view
	class L00,unknown_2 io0
	class L01,__main__:txs io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

{"amount":{"me":300,"you":300}}

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
DEBUG	ordeq.io	Loading cached data for 'txs' in module '__main__'
INFO	ordeq.runner	Running view 'perform_check' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for 'txs' in module '__main__'
INFO	ordeq.runner	Running view 'txs_agg' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for IO(id=ID3)
INFO	ordeq.runner	Running view 'print_agg' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)

```