from ordeq import node, run


@node
def view() -> tuple[str, str]:
    return "Hello", "World!"


@node(inputs=view)
def n(v: tuple[str, str]):
    print(f"Node received {v}")


# This should be runnable (the tuple returned by view should be passed as a
# single argument to n). Currently, this will raise an error because the
# runner checks the number of outputs against the number of arguments.
print(run(n, verbose=True))
