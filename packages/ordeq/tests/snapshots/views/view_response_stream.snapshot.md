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
io-0 --> View:__main__:users_stream
View:__main__:users_stream --> io-1
io-1 --> Node:__main__:printer
Node:__main__:printer --> io-2
<generator object HTTPResponse.stream at HASH1>

```

## Logging

```text
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running view 'users_stream' in module '__main__'
INFO	ordeq.runner	Running node 'printer' in module '__main__'
INFO	ordeq.io	Saving Print()

```