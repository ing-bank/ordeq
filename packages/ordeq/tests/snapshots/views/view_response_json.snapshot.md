## Resource

```python
import requests
from ordeq import Input, node, run

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Input[requests.Response](response)


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
DEBUG	urllib3.connectionpool	Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
DEBUG	urllib3.connectionpool	https://jsonplaceholder.typicode.com:443 "GET /users/1 HTTP/1.1" 200 None
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Loading Input 'users_json:r' in module '__main__'
DEBUG	ordeq.io	Loading cached data for Input 'users_json:r' in module '__main__'
INFO	ordeq.runner	Running view 'users_json' in module '__main__'
INFO	ordeq.runner	Saving IO 'to_yaml:d' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO 'to_yaml:d' in module '__main__'
INFO	ordeq.runner	Loading IO 'to_yaml:d' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'to_yaml:d' in module '__main__'
INFO	ordeq.runner	Running view 'to_yaml' in module '__main__'
INFO	ordeq.runner	Saving IO(id=ID2)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO 'to_yaml:d' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```