## Resource

```python
from example_catalogs import local, remote
from ordeq import node, run

env = "test-local"


def get_catalog():
    return local if env == "test-local" else remote


catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.load())

env = "test-acceptance"
catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


run(func2)
print(catalog.result.load())

```

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/catalog/dynamic.py", line LINO, in <module>
    run(func1)
    ~~~^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```