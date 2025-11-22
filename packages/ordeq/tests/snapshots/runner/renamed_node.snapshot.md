## Resource

```python
from ordeq import run
from resources.runner.example_module_b import renamed

# The runner information shows name 'increment' for this node.
# That's the original name. We'd like to see 'renamed' instead.
# TODO: Add a method _resolve_proxy_to_node that gets the node,
# and sets its name to the proxy's name.
run(renamed, verbose=True)

```

## Output

```text
ValueError: Module 'resources.runner.example_module_b' aliases node 'resources.runner.example_module_b:increment' to 'renamed'. Nodes cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in scan
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    scanned_nodes, _ = scan(*submodules)
                       ~~~~^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/renamed_node.py", line LINO, in <module>
    run(renamed, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/runner/renamed_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner.example_module_b`
Found 1 diagnostic

```