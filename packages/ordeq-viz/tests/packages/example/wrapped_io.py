from dataclasses import dataclass

from ordeq import IO, Input, Output, node, run


@dataclass(kw_only=True, frozen=True)
class NameGenerator(Input[str]):
    name: str

    def load(self) -> str:
        return self.name


@dataclass(kw_only=True, frozen=True)
class NamePrinter(Output[str]):
    def save(self, data: str) -> None:
        print(f"Name: {data}")


@dataclass(kw_only=True, frozen=True)
class SayHello(IO[str]):
    name: Input[str]
    writer: tuple[Output[str]]

    def load(self) -> str:
        return f"Hello, {self.name.load()}!"

    def save(self, data: str) -> None:
        for w in self.writer:
            w.save(data)


name_generator = NameGenerator(name="John")
name_printer = NamePrinter()
message = SayHello(name=name_generator, writer=(name_printer,))


@node(inputs=[name_generator], outputs=[message])
def hello(name: str) -> str:
    return name


@node(inputs=[message], outputs=[name_printer])
def print_message(message: str) -> str:
    return message


run(hello, print_message)
