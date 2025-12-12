## Resource

```python
from ordeq import Input, node


@node(inputs=[Input[str]("A!"), Input(4)])
def func2(a: str, *, something: int) -> None:
    print(a, something)

```

## Output

```text
ValueError: Keyword-only argument 'something' of view 'func2' in module '__main__' must have a default
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in _raise_if_keyword_only_arg_is_missing_default
    raise ValueError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in validate
    _raise_if_keyword_only_arg_is_missing_default(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in __post_init__
    self.validate()
    ~~~~~~~~~~~~~^^

  File "<string>", line LINO, in __init__

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in create_node
    return View(
        func=func,  # type: ignore[arg-type]
    ...<6 lines>...
        name=name,  # type: ignore[arg-type]
    )

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in wrapped
    node_ = create_node(
        inner,
    ...<5 lines>...
        name=f.__name__,
    )

  File "/packages/ordeq/tests/resources/nodes/node_kw_only_without_defaults_mixed.py", line LINO, in <module>
    @node(inputs=[Input[str]("A!"), Input(4)])
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
DEBUG	ordeq.io	Persisting data for Input(id=ID2)

```