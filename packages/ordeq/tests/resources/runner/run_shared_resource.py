from ordeq import run, node, IO
from io import StringIO
from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class Buffer(IO[str]):
    buffer: StringIO

    def load(self) -> str:
        return self.buffer.getvalue()

    def save(self, data: str) -> None:
        self.buffer.write(data)


raw_buffer = StringIO()
first_buffer_io = Buffer(buffer=raw_buffer)
second_buffer_io = Buffer(buffer=raw_buffer)


@node(outputs=first_buffer_io)
def first() -> str:
    return "Hello, world!"


@node(inputs=second_buffer_io)
def second(value: str) -> None:
    print(value)


# The run needs to recognize that 'first' and 'second' share the same resource
# It should plan first -> second.
run(second, first, verbose=True)
