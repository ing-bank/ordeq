from ordeq import node, run
from resources.runner import example_module_a


@node
def noop() -> None:
    return


run(example_module_a, noop, verbose=True)
