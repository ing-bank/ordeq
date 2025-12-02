## Resource

```python
import example_function_reuse
from ordeq import run

run(example_function_reuse, verbose=True)

```

## Output

```text
io-0 --> View:example_function_reuse.nodes:pi
io-0 --> View:example_function_reuse.nodes:a
io-1 --> View:example_function_reuse.nodes:d
io-2 --> View:example_function_reuse.nodes:c
io-3 --> View:example_function_reuse.nodes:b
View:example_function_reuse.nodes:a --> io-4
View:example_function_reuse.nodes:pi --> io-5
View:example_function_reuse.nodes:d --> io-6
View:example_function_reuse.nodes:c --> io-7
View:example_function_reuse.nodes:b --> io-8
B
C
D
A
A

```

## Logging

```text
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH1>)
DEBUG	ordeq.io	Persisting data for IO 'b:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH2>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH2>)
DEBUG	ordeq.io	Persisting data for IO 'c:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH3>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH3>)
DEBUG	ordeq.io	Persisting data for IO 'd:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.runner	Running StringBuffer(_buffer=<_io.StringIO object at HASH4>)
INFO	ordeq.io	Loading StringBuffer(_buffer=<_io.StringIO object at HASH4>)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Loading cached data for IO 'b:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.runner	Running view 'b' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Loading cached data for IO 'c:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.runner	Running view 'c' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
DEBUG	ordeq.io	Loading cached data for IO 'd:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.runner	Running view 'd' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
DEBUG	ordeq.runner	Running view 'pi' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
DEBUG	ordeq.io	Loading cached data for IO(id=ID1)
DEBUG	ordeq.runner	Running view 'a' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID6)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO 'd:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Unpersisting data for IO 'c:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Unpersisting data for IO 'b:input_data' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID5)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID6)

```