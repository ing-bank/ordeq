## Resource

```python
from collections.abc import Generator

import requests
from ordeq import node, run
from ordeq_common import Literal, Print

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Literal(response)


@node(inputs=users_response)
def users_stream(r: requests.Response) -> Generator[bytes]:
    return r.raw.stream()


@node(inputs=users_stream, outputs=Print())
def printer(stream: bytes) -> str:
    return str(stream)


run(printer, verbose=True)

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/view_response_stream.py", line LINO, in <module>
    run(printer, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^

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
     view_response_stream:printer -> []
     view_response_stream:users_stream -> [view_response_stream:printer]
  Nodes:
     view_response_stream:printer: Node(name=view_response_stream:printer, inputs=[View(name=view_response_stream:users_stream, inputs=[Literal(<Response [200]>)])], outputs=[Print()])
     view_response_stream:users_stream: View(name=view_response_stream:users_stream, inputs=[Literal(<Response [200]>)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_stream:users_stream'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```