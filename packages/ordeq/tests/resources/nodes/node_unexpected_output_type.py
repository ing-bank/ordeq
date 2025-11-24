from ordeq import Input, node

x = Input("X")


@node(inputs=x, outputs=x)  # outputs should be of type Output or IO
def func(data: str) -> str:
    return data + data
