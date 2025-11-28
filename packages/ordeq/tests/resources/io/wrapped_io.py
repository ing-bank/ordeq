from dataclasses import dataclass

from ordeq import IO, Input, Output


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
    writer: Output[str]

    def load(self) -> str:
        return f"Hello, {self.name.load()}!"

    def save(self, data: str) -> None:
        self.writer.save(data)


name_generator = NameGenerator(name="John")
print(name_generator)
print(name_generator.references)

name_printer = NamePrinter()
print(name_printer)
print(name_printer.references)

message = SayHello(name=name_generator, writer=name_printer)
print(message)
print(message.references)

assert name_generator != message
