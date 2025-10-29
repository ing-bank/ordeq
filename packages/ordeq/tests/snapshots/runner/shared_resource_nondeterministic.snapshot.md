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
    path = Path(tmp.name)
    first_file = File(path=path)
    second_file = File(path=path)

    @node(outputs=first_file)
    def first() -> str:
        return "1st"

    @node(outputs=second_file)
    def second() -> str:
        return "2nd"

    # This should not be allowed: both nodes write to the same resource.
    # Expecting an error message like:
    # Node 'first' and 'second' both output to the same resource '{path}'.
    run(first, second, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     shared_resource_nondeterministic:first -> []
     shared_resource_nondeterministic:second -> []
  Nodes:
     shared_resource_nondeterministic:first: Node(name=shared_resource_nondeterministic:first, outputs=[File])
     shared_resource_nondeterministic:second: Node(name=shared_resource_nondeterministic:second, outputs=[File])

```

## Logging

```text
INFO	ordeq.runner	Running node "second" in module "shared_resource_nondeterministic"
INFO	ordeq.io	Saving File
INFO	ordeq.runner	Running node "first" in module "shared_resource_nondeterministic"
INFO	ordeq.io	Saving File

```