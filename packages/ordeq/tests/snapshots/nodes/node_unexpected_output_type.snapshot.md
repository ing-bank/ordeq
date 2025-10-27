## Resource

```python
from ordeq import node
from ordeq_common import StringBuffer, Literal

x = Literal("X")


@node(inputs=x, outputs=x)  # outputs should be of type Output or IO
def func(data: str) -> str:
    return data + data

```

## Exception

```text
ValueError: Outputs of node 'node_unexpected_output_type:func' must be of type Output, got <class 'ordeq_common.io.literal.Literal'> 
  File "/packages/ordeq/src/ordeq/_nodes.py", line 139, in _raise_for_invalid_outputs
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line 53, in validate
    _raise_for_invalid_outputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line 47, in __post_init__
    self.validate()
    ~~~~~~~~~~~~~^^

  File "<string>", line 8, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line 285, in create_node
    return Node(
        func=func,
    ...<3 lines>...
        attributes={} if attributes is None else attributes,
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line 442, in wrapped
    inner.__ordeq_node__ = create_node(  # type: ignore[attr-defined]
                           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        inner, inputs=inputs, outputs=outputs, attributes=attributes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py", line 7, in <module>
    @node(inputs=x, outputs=x)  # outputs should be of type Output or IO
     ~~~~^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: error: No overload variant of "node" matches argument types "Literal[str]", "Literal[str]"  [call-overload]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note: Possible overload variants:
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py:7: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
Found 1 error in 1 file (checked 1 source file)

```