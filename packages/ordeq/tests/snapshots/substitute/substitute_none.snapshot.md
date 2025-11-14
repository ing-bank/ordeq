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

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```