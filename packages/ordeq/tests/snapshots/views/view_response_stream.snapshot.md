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

## Output

```text
NodeGraph:
  Edges:
     view_response_stream:printer -> []
     view_response_stream:users_stream -> [view_response_stream:printer]
  Nodes:
     view_response_stream:printer: Node(name=view_response_stream:printer, inputs=[View(name=view_response_stream:users_stream, inputs=[Literal(<Response [200]>)])], outputs=[Print()])
     view_response_stream:users_stream: View(name=view_response_stream:users_stream, inputs=[Literal(<Response [200]>)])
<generator object HTTPResponse.stream at HASH1>

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_stream:users_stream'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running view "users_stream" in module "view_response_stream"
INFO	ordeq.runner	Running node "printer" in module "view_response_stream"
INFO	ordeq.io	Saving Print()

```