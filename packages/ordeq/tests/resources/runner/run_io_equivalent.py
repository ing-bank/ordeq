from dataclasses import dataclass

from ordeq import Output, node, run


@dataclass(frozen=True)
class MyPet(Output[str]):
    name: str

    def save(self, greeting: str) -> None:
        print(greeting, self.name)

    def __eq__(self, other) -> bool:
        return isinstance(other, MyPet) and len(self.name) == len(other.name)

    def __hash__(self) -> int:
        return hash(self.name)


cat = MyPet(name="cat")
dog = MyPet(name="dog")


@node(outputs=[cat])
def feeding():
    return "Feeding my"


print("Should print 'Feeding my dog':")
run(feeding, io={cat: dog})
