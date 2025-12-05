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
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "IO"}
		io_type_1@{shape: rect, label: "Input"}
	end

	__main__:txs --> __main__:perform_check
	__main__:txs --> __main__:txs_agg
	__main__:txs_agg --> __main__:print_agg

	__main__:perform_check@{shape: subroutine, label: "perform_check"}
	__main__:txs_agg@{shape: subroutine, label: "txs_agg"}
	__main__:print_agg@{shape: subroutine, label: "print_agg"}
	__main__:txs@{shape: rect, label: "txs"}

	class view_type,__main__:perform_check,__main__:txs_agg,__main__:print_agg view
	class io_type_0 io0
	class io_type_1,__main__:txs io1
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
INFO	ordeq.runner	Loading Input 'txs' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'txs' in module '__main__'
INFO	ordeq.runner	Running view 'perform_check' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Loading Input 'txs' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'txs' in module '__main__'
INFO	ordeq.runner	Running view 'txs_agg' in module '__main__'
INFO	ordeq.runner	Saving IO 'print_agg:txs_agg' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'print_agg:txs_agg' in module '__main__'
INFO	ordeq.runner	Loading IO 'print_agg:txs_agg' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'print_agg:txs_agg' in module '__main__'
INFO	ordeq.runner	Running view 'print_agg' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID3)
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO 'print_agg:txs_agg' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)

```