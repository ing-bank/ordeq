## Resource

```python
import logging

from ordeq import node
from ordeq._graph import NodeGraph
from ordeq._runner import _run_graph
from ordeq_common import StringBuffer

logging.basicConfig(level=logging.INFO)
A, B, C, D, E, F = [StringBuffer(c) for c in "ABCDEF"]

plus = node(func=lambda x, y: f"{x} + {y}", inputs=(A, B), outputs=(C,))
minus = node(func=lambda x, y: f"{x} - {y}", inputs=(C, D), outputs=(E,))
square = node(func=lambda x: f"({x})^2", inputs=(E,), outputs=(F,))

nodes = {plus, minus, square}
_run_graph(NodeGraph.from_nodes(nodes))

```

## Logging

```text
INFO	ordeq.runner	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.runner	Running Node(func=__main__:<lambda>, ...)
INFO	ordeq.runner	Saving StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Loading cached data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running Node(func=__main__:<lambda>, ...)
INFO	ordeq.runner	Saving StringBuffer(_buffer=<_io.StringIO object at HASH5>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.runner	Loading StringBuffer(_buffer=<_io.StringIO object at HASH5>)
DEBUG	ordeq.io	Loading cached data for StringBuffer(_buffer=<_io.StringIO object at HASH5>)
INFO	ordeq.runner	Running Node(func=__main__:<lambda>, ...)
INFO	ordeq.runner	Saving StringBuffer(_buffer=<_io.StringIO object at HASH6>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH6>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH4>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH5>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH6>)

```