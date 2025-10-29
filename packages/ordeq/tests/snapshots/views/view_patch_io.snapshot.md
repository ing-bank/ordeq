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
NodeGraph:
  Edges:
     view_patch_io:hello_world -> [view_patch_io:n]
     view_patch_io:n -> []
  Nodes:
     view_patch_io:hello_world: View(name=view_patch_io:hello_world, inputs=[Literal('Hello')])
     view_patch_io:n: View(name=view_patch_io:n, inputs=[View(name=view_patch_io:hello_world, inputs=[Literal('Hello')])])
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

## Typing

```text
packages/ordeq/tests/resources/views/view_patch_io.py:17: error: Argument "io" to "run" has incompatible type "dict[Literal[str], Literal[str]]"; expected "dict[Input[Never] | Output[Never], Input[Never] | Output[Never]] | None"  [arg-type]
Found 1 error in 1 file (checked 1 source file)

```