## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import (
    local,
    local_package,
    remote_extended,
    remote_package,
)
from ordeq import node, run
from ordeq_common import Print

catalog = local_package


@node(inputs=local_package.hello, outputs=remote_extended.hello)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=remote_extended.another_io, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(
    uppercase,
    add_world,
    io={local_package: remote_package, remote_extended: local},
)

```

## Output

```text
ValueError: Input to Node(func=__main__:add_world, ...) must be an Input or View, got Print
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

  File "/packages/ordeq/tests/resources/runner/run_io_catalog_package_and_module.py", line LINO, in <module>
    @node(inputs=remote_extended.another_io, outputs=Print())
     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```