## Resource

```python
from ordeq import Output


class Example(Output[str]):
    def save(self, df: str) -> None:
        print("saving!", data)


data = "..."

example = Example()
example.save(data)  # ok
example.save(data=data)  # should give an error

```

## Exception

```text
TypeError: Example.save() missing 1 required positional argument: 'data'
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
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:5: note: "save" of "Example" defined here
packages/ordeq/tests/resources/io/save_with_kwarg_data.py:13: error: Unexpected keyword argument "data" for "save" of "Example"  [call-arg]
Found 1 error in 1 file (checked 1 source file)

```