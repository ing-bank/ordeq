from ordeq import node


def func() -> str:
    return "Hello, World!"


@node(inputs=func)
def hello(data: str) -> None:
    print(data)
