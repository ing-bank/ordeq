## Resource

```python
from ordeq import NodeHook, run


class MyHook(NodeHook):
    def before_node_run(self, node, *args, **kwargs):
        print(f"Before running node: {node.name}")

    def after_node_run(self, node, *args, **kwargs):
        print(f"After running node: {node.name}")


run("example_1", hooks=["example_1.hooks:MyHook", MyHook()])

```

## Output

```text
Starting the run
Before running node: example_1.wrapped_io:hello
Name: John
After running node: example_1.wrapped_io:hello
Before running node: example_1.wrapped_io:print_message
Name: John
After running node: example_1.wrapped_io:print_message
Finished the run

```

## Logging

```text
INFO	ordeq.io	Loading NameGenerator(name='John')
INFO	ordeq.runner	Running node "hello" in module "example_1.wrapped_io"
INFO	ordeq.io	Saving SayHello(name=NameGenerator(name='John'), writer=(NamePrinter(),))
INFO	ordeq.io	Saving NamePrinter()
INFO	ordeq.runner	Running node "print_message" in module "example_1.wrapped_io"
INFO	ordeq.io	Saving NamePrinter()

```