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

## Output

```text
View(name=node_inputs_same_view_twice:hello)
io-0 --> Node:node_inputs_same_view_twice:n
View:node_inputs_same_view_twice:hello --> io-0
Node:node_inputs_same_view_twice:n --> io-1
Hello, World! == Hello, World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_same_view_twice:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "node_inputs_same_view_twice"
INFO	ordeq.runner	Running node "n" in module "node_inputs_same_view_twice"
INFO	ordeq.io	Saving Print()

```