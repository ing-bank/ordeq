# Checks the behaviour when running  a node that inputs the same IO as it
# outputs. We expect this to run without issues. More specifically, the runner
# should not detect cycles.
from ordeq_common import StringBuffer
from ordeq import node, run

io = StringBuffer("Hello, Ordeq!")
copy = StringBuffer()


@node(inputs=io, outputs=[io, copy])
def identity_and_copy(value: str) -> tuple[str, str]:
    return value, value


run(identity_and_copy, verbose=True)
print(copy.load())
