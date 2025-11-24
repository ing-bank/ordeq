from ordeq import Input, node
from ordeq_common import StringBuffer


@node(
    inputs=(StringBuffer("a"), Input[int](value=4)), outputs=StringBuffer("z")
)
def func(*args: str | int) -> str:
    return "".join(str(i) for i in args)


print(func("a", 4))
