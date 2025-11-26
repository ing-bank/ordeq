## Resource

```python
from ordeq import run

run("example_1", hooks=["example_1.hooks:MyHook"])

```

## Output

```text
Starting the run
Name: John
data hello
Name: John
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
INFO	ordeq.io	Loading StringBuffer 'x' in module 'example_1.nodes'
DEBUG	ordeq.io	Persisting data for StringBuffer 'x' in module 'example_1.nodes'
INFO	ordeq.runner	Running node 'world' in module 'example_1.nodes'
INFO	ordeq.io	Saving StringBuffer 'y' in module 'example_1.nodes'
DEBUG	ordeq.io	Persisting data for StringBuffer 'y' in module 'example_1.nodes'
INFO	ordeq.io	Loading Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running node 'transform_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving Output(id=ID2)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node 'transform_mock_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Loading cached data for SayHello 'message' in module 'example_1.wrapped_io'
INFO	ordeq.runner	Running node 'print_message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving NamePrinter 'name_printer' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for NameGenerator 'name_generator' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for SayHello 'message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Unpersisting data for Input(id=ID1)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x' in module 'example_1.nodes'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'y' in module 'example_1.nodes'

```