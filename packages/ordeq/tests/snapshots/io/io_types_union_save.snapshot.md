## Resource

```python
# Captures loading and saving an IO with different load and save type.
# The save type is a union of two data types.
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile

from ordeq import IO


@dataclass(kw_only=True, frozen=True)
class Text(IO[str, bytes | str]):
    path: Path

    def load(self) -> str:
        return str(self)

    def save(self, data: str | bytes) -> None:
        if isinstance(data, str):
            self.path.write_text(data)
        elif isinstance(data, bytes):
            self.path.write_bytes(data)

    def __repr__(self):
        # To clean the output
        return "Text"


with NamedTemporaryFile() as tmp:
    path = Path(tmp.name)
    example_input = Text(path=path)
    print(example_input.load())
    example_input.save("some_string")
    print(path.read_text(encoding="utf8"))
    example_input.save(b"some_bytes")
    print(path.read_text(encoding="utf8"))

```

## Exception

```text
TypeError: Too many arguments for <class 'ordeq._io.IO'>; actual 2, expected 1
  File "/typing.py", line LINO, in _check_generic_specialization
    raise TypeError(f"Too {'many' if actual_len > expected_len else 'few'} arguments"
                    f" for {cls}; actual {actual_len}, expected {expect_val}")

  File "/typing.py", line LINO, in _generic_class_getitem
    _check_generic_specialization(cls, args)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^

  File "/typing.py", line LINO, in inner
    return func(*args, **kwds)

  File "/packages/ordeq/tests/resources/io/io_types_union_save.py", line LINO, in <module>
    class Text(IO[str, bytes | str]):
               ~~^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/io/io_types_union_save.py:11:12: error[too-many-positional-arguments] Too many positional arguments to class `IO`: expected 1, got 2
Found 1 diagnostic

```