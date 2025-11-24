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
INFO	ordeq.io	Loading NameGenerator(name='John')
DEBUG	ordeq.io	Persisting data for NameGenerator(name='John')
INFO	ordeq.runner	Running node 'hello' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
DEBUG	ordeq.io	Persisting data for SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node 'world' in module 'example_1.nodes'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading Input(id=ID1)
DEBUG	ordeq.io	Persisting data for Input(id=ID1)
INFO	ordeq.runner	Running node 'transform_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving Output(id=ID2)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.runner	Running node 'transform_mock_input' in module 'example_1.pipeline'
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH4>)
DEBUG	ordeq.io	Persisting data for StringBuffer(_buffer=<_io.StringIO object at HASH4>)
DEBUG	ordeq.io	Loading cached data for SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
DEBUG	ordeq.io	Persisting data for SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.runner	Running node 'print_message' in module 'example_1.wrapped_io'
INFO	ordeq.io	Saving NamePrinter()
DEBUG	ordeq.io	Unpersisting data for NameGenerator(name='John')
DEBUG	ordeq.io	Unpersisting data for SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH4>)
DEBUG	ordeq.io	Unpersisting data for Input(id=ID1)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Unpersisting data for StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```