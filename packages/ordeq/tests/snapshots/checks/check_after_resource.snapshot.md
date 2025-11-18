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

	IO0 --> __main__:check
	__main__:produce --> IO1

	__main__:check@{shape: subroutine, label: "check"}
	__main__:produce@{shape: rounded, label: "produce"}
	IO0@{shape: rect, label: "csv_polars"}
	IO1@{shape: rect, label: "csv_pandas"}

	class L0,__main__:produce node
	class L2,__main__:check view
	class L00,IO1 io0
	class L01,IO0 io1
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

## Warnings

```text
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.12/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
```

## Logging

```text
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.io	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.nodes	Checks are in preview mode and may change without notice in future releases.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:check'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "produce" in module "__main__"
INFO	ordeq.io	Saving PandasCSV(path=Path('<TEMP_DIR>/my.csv'))
INFO	ordeq.io	Loading PolarsEagerCSV(path=Path('<TEMP_DIR>/my.csv'))
INFO	ordeq.runner	Running view "check" in module "__main__"

```