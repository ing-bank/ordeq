## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def hello() -> str:
    return "Hello, World!"


print(repr(get_node(hello)))


@node(inputs=[hello, hello], outputs=Print())
def n(fst: str, snd: str) -> str:
    return f"{fst} == {snd}'"


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

  File "/packages/ordeq/tests/resources/views/node_inputs_same_view_twice.py", line 19, in <module>
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
View(name=node_inputs_same_view_twice:hello)
NodeGraph:
  Edges:
     node_inputs_same_view_twice:hello -> [node_inputs_same_view_twice:n, node_inputs_same_view_twice:n]
     node_inputs_same_view_twice:n -> []
  Nodes:
     node_inputs_same_view_twice:hello: View(name=node_inputs_same_view_twice:hello)
     node_inputs_same_view_twice:n: Node(name=node_inputs_same_view_twice:n, inputs=[View(name=node_inputs_same_view_twice:hello), View(name=node_inputs_same_view_twice:hello)], outputs=[Print()])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_same_view_twice:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "hello" in "node_inputs_same_view_twice"

```