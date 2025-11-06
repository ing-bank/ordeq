## Resource

```python
from ordeq._substitute import _substitutes_modules_to_ios

# Should return an empty dict:
print(_substitutes_modules_to_ios(None))

```

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    for old, new in io.items():
                    ^^^^^^^^

  File "/packages/ordeq/tests/resources/substitute/substitute_none.py", line LINO, in <module>
    print(_substitutes_modules_to_ios(None))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```