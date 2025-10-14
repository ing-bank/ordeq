from ordeq import IO, view



@view(outputs=IO())
def view() -> str:
    return "Hello, World!"
