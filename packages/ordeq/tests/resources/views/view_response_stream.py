import requests

from ordeq import node, run
from ordeq_common import Print, Literal
from typing import Generator

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
users_response = Literal(response)


@node(inputs=users_response)
def users_stream(r: requests.Response) -> Generator[bytes]:
    return r.raw.stream()


@node(inputs=users_stream, outputs=Print())
def printer(stream: bytes) -> str:
    return str(stream)


print(run(printer, verbose=True))
