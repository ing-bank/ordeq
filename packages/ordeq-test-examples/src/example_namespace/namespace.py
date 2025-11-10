from ordeq import IO, node

from example_namespace.other import a, hello
from example_namespace.other import a as B
from example_namespace.other import hello as hi
from example_namespace.other import hello as world

ios = [a, B]


# node with anonymous IOs
@node(inputs=IO(), outputs=IO())
def node_with_inline_io(_):
    pass


x = node(hello)
y = node(world)


@node(inputs=ios, outputs=IO())
def node_with_list_input(_, __):
    return _


@node(inputs=node(hi), outputs=IO())
def node_with_node_input(_):
    return _
