## Resource

```python
from example_catalogs import inconsistent, local
from ordeq._substitute import _substitutes_modules_to_ios

# NOK: 'inconsistent' contains different entries than 'local'
print(_substitutes_modules_to_ios({local: inconsistent}))

```

## Output

```text
CatalogError: Catalog 'example_catalogs.inconsistent' is missing IO 'result' 
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    raise CatalogError(
        f"Catalog '{new.__name__}' is missing IO '{name}' "
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    _substitute_catalog_by_catalog(old, new, requested)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_modules_with_inconsistent_module.py", line LINO, in <module>
    print(_substitutes_modules_to_ios({local: inconsistent}))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```