## Resource

```python
from example_duplicates import duplicate_io_same_hash
from example_duplicates.duplicate_io_same_hash import MyIO, hello, result
from ordeq import run

sub = MyIO(
    value="sub", attr=result.attr
)  # has the same hash as `result` and `hello`

print("Should print 'Saying hello (attr = 0)'")
run(duplicate_io_same_hash, io={result: sub})

print("Should print 'Saying hello (attr = 0)'")
run(duplicate_io_same_hash, io={sub: hello})

print("Should print 'Saying sub (attr = 0)'")
run(duplicate_io_same_hash, io={hello: sub})

```

## Output

```text
Should print 'Saying hello (attr = 0)'
Saying hello (attr = 0)
Should print 'Saying hello (attr = 0)'
Saying hello (attr = 0)
Should print 'Saying sub (attr = 0)'
Saying sub (attr = 0)

```

## Logging

```text
INFO	ordeq.runner	Loading MyIO 'hello' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Persisting data for MyIO 'hello' in module 'example_duplicates.duplicate_io_same_hash'
INFO	ordeq.runner	Running node 'say' in module 'example_duplicates.duplicate_io_same_hash'
INFO	ordeq.runner	Saving MyIO(value='sub', attr=0)
DEBUG	ordeq.io	Persisting data for MyIO(value='sub', attr=0)
DEBUG	ordeq.io	Unpersisting data for MyIO 'hello' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Unpersisting data for MyIO(value='sub', attr=0)
INFO	ordeq.runner	Loading MyIO 'hello' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Persisting data for MyIO 'hello' in module 'example_duplicates.duplicate_io_same_hash'
INFO	ordeq.runner	Running node 'say' in module 'example_duplicates.duplicate_io_same_hash'
INFO	ordeq.runner	Saving MyIO 'result' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Persisting data for MyIO 'result' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Unpersisting data for MyIO 'hello' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Unpersisting data for MyIO 'result' in module 'example_duplicates.duplicate_io_same_hash'
INFO	ordeq.runner	Loading MyIO(value='sub', attr=0)
DEBUG	ordeq.io	Persisting data for MyIO(value='sub', attr=0)
INFO	ordeq.runner	Running node 'say' in module 'example_duplicates.duplicate_io_same_hash'
INFO	ordeq.runner	Saving MyIO 'result' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Persisting data for MyIO 'result' in module 'example_duplicates.duplicate_io_same_hash'
DEBUG	ordeq.io	Unpersisting data for MyIO(value='sub', attr=0)
DEBUG	ordeq.io	Unpersisting data for MyIO 'result' in module 'example_duplicates.duplicate_io_same_hash'

```