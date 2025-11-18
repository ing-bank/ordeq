## Resource

```python
from example_catalogs import inconsistent as catalog
from ordeq import node


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"

```

## Output

```text
AttributeError: module 'example_catalogs.inconsistent' has no attribute 'result'
  File "/packages/ordeq/tests/resources/catalog/inconsistent_without_check.py", line LINO, in <module>
    @node(inputs=catalog.hello, outputs=catalog.result)
                                        ^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```