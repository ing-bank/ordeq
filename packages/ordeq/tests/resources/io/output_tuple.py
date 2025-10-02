from dataclasses import dataclass

from ordeq import Output

from ordeq import node
from typing import TypeVar


@dataclass(frozen=True)
class Tuple(Output[tuple]):
    def save(self, data: tuple) -> None:
        print(self, 'data:', data)


io = Tuple()
io.save(('hello', 'world'))


@node(outputs=io)
def create_unit() -> int:
    return 1


# This should not raise a type error: io.save accepts tuple[int, int]
@node(outputs=io)
def create_tuple() -> tuple[int, int]:
    return 1, 2
