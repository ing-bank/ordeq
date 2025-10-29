## Resource

```python
import os

from ordeq import node, run

from resources.catalog.catalogs import local, remote

os.environ["CATALOG_ENV"] = "test-local"


def get_catalog():
    return local if os.environ["CATALOG_ENV"] == "test-local" else remote


catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


run(func1)
print(catalog.result.output())

os.environ["CATALOG_ENV"] = "test-acceptance"
catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


run(func2)
print(catalog.result.output())

```

## Exception

```text
AttributeError: 'StringBuffer' object has no attribute 'output'
  File "/packages/ordeq/tests/resources/catalog/dynamic.py", line LINO, in <module>
    print(catalog.result.output())
          ^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "func1" in module "dynamic"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```