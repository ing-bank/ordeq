## Resource

```python
from ordeq import Node, Output, OutputHook


class MyTypedOutputHook(OutputHook[str]):
    def before_output_save(
        self, op: Output[str], data: str
    ) -> None:
        print(f"saving data `{data}` to output `{op}`")

_ = MyTypedOutputHook()

```