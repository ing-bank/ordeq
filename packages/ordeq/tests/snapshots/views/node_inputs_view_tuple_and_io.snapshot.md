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

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/node_inputs_view_tuple_and_io.py", line LINO, in <module>
    run(combine_greeting_with_ending, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

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

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'node_inputs_view_tuple_and_io:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```