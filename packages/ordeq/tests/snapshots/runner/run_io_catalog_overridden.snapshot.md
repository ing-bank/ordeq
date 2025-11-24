## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import remote, remote_overridden
from ordeq import node, run
from ordeq_common import Print

catalog = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world, io={catalog: remote_overridden})

```

## Output

```text
IOException: Failed to load Input(id=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _load_inputs
    data = cast("Input", input_dataset).load()

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    args = _load_inputs(node.inputs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, node_hooks=node_hooks, run_hooks=run_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_io_catalog_overridden.py", line LINO, in <module>
    run(uppercase, add_world, io={catalog: remote_overridden})
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Loading Input(id=ID1)

```