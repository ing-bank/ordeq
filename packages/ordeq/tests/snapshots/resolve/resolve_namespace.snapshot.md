## Resource

```python
from pprint import pprint

import example_namespace.namespace
from ordeq._resolve import _resolve_module_globals

pprint(_resolve_module_globals(example_namespace.namespace))

```

## Output

```text
{'B': IO(idx=ID1),
 'a': IO(idx=ID1),
 'ios': [IO(idx=ID1),
         IO(idx=ID1)],
 'node_with_inline_io': <function node_with_inline_io at HASH1>,
 'node_with_list_input': <function node_with_list_input at HASH2>,
 'node_with_node_input': <function node_with_node_input at HASH3>,
 'x': <function hello at HASH4>,
 'y': <function hello at HASH5>}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_namespace.other:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_namespace.other:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example_namespace.other:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```