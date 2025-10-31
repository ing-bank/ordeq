## Resource

```python
from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def conditional() -> str | None:
    if glob > 2:
        return "Higher value!"
    return None


@node(inputs=conditional, outputs=Print())
def n(v: str | None):
    return v


glob = 3
run(n, verbose=True)

glob = 1
run(n, verbose=True)

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/view_returns_optional.py", line LINO, in <module>
    run(n, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^

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
     view_returns_optional:conditional -> [view_returns_optional:n]
     view_returns_optional:n -> []
  Nodes:
     view_returns_optional:conditional: View(name=view_returns_optional:conditional)
     view_returns_optional:n: Node(name=view_returns_optional:n, inputs=[View(name=view_returns_optional:conditional)], outputs=[Print()])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_returns_optional:conditional'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```