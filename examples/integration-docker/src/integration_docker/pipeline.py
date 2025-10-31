from ordeq import node


@node
def hello_world() -> None:
    """Prints hello world to the console."""
    print("Hello, World!")
