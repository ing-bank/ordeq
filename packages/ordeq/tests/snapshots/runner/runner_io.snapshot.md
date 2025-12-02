## Resource

```python
from ordeq import Input, node
from ordeq._runner import run
from ordeq_common import StringBuffer

x1 = Input[int](1)
x2 = StringBuffer()
x3 = StringBuffer("2")
x4 = StringBuffer()


@node(inputs=x1, outputs=x2)
def increment(x: int) -> str:
    return f"{x + 1}"


@node(inputs=[x2, x3], outputs=x4)
def decrement(x: str, y: str) -> str:
    return f"{int(x) - int(y)}"


run(increment, decrement, verbose=True)

print(x4.load())

# provide alternative IO when running the pipeline
p1 = Input[int](2)
p3 = Input[str]("33")
p4 = StringBuffer()
run(increment, decrement, io={x1: p1, x3: p3, x4: p4}, verbose=True)

print(p4.load())

```

## Output

```text
io-0 --> Node:__main__:decrement
io-1 --> Node:__main__:decrement
io-2 --> Node:__main__:increment
Node:__main__:decrement --> io-3
Node:__main__:increment --> io-4
ValueError: invalid literal for int() with base 10: ''
  File "/packages/ordeq/tests/resources/runner/runner_io.py", line LINO, in decrement
    return f"{int(x) - int(y)}"
              ~~~^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in inner
    return f(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    values = node.func(*args)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node_func
    raise exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    results = _run_node_func(node, args=args, hooks=hooks)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(
    ~~~~~~~~~~^
        graph, node_hooks=resolved_node_hooks, run_hooks=resolved_run_hooks
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/runner/runner_io.py", line LINO, in <module>
    run(increment, decrement, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
DEBUG	ordeq.runner	Running Input(id=ID1)
DEBUG	ordeq.io	Loading cached data for Input(id=ID1)
DEBUG	ordeq.io	Persisting data for IO 'increment:x' in module '__main__'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'decrement:x' in module '__main__'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for IO 'decrement:y' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'increment:x' in module '__main__'
DEBUG	ordeq.runner	Running node 'increment' in module '__main__'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Loading cached data for IO 'decrement:x' in module '__main__'
DEBUG	ordeq.io	Loading cached data for IO 'decrement:y' in module '__main__'
DEBUG	ordeq.runner	Running node 'decrement' in module '__main__'

```