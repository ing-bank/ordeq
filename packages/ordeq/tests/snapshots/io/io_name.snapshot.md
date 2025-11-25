## Resource

```python
from dataclasses import dataclass

from ordeq import IO, Input, Output
from ordeq._fqn import FQN

a = Input[str]()
b = Output[str]()
c = IO[str]()

assert a._name is None
assert b._name is None
assert c._name is None

a.__dict__["_name"] = "input_a"
print("Expect input_a")
print(a._name)
print("Expect Input(id=...):")
print(a)


@dataclass(frozen=True)
class ExampleIO(IO[str]):
    def load(self):
        return "Hello world"

    def save(self, data: str) -> None:
        print("Saving data:", data)


example_io = ExampleIO()
assert example_io._name is None

example_io._set_fqn(FQN(__name__, "_example"))
print(f"Expect 'example_io' in '{__name__}':")
print(example_io)

print("Check if logging outputs name on load and save:")
example_io.load()
example_io.save("Hello world")

```

## Output

```text
Expect input_a
input_a
Expect Input(id=...):
Input(id=ID1)
Expect 'example_io' in '__main__':
'_example' in module '__main__'
Check if logging outputs name on load and save:
Saving data: Hello world

```

## Logging

```text
INFO	ordeq.io	Loading '_example' in module '__main__'
INFO	ordeq.io	Saving '_example' in module '__main__'

```