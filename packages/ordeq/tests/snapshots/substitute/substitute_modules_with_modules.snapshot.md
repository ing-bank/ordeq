## Resource

```python
from example_catalogs import local, package_base, package_overlay, remote
from ordeq._substitute import _substitutes_modules_to_ios

print(_substitutes_modules_to_ios({local: remote, package_base: package_overlay}))

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

  File "/packages/ordeq/tests/resources/substitute/substitute_modules_with_modules.py", line LINO, in <module>
    print(_build_substitution_map({local: remote, package_base: package_overlay}))
          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```
