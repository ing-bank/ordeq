## Resource

```python
from ordeq import node
from ordeq._nodes import get_node
from ordeq_common import Print


def string():
    return "I'm super lazy"


@node(inputs=string)
def func(data: str) -> str:
    return str(data.__reversed__())


@node(inputs=func, outputs=Print())
def hello(data: str) -> None:
    print(data)


print(repr(get_node(hello)))

```

## Exception

```text
ValueError: Input '<function string at HASH1>' to node 'view_inputs_regular_func:func' is not a view
  File "/packages/ordeq/src/ordeq/_nodes.py", line 259, in create_node
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

  File "/packages/ordeq/tests/resources/views/view_inputs_regular_func.py", line 10, in <module>
    @node(inputs=string)
     ~~~~^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```