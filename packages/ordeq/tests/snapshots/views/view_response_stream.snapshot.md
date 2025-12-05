## Resource

```python
from collections.abc import Generator

import requests
from ordeq import Input, node, run
from ordeq_common import Print

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Input[requests.Response](response)


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
DEBUG	urllib3.connectionpool	Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
DEBUG	urllib3.connectionpool	https://jsonplaceholder.typicode.com:443 "GET /users/1 HTTP/1.1" 200 None
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Loading Input 'users_stream:r' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'users_stream:r' in module '__main__'
INFO	ordeq.runner	Running view 'users_stream' in module '__main__'
INFO	ordeq.runner	Saving IO 'printer:stream' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'printer:stream' in module '__main__'
INFO	ordeq.runner	Loading IO 'printer:stream' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'printer:stream' in module '__main__'
INFO	ordeq.runner	Running node 'printer' in module '__main__'
INFO	ordeq.runner	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO 'printer:stream' in module '__main__'

```