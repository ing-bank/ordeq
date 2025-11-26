## Resource

```python
from ordeq import IO, Input, Output


class ExampleStaticInput(Input[str]):
    @staticmethod
    def load() -> str:
        return "loaded"


x = ExampleStaticInput()
print(x.load())


class ExampleStaticOutput(Output[str]):
    @staticmethod
    def save(data: str) -> None:
        print(data)


y = ExampleStaticOutput()
y.save("saved")


class ExampleStaticIO(IO[str]):
    @staticmethod
    def load() -> str:
        return "loaded"

    @staticmethod
    def save(data: str) -> None:
        print(data)


z = ExampleStaticIO()
print(z.load())
z.save("saved")

```

## Output

```text
loaded
saved
loaded
saved

```