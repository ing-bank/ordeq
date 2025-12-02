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
View:example_project.nodes_with_view:greet --> io-1
io-1 --> Node:example_project.nodes_with_view:farewell
io-2 --> Node:example_project.nodes_with_inline_io:greet
io-3 --> Node:example_project.nodes_import_alias:func
io-3 --> Node:example_project.nodes_import:func_b
io-3 --> Node:example_project.nodes_import:func_a
io-4 --> Node:example_project.nodes_import_alias:func
io-4 --> Node:example_project.nodes_import:func_b
io-4 --> Node:example_project.nodes_import:func_a
io-5 --> Node:example_project.nodes:func
io-6 --> Node:example_project.inner.nodes:func
Node:example_project.nodes_with_view:farewell --> io-7
Node:example_project.nodes_with_inline_io:greet --> io-8
Node:example_project.nodes_import:func_a --> io-9
Node:example_project.nodes_import:func_b --> io-10
Node:example_project.nodes_import_alias:func --> io-11
Node:example_project.nodes:func --> io-12
Node:example_project.inner.nodes:func --> io-13
NodeGraph
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> View:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> Node:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> Node:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> Node:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> Node:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> Node:Loader(func=ordeq._io:_raise_not_implemented, ...)
Loader:Loader(func=ordeq_common.io.string_buffer:load, ...) --> Node:Loader(func=ordeq_common.io.string_buffer:load, ...)
Loader:Loader(func=ordeq_common.io.string_buffer:load, ...) --> Node:Loader(func=ordeq_common.io.string_buffer:load, ...)
Loader:Loader(func=ordeq_common.io.string_buffer:load, ...) --> Node:Loader(func=ordeq_common.io.string_buffer:load, ...)
Loader:Loader(func=ordeq._io:_raise_not_implemented, ...) --> Node:Loader(func=ordeq._io:_raise_not_implemented, ...)
View:example_project.nodes_with_view:greet --> Node:example_project.nodes_with_view:greet
Node:example_project.inner.nodes:func
Node:example_project.nodes:func
Node:example_project.nodes_import_alias:func
Node:example_project.nodes_import:func_b
Node:example_project.nodes_import:func_a
Node:example_project.nodes_with_inline_io:greet
Node:example_project.nodes_with_view:farewell
Topological ordering
(Loader(func=<bound method _raise_not_implemented of Input(id=ID1)>,
        inputs=(),
        outputs=(IO(id=ID2),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=Input(id=ID1)),
 Loader(func=<bound method _raise_not_implemented of IO(id=ID3)>,
        inputs=(),
        outputs=(IO(id=ID4),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=IO(id=ID3)),
 Loader(func=<bound method _raise_not_implemented of IO(id=ID5)>,
        inputs=(),
        outputs=(IO(id=ID6),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=IO(id=ID5)),
 Loader(func=<bound method _raise_not_implemented of Input(id=ID7)>,
        inputs=(),
        outputs=(IO(id=ID8),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=Input(id=ID7)),
 Loader(func=<bound method StringBuffer.load of StringBuffer(_buffer=<_io.StringIO object at HASH1>)>,
        inputs=(),
        outputs=(IO(id=ID9),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
 Loader(func=<bound method _raise_not_implemented of Input(id=ID10)>,
        inputs=(),
        outputs=(IO(id=ID11),),
        checks=(),
        attributes={},
        views=(),
        module=None,
        name=None,
        io=Input(id=ID10)),
 View(module=example_project.nodes_with_view, name=greet, inputs=[IO(id=ID2)]),
 Node(module=example_project.inner.nodes, name=func, inputs=[IO(id=ID4)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(module=example_project.nodes, name=func, inputs=[IO(id=ID6)], outputs=[Print()], attributes={'tags': ['dummy']}),
 Node(module=example_project.nodes_import_alias, name=func, inputs=[IO(id=ID8), IO(id=ID9)], outputs=[Print()], attributes={'tags': {'key': 'threshold', 'value': 0.23}}),
 Node(module=example_project.nodes_import, name=func_b, inputs=[IO(id=ID8), IO(id=ID9)], outputs=[Print()], attributes={'tags': {'viz': 'orange'}}),
 Node(module=example_project.nodes_import, name=func_a, inputs=[IO(id=ID8), IO(id=ID9)], outputs=[Print()]),
 Node(module=example_project.nodes_with_inline_io, name=greet, inputs=[IO(id=ID11)], outputs=[IO(id=ID12)]),
 Node(module=example_project.nodes_with_view, name=farewell, inputs=[IO(id=ID13)], outputs=[Print()]))

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID7)
DEBUG	ordeq.io	Persisting data for Input(id=ID14)
DEBUG	ordeq.io	Persisting data for Input(id=ID10)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```