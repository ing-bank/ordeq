## Resource

```python
from ordeq import Input


class MockExceptionIO(Input):
    def load(self):
        raise Exception("Some load exception")


mock = MockExceptionIO()
mock.load()

```

## Exception

```text
IOException: Failed to load Input(idx=ID1).
Some load exception
```

## Logging

```text
INFO	ordeq.io	Loading Input(idx=ID1)

```