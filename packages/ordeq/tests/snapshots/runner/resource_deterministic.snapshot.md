## Resource

```python
from dataclasses import dataclass
from pathlib import Path
from tempfile import NamedTemporaryFile

from ordeq import IO, node, run
from ordeq_common import Print


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
    path = Path(tmp.name)
    first_file = File(path=path) @ "path"
    second_file = File(path=path) @ "path"

    @node(outputs=first_file)
    def first() -> str:
        print("First node")
        return "Hello, world!"

    @node(inputs=second_file, outputs=Print())
    def second(value: str) -> str:
        print("Second node")
        return value

    # The run needs to recognize that 'first_file' and 'second_file'
    # share the same resource. It should plan first -> second.
    run(second, first, verbose=True)
    run(first, second, verbose=True)

```

## Output

```text
io-0 --> Node:__main__:second
Node:__main__:second --> io-1
Node:__main__:first --> io-2
First node
Second node

io-0 --> Node:__main__:second
Node:__main__:second --> io-1
Node:__main__:first --> io-2
First node
Second node
Hello, world!

```

## Logging

```text
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
DEBUG	ordeq.runner	Running File
INFO	ordeq.io	Loading File
DEBUG	ordeq.io	Persisting data for IO 'second:value' in module '__main__'
DEBUG	ordeq.runner	Running node 'first' in module '__main__'
INFO	ordeq.io	Saving File
DEBUG	ordeq.io	Persisting data for File
DEBUG	ordeq.io	Loading cached data for IO 'second:value' in module '__main__'
DEBUG	ordeq.runner	Running node 'second' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO 'second:value' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for File
DEBUG	ordeq.runner	Running File
INFO	ordeq.io	Loading File
DEBUG	ordeq.io	Persisting data for IO 'second:value' in module '__main__'
DEBUG	ordeq.runner	Running node 'first' in module '__main__'
INFO	ordeq.io	Saving File
DEBUG	ordeq.io	Persisting data for File
DEBUG	ordeq.io	Loading cached data for IO 'second:value' in module '__main__'
DEBUG	ordeq.runner	Running node 'second' in module '__main__'
INFO	ordeq.io	Saving Print()
DEBUG	ordeq.io	Unpersisting data for IO 'second:value' in module '__main__'
DEBUG	ordeq.io	Unpersisting data for File

```