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
NodeResourceGraph(edges={View(name=__main__:selected_range, inputs=[Literal(<_duckdb.DuckDBPyConnection object at HASH1>)]): [Resource(value=IO(id=ID1))], View(name=__main__:range_to_csv, inputs=[IO(id=ID1)]): [Resource(value=IO(id=ID2))], Resource(value=Literal(<_duckdb.DuckDBPyConnection object at HASH1>)): [View(name=__main__:selected_range, inputs=[Literal(<_duckdb.DuckDBPyConnection object at HASH1>)])], Resource(value=IO(id=ID1)): [View(name=__main__:range_to_csv, inputs=[IO(id=ID1)])], Resource(value=IO(id=ID2)): []})
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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:selected_range'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:range_to_csv'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<_duckdb.DuckDBPyConnection object at HASH1>)
INFO	ordeq.runner	Running view "selected_range" in module "__main__"
INFO	ordeq.runner	Running view "range_to_csv" in module "__main__"

```