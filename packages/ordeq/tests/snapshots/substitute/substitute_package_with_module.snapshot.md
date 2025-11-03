## Resource

```python
from ordeq._substitute import _build_substitution_map

from example_catalogs import local, local_package, package_base

# This is OK: 'local_package' contains the exact same entries as 'local'
print(_build_substitution_map({local: local_package}))

# This is NOK, 'package_base' contains different entries than 'local':
print(_build_substitution_map({local: package_base}))

```

## Exception

```text
CatalogError: Catalog 'example_catalogs.package_base' is missing IO(s) 'hello', 'result'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError(
        f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    check_catalogs_are_consistent(old, new)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitute
    return _substitute_catalog_by_catalog(old, new)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitution_map
    substitution_map.update(_build_substitute(key, value))
                            ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_package_with_module.py", line LINO, in <module>
    print(_build_substitution_map({local: package_base}))
          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): StringBuffer(_buffer=<_io.StringIO object at HASH2>), StringBuffer(_buffer=<_io.StringIO object at HASH3>): StringBuffer(_buffer=<_io.StringIO object at HASH4>)}

```