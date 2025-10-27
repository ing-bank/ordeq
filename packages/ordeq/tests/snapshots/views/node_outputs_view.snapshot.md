## Resource

```python
from ordeq import node


@node
def hello() -> str:
    return "Hello, World!"


@node(outputs=hello)
def say_hello() -> str:
    return "Hello!"

```

## Exception

```text
ValueError: Outputs of node 'node_outputs_view:say_hello' must be of type Output, got <class 'function'> 
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

  File "/packages/ordeq/tests/resources/views/node_outputs_view.py", line 9, in <module>
    @node(outputs=hello)
     ~~~~^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_outputs_view:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq/tests/resources/views/node_outputs_view.py:9: error: No overload variant of "node" matches argument type "Callable[[], str]"  [call-overload]
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note: Possible overload variants:
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note:     def [FuncParams`-1, FuncReturns] node(func: Callable[FuncParams, FuncReturns], *, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[FuncParams, FuncReturns]
packages/ordeq/tests/resources/views/node_outputs_view.py:9: note:     def node(*, inputs: Sequence[Input[Any] | Callable[..., Any]] | Input[Any] | Callable[..., Any] | None = ..., outputs: Sequence[Output[Any]] | Output[Any] | None = ..., **attributes: Any) -> Callable[[Callable[FuncParams, FuncReturns]], Callable[FuncParams, FuncReturns]]
Found 1 error in 1 file (checked 1 source file)

```