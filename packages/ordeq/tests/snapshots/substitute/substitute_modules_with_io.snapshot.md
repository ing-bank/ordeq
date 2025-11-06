## Resource

```python
from example_catalogs import local
from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios

# This is NOK: each key and value need to be of the same type
print(_substitutes_modules_to_ios({local: IO()}))

```

## Exception

```text
TypeError: Cannot substitute objects of type 'module' and 'IO'
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    raise TypeError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/substitute/substitute_modules_with_io.py", line LINO, in <module>
    print(_substitutes_modules_to_ios({local: IO()}))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```