from ordeq_common import Print
from ordeq import IO, Input

p = Print()

print("Should print 'ordeq_common.io.printer:Print':")
print(p.type_fqn)


class CustomIO(IO[str]):
    def load(self) -> str:
        return "custom data"

    def save(self, data: str) -> None:
        print(f"Saving data: {data}")


custom = CustomIO()
print("Should print '__main__:CustomIO':")
print(custom.type_fqn)

i = Input[str]("my_input")
print("Should print 'ordeq._io:Input':")
print(i.type_fqn)
