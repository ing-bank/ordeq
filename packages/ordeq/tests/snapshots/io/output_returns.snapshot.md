## Resource

```python
from dataclasses import dataclass

from ordeq import Output


@dataclass(kw_only=True, frozen=True, eq=False)
class ExampleOutputNosave(Output):
    def save(self, data: str) -> str:
        return "hello"


_ = ExampleOutputNosave()

```

## Output

```text
TypeError: Save method must have return type None.
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in _process_output_meta
    raise TypeError("Save method must have return type None.")

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in __new__
    class_dict, bases = _process_output_meta(name, bases, class_dict)
                        ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/output_returns.py", line LINO, in <module>
    class ExampleOutputNosave(Output):
        def save(self, data: str) -> str:
            return "hello"

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```