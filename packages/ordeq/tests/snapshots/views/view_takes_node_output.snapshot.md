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

## Exception

```text
IOException: Failed to load IO(idx=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in load_wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in load_wrapper
    return load_func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in load_wrapper
    result = load_func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    return composed(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    cast("Input", input_dataset).load() for input_dataset in node.inputs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=hooks, save=save_node)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

## Output

```text
Node:__main__:hello_from_someone --> io-1
io-1 --> View:__main__:what_i_heard
View:__main__:sink --> io-2
View:__main__:what_i_heard --> io-3
io-3 --> View:__main__:sink
io-4 --> Node:__main__:hello_from_someone
io-5 --> Node:__main__:hello_from_someone
I heard that Jane said 'Hello'
None
View:__main__:sink --> io-1
View:__main__:what_i_heard --> io-2
io-2 --> View:__main__:sink
io-3 --> View:__main__:what_i_heard

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:what_i_heard'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:sink'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.io	Loading Literal('Hello')
INFO	ordeq.runner	Running node "hello_from_someone" in module "__main__"
INFO	ordeq.runner	Running view "what_i_heard" in module "__main__"
INFO	ordeq.runner	Running view "sink" in module "__main__"
INFO	ordeq.io	Loading IO(idx=ID1)

```