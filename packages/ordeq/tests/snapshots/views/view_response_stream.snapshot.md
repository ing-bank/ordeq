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
Node:view_response_stream:printer --> io-1
View:view_response_stream:users_stream --> io-2
io-2 --> Node:view_response_stream:printer
io-3 --> View:view_response_stream:users_stream
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