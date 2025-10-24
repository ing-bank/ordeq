## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=hello, outputs=Print())
def n(greeting: str) -> str:
    return f"She said '{greeting}'"


print(run(n, verbose=True))

```

## Output

```text
View(name=node_inputs_view:hello)
NodeGraph:
  Edges:
     node_inputs_view:hello -> [node_inputs_view:n]
     node_inputs_view:n -> []
  Nodes:
     View(name=node_inputs_view:hello)
     Node(name=node_inputs_view:n, inputs=[View(name=node_inputs_view:hello)], outputs=[Print()])
She said 'Hello, World!'
{View(name=node_inputs_view:hello): 'Hello, World!', Print(): "She said 'Hello, World!'"}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_view:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node View(name=node_inputs_view:hello)
INFO	ordeq.runner	Running node Node(name=node_inputs_view:n, inputs=[IO(idx=ID1)], outputs=[Print()])
INFO	ordeq.io	Saving Print()

```