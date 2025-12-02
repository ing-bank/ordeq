from functools import cache

from ordeq import Input, node, run
from ordeq_common import StringBuffer

out = StringBuffer()


@cache
def func(a: str):
    print("I'm printed only once")
    return a


a = node(func, inputs=Input("test"))
b = node(func, inputs=Input("test"))

run(a, b)
