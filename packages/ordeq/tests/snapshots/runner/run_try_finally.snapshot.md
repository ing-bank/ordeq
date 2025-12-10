## Resource

```python
from ordeq import Input, node, run


class Connection(Input[str]):
    @staticmethod
    def load() -> str:
        try:
            print("Connection opened")
            return "connection"
        finally:
            print("Connection closed")


conn = Connection()


@node(inputs=conn)
def process_first(connection: str) -> None:
    print(f"Processing first with {connection}")


@node(inputs=conn)
def process_second(connection: str) -> None:
    print(f"Processing second with {connection}")


run(process_first, process_second)

conn.load()

```

## Output

```text
Connection opened
Connection closed
Processing first with connection
Connection opened
Connection closed
Processing second with connection
Connection opened
Connection closed

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running view 'process_first' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.runner	Running view 'process_second' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for Input(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```