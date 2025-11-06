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


run(n, verbose=True)

```

## Output

```text
View(name=node_inputs_view_and_io:hello)
View:node_inputs_view_and_io:hello --> io-1
io-1 --> Node:node_inputs_view_and_io:n
Node:node_inputs_view_and_io:n --> io-2
io-3 --> Node:node_inputs_view_and_io:n
Jane said 'Hello, World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_view_and_io:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "node_inputs_view_and_io"
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.runner	Running node "n" in module "node_inputs_view_and_io"
INFO	ordeq.io	Saving Print()

```