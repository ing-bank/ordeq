## Resource

```python
import duckdb
from ordeq import node, run
from ordeq_common import Literal

db = duckdb.connect(":memory:")
connection = Literal(db)


@node(inputs=connection)
def selected_range(conn: duckdb.DuckDBPyConnection) -> duckdb.DuckDBPyRelation:
    return conn.sql("SELECT * from range(3)")


@node(inputs=selected_range)
def range_to_csv(r: duckdb.DuckDBPyRelation) -> None:
    r.show()


run(range_to_csv, verbose=True)

```

## Output

```text
View:view_query:range_to_csv --> io-1
View:view_query:selected_range --> io-2
io-2 --> View:view_query:range_to_csv
┌───────┐
│ range │
│ int64 │
├───────┤
│     0 │
│     1 │
│     2 │
└───────┘


```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_query:selected_range'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_query:range_to_csv'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<_duckdb.DuckDBPyConnection object at HASH1>)
INFO	ordeq.runner	Running view "selected_range" in module "view_query"
INFO	ordeq.runner	Running view "range_to_csv" in module "view_query"

```