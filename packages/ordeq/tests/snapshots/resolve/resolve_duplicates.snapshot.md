## Resource

```python
import importlib
from pprint import pprint

from ordeq._resolve import (
    _resolve_refs_to_modules,
    _resolve_runnables_to_nodes,
    _resolve_runnables_to_nodes_and_ios,
)

runnables = [importlib.import_module("example_duplicates")]

modules = [mod.__name__ for mod in _resolve_refs_to_modules(*runnables)]
pprint(modules)

nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
pprint(sorted(node.name for node in nodes))
pprint(dict(sorted(ios.items())))

pprint(sorted(node.name for node in _resolve_runnables_to_nodes(*runnables)))

```

## Exception

```text
ValueError: Module 'example_duplicates.duplicate_import_alias' contains duplicate keys for the same IO ('b' and 'a')
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_module_to_ios
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_runnables_to_nodes_and_ios
    ios.update({module.__name__: _resolve_module_to_ios(module)})
                                 ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

  File "/packages/ordeq/tests/resources/resolve/resolve_duplicates.py", line LINO, in <module>
    nodes, ios = _resolve_runnables_to_nodes_and_ios(*runnables)
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Output

```text
['example_duplicates',
 'example_duplicates.duplicate_import_alias',
 'example_duplicates.duplicate_import_reassign',
 'example_duplicates.duplicate_io_names',
 'example_duplicates.duplicate_io_objects',
 'example_duplicates.duplicate_node_names',
 'example_duplicates.duplicate_node_objects',
 'example_duplicates.file1',
 'example_duplicates.file2']

```