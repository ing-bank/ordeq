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
  File "/packages/ordeq/src/ordeq/_io.py", line 477, in save_wrapper
    raise IOException(msg) from exc

  File "/packages/ordeq/src/ordeq/_io.py", line 325, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 450, in save_wrapper
    save_func(data, *args, **kwargs)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line 325, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 426, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line 325, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 426, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line 325, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 426, in save_wrapper
    save_func(data, *args, **save_options)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_io.py", line 325, in <lambda>
    lambda prev_func, wrap: lambda d, *a, **k: wrap(
                                               ~~~~^
        self, prev_func, d, *a, **k
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ),
    ^

  File "/packages/ordeq/src/ordeq/_io.py", line 331, in wrapper
    composed(data, *args, **kwargs)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/io/save_exception.py", line 10, in <module>
    mock.save(None)
    ~~~~~~~~~^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Saving Output(idx=ID1)

```