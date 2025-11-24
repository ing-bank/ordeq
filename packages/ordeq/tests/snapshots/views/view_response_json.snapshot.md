## Resource

```python
import requests
from ordeq import node, run
from ordeq_common import Literal

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Literal(response)


@node(inputs=users_response)
def users_json(r: requests.Response) -> dict:
    return r.json()


@node(inputs=users_json)
def to_yaml(d: dict) -> None:
    print("Data:", d)


run(to_yaml, verbose=True)

```

## Output

```text
io-0 --> View:__main__:users_json
View:__main__:users_json --> io-1
io-1 --> View:__main__:to_yaml
View:__main__:to_yaml --> io-2
Data: {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}

```

## Logging

```text
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running view '__main__:users_json'
INFO	ordeq.runner	Running view '__main__:to_yaml'

```