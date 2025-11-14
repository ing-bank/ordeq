from ordeq import node


@node
def hello() -> str:
    return "Hello, World!"


@node(outputs=hello)
def say_hello() -> str:
    return "Hello!"
