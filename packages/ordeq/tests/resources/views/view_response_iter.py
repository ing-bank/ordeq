from collections.abc import Iterator
from typing import Any

import requests
from ordeq import node, run
from ordeq_common import Literal

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
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
