## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello])
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


print(repr(get_node(hello_from_someone)))


@node(inputs=hello_from_someone)
def n(v: str) -> None:
    print(f"I heard that {v}")


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

  File "/packages/ordeq/tests/resources/views/view_inputs_view_and_io.py", line LINO, in <module>
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
View(name=view_inputs_view_and_io:hello)
View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])
NodeGraph:
  Edges:
     view_inputs_view_and_io:hello -> [view_inputs_view_and_io:hello_from_someone]
     view_inputs_view_and_io:hello_from_someone -> [view_inputs_view_and_io:n]
     view_inputs_view_and_io:n -> []
  Nodes:
     view_inputs_view_and_io:hello: View(name=view_inputs_view_and_io:hello)
     view_inputs_view_and_io:hello_from_someone: View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])
     view_inputs_view_and_io:n: View(name=view_inputs_view_and_io:n, inputs=[View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:hello_from_someone'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```