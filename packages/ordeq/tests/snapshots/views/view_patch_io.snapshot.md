## Resource

```python
from ordeq import node, run
from ordeq_common import Literal

hello_io = Literal("Hello")


@node(inputs=hello_io)
def hello_world(hello: str) -> tuple[str, str]:
    return hello, "World!"


@node(inputs=hello_world)
def n(v: tuple[str, ...]):
    print(f"Node received '{' '.join(v)}'")


run(n, verbose=True, io={hello_io: Literal("Buenos dias")})

```

## Output

```text
io-0 --> View:view_patch_io:n
io-2 --> View:view_patch_io:hello_world
View:view_patch_io:n --> io-1
View:view_patch_io:hello_world --> io-0
Node received 'Buenos dias World!'

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_patch_io:hello_world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_patch_io:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal('Buenos dias')
INFO	ordeq.runner	Running view "hello_world" in module "view_patch_io"
INFO	ordeq.runner	Running view "n" in module "view_patch_io"

```