## Resource

```python
from example_catalogs import local, local_package, package_base
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: 'local_package' contains the exact same entries as 'local'
print(_substitutes_modules_to_ios({local: local_package}))

# This is NOK, 'package_base' contains different entries than 'local':
print(_substitutes_modules_to_ios({local: package_base}))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>)}
CatalogError: Catalog 'example_catalogs.package_base' is missing IO 'hello' 
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    raise CatalogError(
        f"Catalog '{new.__name__}' is missing IO '{name}' "
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    _substitute_catalog_by_catalog(old, new, requested)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_package_with_module.py", line LINO, in <module>
    print(_substitutes_modules_to_ios({local: package_base}))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```