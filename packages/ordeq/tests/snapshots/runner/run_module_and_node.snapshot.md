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
INFO	ordeq.runner	Loading Input 'x1' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for Input 'x1' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Running node 'increment' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Saving StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Running View(func=__main__:noop, ...)
INFO	ordeq.runner	Saving IO(id=ID1)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.runner	Loading StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Loading StringBuffer 'x3' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x3' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Running node 'decrement' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Saving StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x3' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module_and_node.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```