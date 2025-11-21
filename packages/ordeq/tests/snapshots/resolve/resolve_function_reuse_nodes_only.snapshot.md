## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_function_reuse.nodes")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_function_reuse.nodes']
[(('example_function_reuse.nodes', 'a'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (('example_function_reuse.nodes', 'b'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])),
 (('example_function_reuse.nodes', 'c'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])),
 (('example_function_reuse.nodes', 'd'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])),
 (('example_function_reuse.nodes', 'pi'),
  View(func=example_function_reuse.nodes:pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]))]
{'example_function_reuse.nodes': {'A': StringBuffer(_buffer=<_io.StringIO object at HASH1>),
                                  'B': StringBuffer(_buffer=<_io.StringIO object at HASH2>)}}
[(('example_function_reuse.nodes', 'a'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)])),
 (('example_function_reuse.nodes', 'b'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)])),
 (('example_function_reuse.nodes', 'c'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])),
 (('example_function_reuse.nodes', 'd'),
  View(func=example_function_reuse.func_defs:print_input, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH4>)])),
 (('example_function_reuse.nodes', 'pi'),
  View(func=example_function_reuse.nodes:pi, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH1>)]))]

```