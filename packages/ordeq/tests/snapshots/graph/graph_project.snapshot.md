## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_project
from ordeq._graph import NamedNodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_project)
node_io_graph = NodeIOGraph.from_nodes(*nodes)
named_node_graph = NamedNodeGraph.from_graph(node_io_graph)
print("NamedNodeGraph:")
print(named_node_graph)

print("Topological ordering:")
pprint(named_node_graph.topological_ordering)

```

## Output

```text
NamedNodeGraph:
View:example_project.nodes_with_view:greet --> Node:example_project.nodes_with_view:farewell
Topological ordering:
(View(name=example_project.nodes_with_view:greet, inputs=[Literal('Hello')]),
 Node(name=example_project.nodes_import_reassign:func_b, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
 Node(name=example_project.inner.nodes:func, inputs=[IO(idx=ID1)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(name=example_project.nodes_import:func_a, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
 Node(name=example_project.nodes_import_reassign:func_a, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()]),
 Node(name=example_project.nodes_import:func_b, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}),
 Node(name=example_project.nodes_import_alias:func, inputs=[Literal('a'), StringBuffer(_buffer=<_io.StringIO object at HASH1>)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}),
 Node(name=example_project.nodes:func, inputs=[IO(idx=ID2)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(name=example_project.nodes_with_inline_io:greet, inputs=[Literal('Buenos dias')], outputs=[IO(idx=ID3)]),
 Node(name=example_project.nodes_with_view:farewell, inputs=[IO(idx=ID4)], outputs=[Print()]))

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_project.nodes_with_view:greet'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```