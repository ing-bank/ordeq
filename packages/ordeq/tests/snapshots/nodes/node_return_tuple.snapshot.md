## Resource

```python
"""A node that returns a tuple to a single output."""
from ordeq import node, run, IO


O = IO[tuple[str, str]]()


@node(outputs=[O])
def node_return_tuple() -> tuple[str, str]:
    return "hello", "world"


@node(inputs=[O])
def node_consume_tuple(data: tuple[str, str]) -> None:
    print(data)


if __name__ == "__main__":
    run(node_return_tuple, node_consume_tuple)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_return_tuple:node_consume_tuple'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```