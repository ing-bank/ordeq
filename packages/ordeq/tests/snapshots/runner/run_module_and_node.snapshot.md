## Resource

```python
from ordeq import node, run
from resources.runner import example_module_a


@node
def noop() -> None:
    return


run(example_module_a, noop, verbose=True)

```

## Output

```text
io-0 --> Node:resources.runner.example_module_a:increment
Node:resources.runner.example_module_a:increment --> io-2
io-1 --> Node:resources.runner.example_module_a:decrement
io-2 --> Node:resources.runner.example_module_a:decrement
Node:resources.runner.example_module_a:decrement --> io-3
View:View(func=__main__:noop, ...) --> io-4
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

  File "/packages/ordeq/tests/resources/runner/run_module_and_node.py", line LINO, in <module>
    run(example_module_a, noop, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

## Typing

```text
packages/ordeq/tests/resources/runner/run_module_and_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```