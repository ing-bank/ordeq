## Resource

```python
from functools import cache

from ordeq import Input, node, run
from ordeq_common import StringBuffer

out = StringBuffer()


@node(inputs=Input("test"), outputs=out)
@cache
def my_node(t: str):
    print("I'm printed only once")
    return t


print(my_node("test"))
print(my_node("test"))

run(my_node)
print("Expect 'test':")
print(out.load())

```

## Output

```text
I'm printed only once
test
test
Expect 'test':
test

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input 'my_node:t' in module '__main__'
INFO	ordeq.runner	Running node 'my_node' in module '__main__'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)

```