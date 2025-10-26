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


print(run(concatenate, verbose=True))

```

## Exception

```text
IOException: Failed to load IO(idx=ID1).

```

## Output

```text
NodeGraph:
  Edges:
     view_response_iter:concatenate -> [view_response_iter:users_lines]
     view_response_iter:users_lines -> []
  Nodes:
     View(name=view_response_iter:concatenate, inputs=[View(name=view_response_iter:users_lines, inputs=[Literal(<Response [200]>)])])
     View(name=view_response_iter:users_lines, inputs=[Literal(<Response [200]>)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:users_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:concatenate'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading IO(idx=ID1)

```