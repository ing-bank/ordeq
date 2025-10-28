## Resource

```python
from ordeq import run

run(0.23)

```

## Exception

```text
TypeError: 0.23 is not something we can run. Expected a module or a node, got <class 'float'>
  File "/packages/ordeq/src/ordeq/_resolve.py", line 231, in _resolve_runnables_to_nodes_and_modules
    raise TypeError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line 251, in _resolve_runnables_to_nodes
    nodes, modules = _resolve_runnables_to_nodes_and_modules(*runnables)
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 177, in run
    nodes = _resolve_runnables_to_nodes(*runnables)

  File "/packages/ordeq/tests/resources/runner/run_non_runnable.py", line 3, in <module>
    run(0.23)
    ~~~^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_non_runnable.py:3: error: Argument 1 to "run" has incompatible type "float"; expected Module | Callable[..., Any] | str  [arg-type]
Found 1 error in 1 file (checked 1 source file)

```