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
Before running node 'hello' in module 'example_1.wrapped_io'
Name: John
After running node 'hello' in module 'example_1.wrapped_io'
Before running node 'print_message' in module 'example_1.wrapped_io'
Name: John
After running node 'print_message' in module 'example_1.wrapped_io'
Before running node 'transform_mock_input' in module 'example_1.pipeline'
After running node 'transform_mock_input' in module 'example_1.pipeline'
Before running node 'transform_input' in module 'example_1.pipeline'
data hello
After running node 'transform_input' in module 'example_1.pipeline'
Before running node 'world' in module 'example_1.nodes'
After running node 'world' in module 'example_1.nodes'
Finished the run

```

## Logging

```text
INFO	ordeq.io	Loading NameGenerator 'name_generator' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Persisting data for NameGenerator 'name_generator' in module 'example_1.wrapped_io'
INFO	ordeq.runner	Running node 'hello' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving SayHello 'message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving NamePrinter 'name_printer' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Persisting data for SayHello 'message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Loading cached data for SayHello 'message' in module 'example_1.wrapped_io'
INFO	ordeq.runner	Running node 'print_message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving NamePrinter 'name_printer' in module 'example_1.wrapped_io'
INFO	ordeq.io	Loading StringBuffer 'Hello' in module 'example_1.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'Hello' in module 'example_1.catalog'
INFO	ordeq.runner	Running node 'transform_mock_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'World' in module 'example_1.catalog'
INFO	ordeq.io	Loading MockInput 'TestInput' in module 'example_1.catalog'
DEBUG	ordeq.io	Persisting data for MockInput 'TestInput' in module 'example_1.catalog'
INFO	ordeq.runner	Running node 'transform_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving MockOutput 'TestOutput' in module 'example_1.catalog'
INFO	ordeq.io	Loading StringBuffer 'x' in module 'example_1.nodes'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x' in module 'example_1.nodes'
INFO	ordeq.runner	Running node 'world' in module 'example_1.nodes'
INFO	ordeq.io	Saving StringBuffer 'y' in module 'example_1.nodes'
DEBUG	ordeq.io	Persisting data for StringBuffer 'y' in module 'example_1.nodes'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x' in module 'example_1.nodes'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'y' in module 'example_1.nodes'
DEBUG	ordeq.io	Unpersisting data for MockInput 'TestInput' in module 'example_1.catalog'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'Hello' in module 'example_1.catalog'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Unpersisting data for NameGenerator 'name_generator' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for SayHello 'message' in module 'example_1.wrapped_io'

```