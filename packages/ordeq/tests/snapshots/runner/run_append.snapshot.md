## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer, Print

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

```

## Output

```text
suffix

```

## Logging

```text
INFO	ordeq.runner	Running node "add_suffix" in module "run_append"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "print_value" in module "run_append"
INFO	ordeq.io	Saving Print()

```