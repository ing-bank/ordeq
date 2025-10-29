## Resource

```python
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


@node(inputs=users_response)
def users_json(r: requests.Response) -> dict:
    return r.json()


@node(inputs=users_json)
def to_yaml(d: dict) -> None:
    print("Data:", d)


run(to_yaml, verbose=True)

```

## Exception

```text
AttributeError: 'dict' object has no attribute 'json'
  File "/packages/ordeq/tests/resources/views/view_response_json.py", line LINO, in users_json
    return r.json()
           ^^^^^^

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

  File "/packages/ordeq/tests/resources/views/view_response_json.py", line LINO, in <module>
    run(to_yaml, verbose=True)
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
     view_response_json:to_yaml -> []
     view_response_json:users_json -> [view_response_json:to_yaml]
  Nodes:
     view_response_json:to_yaml: View(name=view_response_json:to_yaml, inputs=[View(name=view_response_json:users_json, inputs=[Literal({'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}})])])
     view_response_json:users_json: View(name=view_response_json:users_json, inputs=[Literal({'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}})])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_json:users_json'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_json:to_yaml'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal({'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}})
INFO	ordeq.runner	Running view "users_json" in module "view_response_json"

```