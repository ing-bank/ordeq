## Resource

```python
from ordeq import IO, node
from ordeq._runner import run


class CustomIO(IO[str]):
    def __init__(self, attr: str = ""):
        self.attr = attr
        super().__init__()

    def load(self, suffix: str = "") -> str:
        return f"{self.attr} {suffix}"

    def save(self, value: str, suffix: str = "") -> None:
        self.attr += f"{value} {suffix}"

    def __repr__(self):
        return f"CustomIO(attr={self.attr})"


x1 = CustomIO("y did it")
x2 = CustomIO().with_save_options(suffix="!")
x3 = CustomIO("x did it").with_load_options(
    suffix="and I know the murder weapon"
)
x4 = CustomIO()


@node(inputs=x1, outputs=x2)
def increment(x: str) -> str:
    return f"x says {x}"


@node(inputs=[x2, x3], outputs=x4)
def decrement(x: str, y: str) -> str:
    return f"x says '{x}' but y says '{y}'"


run(increment, decrement, verbose=True)
print(x4.load())

```

## Output

```text
NodeGraph:
  Edges:
     runner_load_save_options:decrement -> []
     runner_load_save_options:increment -> [runner_load_save_options:decrement]
  Nodes:
     runner_load_save_options:decrement: Node(name=runner_load_save_options:decrement, inputs=[CustomIO(attr=), CustomIO(attr=x did it)], outputs=[CustomIO(attr=)])
     runner_load_save_options:increment: Node(name=runner_load_save_options:increment, inputs=[CustomIO(attr=y did it)], outputs=[CustomIO(attr=)])
x says 'x says y did it ' but y says 'x did it and I know the murder weapon'  

```

## Logging

```text
INFO	ordeq.io	Loading CustomIO(attr=y did it)
INFO	ordeq.runner	Running node "increment" in module "runner_load_save_options"
INFO	ordeq.io	Saving CustomIO(attr=)
INFO	ordeq.io	Loading CustomIO(attr=x did it)
INFO	ordeq.runner	Running node "decrement" in module "runner_load_save_options"
INFO	ordeq.io	Saving CustomIO(attr=)
INFO	ordeq.io	Loading CustomIO(attr=x says 'x says y did it ' but y says 'x did it and I know the murder weapon' )

```