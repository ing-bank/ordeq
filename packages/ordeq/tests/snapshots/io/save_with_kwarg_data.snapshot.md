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

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
saving! ...

```

## Logging

```text
INFO	ordeq.io	Saving Output(idx=ID1)

```

## Typing

```text
error[missing-argument]: No argument provided for required parameter `df` of bound method `save`
  --> packages/ordeq/tests/resources/io/save_with_kwarg_data.py:13:1
   |
11 | example = Example()
12 | example.save(data)  # ok
13 | example.save(data=data)  # should give an error
   | ^^^^^^^^^^^^^^^^^^^^^^^
   |
info: Parameter declared here
 --> packages/ordeq/tests/resources/io/save_with_kwarg_data.py:5:20
  |
4 | class Example(Output[str]):
5 |     def save(self, df: str) -> None:
  |                    ^^^^^^^
6 |         print("saving!", df)
  |
info: rule `missing-argument` is enabled by default

error[unknown-argument]: Argument `data` does not match any known parameter of bound method `save`
  --> packages/ordeq/tests/resources/io/save_with_kwarg_data.py:13:14
   |
11 | example = Example()
12 | example.save(data)  # ok
13 | example.save(data=data)  # should give an error
   |              ^^^^^^^^^
   |
info: Method signature here
 --> packages/ordeq/tests/resources/io/save_with_kwarg_data.py:5:9
  |
4 | class Example(Output[str]):
5 |     def save(self, df: str) -> None:
  |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
6 |         print("saving!", df)
  |
info: rule `unknown-argument` is enabled by default

Found 2 diagnostics

```