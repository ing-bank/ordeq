## Resource

```python
from ordeq import run
from resources.runner import example_module_a, example_module_b

run(example_module_a, example_module_b, verbose=True)

```

## Output

```text
ValueError: Module 'resources.runner.example_module_b' aliases node 'resources.runner.example_module_b:increment' to 'renamed'. Nodes cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in scan
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    fq_nodes, _ = scan(*submodules)
                  ~~~~^^^^^^^^^^^^^

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