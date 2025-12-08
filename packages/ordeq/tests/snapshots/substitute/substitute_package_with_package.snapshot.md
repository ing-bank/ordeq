## Resource

```python
from example_catalogs import (
    package_base,
    package_inconsistent,
    package_overlay,
)
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: 'package_overlay' contains all entries of 'package_base'
print(_substitutes_modules_to_ios({package_base: package_overlay}))

# This is NOK: 'package_base' is not a subset of 'package_inconsistent'
print(_substitutes_modules_to_ios({package_base: package_inconsistent}))

```

## Output

```text
{Input(id=ID1): Input(id=ID2), IO(id=ID3): IO(id=ID4), IO(id=ID5): StringBuffer(_buffer=<_io.StringIO object at HASH1>), IO(id=ID6): IO(id=ID7), JSON(path=Path('predictions-base.json')): JSON(path=Path('predictions-overlay.json')), IO(id=ID8): IO(id=ID9), IO(id=ID10): IO(id=ID11)}
CatalogError: Catalog 'example_catalogs.package_inconsistent' is missing IO 'secret' 
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    raise CatalogError(
        f"Catalog '{new.__name__}' is missing IO '{name}' "
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    _substitute_catalog_by_catalog(old, new, requested)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_package_with_package.py", line LINO, in <module>
    print(_substitutes_modules_to_ios({package_base: package_inconsistent}))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```