## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal, Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello], outputs=Print())
def n(name: str, greeting: str) -> str:
    return f"{name} said '{greeting}'"


print(run(n, verbose=True))

```

## Output

```text
View(name=node_inputs_view_and_io:hello)
NodeGraph:
  Edges:
     node_inputs_view_and_io:hello -> [node_inputs_view_and_io:n]
     node_inputs_view_and_io:n -> []
  Nodes:
     node_inputs_view_and_io:hello: View(name=node_inputs_view_and_io:hello)
     node_inputs_view_and_io:n: Node(name=node_inputs_view_and_io:n, inputs=[Literal('Jane'), View(name=node_inputs_view_and_io:hello)], outputs=[Print()])
Jane said 'Hello, World!'
{View(name=node_inputs_view_and_io:hello): 'Hello, World!', Print(): "Jane said 'Hello, World!'"}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_view_and_io:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "node_inputs_view_and_io"
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.runner	Running node "n" in module "node_inputs_view_and_io"
INFO	ordeq.io	Saving Print()

```