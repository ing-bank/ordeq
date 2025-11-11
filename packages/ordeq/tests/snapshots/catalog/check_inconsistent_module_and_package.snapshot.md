## Resource

```python
from example_catalogs import package_base, remote
from ordeq import check_catalogs_are_consistent

# Should raise CatalogError:
check_catalogs_are_consistent(remote, package_base)

```

## Exception

```text
CatalogError: Catalog 'example_catalogs.package_base' is missing IO(s) 'hello', 'result'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError(
        f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
    )

  File "/packages/ordeq/tests/resources/catalog/check_inconsistent_module_and_package.py", line LINO, in <module>
    check_catalogs_are_consistent(remote, package_base)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```