from ordeq import IO, node
from ordeq_common import StringBuffer

x = StringBuffer("x")
y = StringBuffer()


def hello():
    pass


@node(inputs=[x], outputs=[y])
def world(a):
    return a


@node(inputs=IO(), outputs=IO())
def node_with_inline_io(_):
    pass
