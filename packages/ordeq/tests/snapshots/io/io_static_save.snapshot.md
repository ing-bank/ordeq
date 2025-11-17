## Resource

```python
from ordeq import Output


class ExampleStaticIO(Output[str]):
    @staticmethod
    def save(data: str) -> None:
        print(data)


_ = ExampleStaticIO()

```

## Exception

```text
ValueError: Save method cannot be static.
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in _process_output_meta
    raise ValueError("Save method cannot be static.")

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in __new__
    class_dict, bases = _process_output_meta(name, bases, class_dict)
                        ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/io_static_save.py", line LINO, in <module>
    class ExampleStaticIO(Output[str]):
    ...<2 lines>...
            print(data)

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```