from ordeq import node


def hello() -> str:
    return "Hello, World!"


# This should raise a TypeError (it does not currently)
@node(outputs=hello)
def say_hello() -> str:
    return "Hello!"
