# Checks the behaviour when running an identity node: a node that inputs the
# same IO as it outputs. We expect this to run without issues. More
# specifically, the runner should not detect cycles.
from ordeq_common import StringBuffer
from ordeq import node, run

io = StringBuffer("Hello, Ordeq!")


@node(inputs=io, outputs=io)
def identity(value: str) -> str:
    return value


run(identity, verbose=True)
print(io.load())  # Prints the value after running the node
