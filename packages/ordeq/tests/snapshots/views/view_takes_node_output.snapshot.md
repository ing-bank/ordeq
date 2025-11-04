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
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/views/view_takes_node_output.py", line LINO, in <module>
    run(hello_from_someone, sink, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     view_takes_node_output:hello_from_someone -> [view_takes_node_output:what_i_heard]
     view_takes_node_output:sink -> []
     view_takes_node_output:what_i_heard -> [view_takes_node_output:sink]
  Nodes:
     view_takes_node_output:hello_from_someone: Node(name=view_takes_node_output:hello_from_someone, inputs=[Literal('Jane'), Literal('Hello')], outputs=[IO(idx=ID1)])
     view_takes_node_output:sink: View(name=view_takes_node_output:sink, inputs=[View(name=view_takes_node_output:what_i_heard, inputs=[IO(idx=ID1)])])
     view_takes_node_output:what_i_heard: View(name=view_takes_node_output:what_i_heard, inputs=[IO(idx=ID1)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_takes_node_output:what_i_heard'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_takes_node_output:sink'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```