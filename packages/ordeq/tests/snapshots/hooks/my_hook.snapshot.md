## Resource

```python
from ordeq import Node, NodeHook, Output, OutputHook, node
from ordeq_common import StringBuffer


class MyUntypedOutputHook(OutputHook):
    def before_output_save(self, op: Output[str], data: str) -> None:
        print(f"saving data `{data}` to output `{op}`")


class MyFixedOutputHook(MyUntypedOutputHook, NodeHook):
    def before_node_run(self, node: Node) -> None:
        print(f"Running {node}")


@node(inputs=StringBuffer("a"), outputs=StringBuffer("b"))
def func(x: str) -> str:
    return x


# This is just to ensure the hook can be instantiated without errors.
untyped_hook = MyUntypedOutputHook()
untyped_hook.before_output_save(StringBuffer("A"), "hello")

fixed_output_hook = MyFixedOutputHook()
fixed_output_hook.before_node_run(func)
fixed_output_hook.before_output_save(StringBuffer("B"), "world")

```

## Output

```text
saving data `hello` to output `StringBuffer(_buffer=<_io.StringIO object at HASH1>)`
Running node 'func' in module '__main__'
saving data `world` to output `StringBuffer(_buffer=<_io.StringIO object at HASH1>)`

```

## Typing

```text
packages/ordeq/tests/resources/hooks/my_hook.py:6:9: error[invalid-method-override] Invalid override of method `before_output_save`: Definition is incompatible with `OutputHook.before_output_save`
Found 1 diagnostic

```