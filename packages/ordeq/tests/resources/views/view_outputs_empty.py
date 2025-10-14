from ordeq import view


@view(outputs=[])
def view() -> str:
    return "Hello, World!"
