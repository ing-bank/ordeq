from collections.abc import Iterator
from typing import Any

import requests
from ordeq import node, run
from ordeq_common import Literal

# Data retrieved from https://jsonplaceholder.typicode.com/users/1
users_response = Literal({
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {"lat": "-37.3159", "lng": "81.1496"},
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets",
    },
})


# View that returns an iterable from a regular/non-iterable IO:
@node(inputs=users_response)
def users_lines(r: requests.Response) -> Iterator[Any]:
    return r.iter_lines()


@node(inputs=users_lines)
def concatenate(lines: Iterator[Any]) -> None:
    for line in lines:
        print(line)


run(concatenate, verbose=True)
