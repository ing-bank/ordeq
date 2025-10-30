## Resource

```python
from ordeq import NodeHook, run


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node: {node.name}")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node: {node.name}")


run("examples.example", hooks=["examples.example.hooks:MyHook", MyHook()])

```

## Output

```text
Starting the run
Before running node: examples.example.wrapped_io:hello
Name: John
After running node: examples.example.wrapped_io:hello
Before running node: examples.example.wrapped_io:print_message
Name: John
After running node: examples.example.wrapped_io:print_message
Before running node: examples.example.pipeline:transform_mock_input
After running node: examples.example.pipeline:transform_mock_input
Before running node: examples.example.pipeline:transform_input
data hello
After running node: examples.example.pipeline:transform_input
Before running node: examples.example.nodes:world
After running node: examples.example.nodes:world
Finished the run

```

## Logging

```text
INFO	ordeq.io	Loading NameGenerator(name='John')
INFO	ordeq.runner	Running node "hello" in module "examples.example.wrapped_io"
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.runner	Running node "print_message" in module "examples.example.wrapped_io"
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "transform_mock_input" in module "examples.example.pipeline"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading Input(idx=ID1)
INFO	ordeq.runner	Running node "transform_input" in module "examples.example.pipeline"
INFO	ordeq.io	Saving Output(idx=ID2)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node "world" in module "examples.example.nodes"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)

```