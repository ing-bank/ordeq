## Resource

```python
from ordeq import node, run
from ordeq_common import Print


@node
def view() -> str:
    return "Hello!"


@node(inputs=view, outputs=Print())
def hello(data: str) -> None:
    print(data)


result = run(hello)
# This should work, but it doesn't because
print(view, 'computed', result[view])

```

## Exception

```text
KeyError: <function view at HASH1>
  File "/packages/ordeq/tests/resources/views/view_index_run_result.py", line 17, in <module>
    print(view, 'computed', result[view])
                            ~~~~~~^^^^^^

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line 84, in run_module
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
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'view_index_run_result:view'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "view" in module "view_index_run_result"
INFO	ordeq.runner	Running node "hello" in module "view_index_run_result"
INFO	ordeq.io	Saving Print()

```

## Typing

```text
packages/ordeq/tests/resources/views/view_index_run_result.py:17: error: Invalid index type "Callable[[], str]" for "dict[Input[Any] | Output[Any] | View[Any, Any], Any]"; expected type "Input[Any] | Output[Any] | View[Any, Any]"  [index]
Found 1 error in 1 file (checked 1 source file)

```