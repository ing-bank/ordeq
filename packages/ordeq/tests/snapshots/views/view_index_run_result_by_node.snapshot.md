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
print(view, 'computed', result[get_node(view)])

```

## Output

```text
Hello!
None
<function view at HASH1> computed Hello!

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
packages/ordeq/tests/resources/views/view_index_run_result_by_node.py:17: error: Invalid index type "Node[Any, Any]" for "dict[Input[Any] | Output[Any] | View[Any, Any], Any]"; expected type "Input[Any] | Output[Any] | View[Any, Any]"  [index]
Found 1 error in 1 file (checked 1 source file)

```