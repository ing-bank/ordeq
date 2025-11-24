from ordeq import Input, node


@node(inputs=[Input("a"), Input("b")])
def my_node(*, a, b):
    print(f"a: {a}, b: {b}")
