## Resource

```python
import requests

from ordeq import node, run
from ordeq_common import Literal

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
users_response = Literal(response)


@node(inputs=users_response)
def users_json(r: requests.Response) -> dict:
    return r.json()


@node(inputs=users_json)
def to_yaml(d: dict) -> None:
    print('Data:', d)


run(to_yaml, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     view_response_json:to_yaml -> []
     view_response_json:users_json -> [view_response_json:to_yaml]
  Nodes:
     view_response_json:to_yaml: View(name=view_response_json:to_yaml, inputs=[View(name=view_response_json:users_json, inputs=[Literal(<Response [200]>)])])
     view_response_json:users_json: View(name=view_response_json:users_json, inputs=[Literal(<Response [200]>)])
Data: {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_json:users_json'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_json:to_yaml'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running view "users_json" in module "view_response_json"
INFO	ordeq.runner	Running view "to_yaml" in module "view_response_json"

```