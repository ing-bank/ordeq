from ordeq import node, Input


@node(inputs=Input[str]("A!"))
def my_node(a: str, *, b: str = "Hello"):
    print(a, b)
