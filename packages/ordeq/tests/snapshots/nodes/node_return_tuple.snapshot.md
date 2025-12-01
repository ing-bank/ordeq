## Resource

```python
"""A node that returns a tuple to a single output."""

from ordeq import IO, node, run

io = IO[tuple[str, str]]()


@node(outputs=[io])
def node_return_tuple() -> tuple[str, str]:
    return "hello", "world"


@node(inputs=[io])
def node_consume_tuple(data: tuple[str, str]) -> None:
    print(data)


if __name__ == "__main__":
    run(node_return_tuple, node_consume_tuple)

```

## Output

```text
('hello', 'world')

```

## Logging

```text
INFO	ordeq.runner	Running node 'node_return_tuple' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'node_consume_tuple:data' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'node_consume_tuple:data' in module '__main__'
INFO	ordeq.runner	Running view 'node_consume_tuple' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO 'node_consume_tuple:data' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```