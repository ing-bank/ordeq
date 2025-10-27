## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[Literal("Jane"), hello])
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


print(repr(get_node(hello_from_someone)))


@node(inputs=hello_from_someone)
def n(v: str) -> None:
    print(f"I heard that {v}")


print(run(n, verbose=True))

```

## Exception

```text
AttributeError: 'View' object has no attribute 'load'
  File "/packages/ordeq/src/ordeq/_runner.py", line 56, in _run_node
    cast("Input", input_dataset).load() for input_dataset in node.inputs
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 135, in _run_graph
    computed = _run_node(
        name, patched_nodes[name, node], hooks=hooks, save=save_node
    )

  File "/packages/ordeq/src/ordeq/_runner.py", line 187, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq/tests/resources/views/view_inputs_view_and_io.py", line 27, in <module>
    print(run(n, verbose=True))
          ~~~^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
View(name=view_inputs_view_and_io:hello)
View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])
NodeGraph:
  Edges:
     view_inputs_view_and_io:hello -> [view_inputs_view_and_io:hello_from_someone]
     view_inputs_view_and_io:hello_from_someone -> [view_inputs_view_and_io:n]
     view_inputs_view_and_io:n -> []
  Nodes:
     view_inputs_view_and_io:hello: View(name=view_inputs_view_and_io:hello)
     view_inputs_view_and_io:hello_from_someone: View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])
     view_inputs_view_and_io:n: View(name=view_inputs_view_and_io:n, inputs=[View(name=view_inputs_view_and_io:hello_from_someone, inputs=[Literal('Jane'), View(name=view_inputs_view_and_io:hello)])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:hello_from_someone'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_view_and_io:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "hello" in "view_inputs_view_and_io"
INFO	ordeq.io	Loading Literal('Jane')

```