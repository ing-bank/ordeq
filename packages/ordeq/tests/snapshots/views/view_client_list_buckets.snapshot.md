## Resource

```python
from ordeq import node, run
from ordeq_common import Literal


class Client:
    @staticmethod
    def list_buckets() -> list[str]:
        return ["bucket1", "bucket2", "bucket3"]


@node(inputs=Literal(Client()))
def buckets(client: Client) -> list[str]:
    return client.list_buckets()


@node(inputs=buckets)
def print_buckets(buckets: list[str]) -> None:
    for bucket in buckets:
        print(bucket)


run(print_buckets, verbose=True)

```

## Output

```text
io-0 --> View:__main__:buckets
View:__main__:buckets --> io-1
io-1 --> View:__main__:print_buckets
View:__main__:print_buckets --> io-2
bucket1
bucket2
bucket3

```

## Logging

```text
INFO	ordeq.io	Loading Literal(<__main__.Client object at HASH1>)
DEBUG	ordeq.io	Persisting data for Literal(<__main__.Client object at HASH1>)
INFO	ordeq.runner	Running view 'buckets' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'print_buckets' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for Literal(<__main__.Client object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```