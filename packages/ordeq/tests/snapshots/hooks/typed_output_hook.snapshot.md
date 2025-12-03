## Resource

```python
from ordeq import Output, OutputHook


class MyTypedOutputHook(OutputHook[str]):
    def before_output_save(self, op: Output[str], data: str) -> None:
        print(f"saving data `{data}` to output `{op}`")


_ = MyTypedOutputHook()

```

## Typing

```text
packages/ordeq/tests/resources/hooks/typed_output_hook.py:5:9: error[invalid-method-override] Invalid override of method `before_output_save`: Definition is incompatible with `OutputHook.before_output_save`
Found 1 diagnostic

```