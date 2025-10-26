# Checks the behaviour when running an identity node:
# a node that inputs the same IO as it outputs.
# Running this node should be allowed: the runner should not detect a cycle.
from ordeq_common import StringBuffer
from ordeq import node, run

io = StringBuffer("Hello, Ordeq!")


@node(inputs=io, outputs=io)
def identity(value: str) -> str:
    return value


run(identity, verbose=True)
print(io.load())  # Prints the value after running the node
