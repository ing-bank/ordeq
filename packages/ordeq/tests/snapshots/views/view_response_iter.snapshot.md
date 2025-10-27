## Resource

```python
import requests
from typing import Any, Iterator

from ordeq import node, run
from ordeq_common import Literal

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
users_response = Literal(response)


# View that returns an iterable from a regular/non-iterable IO:
@node(inputs=users_response)
def users_lines(r: requests.Response) -> Iterator[Any]:
    return r.iter_lines()


@node(inputs=users_lines)
def concatenate(lines: Iterator[Any]) -> None:
    for line in lines:
        print(line)


print(run(concatenate, verbose=True))

```

## Exception

```text
AttributeError: 'View' object has no attribute 'load'
  File "/packages/ordeq/src/ordeq/_runner.py", line 56, in _run_node
    cast("Input", input_dataset).load() for input_dataset in node.inputs
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line 135, in _run_graph
    computed = _run_node(
        name, patched_nodes[name, node], hooks=hooks, save=save_node
    )

  File "/packages/ordeq/src/ordeq/_runner.py", line 187, in run
    result = _run_graph(graph, hooks=node_hooks, save=save, io=io)

  File "/packages/ordeq/tests/resources/views/view_response_iter.py", line 23, in <module>
    print(run(concatenate, verbose=True))
          ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
NodeGraph:
  Edges:
     view_response_iter:concatenate -> []
     view_response_iter:users_lines -> [view_response_iter:concatenate]
  Nodes:
     view_response_iter:concatenate: View(name=view_response_iter:concatenate, inputs=[View(name=view_response_iter:users_lines, inputs=[Literal(<Response [200]>)])])
     view_response_iter:users_lines: View(name=view_response_iter:users_lines, inputs=[Literal(<Response [200]>)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:users_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_iter:concatenate'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading Literal(<Response [200]>)
INFO	ordeq.runner	Running node "users_lines" in "view_response_iter"

```