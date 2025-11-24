## Resource

```python
from ordeq import NodeHook, run


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node '{node}'")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node '{node}'")


run("example_1", hooks=["example_1.hooks:MyHook", MyHook()])

```

## Output

```text
Starting the run
Before running node 'example_1.wrapped_io:hello'
Name: John
After running node 'example_1.wrapped_io:hello'
Before running node 'example_1.nodes:world'
After running node 'example_1.nodes:world'
Before running node 'example_1.pipeline:transform_input'
data hello
After running node 'example_1.pipeline:transform_input'
Before running node 'example_1.pipeline:transform_mock_input'
After running node 'example_1.pipeline:transform_mock_input'
Before running node 'example_1.wrapped_io:print_message'
Name: John
After running node 'example_1.wrapped_io:print_message'
Finished the run

```

## Logging

```text
INFO	ordeq.io	Loading NameGenerator(name='John')
INFO	ordeq.runner	Running node 'example_1.wrapped_io:hello'
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node 'example_1.nodes:world'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading Input(id=ID1)
INFO	ordeq.runner	Running node 'example_1.pipeline:transform_input'
INFO	ordeq.io	Saving Output(id=ID2)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node 'example_1.pipeline:transform_mock_input'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.runner	Running node 'example_1.wrapped_io:print_message'
INFO	ordeq.io	Saving NamePrinter()

```