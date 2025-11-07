## Resource

```python
from example_async import sync_nodes
from ordeq import run

run(sync_nodes)

```

## Output

```text
Start analyzing buffer_2...
Finished analyzing buffer_2 after 2 seconds.
Start fetching buffer_1...
Finished fetching buffer_1 after 4 seconds.

```

## Logging

```text
INFO	ordeq.runner	Running node "write_buffer_2" in module "example_async.sync_nodes"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH1>)
INFO	ordeq.runner	Running node "write_buffer_1" in module "example_async.sync_nodes"
INFO	ordeq.io	Saving StringBuffer(_buffer=<_io.StringIO object at HASH2>)

```