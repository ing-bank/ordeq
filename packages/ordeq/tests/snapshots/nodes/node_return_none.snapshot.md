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
INFO	ordeq.runner	Running node 'node_return_none' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'node_consume_none' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```