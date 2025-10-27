from ordeq import node
from ordeq._runner import run
from ordeq_common import StringBuffer

I1 = StringBuffer("Hello")
I2 = StringBuffer("world!")


def f1(i: str, j: str) -> str:
    return f"{i} {j}"


def c():
    a = I1.load()
    b = I2.load()
    return f1(a, b)


print(c())

print(node(c, outputs=StringBuffer("result"))())

output = StringBuffer("Result: ")
run(node(c, outputs=output))
print(output.load())
