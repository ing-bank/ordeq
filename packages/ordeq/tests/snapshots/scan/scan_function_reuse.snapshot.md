## Resource

```python
from pprint import pprint

import example_function_reuse
from ordeq._scan import scan

nodes, ios = scan(example_function_reuse)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios)

```

## Output

```text
Nodes:
[(('example_function_reuse.nodes', 'a'),
  View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (('example_function_reuse.nodes', 'b'),
  View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])),
 (('example_function_reuse.nodes', 'c'),
  View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])),
 (('example_function_reuse.nodes', 'd'),
  View(name=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])),
 (('example_function_reuse.nodes', 'pi'),
  View(name=example_function_reuse.nodes:pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]))]
IOs:
[[(('example_function_reuse.catalog', 'A'),
   StringBuffer(_buffer=<_io.StringIO object at HASH1>)),
  (('example_function_reuse.nodes', 'A'),
   StringBuffer(_buffer=<_io.StringIO object at HASH1>))],
 [(('example_function_reuse.catalog', 'B'),
   StringBuffer(_buffer=<_io.StringIO object at HASH2>)),
  (('example_function_reuse.nodes', 'B'),
   StringBuffer(_buffer=<_io.StringIO object at HASH2>))],
 [(('example_function_reuse.catalog', 'C'),
   StringBuffer(_buffer=<_io.StringIO object at HASH3>))],
 [(('example_function_reuse.catalog', 'D'),
   StringBuffer(_buffer=<_io.StringIO object at HASH4>))]]

```