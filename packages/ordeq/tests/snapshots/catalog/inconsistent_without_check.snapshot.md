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