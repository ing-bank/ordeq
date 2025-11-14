## Resource

```python
from dataclasses import dataclass

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputNosave(Output):
    def save(self) -> None:
        pass


_ = ExampleOutputNosave()

```

## Exception

```text
TypeError: Save method requires a data parameter.
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in __new__
    raise TypeError("Save method requires a data parameter.")

  File "/packages/ordeq/tests/resources/io/output_save_without_argument.py", line LINO, in <module>
    class ExampleOutputNosave(Output):
        def save(self) -> None:
            pass

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```