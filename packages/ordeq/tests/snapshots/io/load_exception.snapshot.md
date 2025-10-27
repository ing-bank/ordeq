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
  File "/packages/ordeq/src/ordeq/_io.py", line 241, in load_wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 224, in load_wrapper
    return load_func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 194, in load_wrapper
    result = load_func(*args, **kwargs)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 170, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 170, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 170, in load_wrapper
    return load_func(*args, **load_options)

  File "/packages/ordeq/src/ordeq/_io.py", line 73, in <lambda>
    lambda prev_func, wrap: lambda *a, **k: wrap(
                                            ~~~~^
        self, prev_func, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 79, in wrapper
    return composed(*args, **kwargs)

  File "/packages/ordeq/tests/resources/io/load_exception.py", line 10, in <module>
    mock.load()
    ~~~~~~~~~^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Loading Input(idx=ID1)

```