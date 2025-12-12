from ordeq import node


@node
def my_node(*, a: str = "Hello"):
    print(a)
