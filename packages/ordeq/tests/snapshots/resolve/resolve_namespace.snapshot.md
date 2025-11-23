## Resource

```python
from pprint import pprint

import example_namespace.namespace
from ordeq._resolve import _resolve_module_globals

pprint(_resolve_module_globals(example_namespace.namespace))

```

## Output

```text
{'B': IO(id=ID1),
 'a': IO(id=ID1),
 'ios': [IO(id=ID1), IO(id=ID1)],
 'node_with_inline_io': Node(func=example_namespace.namespace:node_with_inline_io, inputs=[IO(id=ID2)], outputs=[IO(id=ID3)]),
 'node_with_list_input': Node(func=example_namespace.namespace:node_with_list_input, inputs=[IO(id=ID1), IO(id=ID1)], outputs=[IO(id=ID4)]),
 'node_with_node_input': Node(func=example_namespace.namespace:node_with_node_input, inputs=[IO(id=ID5)], outputs=[IO(id=ID6)]),
 'x': View(func=example_namespace.other:hello),
 'y': View(func=example_namespace.other:hello)}

```