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
 'node_with_inline_io': Node(module=example_namespace.namespace, name=node_with_inline_io, inputs=[IO(id=ID2)], outputs=[IO(id=ID3)]),
 'node_with_list_input': Node(module=example_namespace.namespace, name=node_with_list_input, inputs=[IO(id=ID4), IO(id=ID4)], outputs=[IO(id=ID5)]),
 'node_with_node_input': Node(module=example_namespace.namespace, name=node_with_node_input, inputs=[IO(id=ID6)], outputs=[IO(id=ID7)]),
 'x': View(func=example_namespace.other:hello),
 'y': View(func=example_namespace.other:hello)}

```