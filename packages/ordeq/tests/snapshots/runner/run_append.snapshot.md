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
INFO	ordeq.runner	Saving StringBuffer 'print_value:val' in module '__main__'
DEBUG	ordeq.io	Persisting data for StringBuffer 'print_value:val' in module '__main__'
INFO	ordeq.runner	Loading StringBuffer 'print_value:val' in module '__main__'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'print_value:val' in module '__main__'
INFO	ordeq.runner	Running node 'print_value' in module '__main__'
INFO	ordeq.runner	Saving Print()
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'print_value:val' in module '__main__'

```