## Resource

```python
import tempfile
from pathlib import Path

import pandas as pd
import polars as pl
from ordeq import node, run
from ordeq_pandas import PandasCSV
from ordeq_polars import PolarsEagerCSV
from ordeq_viz import viz

csv = Path(tempfile.gettempdir()) / "my.csv"
csv_pandas = PandasCSV(path=csv) @ csv
csv_polars = PolarsEagerCSV(path=csv) @ csv


@node(inputs=csv_polars, checks=csv)
def check(data: pl.DataFrame):
    print(data.head())


@node(outputs=csv_pandas)
def produce() -> pd.DataFrame:
    return pd.DataFrame({"hello": [1, 2, 3], "world": ["A", "B", "C"]})


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
		L00@{shape: rect, label: "PandasCSV"}
		L01@{shape: rect, label: "PolarsEagerCSV"}
	end

	__main__:produce --> IO0
	IO1 --> __main__:check

	__main__:produce@{shape: rounded, label: "produce"}
	__main__:check@{shape: subroutine, label: "check"}
	IO0@{shape: rect, label: "csv_pandas"}
	IO1@{shape: rect, label: "csv_polars"}

	class L0,__main__:produce node
	class L2,__main__:check view
	class L00,IO0 io0
	class L01,IO1 io1
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62

shape: (3, 3)
┌─────┬───────┬───────┐
│     ┆ hello ┆ world │
│ --- ┆ ---   ┆ ---   │
│ i64 ┆ i64   ┆ str   │
╞═════╪═══════╪═══════╡
│ 0   ┆ 1     ┆ A     │
│ 1   ┆ 2     ┆ B     │
│ 2   ┆ 3     ┆ C     │
└─────┴───────┴───────┘

```

## Logging

```text
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.
INFO	ordeq.runner	Running node "produce" in module "__main__"
INFO	ordeq.io	Saving PandasCSV(path=Path('<TEMP_DIR>/my.csv'))
INFO	ordeq.io	Loading PolarsEagerCSV(path=Path('<TEMP_DIR>/my.csv'))
INFO	ordeq.runner	Running view "check" in module "__main__"

```