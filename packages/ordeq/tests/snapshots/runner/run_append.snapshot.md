## Resource

```python
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

```

## Output

```text
asuffix

```

## Logging

```text
INFO	ordeq.runner	Running node 'add_suffix' in module '__main__'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Loading cached data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node 'print_value' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```