## Resource

```python
from ordeq import node, run
from ordeq_common import Literal

hello_io = Literal("Hello")


@node(inputs=hello_io)
def hello_world(hello: str) -> tuple[str, str]:
    return hello, "World!"


@node(inputs=hello_world)
def n(v: tuple[str, ...]):
    print(f"Node received '{' '.join(v)}'")


print(run(n, verbose=True, io={hello_io: Literal("Buenos dias")}))

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

  File "/packages/ordeq/tests/resources/views/view_patch_io.py", line 17, in <module>
    print(run(n, verbose=True, io={hello_io: Literal("Buenos dias")}))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     view_patch_io:hello_world -> [view_patch_io:n]
     view_patch_io:n -> []
  Nodes:
     view_patch_io:hello_world: View(name=view_patch_io:hello_world, inputs=[Literal('Hello')])
     view_patch_io:n: View(name=view_patch_io:n, inputs=[View(name=view_patch_io:hello_world, inputs=[Literal('Hello')])])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_patch_io:hello_world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_patch_io:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('Buenos dias')
INFO	ordeq.runner	Running node "hello_world" in "view_patch_io"

```

## Typing

```text
packages/ordeq/tests/resources/views/view_patch_io.py:17: error: Argument "io" to "run" has incompatible type "dict[Literal[str], Literal[str]]"; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
Found 1 error in 1 file (checked 1 source file)

```