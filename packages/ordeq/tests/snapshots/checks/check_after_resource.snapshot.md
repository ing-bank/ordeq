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

csv = Path(tempfile.mkdtemp()) / "my.csv"
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
AttributeError: 'Path' object has no attribute '_resource'
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    resource = Resource(check._resource)  # noqa: SLF001 (private-member-access)
                        ^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(NodeResourceGraph.from_nodes(nodes))
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/graph.py", line LINO, in _gather_graph
    node_graph = NodeGraph.from_nodes(nodes_and_views)

  File "/packages/ordeq-viz/src/ordeq_viz/to_mermaid.py", line LINO, in pipeline_to_mermaid
    node_modules, io_modules = _gather_graph(nodes, ios)
                               ~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq-viz/src/ordeq_viz/api.py", line LINO, in viz
    result = pipeline_to_mermaid(nodes_, ios, **options)

  File "/packages/ordeq/tests/resources/checks/check_after_resource.py", line LINO, in <module>
    print(viz(__name__, fmt="mermaid"))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:check'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```