## Resource

```python
from ordeq import run

run(0.23)

```

## Output

```text
TypeError: 0.23 is not something we can run. Expected a module or a node, got <class 'float'>
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_runnables_to_nodes_and_modules
    raise TypeError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_runnables_to_nodes
    nodes, modules = _resolve_runnables_to_nodes_and_modules(*runnables)
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    nodes = [node for _, node in _resolve_runnables_to_nodes(*runnables)]
                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_non_runnable.py", line LINO, in <module>
    run(0.23)
    ~~~^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```