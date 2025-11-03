## Resource

```python
from ordeq._substitute import _build_substitution_map

from example_catalogs import local, remote, remote_extended, inconsistent

print(_build_substitution_map({local: remote, package_base: package_overlay}))

```

## Exception

```text
NameError: name 'package_base' is not defined
  File "/packages/ordeq/tests/resources/substitute/substitute_modules_with_modules.py", line LINO, in <module>
    print(_build_substitution_map({local: remote, package_base: package_overlay}))
                                                  ^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```