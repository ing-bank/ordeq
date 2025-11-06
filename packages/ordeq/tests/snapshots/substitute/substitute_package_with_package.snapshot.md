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

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute
    return _substitute_catalog_by_catalog(old, new)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    substitution_map.update(_substitute(key, value))
                            ~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_package_with_package.py", line LINO, in <module>
    print(_substitutes_modules_to_ios({package_base: package_inconsistent}))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
{Literal('ohSoSecret!@#'): Literal('ohSoSecret!@#'), IO(idx=ID1): IO(idx=ID2), IO(idx=ID3): StringBuffer(_buffer=<_io.StringIO object at HASH1>), IO(idx=ID4): IO(idx=ID5), JSON(path=Path('predictions-base.json')): JSON(path=Path('predictions-overlay.json')), IO(idx=ID6): IO(idx=ID7), IO(idx=ID8): IO(idx=ID9)}

```