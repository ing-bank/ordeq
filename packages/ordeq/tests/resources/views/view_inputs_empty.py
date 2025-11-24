from ordeq import node


@node()
def my_view() -> None:
    print("Hello, world!")


print(repr(my_view))
