## Resource

```python
from example_catalogs import local
from ordeq import IO
from ordeq._substitute import _substitutes_modules_to_ios

# This is NOK: cannot substitute IO with module
print(_substitutes_modules_to_ios({IO(): local}))

```

## Output

```text
TypeError: Cannot substitute objects of type 'IO' and 'module'
  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitutes_modules_to_ios
    raise TypeError(
    ...<3 lines>...
    )

  File "/packages/ordeq/tests/resources/substitute/substitute_io_with_module.py", line LINO, in <module>
    print(_substitutes_modules_to_ios({IO(): local}))
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```