from ordeq import IO, node

a = IO()  # type: ignore


def hello():
    pass


@node(inputs=a, outputs=IO())
def func(b):
    return b
