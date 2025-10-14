import requests

from ordeq import node, run
from ordeq_requests import Response
from ordeq_yaml import YAML
from pathlib import Path

users_response = Response(
    url="https://jsonplaceholder.typicode.com/users/"
)
yaml = YAML(path=Path(".yml"))


@node(inputs=users_response)
def users_json(r: requests.Response) -> dict:
    return r.json()


@node(inputs=users_json, outputs=yaml)
def to_yaml(d: dict) -> dict:
    return d


print(run(to_yaml, verbose=True))
