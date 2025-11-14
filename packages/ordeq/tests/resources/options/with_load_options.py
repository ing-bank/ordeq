from dataclasses import dataclass
from pathlib import Path

from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class ExampleInputLoadKwarg(Input):
    path: Path
    attribute: str

    def load(self, hello: str = "Hi") -> str:
        return f"{self.path}@{self.attribute}: {hello} world!"


example_input = ExampleInputLoadKwarg(path=Path("hello.txt"), attribute="L1")
# No kwarg:
print(example_input.load())
# Alternative kwarg:
print(example_input.load(hello="Hello"))
print(type(example_input))

with_options = example_input.with_load_options(hello="Hello")
# No kwarg, with load options:
print(with_options.load())
# Alternative kwarg, with load options:
print(with_options.load(hello="Hello"))
print(type(with_options))


@dataclass(kw_only=True, frozen=True)
class ExampleInputLoadArg(Input):
    path: Path
    attribute: str

    def load(self, hello: str = "Hello") -> str:
        return f"{self.path}@{self.attribute}: {hello} world!"


example_input_arg = ExampleInputLoadArg(path=Path("hello.txt"), attribute="L1")
print(example_input_arg.load(hello="Hello"))
print(type(example_input_arg))

with_options_arg = example_input_arg.with_load_options(hello="Hello")
# This should raise a type error,
# but still run as we fill the missing kwarg on load:
# TODO: Add a check during with_load_options to ensure all required load_args
#  are set.
print(with_options_arg.load())
# Alternative kwarg, with load options:
print(with_options_arg.load(hello="Hi"))
print(type(with_options_arg))
# Unknown kwarg:
example_input_arg.with_load_options(unknown_kwarg="Hello")  # should error
