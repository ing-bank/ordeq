from ordeq import Input
from ordeq_common import Literal


class MyIO(Input[str]):
    def __init__(self, other_io: Input) -> None:
        super().__init__()
        self.other_io = other_io

    def load(self) -> str:
        return "Hello" + self.other_io.load()


# unnamed
test_io = MyIO(other_io=Literal("World!"))
nested_test_io = MyIO(other_io=MyIO(other_io=Literal("World!")))

# named
world = Literal("World!")
named_test_io = MyIO(other_io=world)
named_nested_test_io = MyIO(other_io=MyIO(other_io=world))
