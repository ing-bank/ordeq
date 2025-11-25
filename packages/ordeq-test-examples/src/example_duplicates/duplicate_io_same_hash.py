from dataclasses import dataclass, field

from ordeq import Input


@dataclass(frozen=True)
class MyIO(Input[str]):
    value: str = field(hash=False)
    attr: int  # only 'attr' affects the hash

    def load(self) -> str:
        return self.value

    @staticmethod
    def save(data: str) -> None:
        print(f"Saving data: {data}")


hello = MyIO("hello", attr=0)
result = MyIO("result", attr=0)

assert hash(hello) == hash(result), "Hashes should be the same"
