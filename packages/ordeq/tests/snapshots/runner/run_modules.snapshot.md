## Resource

```python
from ordeq import run
from resources.runner import example_module_a, example_module_b

run(example_module_a, example_module_b, verbose=True)

```

## Output

```text
ValueError: Module 'resources.runner.example_module_b' contains duplicate keys for the same node ('renamed' and 'increment')
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_to_nodes
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_runnables_to_nodes
    for node_name, node in _resolve_module_to_nodes(module).items()
                           ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    nodes = [node for _, node in _resolve_runnables_to_nodes(*runnables)]
                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_modules.py", line LINO, in <module>
    run(example_module_a, example_module_b, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_modules.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```