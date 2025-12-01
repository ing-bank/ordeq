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
io-0 --> Node:__main__:increment
Node:__main__:increment --> io-2
io-1 --> Node:__main__:decrement
io-2 --> Node:__main__:decrement
Node:__main__:decrement --> io-3
x says 'x says y did it ' but y says 'x did it and I know the murder weapon'  

```

## Logging

```text
INFO	ordeq.io	Loading CustomIO 'increment:x' in module '__main__'
DEBUG	ordeq.io	Persisting data for CustomIO 'increment:x' in module '__main__'
INFO	ordeq.runner	Running node 'increment' in module '__main__'
INFO	ordeq.io	Saving CustomIO 'decrement:x' in module '__main__'
DEBUG	ordeq.io	Persisting data for CustomIO 'decrement:x' in module '__main__'
DEBUG	ordeq.io	Loading cached data for CustomIO 'decrement:x' in module '__main__'
INFO	ordeq.io	Loading CustomIO 'decrement:y' in module '__main__'
DEBUG	ordeq.io	Persisting data for CustomIO 'decrement:y' in module '__main__'
INFO	ordeq.runner	Running node 'decrement' in module '__main__'
INFO	ordeq.io	Saving CustomIO(attr=)
DEBUG	ordeq.io	Persisting data for CustomIO(attr=x says 'x says y did it ' but y says 'x did it and I know the murder weapon' )
DEBUG	ordeq.io	Unpersisting data for CustomIO 'increment:x' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for CustomIO 'decrement:x' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for CustomIO 'decrement:y' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for CustomIO(attr=x says 'x says y did it ' but y says 'x did it and I know the murder weapon' )
INFO	ordeq.io	Loading CustomIO(attr=x says 'x says y did it ' but y says 'x did it and I know the murder weapon' )

```