from ordeq import node, run

from ordeq_common import Print

import module_views as module

printer = Print()


# This may be evidence that we should encourage the user to
# create views in a separate module.
# Unlike the other resources, we don't have a name clash between the
# inputs and the node function argument.
@node(inputs=module.my_view, outputs=printer)
def n(my_view: str) -> str:
    return f"Node received {my_view}"


run(n, verbose=True)
