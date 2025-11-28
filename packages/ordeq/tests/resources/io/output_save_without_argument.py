from dataclasses import dataclass

from ordeq import Output


@dataclass(kw_only=True, frozen=True, eq=False)
class ExampleOutputNosave(Output):
    def save(self) -> None:
        pass


_ = ExampleOutputNosave()
