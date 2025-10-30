## Resource

```python
# Checks the behaviour when running nodes with an alternative catalog
# We want to support this syntax and behaviour since it allows users to
# easily switch between different catalogs, for instance during tests.
from ordeq import node, run
from ordeq_common import Print

from resources.catalog.catalogs import local, remote

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
AttributeError: module 'resources.catalog.catalogs.remote' has no attribute 'get'
  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in <genexpr>
    inputs=tuple(io.get(ip, ip) for ip in self.inputs),  # type: ignore[misc,arg-type]
                 ^^^^^^

  File "/packages/ordeq/src/ordeq/_nodes.py", line LINO, in _patch_io
    inputs=tuple(io.get(ip, ip) for ip in self.inputs),  # type: ignore[misc,arg-type]
           ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in _run_graph
    patched_nodes[node] = node._patch_io(io_ or {})  # noqa: SLF001 (private access)
                          ~~~~~~~~~~~~~~^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=io)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/tests/resources/catalog/run_with_module_catalog.py", line LINO, in <module>
    run(uppercase, add_world, io=remote)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/catalog/run_with_module_catalog.py:22: error: Argument "io" to "run" has incompatible type Module; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
Found 1 error in 1 file (checked 1 source file)

```