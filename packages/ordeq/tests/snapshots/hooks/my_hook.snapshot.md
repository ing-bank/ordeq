## Resource

```python
from ordeq import Node, NodeHook, Output, OutputHook, node
from ordeq._nodes import get_node
from ordeq_common import StringBuffer


class MyUntypedOutputHook(OutputHook):
    def before_output_save(
        self, op: Output[str], data: str
    ) -> None:
        print(f"saving data `{data}` to output `{op}`")


class MyFixedOutputHook(MyUntypedOutputHook, NodeHook):
    def before_node_run(self, node: Node) -> None:
        print(f"running node {node}")


@node(inputs=StringBuffer("a"), outputs=StringBuffer("b"))
def func(x: str) -> str:
    return x


# This is just to ensure the hook can be instantiated without errors.
untyped_hook = MyUntypedOutputHook()
untyped_hook.before_output_save(StringBuffer("A"), "hello")

fixed_output_hook = MyFixedOutputHook()
fixed_output_hook.before_node_run(get_node(func))
fixed_output_hook.before_output_save(StringBuffer("B"), "world")

```

## Output

```text
saving data `hello` to output `StringBuffer(_buffer=<_io.StringIO object at HASH1>)`
running node Node(name=my_hook:func, inputs=[StringBuffer(_buffer=<_io.StringIO object at HASH2>)], outputs=[StringBuffer(_buffer=<_io.StringIO object at HASH3>)])
saving data `world` to output `StringBuffer(_buffer=<_io.StringIO object at HASH1>)`

```