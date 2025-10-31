## Resource

```python
import example_catalogs.remote_overridden as catalog
from ordeq import node, run


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.load())

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/catalog/extended.py", line LINO, in <module>
    run(func1)
    ~~~^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/catalog/extended.py:1: error: Skipping analyzing "example_catalogs.remote_overridden": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq/tests/resources/catalog/extended.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
packages/ordeq/tests/resources/catalog/extended.py:1: error: Skipping analyzing "example_catalogs": module is installed, but missing library stubs or py.typed marker  [import-untyped]
Found 2 errors in 1 file (checked 1 source file)

```