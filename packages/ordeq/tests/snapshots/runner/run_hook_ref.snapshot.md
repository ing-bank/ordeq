## Resource

```python
from ordeq import run

run(
    "packages.example",
    hooks=["packages.example.hooks:MyHook"]
)

```

## Output

```text
Starting the run
Name: John
Name: John
data hello
Finished the run

```

## Logging

```text
INFO	ordeq.io	Loading NameGenerator(name='John')
INFO	ordeq.runner	Running node "hello" in module "packages.example.wrapped_io"
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.runner	Running node "print_message" in module "packages.example.wrapped_io"
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "transform_mock_input" in module "packages.example.pipeline"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading Input(idx=ID1)
INFO	ordeq.runner	Running node "transform_input" in module "packages.example.pipeline"
INFO	ordeq.io	Saving Output(idx=ID2)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "world" in module "packages.example.nodes"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)

```