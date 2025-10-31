## Resource

```python
from example_catalogs import remote_extended
from ordeq import node, run

catalog = remote_extended


@node(inputs=catalog.hello, outputs=catalog.another_io)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)  # 'catalog.another_io' prints the output to stdout

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/catalog/overriden.py", line LINO, in <module>
    run(func1)  # 'catalog.another_io' prints the output to stdout
    ~~~^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/catalog/overriden.py:1: error: Skipping analyzing "example_catalogs": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq/tests/resources/catalog/overriden.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```