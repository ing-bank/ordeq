from ordeq import Input, node


@node(inputs=[Input[str]("A!"), Input(4)])
def func2(a: str, *, something: int) -> None:
    print(a, something)
