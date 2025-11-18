## Resource

```python
from ordeq import Input


class ExampleStaticIO(Input[str]):
    @staticmethod
    def load() -> None:
        print("Hello!")


_ = ExampleStaticIO()

```

## Output

```text
ValueError: Load method cannot be static.
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in _process_input_meta
    raise ValueError("Load method cannot be static.")

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in __new__
    class_dict, bases = _process_input_meta(name, bases, class_dict)
                        ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/io_static_load.py", line LINO, in <module>
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