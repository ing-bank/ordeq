## Resource

```python
from ordeq import Input


class MockExceptionIO(Input):
    def load(self):
        raise Exception("Some load exception")


mock = MockExceptionIO()
mock.load()

```

## Output

```text
IOException: Failed to load Input(id=ID1).
Some load exception
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in __call__
    return self.func(*args, **kwargs)  # type: ignore[invalid-return-type]
           ~~~~~~~~~^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/load_exception.py", line LINO, in <module>
    mock.load()
    ~~~~~~~~~^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Loading Input(id=ID1)

```