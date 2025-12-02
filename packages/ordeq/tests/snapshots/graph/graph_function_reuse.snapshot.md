## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_function_reuse
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

nodes = _resolve_runnables_to_nodes(example_function_reuse)
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint(node_graph.topological_ordering)

```

## Output

```text
NodeIOGraph
io-0 --> View:View(func=example_function_reuse.func_defs:print_input, ...)
io-0 --> View:example_function_reuse.nodes:pi
io-1 --> View:View(func=example_function_reuse.func_defs:print_input, ...)
io-2 --> View:View(func=example_function_reuse.func_defs:print_input, ...)
io-3 --> View:View(func=example_function_reuse.func_defs:print_input, ...)
View:example_function_reuse.nodes:pi --> io-4
View:View(func=example_function_reuse.func_defs:print_input, ...) --> io-5
View:View(func=example_function_reuse.func_defs:print_input, ...) --> io-6
View:View(func=example_function_reuse.func_defs:print_input, ...) --> io-7
View:View(func=example_function_reuse.func_defs:print_input, ...) --> io-8
NodeGraph
View:View(func=example_function_reuse.func_defs:print_input, ...)
View:View(func=example_function_reuse.func_defs:print_input, ...)
View:View(func=example_function_reuse.func_defs:print_input, ...)
View:View(func=example_function_reuse.func_defs:print_input, ...)
View:example_function_reuse.nodes:pi
Topological ordering
(View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID1)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID2)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID3)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID4)]),
 View(module=example_function_reuse.nodes, name=pi, inputs=[IO(id=ID1)]))

```