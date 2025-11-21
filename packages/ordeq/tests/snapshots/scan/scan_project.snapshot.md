## Resource

```python
from pprint import pprint

import example_project
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import scan

nodes, ios = scan(*_resolve_packages_to_modules(example_project))
print("Nodes:")
pprint(nodes, width=200)
print("IOs:")
pprint(list(ios.values()), width=200)

```

## Output

```text
ValueError: Module 'example_project.nodes_import_alias' aliases IO 'example_project.nodes_import:b' to 'B'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in scan
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/scan/scan_project.py", line LINO, in <module>
    nodes, ios = scan(*_resolve_packages_to_modules(example_project))
                 ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```