## Resource

```python
from example_catalogs import inconsistent as catalog
from ordeq import node


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"

```

## Exception

```text
AttributeError: module 'example_catalogs.inconsistent' has no attribute 'result'
  File "/packages/ordeq/tests/resources/catalog/inconsistent_without_check.py", line LINO, in <module>
    @node(inputs=catalog.hello, outputs=catalog.result)
                                        ^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/catalog/inconsistent_without_check.py:1: error: Skipping analyzing "example_catalogs": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq/tests/resources/catalog/inconsistent_without_check.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 1 source file)

```