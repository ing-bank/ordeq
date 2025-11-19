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
NodeResourceGraph(edges={View(name=__main__:users_stream, inputs=[Literal(<Response [200]>)]): [Resource(value=IO(id=ID1))], Node(name=__main__:printer, inputs=[IO(id=ID1)], outputs=[Print()]): [Resource(value=Print())], Resource(value=Literal(<Response [200]>)): [View(name=__main__:users_stream, inputs=[Literal(<Response [200]>)])], Resource(value=IO(id=ID1)): [Node(name=__main__:printer, inputs=[IO(id=ID1)], outputs=[Print()])], Resource(value=Print()): []})
<generator object HTTPResponse.stream at HASH1>

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:users_stream'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running view "users_stream" in module "__main__"
INFO	ordeq.runner	Running node "printer" in module "__main__"
INFO	ordeq.io	Saving Print()

```