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


print(run(print_buckets, verbose=True))

```

## Output

```text
NodeGraph:
  Edges:
     view_client_list_buckets:buckets -> [view_client_list_buckets:print_buckets]
     view_client_list_buckets:print_buckets -> []
  Nodes:
     view_client_list_buckets:buckets: View(name=view_client_list_buckets:buckets, inputs=[Literal(<view_client_list_buckets.Client object at HASH1>)])
     view_client_list_buckets:print_buckets: View(name=view_client_list_buckets:print_buckets, inputs=[View(name=view_client_list_buckets:buckets, inputs=[Literal(<view_client_list_buckets.Client object at HASH1>)])])
bucket1
bucket2
bucket3
{View(name=view_client_list_buckets:buckets, inputs=[Literal(<view_client_list_buckets.Client object at HASH1>)]): ['bucket1', 'bucket2', 'bucket3'], View(name=view_client_list_buckets:print_buckets, inputs=[View(name=view_client_list_buckets:buckets, inputs=[Literal(<view_client_list_buckets.Client object at HASH1>)])]): None}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_client_list_buckets:buckets'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_client_list_buckets:print_buckets'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<view_client_list_buckets.Client object at HASH1>)
INFO	ordeq.runner	Running view "buckets" in module "view_client_list_buckets"
INFO	ordeq.runner	Running view "print_buckets" in module "view_client_list_buckets"

```