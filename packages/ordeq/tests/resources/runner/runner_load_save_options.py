from ordeq import node, IO
from ordeq._runner import run
from ordeq_common import Literal, StringBuffer


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
x2 = CustomIO().with_save_options(
    suffix="!"
)
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
