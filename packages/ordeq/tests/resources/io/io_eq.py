# ruff: noqa: PLR0124 (comparison to self)
from ordeq import IO

a = IO[str]()
b = IO[str]()

assert a is not b
assert a != b
assert hash(a) != hash(b)

assert a is a
assert a == a
assert hash(a) == hash(a)
