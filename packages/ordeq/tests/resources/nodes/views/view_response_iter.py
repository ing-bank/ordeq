import requests
from typing import Any, Iterator

from ordeq import node, run
from ordeq_requests import Response
from ordeq_common import Print

users_response = Response(
    url="https://jsonplaceholder.typicode.com/users/"
)


# View that returns an iterable from a regular/non-iterable IO:
@node(inputs=users_response)
def users_lines(r: requests.Response) -> Iterator[Any]:
    return r.iter_lines()


@node(inputs=users_lines, outputs=Print())
def concatenate(lines: Iterator[Any]) -> str:
    return ''.join(lines)


print(run(concatenate, verbose=True))
