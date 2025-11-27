# ruff: noqa: PLR0124 (comparison to self)
from dataclasses import dataclass

from ordeq import IO


@dataclass(frozen=True)
class CustomIO(IO):
    attr: str

    def load(self) -> str:
        return self.attr

    def save(self, data: str) -> None:
        print(data)


a = CustomIO("a")
b = CustomIO("b")

assert a is not b
assert a != b
assert hash(a) != hash(b)

assert a is a
assert a == a
assert hash(a) == hash(a)

B = CustomIO("b")

assert b is not B
assert b != B
assert hash(b) != hash(B)
