## Resource

```python
from ordeq import run

run("example_1", "example_1.pipeline")

```

## Output

```text
Name: John
data hello
Name: John

```

## Warnings

```text
UserWarning: Module 'example_1.pipeline' was provided more than once. Duplicates will be ignored.
UserWarning: Node 'transform_input' in module 'example_1.pipeline' was provided more than once. Duplicates are ignored.
UserWarning: Node 'transform_mock_input' in module 'example_1.pipeline' was provided more than once. Duplicates are ignored.
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
INFO	ordeq.io	Loading MockInput 'TestInput' in module 'example_1.catalog'
DEBUG	ordeq.io	Persisting data for MockInput 'TestInput' in module 'example_1.catalog'
INFO	ordeq.runner	Running node 'transform_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving MockOutput 'TestOutput' in module 'example_1.catalog'
INFO	ordeq.io	Loading StringBuffer 'Hello' in module 'example_1.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'Hello' in module 'example_1.catalog'
INFO	ordeq.runner	Running node 'transform_mock_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Loading cached data for SayHello 'message' in module 'example_1.wrapped_io'
INFO	ordeq.runner	Running node 'print_message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving NamePrinter 'name_printer' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for NameGenerator 'name_generator' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for SayHello 'message' in module 'example_1.wrapped_io'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'Hello' in module 'example_1.catalog'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'World' in module 'example_1.catalog'
DEBUG	ordeq.io	Unpersisting data for MockInput 'TestInput' in module 'example_1.catalog'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'x' in module 'example_1.nodes'
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'y' in module 'example_1.nodes'

```