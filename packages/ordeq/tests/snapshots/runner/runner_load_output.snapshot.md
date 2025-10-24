## Resource

```python
from ordeq import Output, node, run


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


example = Example()


@node(outputs=[example])
def my_node() -> str:
    return "Hello, World!"

@node(inputs=[example])
def load_node(data: str) -> None:
    print("loading!", data)


run(my_node, load_node)

```

## Exception

```text
AttributeError: 'Example' object has no attribute 'load'
```

## Output

```text
saving! Hello, World!

```

## Logging

```text
INFO	ordeq.runner	Running node Node(name=runner_load_output:my_node, outputs=[Output(idx=ID1)])
INFO	ordeq.io	Saving Output(idx=ID1)

```

## Typing

```text
packages/ordeq/tests/resources/runner/runner_load_output.py:16: error: List item 0 has incompatible type "Example"; expected "Input[Any]"  [list-item]
Found 1 error in 1 file (checked 1 source file)

```