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
		node_type@{shape: rounded, label: "Node"}
		view_type@{shape: subroutine, label: "View"}
		io_type_0@{shape: rect, label: "PandasCSV"}
		io_type_1@{shape: rect, label: "PolarsEagerCSV"}
	end

	__main__:produce --> __main__:csv_pandas
	__main__:csv_polars --> __main__:check

	__main__:produce@{shape: rounded, label: "produce"}
	__main__:check@{shape: subroutine, label: "check"}
	__main__:csv_pandas@{shape: rect, label: "csv_pandas"}
	__main__:csv_polars@{shape: rect, label: "csv_polars"}

	class node_type,__main__:produce node
	class view_type,__main__:check view
	class io_type_0,__main__:csv_pandas io0
	class io_type_1,__main__:csv_polars io1
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
INFO	ordeq.runner	Running node 'produce' in module '__main__'
INFO	ordeq.io	Saving PandasCSV 'csv_pandas' in module '__main__'
DEBUG	ordeq.io	Persisting data for PandasCSV 'csv_pandas' in module '__main__'
INFO	ordeq.io	Loading PolarsEagerCSV 'csv_polars' in module '__main__'
DEBUG	ordeq.io	Persisting data for PolarsEagerCSV 'csv_polars' in module '__main__'
INFO	ordeq.runner	Running view 'check' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for PolarsEagerCSV 'csv_polars' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for PandasCSV 'csv_pandas' in module '__main__'

```
