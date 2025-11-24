import requests
from ordeq import Input, node, run

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Input(response)


@node(inputs=users_response)
def users_json(r: requests.Response) -> dict:
    return r.json()


@node(inputs=users_json)
def to_yaml(d: dict) -> None:
    print("Data:", d)


run(to_yaml, verbose=True)
