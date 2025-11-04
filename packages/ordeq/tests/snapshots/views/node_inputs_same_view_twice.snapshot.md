## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[hello, hello], outputs=Print())
def n(fst: str, snd: str) -> str:
    return f"{fst} == {snd}'"


run(n, verbose=True)

```

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/views/node_inputs_same_view_twice.py", line LINO, in <module>
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
View(name=node_inputs_same_view_twice:hello)
NodeGraph:
  Edges:
     node_inputs_same_view_twice:hello -> [node_inputs_same_view_twice:n, node_inputs_same_view_twice:n]
     node_inputs_same_view_twice:n -> []
  Nodes:
     node_inputs_same_view_twice:hello: View(name=node_inputs_same_view_twice:hello)
     node_inputs_same_view_twice:n: Node(name=node_inputs_same_view_twice:n, inputs=[View(name=node_inputs_same_view_twice:hello), View(name=node_inputs_same_view_twice:hello)], outputs=[Print()])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_same_view_twice:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```