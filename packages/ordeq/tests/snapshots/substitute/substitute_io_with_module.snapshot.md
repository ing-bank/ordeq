## Resource

```python
from example_catalogs import local
from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios

print(_substitutes_modules_to_ios({IO(): local}))

```

## Exception

```text
TypeError: Cannot substitute objects of type 'IO' and 'module'
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitute
    raise TypeError(
    ...<3 lines>...
    )

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitution_map
    substitution_map.update(_build_substitute(key, value))
                            ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_io_with_module.py", line LINO, in <module>
    print(_build_substitution_map({IO(): local}))
          ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```
