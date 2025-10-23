from ordeq import node


@node(outputs=[])
def view() -> str:
    return "Hello, World!"
