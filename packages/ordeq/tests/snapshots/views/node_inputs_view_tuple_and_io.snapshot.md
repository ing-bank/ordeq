## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Literal, Print


@node
def hello() -> tuple[str, str]:
    return "Hello", "world"


print(repr(get_node(hello)))


@node(inputs=[hello, Literal("!!!")], outputs=Print())
def combine_greeting_with_ending(greeting: tuple[str, str], e: str):
    return f"{' '.join(greeting)} {e}"


run(combine_greeting_with_ending, verbose=True)

```

## Output

```text
View(name=node_inputs_view_tuple_and_io:hello)
NodeGraph:
  Edges:
     node_inputs_view_tuple_and_io:combine_greeting_with_ending -> []
     node_inputs_view_tuple_and_io:hello -> [node_inputs_view_tuple_and_io:combine_greeting_with_ending]
  Nodes:
     node_inputs_view_tuple_and_io:combine_greeting_with_ending: Node(name=node_inputs_view_tuple_and_io:combine_greeting_with_ending, inputs=[View(name=node_inputs_view_tuple_and_io:hello), Literal('!!!')], outputs=[Print()])
     node_inputs_view_tuple_and_io:hello: View(name=node_inputs_view_tuple_and_io:hello)
Hello world !!!

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_view_tuple_and_io:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "hello" in module "node_inputs_view_tuple_and_io"
INFO	ordeq.io	Loading Literal('!!!')
INFO	ordeq.runner	Running node "combine_greeting_with_ending" in module "node_inputs_view_tuple_and_io"
INFO	ordeq.io	Saving Print()

```