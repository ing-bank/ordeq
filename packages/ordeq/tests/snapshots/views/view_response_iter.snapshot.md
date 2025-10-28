## Resource

```python
import requests
from typing import Any, Iterator

from ordeq import node, run
from ordeq_common import Literal

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
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
NodeGraph:
  Edges:
     view_response_iter:concatenate -> []
     view_response_iter:users_lines -> [view_response_iter:concatenate]
  Nodes:
     view_response_iter:concatenate: View(name=view_response_iter:concatenate, inputs=[View(name=view_response_iter:users_lines, inputs=[Literal(<Response [200]>)])])
     view_response_iter:users_lines: View(name=view_response_iter:users_lines, inputs=[Literal(<Response [200]>)])
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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:users_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:concatenate'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running view "users_lines" in module "view_response_iter"
INFO	ordeq.runner	Running view "concatenate" in module "view_response_iter"

```