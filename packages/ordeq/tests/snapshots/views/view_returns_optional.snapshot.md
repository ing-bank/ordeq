## Resource

```python
from ordeq import node, run
from ordeq_common import Print

glob = 2


@node
def conditional() -> None | str:
    if glob > 2:
        return "Higher value!"
    return None


@node(inputs=conditional, outputs=Print())
def n(v: None | str):
    return v


glob = 3
print(run(n, verbose=True))

glob = 1
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

  File "/packages/ordeq/tests/resources/views/view_returns_optional.py", line 20, in <module>
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
NodeGraph:
  Edges:
     view_returns_optional:conditional -> [view_returns_optional:n]
     view_returns_optional:n -> []
  Nodes:
     view_returns_optional:conditional: View(name=view_returns_optional:conditional)
     view_returns_optional:n: Node(name=view_returns_optional:n, inputs=[View(name=view_returns_optional:conditional)], outputs=[Print()])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_returns_optional:conditional'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "conditional" in "view_returns_optional"

```