from dataclasses import dataclass

from ordeq import IO, Input, Output

a = Input()
b = Output()
c = IO()

assert a._name is None
assert b._name is None
assert c._name is None

a.__dict__["_name"] = "input_a"
print("Expect input_a")
print(a._name)


@dataclass(frozen=True)
class ExampleIO(IO[str]):
    def load(self):
        return "Hello world"

    def save(self, data: str) -> None:
        print("Saving data:", data)


example_io = ExampleIO()
assert example_io._name is None

example_io.__dict__["_name"] = "example_io"
print("Expect example_io")
print(example_io._name)

print("Check if logging outputs name on load and save:")
example_io.load()
example_io.save("Hello world")
