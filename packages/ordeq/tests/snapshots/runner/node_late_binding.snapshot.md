## Resource

```python
from ordeq import node


@node
def func(x: str) -> str:
    return x

```

## Exception

```text
ValueError: Node inputs invalid for function arguments: Node(name=node_late_binding:func,...)
  File "/packages/ordeq/src/ordeq/_nodes.py", line 118, in _raise_for_invalid_inputs
    raise ValueError(
    ...<2 lines>...
    ) from e

  File "/packages/ordeq/src/ordeq/_nodes.py", line 52, in validate
    _raise_for_invalid_inputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line 297, in __post_init__
    self.validate()
    ~~~~~~~~~~~~~^^

  File "<string>", line 8, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line 278, in create_node
    return View(
        func=func,  # type: ignore[arg-type]
    ...<3 lines>...
        attributes={} if attributes is None else attributes,  # type: ignore[arg-type]
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line 456, in node
    wrapper.__ordeq_node__ = create_node(  # type: ignore[attr-defined]
                             ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        wrapper, inputs=inputs, outputs=outputs, attributes=attributes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/runner/node_late_binding.py", line 4, in <module>
    @node
     ^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_late_binding:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```