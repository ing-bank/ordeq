import logging

from ordeq import IO, node, run

io1 = IO[str]()
io2 = IO[str]()


@node(outputs=io1)
def hello():
    return "Hello"


@node(inputs=io1, outputs=io2)
def greet(name: str):
    return f"{name}, World!"


logging.basicConfig(level=logging.INFO)
assert __name__ == "__main__"
run(__name__)
