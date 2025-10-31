## Resource

```python
from ordeq import Node, NodeHook, Output, OutputHook, node, run


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


class MixedHook(NodeHook, OutputHook):
    node: Node | None = None

    def before_node_run(self, node: Node):
        self.node = node

    def before_output_save(self, output: Output, data) -> None:
        if self.node is not None:
            print(
                f"Hook: before saving output of node {self.node.name} "
                f"with data: {data}"
            )


hook = MixedHook()
example = Example().with_output_hooks(hook)


@node(outputs=[example])
def my_node() -> str:
    return "Hello, World!"


run(my_node, hooks=[hook])

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/hooks/mixed_hook.py", line LINO, in <module>
    run(my_node, hooks=[hook])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```