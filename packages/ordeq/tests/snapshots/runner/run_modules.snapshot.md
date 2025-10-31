## Resource

```python
from ordeq import run
from resources.runner import example_module_a, example_module_b

run(example_module_a, example_module_b, verbose=True)

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/run_modules.py", line LINO, in <module>
    run(example_module_a, example_module_b, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     resources.runner.example_module_a:decrement -> []
     resources.runner.example_module_a:increment -> [resources.runner.example_module_a:decrement]
     resources.runner.example_module_b:decrement -> []
     resources.runner.example_module_b:increment -> [resources.runner.example_module_b:decrement]
  Nodes:
     resources.runner.example_module_a:decrement: Node(name=resources.runner.example_module_a:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>), StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
     resources.runner.example_module_a:increment: Node(name=resources.runner.example_module_a:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])
     resources.runner.example_module_b:decrement: Node(name=resources.runner.example_module_b:decrement, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>), StringBuffer(_buffer=<_io.StringIO object at HASH5>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH6>)])
     resources.runner.example_module_b:increment: Node(name=resources.runner.example_module_b:increment, inputs=[Literal(12345)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])

```