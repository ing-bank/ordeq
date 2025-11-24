## Resource

```python
from ordeq import node, run
from resources.runner import example_module_a


@node
def noop() -> None:
    return


run(example_module_a, noop, verbose=True)

```

## Output

```text
io-0 --> Node:resources.runner.example_module_a:increment
Node:resources.runner.example_module_a:increment --> io-2
io-1 --> Node:resources.runner.example_module_a:decrement
io-2 --> Node:resources.runner.example_module_a:decrement
Node:resources.runner.example_module_a:decrement --> io-3
View:View(func=__main__:noop, ...) --> io-4

```

## Logging

```text
INFO	ordeq.io	Loading Literal(12345)
DEBUG	ordeq.io	Persisting data for Literal(12345)
INFO	ordeq.runner	Running node 'increment' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running view View(func=__main__:noop, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running node 'decrement' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Unpersisting data for Literal(12345)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module_and_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```