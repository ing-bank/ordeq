## Resource

```python
import example_1
import example_1.nodes
import example_1.wrapped_io
from ordeq import run

run(example_1, example_1, example_1, example_1.wrapped_io, example_1.nodes)

```

## Output

```text
Name: John
data hello
Name: John

```

## Warnings

```text
UserWarning: Node 'example_1.nodes:world' already provided in another runnable
UserWarning: Node 'example_1.pipeline:transform_input' already provided in another runnable
UserWarning: Node 'example_1.pipeline:transform_mock_input' already provided in another runnable
UserWarning: Node 'example_1.wrapped_io:hello' already provided in another runnable
UserWarning: Node 'example_1.wrapped_io:print_message' already provided in another runnable
```

## Logging

```text
INFO	ordeq.io	Loading NameGenerator(name='John')
INFO	ordeq.runner	Running node "hello" in module "example_1.wrapped_io"
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "world" in module "example_1.nodes"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading Input(id=ID1)
INFO	ordeq.runner	Running node "transform_input" in module "example_1.pipeline"
INFO	ordeq.io	Saving Output(id=ID2)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "transform_mock_input" in module "example_1.pipeline"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node "print_message" in module "example_1.wrapped_io"
INFO	ordeq.io	Saving NamePrinter()

```