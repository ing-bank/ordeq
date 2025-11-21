## Resource

```python
from ordeq import node, run


@node
def print_message():
    print("Hello from printer")


run(print_message, verbose=True)

show_message = print_message

run(show_message, verbose=True)

```

## Output

```text
View:__main__:print_message --> io-0
Hello from printer
ValueError: Module '__main__' aliases node '__main__:print_message' to 'show_message'. Nodes cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in scan
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    scanned_nodes, _ = scan(*submodules)
                       ~~~~^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_rename_run.py", line LINO, in <module>
    run(show_message, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.runner	Running view "print_message" in module "__main__"

```