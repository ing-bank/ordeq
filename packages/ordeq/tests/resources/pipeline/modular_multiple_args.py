# Users should be able to run runnables in idiomatic Python:
# 1. running a pipeline should be as simple as calling a function
# 2. args should be passed in-memory, not through IOs
from typing import Any

from ordeq import IO, node, pipeline

x1 = IO[Any]()
x2 = IO[Any]()
x3 = IO[Any]()
y = IO[Any]()


@node(inputs=[x1, x2, x3])
def n1(a, b, c):
    return a + 1 + 2 * b + 3 * c


@node(inputs=n1)
def n2(b):
    return b * 2


@node(inputs=n2, outputs=y)
def n3(c):
    return c - 3


my_pipeline = pipeline(n1, n2, n3, inputs=[x1, x2, x3], outputs=[y])

output = my_pipeline(30, 1, 3)
assert output == 81

print("Should raise error for wrong number of args")
my_pipeline(30, 1)
