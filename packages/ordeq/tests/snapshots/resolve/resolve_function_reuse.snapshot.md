## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_function_reuse")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(nodes)
pprint(ios)

pprint(_resolve_runnables_to_nodes(*runnables))

```

## Output

```text
['example_function_reuse',
 'example_function_reuse.catalog',
 'example_function_reuse.func_defs',
 'example_function_reuse.nodes']
ValueError: Module 'example_function_reuse.catalog' contains duplicate keys for the same IO ('another_name' and 'A')
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_to_ios
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_runnables_to_nodes_and_ios
    ios.update({module.__name__: _resolve_module_to_ios(module)})
                                 ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/resolve/resolve_function_reuse.py", line LINO, in <module>
    nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```