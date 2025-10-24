## Resource

```python
from ordeq import node


def hello() -> str:
    return "Hello, World!"


@node(outputs=hello)
def say_hello() -> str:
    return "Hello!"

```

## Exception

```text
ValueError: Outputs of node 'node_outputs_regular_func:say_hello' must be of type Output, got <class 'function'> 
```

## Typing

```text
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: error: No overload variant of "node" matches argument type "Callable[[], str]"  [call-overload]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note: Possible overload variants:
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/node_outputs_regular_func.py:8: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
Found 1 error in 1 file (checked 1 source file)

```