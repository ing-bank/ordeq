from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def view() -> None | int:
    if glob > 2:
        return glob
    return None


@node(inputs=view, outputs=Print())
def n(v: None | int):
    return v


glob = 3
print(run(n, verbose=True))

glob = 1
print(run(n, verbose=True))
