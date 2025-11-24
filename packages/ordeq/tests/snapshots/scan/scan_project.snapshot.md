## Resource

```python
from pprint import pprint

import example_project
from ordeq._resolve import _resolve_packages_to_modules
from ordeq._scan import _scan_fqns

nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_project))
print("Nodes:")
pprint(sorted(nodes, key=lambda n: (nodes[n], n.ref)), width=40)
print("IOs:")
pprint(list(ios.values()), width=40)

```

## Output

```text
ValueError: Module 'example_project.nodes_import_alias' aliases IO 'example_project.catalog_1:b' to 'B'. IOs cannot be aliased.
  File "/packages/ordeq/src/ordeq/_scan.py", line LINO, in _scan_fqns
    raise ValueError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/scan/scan_project.py", line LINO, in <module>
    nodes, ios = _scan_fqns(*_resolve_packages_to_modules(example_project))
                 ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Warnings

```text
UserWarning: Module 'example_project.catalog_1' already provided as runnable
UserWarning: Module 'example_project.catalog_2' already provided as runnable
UserWarning: Module 'example_project.inner' already provided as runnable
UserWarning: Module 'example_project.inner.nodes' already provided as runnable
UserWarning: Module 'example_project.misc' already provided as runnable
UserWarning: Module 'example_project.nodes' already provided as runnable
UserWarning: Module 'example_project.nodes_import' already provided as runnable
UserWarning: Module 'example_project.nodes_import_alias' already provided as runnable
UserWarning: Module 'example_project.nodes_with_inline_io' already provided as runnable
UserWarning: Module 'example_project.nodes_with_view' already provided as runnable
```