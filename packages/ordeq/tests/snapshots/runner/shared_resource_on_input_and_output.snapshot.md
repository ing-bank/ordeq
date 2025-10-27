## Resource

```python
from tempfile import NamedTemporaryFile

from ordeq import run, node, IO
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, eq=False)
class File(IO[str]):
    path: Path

    def load(self) -> str:
        return self.path.read_text()

    def save(self, data: str) -> None:
        with self.path.open(mode='wt') as file:
            file.write(data)

    def __resources__(self) -> list[str]:
        return [self.path.__fspath__()]

    def __repr__(self):
        # To clean the output
        return "File"


with NamedTemporaryFile(delete=False, mode='wt') as tmp:
    tmp.write("Hello, world!")
    tmp.flush()

    path = Path(tmp.name)
    first_file = File(path=path)
    second_file = File(path=path)


    @node(inputs=first_file, outputs=second_file)
    def reverse(value: str) -> str:
        return ''.join(reversed(value))


    run(reverse)
    # This is allowed: one node can read and write the same resource.
    print(second_file.load())

```

## Exception

```text
CycleError: ('nodes are in a cycle', [Node(name=shared_resource_on_input_and_output:reverse, inputs=[File], outputs=[File]), Node(name=shared_resource_on_input_and_output:reverse, inputs=[File], outputs=[File])])
```