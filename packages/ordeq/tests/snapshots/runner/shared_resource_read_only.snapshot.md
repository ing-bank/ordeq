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


    @node(inputs=first_file)
    def first(value: str) -> None:
        print(value)


    @node(inputs=second_file)
    def second(value: str) -> None:
        print(value)


    # The run can schedule 'first' and 'second' in any order,
    # since both only read from the shared resource.
    # (The graph is still deterministic.)
    run(first, second, verbose=True)

```

## Output

```text
NodeGraph:
  Edges:
     shared_resource_read_only:first -> []
     shared_resource_read_only:second -> []
  Nodes:
     shared_resource_read_only:first: View(name=shared_resource_read_only:first, inputs=[File])
     shared_resource_read_only:second: View(name=shared_resource_read_only:second, inputs=[File])



```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'shared_resource_read_only:first'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'shared_resource_read_only:second'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running view "second" in module "shared_resource_read_only"
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running view "first" in module "shared_resource_read_only"

```