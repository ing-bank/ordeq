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

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/views/view_client_list_buckets.py", line LINO, in <module>
    run(print_buckets, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

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

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_client_list_buckets:buckets'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_client_list_buckets:print_buckets'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```