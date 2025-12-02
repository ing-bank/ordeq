## Resource

```python
from ordeq import run

run("example_1", "example_1.pipeline")

```

## Output

```text
data hello
Name: John
Name: Hello, John!

```

## Warnings

```text
UserWarning: Module 'example_1.pipeline' was provided more than once. Duplicates will be ignored.
UserWarning: Node 'transform_input' in module 'example_1.pipeline' was provided more than once. Duplicates are ignored.
UserWarning: Node 'transform_mock_input' in module 'example_1.pipeline' was provided more than once. Duplicates are ignored.
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