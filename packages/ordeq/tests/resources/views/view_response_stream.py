from collections.abc import Generator

import requests
from ordeq import Input, node, run
from ordeq_common import Print

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Input(response)


@node(inputs=users_response)
def users_stream(r: requests.Response) -> Generator[bytes]:
    return r.raw.stream()


@node(inputs=users_stream, outputs=Print())
def printer(stream: bytes) -> str:
    return str(stream)


run(printer, verbose=True)
