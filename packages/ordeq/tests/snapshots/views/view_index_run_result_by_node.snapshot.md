## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def view() -> str:
    return "Hello!"


@node(inputs=view, outputs=Print())
def hello(data: str) -> None:
    print(data)


result = run(hello)
print(view, 'computed', result[get_node(view)])

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

  File "/packages/ordeq/tests/resources/views/view_index_run_result_by_node.py", line 16, in <module>
    result = run(hello)

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_index_run_result_by_node:view'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "view" in "view_index_run_result_by_node"

```

## Typing

```text
packages/ordeq/tests/resources/views/view_index_run_result_by_node.py:17: error: Invalid index type "Node[Any, Any]" for "dict[Input[Any] | Output[Any] | View[Any, Any], Any]"; expected type "Input[Any] | Output[Any] | View[Any, Any]"  [index]
Found 1 error in 1 file (checked 1 source file)

```