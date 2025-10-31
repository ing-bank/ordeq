## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import local, remote
from ordeq import node, run
from ordeq_common import Print

catalog = local


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello.upper()}, world!!"


run(uppercase, add_world, io=remote)

```

## Exception

```text
AttributeError: module 'example_catalogs.remote' has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in _patch_io
    for key, value in io.items():
                      ^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    patched_io = _patch_io(io)

  File "/packages/ordeq/tests/resources/catalog/run_with_module_catalog.py", line LINO, in <module>
    run(uppercase, add_world, io=remote)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```