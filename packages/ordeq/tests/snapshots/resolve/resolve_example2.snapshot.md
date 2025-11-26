## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_2")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_2', 'example_2.catalog', 'example_2.nodes']
[Node(module=example_2.nodes, name=transform_input_2, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)])]
{'example_2.catalog': {'TestInput2': Input(id=ID1),
                       'TestOutput2': Output(id=ID2)},
 'example_2.nodes': {'TestInput2': Input(id=ID1),
                     'TestOutput2': Output(id=ID2)}}
[Node(module=example_2.nodes, name=transform_input_2, inputs=[Input(id=ID1)], outputs=[Output(id=ID2)])]

```