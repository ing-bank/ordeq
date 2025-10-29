from ordeq import IO, node


@node(inputs=IO(), outputs=IO())
def node_with_inline_io(_):
    pass
