## Resource

```python
from example_catalogs import package_base, package_inconsistent
from ordeq._substitute import _substitutes_modules_to_ios

# NOK: 'package_inconsistent' contains different entries than 'package_base'
print(_substitutes_modules_to_ios({package_base: package_inconsistent}))

```

## Exception

```text
CatalogError: Catalog 'example_catalogs.package_inconsistent' is missing IO(s) 'creds:secret', 'ml:metrics', 'ml:model', 'ml:plot', 'ml:predictions'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError(
        f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    check_catalogs_are_consistent(old, new)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    substitution_map.update(_substitute_catalog_by_catalog(old, new))
                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_package_with_inconsistent_package.py", line LINO, in <module>
    print(_substitutes_modules_to_ios({package_base: package_inconsistent}))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```