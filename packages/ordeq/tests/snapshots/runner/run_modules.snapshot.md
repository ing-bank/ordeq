## Resource

```python
import resources.runner.example_module_a as example_module_a
import resources.runner.example_module_b as example_module_b
from ordeq import run

run(example_module_a, example_module_b, verbose=True)

```

## Exception

```text
ValueError: IO StringBuffer(_buffer=<_io.StringIO object at HASH1>) cannot be outputted by more than one node
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in _build_graph
    raise ValueError(msg)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls(_build_graph(nodes | views))
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    graph = NodeGraph.from_nodes(nodes)

  File "/packages/ordeq/tests/resources/runner/run_modules.py", line LINO, in <module>
    run(example_module_a, example_module_b, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```