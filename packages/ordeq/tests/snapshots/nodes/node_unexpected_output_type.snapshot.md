## Resource

```python
from ordeq import Input, node

x = Input[str]("X")


@node(inputs=x, outputs=x)  # outputs should be of type Output or IO
def func(data: str) -> str:
    return data + data

```

## Output

```text
ValueError: Outputs of node 'func' in module '__main__' must be of type Output, got Input 
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in _raise_for_invalid_outputs
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in validate
    _raise_for_invalid_outputs(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in __post_init__
    self.validate()
    ~~~~~~~~~~~~~^^

  File "<string>", line LINO, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    return Node(
        func=func,
    ...<6 lines>...
        name=name,
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapped
    node_ = create_node(
        inner,
    ...<5 lines>...
        name=f.__name__,
    )

  File "/packages/ordeq/tests/resources/nodes/node_unexpected_output_type.py", line LINO, in <module>
    @node(inputs=x, outputs=x)  # outputs should be of type Output or IO
     ~~~~^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```