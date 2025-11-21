## Resource

```python
from typing import Any

from ordeq import IO, node, run
from ordeq_viz import viz
from pandas import DataFrame

txs = IO[Any]()
txs_agg = IO[Any]()


@node(checks=txs_agg)
def perform_check(txs_agg: DataFrame) -> None:
    assert txs_agg.count() > 1000


@node(inputs=txs, outputs=txs_agg)
def agg_txs(txs: DataFrame) -> DataFrame:
    return txs.groupBy(...).agg(...)


if __name__ == "__main__":
    print(viz(__name__, fmt="mermaid"))
    run(__name__)

```

## Output

```text
ValueError: Node inputs invalid for function arguments: Node(name=__main__:perform_check,...)
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
    ...<5 lines>...
        views=tuple(views),  # type: ignore[arg-type]
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

  File "/packages/ordeq/tests/resources/checks/check_after_save.py", line LINO, in <module>
    @node(checks=txs_agg)
     ~~~~^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
WARNING	ordeq.preview	Checks are in preview mode and may change without notice in future releases.

```

## Typing

```text
packages/ordeq/tests/resources/checks/check_after_save.py:18:12: error[call-non-callable] Object of type `Series[Any]` is not callable
Found 1 diagnostic

```