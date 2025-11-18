## Resource

```python
from ordeq import Output


class MockExceptionIO(Output):
    def save(self, df):
        raise Exception("Some save exception")


mock = MockExceptionIO()
mock.save(None)

```

## Output

```text
IOException: Failed to save Output(id=ID1).
Some save exception
  File "/packages/ordeq/src/ordeq/_io.py", line LINO, in wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/tests/resources/io/save_exception.py", line LINO, in <module>
    mock.save(None)
    ~~~~~~~~~^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Saving Output(id=ID1)

```