from ordeq import node, run


@node
def world() -> None:
    print("Hello, World!")
