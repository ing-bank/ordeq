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

## Output

```text
This should run first
This should run second

```

## Logging

```text
WARNING	ordeq.preview	Creating a view, as no outputs were provided for node '__main__:node_consume_none'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "node_return_none" in module "__main__"
INFO	ordeq.runner	Running view "node_consume_none" in module "__main__"

```