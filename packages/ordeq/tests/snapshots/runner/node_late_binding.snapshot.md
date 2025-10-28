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
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in _raise_for_invalid_inputs
    raise ValueError(
    ...<2 lines>...
    ) from e

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in validate
    _raise_for_invalid_inputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in __post_init__
    self.validate()
    ~~~~~~~~~~~~~^^

  File "<string>", line LINO, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    return View(
        func=func,  # type: ignore[arg-type]
    ...<3 lines>...
        attributes={} if attributes is None else attributes,  # type: ignore[arg-type]
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in node
    wrapper.__ordeq_node__ = create_node(  # type: ignore[attr-defined]
                             ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        wrapper, inputs=inputs, outputs=outputs, attributes=attributes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/runner/node_late_binding.py", line LINO, in <module>
    @node
     ^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_late_binding:func'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```