from dataclasses import dataclass

from ordeq import Output


@dataclass(kw_only=True, frozen=True)
class ExampleOutputsaveArg(Output):
    def save(self, data: str, hello: str = "...") -> None:
        pass


_ = ExampleOutputsaveArg().with_save_options(world="hello world")
