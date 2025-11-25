from dataclasses import dataclass

from ordeq import Input


@dataclass(frozen=True)
class MyIO(Input[str]):
    value: str

    def load(self) -> str:
        return self.value

    @staticmethod
    def save(data: str) -> None:
        print(f"Saving data: {data}")


hello = MyIO("hello")
result = MyIO("result")
