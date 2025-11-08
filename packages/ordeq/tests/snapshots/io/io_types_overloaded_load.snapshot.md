## Resource

```python
from dataclasses import dataclass
from tempfile import NamedTemporaryFile
from typing import overload
from ordeq import IO
from pathlib import Path


@dataclass(kw_only=True, frozen=True)
class Text(IO[bytes | str, str]):
    path: Path

    @overload
    def load(self, encoding: str | None = None):
        ...

    @overload
    def load(self, encoding: None = None):
        ...

    def load(self) -> str:
        if isinstance(data, str):
            self.path.write_text(data, encoding)
        elif isinstance(data, bytes):
            self.path.write_bytes(data)

    def save(self, data: str | bytes, encoding: str | None = None) -> None:
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
    example.save("some_string", encoding="utf8")
    example.save(b"some_bytes", encoding="utf8")
    print(path.read_text())
    example.save(b"some_bytes", encoding="utf8", x="x")

```

## Exception

```text
IOException: Failed to save Text.
Text.save() got an unexpected keyword argument 'x'
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **kwargs)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    composed(data, *args, **kwargs)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/io_types_overloaded_load.py", line LINO, in <module>
    example.save(b"some_bytes", encoding="utf8", x="x")
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
some_bytes

```

## Logging

```text
INFO	ordeq.io	Saving Text
INFO	ordeq.io	Saving Text
INFO	ordeq.io	Saving Text

```

## Typing

```text
packages/ordeq/tests/resources/io/io_types_overloaded_load.py:20:23: error[invalid-return-type] Function always implicitly returns `None`, which is not assignable to return type `str`
packages/ordeq/tests/resources/io/io_types_overloaded_load.py:21:23: error[unresolved-reference] Name `data` used when not defined
packages/ordeq/tests/resources/io/io_types_overloaded_load.py:22:34: error[unresolved-reference] Name `data` used when not defined
packages/ordeq/tests/resources/io/io_types_overloaded_load.py:22:40: error[unresolved-reference] Name `encoding` used when not defined
packages/ordeq/tests/resources/io/io_types_overloaded_load.py:23:25: error[unresolved-reference] Name `data` used when not defined
packages/ordeq/tests/resources/io/io_types_overloaded_load.py:24:35: error[unresolved-reference] Name `data` used when not defined
packages/ordeq/tests/resources/io/io_types_overloaded_load.py:43:50: error[unknown-argument] Argument `x` does not match any known parameter of bound method `save`
Found 7 diagnostics

```