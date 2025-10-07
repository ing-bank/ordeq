# Imported by ./run_module.py, ./run_modules.py and ./run_module_and_nodes.py
from ordeq import node
from ordeq_common import Literal, StringBuffer

x1 = Literal(12345)
x2 = StringBuffer()
x3 = StringBuffer("12345")
x4 = StringBuffer()


@node(inputs=x1, outputs=x2)
def increment(x: int) -> str:
    return f"{x + 1}"


@node(inputs=[x2, x3], outputs=x4)
def decrement(x: str, y: str) -> str:
    return f"{int(x) - int(y)}"
