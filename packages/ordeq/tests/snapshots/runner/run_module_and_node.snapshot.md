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
io-0 --> Node:resources.runner.example_module_a:decrement
io-1 --> Node:resources.runner.example_module_a:decrement
io-2 --> Node:resources.runner.example_module_a:increment
Node:resources.runner.example_module_a:decrement --> io-3
Node:resources.runner.example_module_a:increment --> io-4
View:View(func=__main__:noop, ...) --> io-5

```

## Logging

```text
DEBUG	ordeq.runner	Running Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for IO 'increment:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for IO 'decrement:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'decrement:y' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running View(func=__main__:noop, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO 'increment:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running node 'increment' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Saving StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for IO 'decrement:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for IO 'decrement:y' in module 'resources.runner.example_module_a'
DEBUG	ordeq.runner	Running node 'decrement' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Saving StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for IO 'decrement:y' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for IO 'decrement:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for IO 'increment:x' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module_and_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```