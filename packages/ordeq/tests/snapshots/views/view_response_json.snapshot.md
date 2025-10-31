## Resource

```python
import requests
from ordeq import node, run
from ordeq_common import Literal

response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # noqa: S113 (call without timeout)
users_response = Literal(response)


@node(inputs=users_response)
def users_json(r: requests.Response) -> dict:
    return r.json()


@node(inputs=users_json)
def to_yaml(d: dict) -> None:
    print("Data:", d)


run(to_yaml, verbose=True)

```

## Exception

```text
UnboundLocalError: cannot access local variable 'patched_io' where it is not associated with a value
  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _run_graph(graph, hooks=node_hooks, save=save, io=patched_io)
                                                      ^^^^^^^^^^

  File "/packages/ordeq/tests/resources/views/view_response_json.py", line LINO, in <module>
    run(to_yaml, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^

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
     view_response_json:to_yaml -> []
     view_response_json:users_json -> [view_response_json:to_yaml]
  Nodes:
     view_response_json:to_yaml: View(name=view_response_json:to_yaml, inputs=[View(name=view_response_json:users_json, inputs=[Literal(<Response [200]>)])])
     view_response_json:users_json: View(name=view_response_json:users_json, inputs=[Literal(<Response [200]>)])

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_json:users_json'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_response_json:to_yaml'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```