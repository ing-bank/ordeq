## Resource

```python
from ordeq._substitute import _build_substitution_map
from ordeq import IO
from example_catalogs import local_package

# This is NOK: each key and value need to be of the same type
print(_build_substitution_map({local_package: IO()}))

```

## Exception

```text
TypeError: Cannot substitute objects of type 'module' and 'IO'
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitute
    raise TypeError(
    ...<3 lines>...
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitution_map
    substitution_map.update(_build_substitute(key, value))
                            ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_package_with_io.py", line LINO, in <module>
    print(_build_substitution_map({local_package: IO()}))
          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```