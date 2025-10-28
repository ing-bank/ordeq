## Resource

```python
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

```

## Output

```text
NodeGraph:
  Edges:
     identity_node_with_copy:identity_and_copy -> []
  Nodes:
     identity_node_with_copy:identity_and_copy: Node(name=identity_node_with_copy:identity_and_copy, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)])
Hello, Ordeq!

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "identity_and_copy" in module "identity_node_with_copy"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```