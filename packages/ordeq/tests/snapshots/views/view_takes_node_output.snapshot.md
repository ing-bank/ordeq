## Resource

```python
from ordeq import IO, node, run
from ordeq_common import Literal

placeholder = IO()

hello = Literal("Hello")


@node(inputs=[Literal("Jane"), hello], outputs=placeholder)
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


@node(inputs=placeholder)
def what_i_heard(v: str) -> None:
    print(f"I heard that {v}")


@node(inputs=what_i_heard)
def sink(s: str) -> None:
    print(s)


# This should succeed, as it produces the placeholder IO's value
run(hello_from_someone, sink, verbose=True)

# This should fail: it attempts to load placeholder IO
run(sink, verbose=True)

```

## Output

```text
io-0 --> Node:__main__:hello_from_someone
io-1 --> Node:__main__:hello_from_someone
Node:__main__:hello_from_someone --> io-2
io-2 --> View:__main__:what_i_heard
View:__main__:what_i_heard --> io-3
io-3 --> View:__main__:sink
View:__main__:sink --> io-4
I heard that Jane said 'Hello'
None
io-0 --> View:__main__:what_i_heard
View:__main__:what_i_heard --> io-1
io-1 --> View:__main__:sink
View:__main__:sink --> io-2
IOException: Failed to load IO(id=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _load_inputs
    data = cast("Input", input_io).load()

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    args = _load_inputs(node.inputs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=node_hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, node_hooks=node_hooks, run_hooks=run_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/view_takes_node_output.py", line LINO, in <module>
    run(sink, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Loading Literal('Jane')
DEBUG	ordeq.io	Persisting data for Literal('Jane')
INFO	ordeq.io	Loading Literal('Hello')
DEBUG	ordeq.io	Persisting data for Literal('Hello')
INFO	ordeq.runner	Running node 'hello_from_someone' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
INFO	ordeq.runner	Running view 'what_i_heard' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO(id=ID2)
INFO	ordeq.runner	Running view 'sink' in module '__main__'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for Literal('Jane')
DEBUG	ordeq.io	Unpersisting data for Literal('Hello')
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
INFO	ordeq.io	Loading IO(id=ID1)

```