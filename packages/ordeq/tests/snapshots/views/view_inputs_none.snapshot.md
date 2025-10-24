## Resource

```python
from ordeq import node
from ordeq._nodes import get_node


@node(None)
def my_view() -> None:
    print("Hello, world!")


print(repr(get_node(my_view)))

```

## Output

```text
View(name=view_inputs_none:my_view)

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_inputs_none:my_view'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq/tests/resources/views/view_inputs_none.py:5: error: No overload variant of "node" matches argument type "None"  [call-overload]
packages/ordeq/tests/resources/views/view_inputs_none.py:5: note: Possible overload variants:
packages/ordeq/tests/resources/views/view_inputs_none.py:5: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/view_inputs_none.py:5: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
Found 1 error in 1 file (checked 1 source file)

```