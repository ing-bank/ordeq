## Resource

```python
from ordeq import Output


class Example(Output[str]):
    def save(self, df: str) -> None:
        print("saving!", df)


data = "..."

example = Example()
example.save(data)  # ok
example.save(data=data)  # should give an error

```

## Exception

```text
TypeError: Example.save() missing 1 required positional argument: 'data'
  File "/packages/ordeq/tests/resources/io/save_with_kwarg_data.py", line LINO, in <module>
    example.save(data=data)  # should give an error
    ~~~~~~~~~~~~^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Output

```text
saving! ...

```

## Logging

```text
INFO	ordeq.io	Saving Output(id=ID1)

```

## Typing

```text
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:13:1: error[missing-argument] No argument provided for required parameter `df` of bound method `save`
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:13:14: error[unknown-argument] Argument `data` does not match any known parameter of bound method `save`
Found 2 diagnostics

```