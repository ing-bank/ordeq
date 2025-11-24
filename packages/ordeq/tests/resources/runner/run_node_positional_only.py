from ordeq import Input, node, run


@node(inputs=[Input("a"), Input("b")])
def my_node(a, /, b):
    print(f"a: {a}, b: {b}")


run(my_node)
