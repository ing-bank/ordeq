## Resource

```python
# Captures loading and saving an IO with different load and save type.
# The save method has been overloaded to facilitate writing both bytes and
# text. This resource also captures the interaction of overloaded save
# methods with save options.
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import overload

from ordeq import IO


@dataclass(kw_only=True, frozen=True)
class Text(IO[str, bytes | str]):
    path: Path

    def load(self) -> str:
        return str(self)

    @overload
    def save(self, data: str, encoding: str | None = None): ...

    @overload
    def save(self, data: bytes, encoding: None = None): ...

    def save(self, data: str | bytes, encoding: str | None = None) -> None:
        print("Saving with encoding", encoding)
        if isinstance(data, str):
            self.path.write_text(data, encoding)
        elif isinstance(data, bytes):
            self.path.write_bytes(data)

    def __repr__(self):
        # To clean the output
        return "Text"


with NamedTemporaryFile() as tmp:
    path = Path(tmp.name)
    example = Text(path=path)
    example = example.with_save_options(encoding="utf8")
    example.save("some_bytes")
    example.save("some_bytes", encoding="koi8_t")

```

## Output

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

  File "/packages/ordeq/tests/resources/io/io_types_overloaded_save_options.py", line LINO, in <module>
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
packages/ordeq/tests/resources/io/io_types_overloaded_save_options.py:14:12: error[too-many-positional-arguments] Too many positional arguments to class `IO`: expected 1, got 2
Found 1 diagnostic

```