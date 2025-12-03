## Resource

```python
from ordeq._runner import run

run("example_nested.subpackage.subsubpackage.hello:world", verbose=True)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested",
)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage",
)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage.subsubpackage",
)

print("Should assign FQNs from context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage.subsubpackage.hello",
)

print("FQNs not found in context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.subpackage.subsubpackage.hello_relative",
)

print("FQNs not found in context:")
run(
    "example_nested.subpackage.subsubpackage.hello:world",
    verbose=True,
    context="example_nested.catalog",
)

```

## Output

```text
View:View(func=example_nested.subpackage.subsubpackage.hello:world, ...) --> io-1
Hello, World!
Should assign FQNs from context:
View:example_nested.subpackage.subsubpackage.hello:world --> io-1
Hello, World!
Should assign FQNs from context:
View:example_nested.subpackage.subsubpackage.hello:world --> io-1
Hello, World!
Should assign FQNs from context:
View:example_nested.subpackage.subsubpackage.hello:world --> io-1
Hello, World!
Should assign FQNs from context:
View:example_nested.subpackage.subsubpackage.hello:world --> io-1
Hello, World!
FQNs not found in context:
View:View(func=example_nested.subpackage.subsubpackage.hello:world, ...) --> io-1
Hello, World!
FQNs not found in context:
View:View(func=example_nested.subpackage.subsubpackage.hello:world, ...) --> io-1
Hello, World!

```

## Logging

```text
INFO	ordeq.runner	Running View(func=example_nested.subpackage.subsubpackage.hello:world, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'world' in module 'example_nested.subpackage.subsubpackage.hello'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'world' in module 'example_nested.subpackage.subsubpackage.hello'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'world' in module 'example_nested.subpackage.subsubpackage.hello'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'world' in module 'example_nested.subpackage.subsubpackage.hello'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
INFO	ordeq.runner	Running View(func=example_nested.subpackage.subsubpackage.hello:world, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)
INFO	ordeq.runner	Running View(func=example_nested.subpackage.subsubpackage.hello:world, ...)
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```