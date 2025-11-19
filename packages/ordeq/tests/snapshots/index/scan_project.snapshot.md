## Resource

```python
from pprint import pprint

import example_project
from ordeq._index import index

nodes, ios = index(example_project)
print("Nodes:")
pprint(nodes)
print("IOs:")
pprint(ios, width=40)

```

## Output

```text
ValueError: Module 'example_project.nodes_import_alias' aliases IO 'example_project.nodes_import:b' to 'B'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_index.py", line LINO, in index
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/index/scan_project.py", line LINO, in <module>
    nodes, ios = index(example_project)
                 ~~~~~^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```