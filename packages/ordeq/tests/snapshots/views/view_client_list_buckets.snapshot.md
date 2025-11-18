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
NodeResourceGraph(nodes=2, resources=3, edges={View(name=__main__:buckets, inputs=[Literal(<__main__.Client object at HASH1>)]): [Resource(value=IO(id=ID1))], View(name=__main__:print_buckets, inputs=[IO(id=ID1)]): [Resource(value=IO(id=ID2))], Resource(value=Literal(<__main__.Client object at HASH1>)): [View(name=__main__:buckets, inputs=[Literal(<__main__.Client object at HASH1>)])], Resource(value=IO(id=ID1)): [View(name=__main__:print_buckets, inputs=[IO(id=ID1)])], Resource(value=IO(id=ID2)): []})
bucket1
bucket2
bucket3

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:buckets'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:print_buckets'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<__main__.Client object at HASH1>)
INFO	ordeq.runner	Running view "buckets" in module "__main__"
INFO	ordeq.runner	Running view "print_buckets" in module "__main__"

```