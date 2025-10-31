from pathlib import Path

from ordeq_requests import ResponseJSON
from ordeq_yaml import YAML

user = ResponseJSON(url="https://jsonplaceholder.typicode.com/users/1")
yaml = YAML(path=Path("users.yml"))
