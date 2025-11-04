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
        return "Hello, world!"

    @node(inputs=second_file)
    def second(value: str) -> None:
        print(value)

    # The run needs to recognize that 'first_file' and 'second_file'
    # share the same resource. It should plan first -> second.
    run(second, first, verbose=True)

```

## Exception

```text
AttributeError: 'NoneType' object has no attribute 'items'
  File "/packages/ordeq/src/ordeq/_resolve.py", line LINO, in _resolve_strings_to_subs
    for old, new in subs.items():
                    ^^^^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    _resolve_strings_to_subs(io)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^

  File "/packages/ordeq/tests/resources/runner/shared_resource_deterministic.py", line LINO, in <module>
    run(second, first, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line LINO, in _call_with_frames_removed

  File "<frozen importlib._bootstrap_external>", line LINO, in exec_module

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^

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

```