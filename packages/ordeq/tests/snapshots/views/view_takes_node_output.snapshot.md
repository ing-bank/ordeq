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
NodeResourceGraph(edges={Node(name=__main__:hello_from_someone, inputs=[Literal('Jane'), Literal('Hello')], outputs=[IO(id=ID1)]): [Resource(value=IO(id=ID1))], View(name=__main__:what_i_heard, inputs=[IO(id=ID1)]): [Resource(value=IO(id=ID2))], View(name=__main__:sink, inputs=[IO(id=ID2)]): [Resource(value=IO(id=ID3))], Resource(value=Literal('Jane')): [Node(name=__main__:hello_from_someone, inputs=[Literal('Jane'), Literal('Hello')], outputs=[IO(id=ID1)])], Resource(value=Literal('Hello')): [Node(name=__main__:hello_from_someone, inputs=[Literal('Jane'), Literal('Hello')], outputs=[IO(id=ID1)])], Resource(value=IO(id=ID1)): [View(name=__main__:what_i_heard, inputs=[IO(id=ID1)])], Resource(value=IO(id=ID2)): [View(name=__main__:sink, inputs=[IO(id=ID2)])], Resource(value=IO(id=ID3)): []})
I heard that Jane said 'Hello'
None
NodeResourceGraph(edges={View(name=__main__:what_i_heard, inputs=[IO(id=ID1)]): [Resource(value=IO(id=ID2))], View(name=__main__:sink, inputs=[IO(id=ID2)]): [Resource(value=IO(id=ID3))], Resource(value=IO(id=ID1)): [View(name=__main__:what_i_heard, inputs=[IO(id=ID1)])], Resource(value=IO(id=ID2)): [View(name=__main__:sink, inputs=[IO(id=ID2)])], Resource(value=IO(id=ID3)): []})
IOException: Failed to load IO(id=ID1).

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_node
    data = cast("Input", input_dataset).load()

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    _run_node(node, hooks=hooks)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:what_i_heard'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:sink'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('Jane')
INFO	ordeq.io	Loading Literal('Hello')
INFO	ordeq.runner	Running node "hello_from_someone" in module "__main__"
INFO	ordeq.runner	Running view "what_i_heard" in module "__main__"
INFO	ordeq.runner	Running view "sink" in module "__main__"
INFO	ordeq.io	Loading IO(id=ID1)

```