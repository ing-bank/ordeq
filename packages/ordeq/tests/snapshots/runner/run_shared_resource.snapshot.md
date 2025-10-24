## Resource:
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
    # share the same resource.
    # It should plan first -> second.
    run(second, first, verbose=True)

```

## Output:
```text
NodeGraph:
  Edges:
     run_shared_resource:first -> []
     run_shared_resource:second -> []
  Nodes:
     Node(name=run_shared_resource:first, outputs=[File])
     Node(name=run_shared_resource:second, inputs=[File])


```

## Logging:
```text
INFO	ordeq.io	Loading File
INFO	ordeq.runner	Running node Node(name=run_shared_resource:second, inputs=[File])
INFO	ordeq.runner	Running node Node(name=run_shared_resource:first, outputs=[File])
INFO	ordeq.io	Saving File

```