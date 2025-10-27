## Resource

```python
from dataclasses import dataclass
from pathlib import Path

from ordeq import IO


class ExampleStaticIO(IO[str]):
    @staticmethod
    def load() -> str:
        return "loaded"

    @staticmethod
    def save(data: str) -> None:
        print(data)


# This currently raises an exception because the first argument of `save` needs
# to be `self`.
example_io = ExampleStaticIO()
print(example_io.load())
print(example_io.save("saved"))

```

## Exception

```text
TypeError: Save method requires a data parameter.
  File "/packages/ordeq/src/ordeq/_io.py", line 359, in __new__
    raise TypeError("Save method requires a data parameter.")

  File "/packages/ordeq/src/ordeq/_io.py", line 131, in __new__
    return super().__new__(cls, name, bases, class_dict)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/io_static.py", line 7, in <module>
    class ExampleStaticIO(IO[str]):
    ...<6 lines>...
            print(data)

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```