from dataclasses import dataclass

from ordeq import Input


@dataclass(kw_only=True, frozen=True, eq=False)
class ExampleInputNoLoad(Input): ...


_ = ExampleInputNoLoad()
