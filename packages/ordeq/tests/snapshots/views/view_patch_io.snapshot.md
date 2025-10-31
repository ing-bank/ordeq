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

## Exception

```text
AttributeError: 'Literal' object has no attribute '__name__'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_package_to_ios
    modules = _resolve_packages_to_modules([(package.__name__, package)])
                                             ^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _substitute_catalog_by_catalog
    sorted(_resolve_package_to_ios(old).items()),
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitute
    return _substitute_catalog_by_catalog(old, new)

  File "/packages/ordeq/src/ordeq/_substitute.py", line LINO, in _build_substitution_map
    substitution_map.update(_build_substitute(key, value))
                            ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    substitution_map = _build_substitution_map(io)

  File "/packages/ordeq/tests/resources/views/view_patch_io.py", line LINO, in <module>
    run(n, verbose=True, io={hello_io: Literal("Buenos dias")})
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

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

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_patch_io:hello_world'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_patch_io:n'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```