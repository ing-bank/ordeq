## Resource

```python
from example_catalogs import inconsistent, local
from ordeq import node
from ordeq._catalog import check_catalogs_are_consistent

check_catalogs_are_consistent(local, inconsistent)
catalog = inconsistent


@node(inputs=catalog.hello, outputs=catalog.result)
def func(hello: str) -> str:
    return f"{hello.upper()}!"

```

## Output

```text
CatalogError: Catalog 'example_catalogs.inconsistent' is missing IO(s) 'result'
  File "/packages/ordeq/src/ordeq/_catalog.py", line LINO, in check_catalogs_are_consistent
    raise CatalogError(
        f"Catalog '{module.__name__}' is missing IO(s) {missing_ios}"
    )

  File "/packages/ordeq/tests/resources/catalog/inconsistent_with_check.py", line LINO, in <module>
    check_catalogs_are_consistent(local, inconsistent)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```