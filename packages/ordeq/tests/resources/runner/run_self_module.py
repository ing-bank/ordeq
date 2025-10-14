from ordeq import node, run


@node
def hello() -> None:
    print("Hello world!")


run(__name__)
