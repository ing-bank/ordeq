## Resource

```python
from example_catalogs import (
    package_base,
    package_inconsistent,
    package_overlay,
)
from ordeq import check_catalogs_are_consistent

# Should raise CatalogError:
check_catalogs_are_consistent(
    package_base, package_overlay, package_inconsistent
)

```

## Exception

```text
CatalogError: Catalog 'example_catalogs.package_inconsistent' is missing IO(s) 'creds:secret', 'ml:metrics', 'ml:model', 'ml:plot', 'ml:predictions'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError(
        f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
    )

  File "/packages/ordeq/tests/resources/catalog/check_inconsistent_packages.py", line LINO, in <module>
    check_catalogs_are_consistent(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        package_base, package_overlay, package_inconsistent
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```