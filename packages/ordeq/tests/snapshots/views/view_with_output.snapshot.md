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

## Output

```text
ValueError: Input 'hello' in module '__main__' to node Node(func=__main__:say_hello, ...) is not a view
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapped
    node_ = create_node(
        inner,
    ...<5 lines>...
        name=f.__name__,
    )

  File "/packages/ordeq/tests/resources/views/view_with_output.py", line LINO, in <module>
    @node(inputs=hello)
     ~~~~^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```