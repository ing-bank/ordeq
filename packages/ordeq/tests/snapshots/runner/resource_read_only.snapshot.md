## Resource

```python
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile

from ordeq import IO, node, run


@dataclass(frozen=True, eq=False)
class File(IO[str]):
    path: Path

    def load(self) -> str:
        return self.path.read_text()

    def save(self, data: str) -> None:
        with self.path.open(mode="wt") as file:
            file.write(data)

    def __repr__(self):
        # To clean the output
        return "File"


with NamedTemporaryFile(delete=False, mode="wt", encoding="utf8") as tmp:
    tmp.write("Helloooo")
    tmp.flush()

    path = Path(tmp.name)
    first_file = File(path=path) @ "path"
    second_file = File(path=path) @ "path"

    @node(inputs=first_file)
    def first(value: str) -> None:
        print("1st node:", value)

    @node(inputs=second_file)
    def second(value: str) -> None:
        print("2nd node:", value)

    # This should not raise an error
    # The run can schedule 'first' and 'second' in any order,
    # since both only read from the shared resource.
    # The graph is still deterministic.
    run(first, second, verbose=True)
    run(second, first, verbose=True)

```

## Output

```text
io-0 --> View:__main__:second
io-1 --> View:__main__:first
View:__main__:second --> io-2
View:__main__:first --> io-3
1st node: Helloooo
2nd node: Helloooo
io-0 --> View:__main__:first
io-1 --> View:__main__:second
View:__main__:first --> io-2
View:__main__:second --> io-3
2nd node: Helloooo
1st node: Helloooo

```

## Logging

```text
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running view "first" in module "__main__"
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running view "second" in module "__main__"
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running view "second" in module "__main__"
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running view "first" in module "__main__"

```