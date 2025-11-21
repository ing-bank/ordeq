## Resource

```python
from ordeq import node
from ordeq._nodes import get_node
from ordeq_common import Print


def string():
    return "I'm super lazy"


@node(inputs=string)
def func(data: str) -> str:
    return str(reversed(data))


@node(inputs=func, outputs=Print())
def hello(data: str) -> None:
    print(data)


print(repr(get_node(hello)))

```

## Output

```text
ValueError: Input '<function string at HASH1>' to node '__main__:func' is not a node
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    raise ValueError(
        f"Input '{input_}' to node '{resolved_name}' is not a node"
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapped
    inner.__ordeq_node__ = create_node(  # type: ignore[attr-defined]
                           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        inner,
        ^^^^^^
    ...<3 lines>...
        attributes=attributes,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "/packages/ordeq/tests/resources/views/view_inputs_regular_func.py", line LINO, in <module>
    @node(inputs=string)
     ~~~~^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```