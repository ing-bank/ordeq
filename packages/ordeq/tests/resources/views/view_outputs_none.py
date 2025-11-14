from ordeq import node


@node(outputs=None)
def view() -> str:
    return "Hello, World!"
