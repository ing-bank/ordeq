from ordeq.framework import node
from ordeq_common import StringBuffer

x = StringBuffer("x")
y = StringBuffer()


def hello():
    pass


@node(inputs=[x], outputs=[y])
def world(a):
    return a
