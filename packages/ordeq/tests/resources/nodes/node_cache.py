from functools import cache

from ordeq import Input, node, run
from ordeq_common import StringBuffer

out = StringBuffer()


@node(inputs=Input("test"), outputs=out)
@cache
def my_node(t: str):
    print("I'm printed only once")
    return t


print(my_node("test"))
print(my_node("test"))

run(my_node)
print("Expect 'test':")
print(out.load())
