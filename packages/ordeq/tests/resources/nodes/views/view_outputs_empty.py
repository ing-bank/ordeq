from ordeq import node, run


@node(outputs=[])
def view() -> str:
    return "Hello, World!"


@node(inputs=view)
def n(v: str) -> None:
    print(f"Node received {v}")


run(n, verbose=True)
