from ordeq import node, run
from ordeq_common import Print, StringBuffer

io = StringBuffer("a")


@node(outputs=io)
def add_suffix() -> str:
    return "suffix"


@node(inputs=io, outputs=Print())
def print_value(val: str):
    return val


# This resource shows that IOs that are loaded after being outputted only
# load the data computed by the node, not the full data.
run(add_suffix, print_value)
