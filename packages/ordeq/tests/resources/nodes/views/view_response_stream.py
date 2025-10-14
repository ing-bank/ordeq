import requests

from ordeq import node, run
from ordeq_requests import Response
from ordeq_common import Print

users_response = Response(
    url="https://jsonplaceholder.typicode.com/users/"
)


@node(inputs=users_response)
def users_stream(r: requests.Response) -> bytes:
    return r.raw


@node(inputs=users_stream, outputs=Print())
def printer(stream: bytes) -> str:
    return str(stream)


print(run(printer, verbose=True))
