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


print(run(n, verbose=True))

```

## Exception

```text
IOException: Failed to load IO(idx=ID1).

```

## Output

```text
View(name=view_inputs_view_and_io:hello)
View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])
NodeGraph:
  Edges:
     view_inputs_view_and_io:hello -> []
     view_inputs_view_and_io:hello_from_someone -> []
     view_inputs_view_and_io:n -> []
  Nodes:
     View(name=view_inputs_view_and_io:hello)
     View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])
     View(name=view_inputs_view_and_io:n, inputs=[View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:hello_from_someone'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading IO(idx=ID1)

```