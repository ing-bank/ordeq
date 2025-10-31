from ordeq import IO, node


@node(inputs=IO(), output=IO())
def my_node(a):
    return a
