## Resource

```python
from ordeq import IO, node, run

io = IO[None]()


@node(outputs=[io])
def node_return_none() -> None:
    print("This should run first")


@node(inputs=[io])
def node_consume_none(_data: None) -> None:
    print("This should run second")


if __name__ == "__main__":
    run(node_return_none, node_consume_none)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_return_none:node_consume_none'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```