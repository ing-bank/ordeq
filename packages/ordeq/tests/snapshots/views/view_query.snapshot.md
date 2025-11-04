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

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/views/view_query.py", line LINO, in <module>
    run(range_to_csv, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     view_query:range_to_csv -> []
     view_query:selected_range -> [view_query:range_to_csv]
  Nodes:
     view_query:range_to_csv: View(name=view_query:range_to_csv, inputs=[View(name=view_query:selected_range, inputs=[Literal(<_duckdb.DuckDBPyConnection object at HASH1>)])])
     view_query:selected_range: View(name=view_query:selected_range, inputs=[Literal(<_duckdb.DuckDBPyConnection object at HASH1>)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_query:selected_range'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_query:range_to_csv'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```