## Resource

```python
from ordeq import Output, node, run


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


example = Example()


@node(outputs=[example])
def my_node() -> str:
    return "Hello, World!"

@node(inputs=[example])
def load_node(data: str) -> None:
    print("loading!", data)


run(my_node, load_node)

```

## Exception

```text
AttributeError: 'Example' object has no attribute 'load'
  File "/packages/ordeq/src/ordeq/_runner.py", line 53, in _run_node
    cast("Input", input_dataset).load() for input_dataset in node.inputs
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 132, in _run_graph
    computed = _run_node(patched_nodes[node], hooks=hooks, save=save_node)

  File "/packages/ordeq/src/ordeq/_runner.py", line 182, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq/tests/resources/runner/runner_load_output.py", line 21, in <module>
    run(my_node, load_node)
    ~~~^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
saving! Hello, World!

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'runner_load_output:load_node'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node Node(name=runner_load_output:my_node, outputs=[Output(idx=ID1)])
INFO	ordeq.io	Saving Output(idx=ID1)

```

## Typing

```text
packages/ordeq/tests/resources/runner/runner_load_output.py:16: error: List item 0 has incompatible type "Example"; expected "Input[Any] | Callable[..., Any]"  [list-item]
Found 1 error in 1 file (checked 1 source file)

```