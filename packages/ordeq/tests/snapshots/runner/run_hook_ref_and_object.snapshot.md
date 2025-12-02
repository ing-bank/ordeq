## Resource

```python
from ordeq import NodeHook, run


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running {node}")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running {node}")


run("example_1", hooks=["example_1.hooks:MyHook", MyHook()])

```

## Output

```text
Starting the run
Before running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
After running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
Before running Input(id=ID1)
After running Input(id=ID1)
Before running StringBuffer(_buffer=<_io.StringIO object at HASH2>)
After running StringBuffer(_buffer=<_io.StringIO object at HASH2>)
Before running NameGenerator(name='John')
After running NameGenerator(name='John')
Before running SayHello 'message' in module 'example_1.wrapped_io'
After running SayHello 'message' in module 'example_1.wrapped_io'
Before running node 'world' in module 'example_1.nodes'
After running node 'world' in module 'example_1.nodes'
Before running node 'transform_input' in module 'example_1.pipeline'
data hello
After running node 'transform_input' in module 'example_1.pipeline'
Before running node 'transform_mock_input' in module 'example_1.pipeline'
After running node 'transform_mock_input' in module 'example_1.pipeline'
Before running node 'hello' in module 'example_1.wrapped_io'
Name: John
After running node 'hello' in module 'example_1.wrapped_io'
Before running node 'print_message' in module 'example_1.wrapped_io'
Name: Hello, John!
After running node 'print_message' in module 'example_1.wrapped_io'
Finished the run

```

## Logging

```text
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'world:a' in module 'example_1.nodes'
DEBUG	ordeq.runner	Running Input(id=ID1)
INFO	ordeq.io	Loading Input(id=ID1)
DEBUG	ordeq.io	Persisting data for IO 'transform_input:input_data' in module 'example_1.pipeline'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for IO 'transform_mock_input:input_data' in module 'example_1.pipeline'
DEBUG	ordeq.runner	Running NameGenerator(name='John')
INFO	ordeq.io	Loading NameGenerator(name='John')
DEBUG	ordeq.io	Persisting data for IO 'hello:name' in module 'example_1.wrapped_io'
DEBUG	ordeq.runner	Running SayHello 'message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Loading SayHello 'message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Loading NameGenerator(name='John')
DEBUG	ordeq.io	Persisting data for IO 'print_message:message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Loading cached data for IO 'world:a' in module 'example_1.nodes'
DEBUG	ordeq.runner	Running node 'world' in module 'example_1.nodes'
INFO	ordeq.io	Saving StringBuffer 'y' in module 'example_1.nodes'
DEBUG	ordeq.io	Persisting data for StringBuffer 'y' in module 'example_1.nodes'
DEBUG	ordeq.io	Loading cached data for IO 'transform_input:input_data' in module 'example_1.pipeline'
DEBUG	ordeq.runner	Running node 'transform_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving MockOutput 'TestOutput' in module 'example_1.catalog'
DEBUG	ordeq.io	Loading cached data for IO 'transform_mock_input:input_data' in module 'example_1.pipeline'
DEBUG	ordeq.runner	Running node 'transform_mock_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Loading cached data for IO 'hello:name' in module 'example_1.wrapped_io'
DEBUG	ordeq.runner	Running node 'hello' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving SayHello 'message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving NamePrinter 'name_printer' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Persisting data for SayHello 'message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Loading cached data for IO 'print_message:message' in module 'example_1.wrapped_io'
DEBUG	ordeq.runner	Running node 'print_message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving NamePrinter 'name_printer' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for IO 'print_message:message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for IO 'hello:name' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for IO 'transform_mock_input:input_data' in module 'example_1.pipeline'
DEBUG	ordeq.io	Unpersisting data for IO 'transform_input:input_data' in module 'example_1.pipeline'
DEBUG	ordeq.io	Unpersisting data for IO 'world:a' in module 'example_1.nodes'
DEBUG	ordeq.io	Unpersisting data for SayHello 'message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'y' in module 'example_1.nodes'

```