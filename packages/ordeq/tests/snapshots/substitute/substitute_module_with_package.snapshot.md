## Resource

```python
from example_catalogs import local, remote_package
from ordeq._substitute import _substitutes_modules_to_ios

# This is OK: though 'local' is a file-module and 'remote_package' is a
# package, they both define the same entries and are both of ModuleType.
print(_substitutes_modules_to_ios({local: remote_package}))

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

  File "/packages/ordeq/tests/resources/substitute/substitute_module_with_package.py", line LINO, in <module>
    print(_build_substitution_map({local: remote_package}))
          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```
