## Resource

```python
import example_function_reuse
from ordeq import run

run(example_function_reuse, verbose=True)

```

## Output

```text
io-0 --> View:example_function_reuse.nodes:a
io-0 --> View:example_function_reuse.nodes:pi
io-1 --> View:example_function_reuse.nodes:d
io-2 --> View:example_function_reuse.nodes:c
io-3 --> View:example_function_reuse.nodes:b
View:example_function_reuse.nodes:pi --> io-4
View:example_function_reuse.nodes:d --> io-5
View:example_function_reuse.nodes:c --> io-6
View:example_function_reuse.nodes:b --> io-7
View:example_function_reuse.nodes:a --> io-8
A
B
C
D
A

```

## Logging

```text
INFO	ordeq.io	Loading StringBuffer 'A' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'A' in module 'example_function_reuse.catalog'
INFO	ordeq.runner	Running view 'a' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.io	Loading StringBuffer 'B' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'B' in module 'example_function_reuse.catalog'
INFO	ordeq.runner	Running view 'b' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
INFO	ordeq.io	Loading StringBuffer 'C' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'C' in module 'example_function_reuse.catalog'
INFO	ordeq.runner	Running view 'c' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID3)
INFO	ordeq.io	Loading StringBuffer 'D' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Persisting data for StringBuffer 'D' in module 'example_function_reuse.catalog'
INFO	ordeq.runner	Running view 'd' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID4)
DEBUG	ordeq.io	Loading cached data for StringBuffer 'A' in module 'example_function_reuse.catalog'
INFO	ordeq.runner	Running view 'pi' in module 'example_function_reuse.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID5)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'A' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID5)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'D' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID4)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'C' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID3)
DEBUG	ordeq.io	Unpersisting data for StringBuffer 'B' in module 'example_function_reuse.catalog'
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```