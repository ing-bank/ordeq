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

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_rename_run.py", line LINO, in <module>
    run(print_message, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     run_rename_run:print_message -> []
  Nodes:
     run_rename_run:print_message: View(name=run_rename_run:print_message)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'run_rename_run:print_message'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```