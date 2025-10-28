## Resource

```python
from ordeq import Output


class Example(Output[str]):
    def save(self, df: str) -> None:
        print("saving!", data)


data = "..."

example = Example()
example.save(df=data)  # should give an error

```

## Exception

```text
TypeError: Example.save() missing 1 required positional argument: 'data'
  File "/packages/ordeq/tests/resources/io/save_with_kwarg.py", line LINO, in <module>
    example.save(df=data)  # should give an error
    ~~~~~~~~~~~~^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```