## Resource

```python
from example_catalogs import package_base, remote
from ordeq import check_catalogs_are_consistent

# Should raise CatalogError:
check_catalogs_are_consistent(package_base, remote)

```

## Exception

```text
CatalogError: Catalog 'example_catalogs.remote' is missing IO(s) 'creds:secret', 'etl:clients', 'etl:txs', 'ml:metrics', 'ml:model', 'ml:plot', 'ml:predictions'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError(
        f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
    )

  File "/packages/ordeq/tests/resources/catalog/check_inconsistent_package_and_module.py", line LINO, in <module>
    check_catalogs_are_consistent(package_base, remote)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```