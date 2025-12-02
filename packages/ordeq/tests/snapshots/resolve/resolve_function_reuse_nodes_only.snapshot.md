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
[View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID1)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID2)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID3)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID4)]),
 View(module=example_function_reuse.nodes, name=pi, inputs=[IO(id=ID1)])]
{'example_function_reuse.nodes': {'A': StringBuffer(_buffer=<_io.StringIO object at HASH1>),
                                  'B': StringBuffer(_buffer=<_io.StringIO object at HASH2>)}}
[View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID1)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID2)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID3)]),
 View(func=example_function_reuse.func_defs:print_input, inputs=[IO(id=ID4)]),
 View(module=example_function_reuse.nodes, name=pi, inputs=[IO(id=ID1)])]

```