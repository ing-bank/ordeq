## Resource

```python
from collections.abc import Iterator
from typing import Any

import requests
from ordeq import node, run
from ordeq_common import Literal

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Literal(response)


# View that returns an iterable from a regular/non-iterable IO:
@node(inputs=users_response)
def users_lines(r: requests.Response) -> Iterator[Any]:
    return r.iter_lines()


@node(inputs=users_lines)
def concatenate(lines: Iterator[Any]) -> None:
    for line in lines:
        print(line)


run(concatenate, verbose=True)

```

## Output

```text
io-0 --> View:__main__:users_lines
View:__main__:users_lines --> io-1
io-1 --> View:__main__:concatenate
View:__main__:concatenate --> io-2
b'{'
b'  "id": 1,'
b'  "name": "Leanne Graham",'
b'  "username": "Bret",'
b'  "email": "Sincere@april.biz",'
b'  "address": {'
b'    "street": "Kulas Light",'
b'    "suite": "Apt. 556",'
b'    "city": "Gwenborough",'
b'    "zipcode": "92998-3874",'
b'    "geo": {'
b'      "lat": "-37.3159",'
b'      "lng": "81.1496"'
b'    }'
b'  },'
b'  "phone": "1-770-736-8031 x56442",'
b'  "website": "hildegard.org",'
b'  "company": {'
b'    "name": "Romaguera-Crona",'
b'    "catchPhrase": "Multi-layered client-server neural-net",'
b'    "bs": "harness real-time e-markets"'
b'  }'
b'}'

```

## Logging

```text
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running view "users_lines" in module "__main__"
INFO	ordeq.runner	Running view "concatenate" in module "__main__"

```