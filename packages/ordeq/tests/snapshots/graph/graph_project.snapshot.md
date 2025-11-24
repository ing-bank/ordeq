## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_project
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._process_nodes import _collect_views
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_project)
fq_nodes_and_views = _collect_views(*fqn_nodes)
nodes_and_views = [node for _, node in fq_nodes_and_views]
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
View:example_project.nodes_with_view:greet --> io-1
io-1 --> Node:example_project.nodes_with_view:farewell
io-2 --> Node:example_project.nodes_with_inline_io:greet
io-3 --> Node:example_project.nodes_import:func_a
io-3 --> Node:example_project.nodes_import:func_b
io-3 --> Node:example_project.nodes_import_alias:func
io-4 --> Node:example_project.nodes_import:func_a
io-4 --> Node:example_project.nodes_import:func_b
io-4 --> Node:example_project.nodes_import_alias:func
io-5 --> Node:example_project.nodes:func
io-6 --> Node:example_project.inner.nodes:func
Node:example_project.nodes_with_view:farewell --> io-7
Node:example_project.nodes_with_inline_io:greet --> io-8
Node:example_project.nodes_import_alias:func --> io-9
Node:example_project.nodes_import:func_b --> io-10
Node:example_project.nodes_import:func_a --> io-11
Node:example_project.nodes:func --> io-12
Node:example_project.inner.nodes:func --> io-13
NodeGraph
View:example_project.nodes_with_view:greet --> Node:example_project.nodes_with_view:greet
Node:example_project.inner.nodes:func
Node:example_project.nodes:func
Node:example_project.nodes_import:func_a
Node:example_project.nodes_import:func_b
Node:example_project.nodes_import_alias:func
Node:example_project.nodes_with_inline_io:greet
Node:example_project.nodes_with_view:farewell
Topological ordering
(View(module=example_project.nodes_with_view, name=greet, inputs=[Input(id=ID1)]),
 Node(module=example_project.inner.nodes, name=func, inputs=[IO(id=ID2)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(module=example_project.nodes, name=func, inputs=[IO(id=ID3)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(module=example_project.nodes_import, name=func_a, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
 Node(module=example_project.nodes_import, name=func_b, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}),
 Node(module=example_project.nodes_import_alias, name=func, inputs=[Input(id=ID4), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}),
 Node(module=example_project.nodes_with_inline_io, name=greet, inputs=[Input(id=ID5)], outputs=[IO(id=ID6)]),
 Node(module=example_project.nodes_with_view, name=farewell, inputs=[IO(id=ID7)], outputs=[Print()]))

```