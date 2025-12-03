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
Node:example_project.inner.nodes:func --> io-20
Node:example_project.nodes:func --> io-21
Node:example_project.nodes_import:func_a --> io-22
Node:example_project.nodes_import:func_b --> io-23
Node:example_project.nodes_import_alias:func --> io-24
Node:example_project.nodes_with_inline_io:greet --> io-25
Node:example_project.nodes_with_view:farewell --> io-26
NodeGraph
View:example_project.nodes_with_view:greet --> Stub:example_project.nodes_with_view:greet
Node:example_project.nodes_with_view:farewell --> Stub:example_project.nodes_with_view:farewell
Node:example_project.nodes_with_inline_io:greet --> Stub:example_project.nodes_with_inline_io:greet
Node:example_project.nodes_import_alias:func --> Stub:example_project.nodes_import_alias:func
Node:example_project.nodes_import:func_b --> Stub:example_project.nodes_import:func_b
Node:example_project.nodes_import:func_a --> Stub:example_project.nodes_import:func_a
Node:example_project.nodes:func --> Stub:example_project.nodes:func
Node:example_project.inner.nodes:func --> Stub:example_project.inner.nodes:func
Topological ordering
(Stub(value=Input(id=ID1)),
 View(module=example_project.nodes_with_view, name=greet, inputs=[Input(id=ID1)]),
 Stub(value=IO(id=ID2)),
 Stub(value=Input(id=ID3)),
 Stub(value=StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 Stub(value=Input(id=ID4)),
 Stub(value=IO(id=ID5)),
 Stub(value=IO(id=ID6)),
 Node(module=example_project.nodes_with_view, name=farewell, inputs=[IO(id=ID2)], outputs=[Print()]),
 Node(module=example_project.nodes_with_inline_io, name=greet, inputs=[Input(id=ID3)], outputs=[IO(id=ID7)]),
 Node(module=example_project.nodes_import_alias, name=func, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}),
 Node(module=example_project.nodes_import, name=func_b, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}),
 Node(module=example_project.nodes_import, name=func_a, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
 Node(module=example_project.nodes, name=func, inputs=[IO(id=ID5)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(module=example_project.inner.nodes, name=func, inputs=[IO(id=ID6)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Stub(value=Print()),
 Stub(value=IO(id=ID8)),
 Stub(value=IO(id=ID9)),
 Stub(value=IO(id=ID7)),
 Stub(value=Print()),
 Stub(value=Print()),
 Stub(value=IO(id=ID10)),
 Stub(value=IO(id=ID11)),
 Stub(value=Print()),
 Stub(value=IO(id=ID12)),
 Stub(value=Print()),
 Stub(value=IO(id=ID13)),
 Stub(value=Print()))

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID4)
DEBUG	ordeq.io	Persisting data for Input(id=ID14)
DEBUG	ordeq.io	Persisting data for Input(id=ID3)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```