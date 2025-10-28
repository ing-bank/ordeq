## Resource

```python
from ordeq import node
from ordeq._catalog import check_catalogs_are_consistent

from resources.catalog.catalogs import inconsistent, local

check_catalogs_are_consistent(local, inconsistent)
catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"

```

## Exception

```text
CatalogError: Catalogs are inconsistent.
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError("Catalogs are inconsistent.")

  File "/packages/ordeq/tests/resources/catalog/inconsistent_with_check.py", line LINO, in <module>
    check_catalogs_are_consistent(local, inconsistent)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/catalog/inconsistent_with_check.py:10: error: Module has no attribute "result"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```