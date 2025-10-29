## Resource

```python
from collections.abc import Iterator
from typing import Any

import requests
from ordeq import node, run
from ordeq_common import Literal

# Data retrieved from https://jsonplaceholder.typicode.com/users/1
users_response = Literal({
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {"lat": "-37.3159", "lng": "81.1496"},
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets",
    },
})


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

## Exception

```text
AttributeError: 'dict' object has no attribute 'iter_lines'
  File "/packages/ordeq/tests/resources/views/view_response_iter.py", line LINO, in users_lines
    return r.iter_lines()
           ^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in inner
    return f(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(patched_nodes[node], hooks=hooks, save=save_node)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=io)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/view_response_iter.py", line LINO, in <module>
    run(concatenate, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     view_response_iter:concatenate -> []
     view_response_iter:users_lines -> [view_response_iter:concatenate]
  Nodes:
     view_response_iter:concatenate: View(name=view_response_iter:concatenate, inputs=[View(name=view_response_iter:users_lines, inputs=[Literal({'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}})])])
     view_response_iter:users_lines: View(name=view_response_iter:users_lines, inputs=[Literal({'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}})])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:users_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:concatenate'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal({'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}})
INFO	ordeq.runner	Running view "users_lines" in module "view_response_iter"

```