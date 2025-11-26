## Resource

```python
from typing import Any

from ordeq import IO, Input, InputHook


class ExampleHook(InputHook):
    def __init__(self, value):
        self.value = value

    def before_input_load(self, _io: Input[Any]) -> None:
        pass

    def __repr__(self):
        return f"ExampleHook(value={self.value})"


io = IO[Any]()
print(io.input_hooks)
io = io.with_input_hooks(ExampleHook(1))
print(io.input_hooks)
io = io.with_input_hooks(ExampleHook(2))
print(io.input_hooks)

```

## Output

```text
()
(ExampleHook(value=1),)
(ExampleHook(value=2),)

```