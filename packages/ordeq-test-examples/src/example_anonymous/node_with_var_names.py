from ordeq import Input, node


@node(inputs=[Input(1), Input(3)])
def add(a: int, b: int) -> int:
    return a + b
