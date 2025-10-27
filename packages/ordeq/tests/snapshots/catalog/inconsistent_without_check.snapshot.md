## Resource

```python
from ordeq import node

from resources.catalog.catalogs import inconsistent

catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"

```

## Exception

```text
AttributeError: module 'resources.catalog.catalogs.inconsistent' has no attribute 'result'
  File "/packages/ordeq/tests/resources/catalog/inconsistent_without_check.py", line 8, in <module>
    @node(inputs=catalog.hello, outputs=catalog.result)
                                        ^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 85, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Typing

```text
packages/ordeq/tests/resources/catalog/inconsistent_without_check.py:8: error: Module has no attribute "result"  [attr-defined]
Found 1 error in 1 file (checked 1 source file)

```