from ordeq import IO, node


@node(input=IO(), outputs=IO())
def my_node(a):
    return a
