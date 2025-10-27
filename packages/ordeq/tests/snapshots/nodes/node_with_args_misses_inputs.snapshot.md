## Resource

```python
from ordeq import node, run
from ordeq_common import StringBuffer


@node(outputs=[StringBuffer("a")])
def func(a: str) -> str:
    return a


run(func)

```

## Exception

```text
ValueError: Node inputs invalid for function arguments: Node(name=node_with_args_misses_inputs:func,...)
  File "/packages/ordeq/src/ordeq/_nodes.py", line 118, in _raise_for_invalid_inputs
    raise ValueError(
    ...<2 lines>...
    ) from e

  File "/packages/ordeq/src/ordeq/_nodes.py", line 52, in validate
    _raise_for_invalid_inputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

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

  File "/packages/ordeq/tests/resources/nodes/node_with_args_misses_inputs.py", line 5, in <module>
    @node(outputs=[StringBuffer("a")])
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```