## Resource

```python
# Capture the graph representation and topological ordering
from pprint import pprint

import example_1
from ordeq._graph import NodeGraph, NodeIOGraph
from ordeq._resolve import _resolve_runnables_to_nodes

fqn_nodes = _resolve_runnables_to_nodes(example_1)
nodes = [node for _, node in fqn_nodes]
base_graph = NodeIOGraph.from_nodes(nodes)
print("NodeIOGraph")
print(base_graph)

node_graph = NodeGraph.from_nodes(nodes)
print("NodeGraph")
print(node_graph)

print("Topological ordering")
pprint([node.name for node in node_graph.topological_ordering])

```

## Output

```text
NodeIOGraph
io-0 --> Node:example_1.wrapped_io:hello
Node:example_1.wrapped_io:hello --> io-1
io-1 --> Node:example_1.wrapped_io:print_message
io-2 --> Node:example_1.pipeline:transform_mock_input
io-3 --> Node:example_1.pipeline:transform_input
io-4 --> Node:example_1.nodes:world
Node:example_1.wrapped_io:print_message --> io-5
Node:example_1.pipeline:transform_mock_input --> io-6
Node:example_1.pipeline:transform_input --> io-7
Node:example_1.nodes:world --> io-8
NodeGraph
Node:example_1.wrapped_io:hello --> Node:example_1.wrapped_io:print_message
Node:example_1.nodes:world
Node:example_1.pipeline:transform_input
Node:example_1.pipeline:transform_mock_input
Node:example_1.wrapped_io:print_message
Topological ordering
['example_1.wrapped_io:hello',
 'example_1.nodes:world',
 'example_1.pipeline:transform_input',
 'example_1.pipeline:transform_mock_input',
 'example_1.wrapped_io:print_message']

```