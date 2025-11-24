## Resource

```python
from ordeq import NodeHook, run


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node {node}")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node {node}")


run("example_1", hooks=["example_1.hooks:MyHook", MyHook()])

```

## Output

```text
Starting the run
Before running node 'hello' in module 'example_1.wrapped_io'
Name: John
After running node 'hello' in module 'example_1.wrapped_io'
Before running node 'world' in module 'example_1.nodes'
After running node 'world' in module 'example_1.nodes'
Before running node 'transform_input' in module 'example_1.pipeline'
data hello
After running node 'transform_input' in module 'example_1.pipeline'
Before running node 'transform_mock_input' in module 'example_1.pipeline'
After running node 'transform_mock_input' in module 'example_1.pipeline'
Before running node 'print_message' in module 'example_1.wrapped_io'
Name: John
After running node 'print_message' in module 'example_1.wrapped_io'
Finished the run

```

## Logging

```text
INFO	ordeq.io	Loading 'name_generator' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Persisting data for 'name_generator' in module 'example_1.wrapped_io'
INFO	ordeq.runner	Running node 'hello' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving 'message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving 'name_printer' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Persisting data for 'message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Loading 'x' in module 'example_1.nodes'
DEBUG	ordeq.io	Persisting data for 'x' in module 'example_1.nodes'
INFO	ordeq.runner	Running node 'world' in module 'example_1.nodes'
INFO	ordeq.io	Saving 'y' in module 'example_1.nodes'
DEBUG	ordeq.io	Persisting data for 'y' in module 'example_1.nodes'
INFO	ordeq.io	Loading Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running node 'transform_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving Output(id=ID2)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node 'transform_mock_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Loading cached data for 'message' in module 'example_1.wrapped_io'
INFO	ordeq.runner	Running node 'print_message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving 'name_printer' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for 'name_generator' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for 'message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Unpersisting data for Input(id=ID1)
DEBUG	ordeq.io	Unpersisting data for 'x' in module 'example_1.nodes'
DEBUG	ordeq.io	Unpersisting data for 'y' in module 'example_1.nodes'

```