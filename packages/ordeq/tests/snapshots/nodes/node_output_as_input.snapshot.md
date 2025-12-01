## Resource

```python
from ordeq import Output, node


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


example = Example()

print("Should raise an error ('example' is an output):")


@node(inputs=[example])
def load_node(data: str) -> None:
    print("loading!", data)

```

## Output

```text
Should raise an error ('example' is an output):
ValueError: Input to Node(func=__main__:load_node, ...) must be of type Input or View, got Example
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

  File "/packages/ordeq/tests/resources/nodes/node_output_as_input.py", line LINO, in <module>
    @node(inputs=[example])
     ~~~~^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```