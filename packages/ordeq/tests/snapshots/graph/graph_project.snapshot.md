## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_project
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._process_nodes import _collect_views
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_project)
nodes_and_views = _collect_views(*nodes)
base_graph = NodeIOGraph.from_nodes(nodes_and_views)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes_and_views)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph
io-0 --> View:example_project.nodes_with_view:greet
View:example_project.nodes_with_view:greet --> io-6
io-1 --> Node:example_project.inner.nodes:func
io-2 --> Node:example_project.nodes:func
io-3 --> Node:example_project.nodes_import_alias:func
io-3 --> Node:example_project.nodes_import:func_b
io-3 --> Node:example_project.nodes_import:func_a
io-4 --> Node:example_project.nodes_import_alias:func
io-4 --> Node:example_project.nodes_import:func_b
io-4 --> Node:example_project.nodes_import:func_a
io-5 --> Node:example_project.nodes_with_inline_io:greet
io-6 --> Node:example_project.nodes_with_view:farewell
Node:example_project.inner.nodes:func --> io-7
Node:example_project.nodes:func --> io-8
Node:example_project.nodes_import:func_a --> io-9
Node:example_project.nodes_import:func_b --> io-10
Node:example_project.nodes_import_alias:func --> io-11
Node:example_project.nodes_with_inline_io:greet --> io-12
Node:example_project.nodes_with_view:farewell --> io-13
NodeGraph
View:example_project.nodes_with_view:greet --> Unit:example_project.nodes_with_view:greet
Node:example_project.nodes_with_view:farewell --> Unit:example_project.nodes_with_view:farewell
Node:example_project.nodes_with_inline_io:greet --> Unit:example_project.nodes_with_inline_io:greet
Node:example_project.nodes_import_alias:func --> Unit:example_project.nodes_import_alias:func
Node:example_project.nodes_import:func_b --> Unit:example_project.nodes_import:func_b
Node:example_project.nodes_import:func_a --> Unit:example_project.nodes_import:func_a
Node:example_project.nodes:func --> Unit:example_project.nodes:func
Node:example_project.inner.nodes:func --> Unit:example_project.inner.nodes:func
Topological ordering
(Unit(value=Input(id=ID1)),
 View(module=example_project.nodes_with_view, name=greet, inputs=[Input(id=ID1)]),
 Unit(value=IO(id=ID2)),
 Unit(value=Input(id=ID3)),
 Unit(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 Unit(value=Input(id=ID4)),
 Unit(value=IO(id=ID5)),
 Unit(value=IO(id=ID6)),
 Node(module=example_project.nodes_with_view, name=farewell, inputs=[IO(id=ID2)], outputs=[Print()]),
 Node(module=example_project.nodes_with_inline_io, name=greet, inputs=[Input(id=ID3)], outputs=[IO(id=ID7)]),
 Node(module=example_project.nodes_import_alias, name=func, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}),
 Node(module=example_project.nodes_import, name=func_b, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}),
 Node(module=example_project.nodes_import, name=func_a, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
 Node(module=example_project.nodes, name=func, inputs=[IO(id=ID5)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(module=example_project.inner.nodes, name=func, inputs=[IO(id=ID6)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Unit(value=Print()),
 Unit(value=IO(id=ID7)),
 Unit(value=Print()),
 Unit(value=Print()),
 Unit(value=Print()),
 Unit(value=Print()),
 Unit(value=Print()))

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID4)
DEBUG	ordeq.io	Persisting data for Input(id=ID8)
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```