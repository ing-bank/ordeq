## Resource

```python
from ordeq import Input


class ExampleStaticIO(Input[str]):
    @staticmethod
    def load() -> None:
        print("Hello!")


_ = ExampleStaticIO()

```

## Exception

```text
ValueError: Load method cannot be static.
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in __new__
    raise ValueError(
        "Load method cannot be static."
    )

  File "/packages/ordeq/tests/resources/io/io_static_save.py", line LINO, in <module>
    class ExampleStaticIO(Input[str]):
    ...<2 lines>...
            print("Hello!")

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```