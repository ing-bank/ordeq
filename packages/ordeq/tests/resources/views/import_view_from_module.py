from ordeq import node, run

from ordeq_common import Print

import import_view_from_module as module

printer = Print()


@node(inputs=module.my_view, outputs=printer)
def n(my_view: str) -> str:
    return f"Node received {my_view}"


run(n, verbose=True)
