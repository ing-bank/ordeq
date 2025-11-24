from ordeq import Input, node, run


@node(inputs=[Input[str]("a"), Input[str]("b")])
def my_node(a, /, b):
    print(f"a: {a}, b: {b}")


run(my_node)
