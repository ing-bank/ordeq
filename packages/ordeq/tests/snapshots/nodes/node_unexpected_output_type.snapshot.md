## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer, Literal

x = Literal("X")


@node(inputs=x, outputs=x)  # outputs should be of type Output or IO
def func(data: str) -> str:
    return data + data

```

## Typing

```text
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: error: No overload variant of "node" matches argument types "Literal[str]", "Literal[str]"  [call-overload]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any]] | Input[Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def node(*, inputs: Sequence[Input[Any]] | Input[Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
Found 1 error in 1 file (checked 1 source file)

```