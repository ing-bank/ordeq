## Resource

```python
from ordeq import Input


class ExampleStaticIO(Input[str]):
    @staticmethod
    def load() -> None:
        print("Hello!")


_ = ExampleStaticIO()

```