from dataclasses import dataclass

from ordeq import Input


@dataclass(kw_only=True, frozen=True)
class ExampleInputLoadArg(Input):
    def load(self) -> str:
        return "Hello world"


_ = ExampleInputLoadArg().with_load_options(hello="hello world")
