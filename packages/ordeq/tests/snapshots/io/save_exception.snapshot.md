## Resource

```python
from ordeq import Output


class MockExceptionIO(Output):
    def save(self, df):
        raise Exception("Some save exception")


mock = MockExceptionIO()
mock.save(None)

```

## Exception

```text
IOException: Failed to save Output(idx=ID1).
Some save exception
```

## Logging

```text
INFO	ordeq.io	Saving Output(idx=ID1)

```