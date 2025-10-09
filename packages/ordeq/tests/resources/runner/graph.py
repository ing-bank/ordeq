from ordeq import node
from ordeq.runner import run
from ordeq_common import StringBuffer

I1 = StringBuffer("Hello")
I2 = StringBuffer("world!")
R1 = StringBuffer()
R2 = StringBuffer()
R3 = StringBuffer()
R4 = StringBuffer()


@node(inputs=[I1, I2], outputs=[R1])
def f1(i: str, j: str) -> str:
    return f"{i} + {j}"


@node(inputs=[I2, R1], outputs=[R2])
def f2(i: str, j: str) -> str:
    return f"{i} - {j}"


@node(inputs=[R1], outputs=[R3])
def f3(i: str) -> str:
    return f"{i} * 2"


@node(inputs=[R1, R2, R3], outputs=[R4])
def f4(i: str, j: str, k: str) -> str:
    return f"{i} / {j} + {k}"


pipeline = {f1, f2, f3, f4}

output = run(*pipeline, save="all", verbose=True)
print(output[R4])

output = run(*pipeline, save="sinks", verbose=True)
print(output[R4])

output = run(*pipeline, save="none", verbose=True)
print(output[R4])
