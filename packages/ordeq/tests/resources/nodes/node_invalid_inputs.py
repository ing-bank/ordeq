from ordeq import node

print("Should raise an error:")


@node(inputs=["blabla"])
def func() -> None:
    pass
