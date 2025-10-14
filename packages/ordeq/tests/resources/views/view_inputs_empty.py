from ordeq import view
from ordeq._nodes import get_view


@view()
def my_view() -> None:
    print("Hello, world!")


print(repr(get_view(my_view)))
