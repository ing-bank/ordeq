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
TypeError: unhashable type: 'dict'
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    io[old_io] = new_io
    ~~^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitute
    return _substitute_catalog_by_catalog(old, new)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitution_map
    substitution_map.update(_build_substitute(key, value))
                            ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_package_with_package.py", line LINO, in <module>
    print(_build_substitution_map({package_base: package_overlay}))
          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```
