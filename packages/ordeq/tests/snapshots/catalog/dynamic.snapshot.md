## Resource

```python
import os

from ordeq import node, run

from resources.catalog.catalogs import local, remote

os.environ["ENV"] = "local"


def get_catalog():
    return local if os.environ["ENV"] == "local" else remote


catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func1(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func1))

os.environ["ENV"] = "acceptance"
catalog = get_catalog()


@node(inputs=catalog.hello, outputs=catalog.result)
def func2(hello: str) -> str:
    return f"{hello.upper()}!"


print(run(func2))

```

## Output

```text
{StringBuffer(_buffer=<_io.StringIO object at HASH1>): 'HELLO FROM LOCAL!'}
{StringBuffer(_buffer=<_io.StringIO object at HASH2>): 'HELLO FROM REMOTE!'}

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "func1" in module "dynamic"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node "func2" in module "dynamic"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```