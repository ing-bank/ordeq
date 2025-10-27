from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def conditional() -> None | str:
    if glob > 2:
        return "Higher value!"
    return None


@node(inputs=conditional, outputs=Print())
def n(v: None | str):
    return v


glob = 3
print(run(n, verbose=True))

glob = 1
print(run(n, verbose=True))
