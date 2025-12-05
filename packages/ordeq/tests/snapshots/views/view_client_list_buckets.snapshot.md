## Resource

```python
from ordeq import Input, node, run


class Client:
    @staticmethod
    def list_buckets() -> list[str]:
        return ["bucket1", "bucket2", "bucket3"]


@node(inputs=Input(Client()))
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
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input 'buckets:client' in module '__main__'
INFO	ordeq.runner	Running view 'buckets' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'print_buckets:buckets' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'print_buckets:buckets' in module '__main__'
INFO	ordeq.runner	Running view 'print_buckets' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO 'print_buckets:buckets' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```