## Resource

```python
from ordeq import Output


class ExampleStaticIO(Output[str]):
    @staticmethod
    def save(data: str) -> None:
        print(data)


_ = ExampleStaticIO()

```