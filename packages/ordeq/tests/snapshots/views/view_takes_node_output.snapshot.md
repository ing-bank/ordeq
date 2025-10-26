## Resource

```python
from ordeq import node, run, IO
from ordeq_common import Literal

placeholder = IO()

hello = Literal("Hello")


@node(inputs=[Literal("Jane"), hello], outputs=placeholder)
def hello_from_someone(name: str, v: str) -> str:
    return f"{name} said '{v}'"


@node(inputs=placeholder)
def what_i_heard(v: str) -> None:
    print(f"I heard that {v}")


@node(inputs=what_i_heard)
def sink(s: str) -> None:
    print(s)


# This should succeed, as it produces the placeholder IO's value
print(run(hello_from_someone, sink, verbose=True))

# This should fail: it attempts to load placeholder IO
print(run(sink, verbose=True))

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=view_takes_node_output:hello_from_someone, inputs=[Literal('Jane'), Literal('Hello')], outputs=[IO(idx=ID1)]), Node(name=view_takes_node_output:hello_from_someone, inputs=[Literal('Jane'), Literal('Hello')], outputs=[IO(idx=ID1)])])
```

## Output

```text
NodeGraph:
  Edges:
     view_takes_node_output:hello_from_someone -> [view_takes_node_output:hello_from_someone, view_takes_node_output:hello_from_someone, view_takes_node_output:what_i_heard]
     view_takes_node_output:sink -> []
     view_takes_node_output:what_i_heard -> []
  Nodes:
     Node(name=view_takes_node_output:hello_from_someone, inputs=[Literal('Jane'), Literal('Hello')], outputs=[IO(idx=ID1)])
     View(name=view_takes_node_output:sink, inputs=[View(name=view_takes_node_output:what_i_heard, inputs=[IO(idx=ID1)])])
     View(name=view_takes_node_output:what_i_heard, inputs=[IO(idx=ID1)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_takes_node_output:what_i_heard'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_takes_node_output:sink'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq/tests/resources/views/view_takes_node_output.py:4: error: Need type annotation for "placeholder"  [var-annotated]
Found 1 error in 1 file (checked 1 source file)

```