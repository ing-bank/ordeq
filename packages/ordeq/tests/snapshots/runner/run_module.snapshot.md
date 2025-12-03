## Resource

```python
from ordeq import run
from resources.runner import example_module_a

run(example_module_a, verbose=True)

```

## Output

```text
io-0 --> Node:resources.runner.example_module_a:increment
Node:resources.runner.example_module_a:increment --> io-2
io-1 --> Node:resources.runner.example_module_a:decrement
io-2 --> Node:resources.runner.example_module_a:decrement
Node:resources.runner.example_module_a:decrement --> io-7

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input 'x1' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Running node 'increment' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Saving StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Loading cached data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Loading StringBuffer 'x3' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x3' in module 'resources.runner.example_module_a'
INFO	ordeq.runner	Running node 'decrement' in module 'resources.runner.example_module_a'
INFO	ordeq.io	Saving StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x4' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x2' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x3' in module 'resources.runner.example_module_a'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x4' in module 'resources.runner.example_module_a'

```

## Typing

```text
packages/ordeq/tests/resources/runner/run_module.py:2:6: error[unresolved-import] Cannot resolve imported module `resources.runner`
Found 1 diagnostic

```