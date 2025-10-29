## Resource

```python
from ordeq import node, run
from ordeq._nodes import get_node
from ordeq_common import Print


@node
def view() -> str:
    return "Hello!"


@node(inputs=view, outputs=Print())
def hello(data: str) -> None:
    print(data)


result = run(hello)
print(view, "computed", result[get_node(view)])

```

## Exception

```text
TypeError: 'NoneType' object is not subscriptable
  File "/packages/ordeq/tests/resources/views/view_index_run_result_by_node.py", line LINO, in <module>
    print(view, "computed", result[get_node(view)])
                            ~~~~~~^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

```

## Output

```text
Hello!
None

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_index_run_result_by_node:view'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "view" in module "view_index_run_result_by_node"
INFO	ordeq.runner	Running node "hello" in module "view_index_run_result_by_node"
INFO	ordeq.io	Saving Print()

```

## Typing

```text
packages/ordeq/tests/resources/views/view_index_run_result_by_node.py:16: error: "run" does not return a value (it only ever returns None)  [func-returns-value]
Found 1 error in 1 file (checked 1 source file)

```