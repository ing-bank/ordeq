## Resource

```python
from ordeq import IO, Input
from ordeq_common import Print

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

```

## Output

```text
Should print 'ordeq_common.io.printer:Print':
ordeq_common.io.printer:Print
Should print '__main__:CustomIO':
__main__:CustomIO
Should print 'ordeq._io:Input':
ordeq._io:Input

```

## Logging

```text
DEBUG	ordeq.io	Persisting data for Input(id=ID1)

```