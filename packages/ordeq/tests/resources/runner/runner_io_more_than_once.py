from ordeq import Input, node
from ordeq._runner import run
from ordeq_common import StringBuffer

x1 = Input(1)
x2 = StringBuffer()
x3 = StringBuffer()


@node(inputs=x1, outputs=x2)
def increment(x: int) -> str:
    return f"{x + 1}"


@node(inputs=[x2, x1], outputs=x3)
def decrement(x: str, y: str) -> str:
    return f"{int(x) - int(y)}"


run(increment, decrement, verbose=True)

print(x3.load())

# provide alternative IO when running the pipeline
p1 = Input(200)
run(increment, decrement, io={x1: p1}, verbose=True)

print(x3.load())
