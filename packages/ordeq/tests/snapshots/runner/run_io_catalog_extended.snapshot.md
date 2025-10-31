## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from example_catalogs import remote, remote_extended
from ordeq import node, run
from ordeq_common import Print

catalog = remote


@node(inputs=catalog.hello, outputs=catalog.result)
def uppercase(hello: str) -> str:
    return f"{hello.upper()}!"


@node(inputs=catalog.result, outputs=Print())
def add_world(hello: str) -> str:
    return f"{hello}, world!!"


run(uppercase, add_world, io={catalog: remote_extended})

```

## Exception

```text
CatalogError: IO 'hello' was not found in catalog 'example_catalogs.remote_extended'. Cannot patch.
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in _patch_catalog_by_catalog
    raise CatalogError(
    ...<2 lines>...
    )

  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in _patch
    return _patch_catalog_by_catalog(patched, patched_by)

  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in _patch_io
    patched_io.update(_patch(key, value))
                      ~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    patched_io = _patch_io(io)

  File "/packages/ordeq/tests/resources/runner/run_io_catalog_extended.py", line LINO, in <module>
    run(uppercase, add_world, io={catalog: remote_extended})
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```