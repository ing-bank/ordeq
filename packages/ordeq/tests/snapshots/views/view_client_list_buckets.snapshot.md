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
INFO	ordeq.runner	Running view 'buckets' in module '__main__'
INFO	ordeq.runner	Running view 'print_buckets' in module '__main__'

```