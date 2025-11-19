## Resource

```python
from pprint import pprint

import example_project
from ordeq._scan import scan

nodes, ios = scan(example_project)
print("Nodes:")
pprint(list(nodes.items()))
print("IOs:")
pprint(list(ios.values()))

```

## Output

```text
ValueError: Module 'example_project.nodes_import_alias' aliases IO 'example_project.catalog_1:b' to 'B'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in scan
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/tests/resources/scan/scan_project.py", line LINO, in <module>
    nodes, ios = scan(example_project)
                 ~~~~^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```