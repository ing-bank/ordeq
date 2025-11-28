## Resource

```python
from ordeq import Output, node


class Example(Output[str]):
    def save(self, data: str) -> None:
        print("saving!", data)


example = Example()

print("Should raise an error ('example' is an output):")


@node(inputs=[example])
def load_node(data: str) -> None:
    print("loading!", data)

```

## Output

```text
Should raise an error ('example' is an output):

```