## Resource

```python
from ordeq import NodeHook, run


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node: {node.name}")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node: {node.name}")


run("example_1", hooks=["example_1.hooks:MyHook", MyHook()])

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_hook_ref_and_object.py", line LINO, in <module>
    run("example_1", hooks=["example_1.hooks:MyHook", MyHook()])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
Starting the run

```