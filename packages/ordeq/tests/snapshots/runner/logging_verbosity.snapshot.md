## Resource

```python
import logging

from ordeq import node
from ordeq._graph import NodeGraph
from ordeq._nodes import get_node
from ordeq._runner import _run_graph
from ordeq_common import StringBuffer

logging.basicConfig(level=logging.INFO)
A, B, C, D, E, F = [StringBuffer(c) for c in "ABCDEF"]

plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
square = node(func=lambda x: f"({x})^2", inputs=(E,), outputs=(F,))

nodes = {get_node(n) for n in (plus, minus, square)}
_run_graph(NodeGraph.from_nodes(nodes))

```

## Exception

```text
AttributeError: 'set' object has no attribute 'views'
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in _collect
    for view in n.views:
                ^^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in _collect_views
    _collect(node)
    ~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    views = _collect_views(*nodes)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(BaseGraph.from_nodes(*nodes, patches=patches))
                          ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(NodeIOGraph.from_nodes(*nodes))
                          ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/runner/logging_verbosity.py", line LINO, in <module>
    _run_graph(NodeGraph.from_nodes(nodes))
               ~~~~~~~~~~~~~~~~~~~~^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```