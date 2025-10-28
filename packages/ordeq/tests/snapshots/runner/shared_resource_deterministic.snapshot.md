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

    def __repr__(self):
        # To clean the output
        return "File"


with NamedTemporaryFile(delete=False, mode='wt') as tmp:
    path = Path(tmp.name)
    first_file = File(path=path)
    second_file = File(path=path)


    @node(outputs=first_file)
    def first() -> str:
        return "Hello, world!"


    @node(inputs=second_file)
    def second(value: str) -> None:
        print(value)


    # The run needs to recognize that 'first_file' and 'second_file'
    # share the same resource. It should plan first -> second.
    run(second, first, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     shared_resource_deterministic:first -> []
     shared_resource_deterministic:second -> []
  Nodes:
     shared_resource_deterministic:first: Node(name=shared_resource_deterministic:first, outputs=[File])
     shared_resource_deterministic:second: View(name=shared_resource_deterministic:second, inputs=[File])


```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'shared_resource_deterministic:second'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running view "second" in module "shared_resource_deterministic"
INFO	ordeq.runner	Running node "first" in module "shared_resource_deterministic"
INFO	ordeq.io	Saving File

```