## Resource

```python
from ordeq import node
from ordeq_common import Print


@node(outputs=Print())
def hello() -> str:
    return "Hello, World!"


@node(inputs=hello)
def say_hello(value: str) -> str:
    return value

```

## Exception

```text
ValueError: Input '<function hello at HASH1>' to node 'view_with_output:say_hello' is not a view
  File "/packages/ordeq/src/ordeq/_nodes.py", line 264, in create_node
    raise ValueError(
        f"Input '{input_}' to node '{resolved_name}' is not a view"
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line 442, in wrapped
    inner.__ordeq_node__ = create_node(  # type: ignore[attr-defined]
                           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        inner, inputs=inputs, outputs=outputs, attributes=attributes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/views/view_with_output.py", line 10, in <module>
    @node(inputs=hello)
     ~~~~^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```