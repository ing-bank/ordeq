from dataclasses import dataclass, field

from ordeq import IO, node


@dataclass(frozen=True)
class MyIO(IO[str]):
    value: str = field(hash=False)
    attr: int  # only 'attr' affects the hash

    def load(self) -> str:
        return self.value

    def save(self, data: str) -> None:
        print(f"{data} (attr = {self.attr})")


hello = MyIO("hello", attr=0)
result = MyIO("result", attr=0)


@node(inputs=[hello], outputs=[result])
def say(hi: str) -> str:
    return f"Saying {hi}"
