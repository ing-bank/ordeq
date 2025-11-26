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
    first_file = File(path=path) @ "path"
    second_file = File(path=path) @ "path"

    @node(outputs=first_file)
    def first() -> str:
        return "1st"

    @node(outputs=second_file)
    def second() -> str:
        return "2nd"

    # This should raise an error: both nodes write to the same resource.
    run(first, second, verbose=True)

```

## Output

```text
ValueError: Nodes '__main__:second' and '__main__:first' both output to Resource(value='path'). Nodes cannot output to the same resource.
  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    raise ValueError(msg)

  File "/packages/ordeq/src/ordeq/_graph.py", line LINO, in from_nodes
    return cls.from_graph(NodeResourceGraph.from_nodes(nodes))
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^

  File "/packages/ordeq/src/ordeq/_runner.py", line LINO, in run
    graph = NodeGraph.from_nodes(nodes)

  File "/packages/ordeq/tests/resources/runner/resource_nondeterministic.py", line LINO, in <module>
    run(first, second, verbose=True)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

## Logging

```text
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.
WARNING	ordeq.preview	Resources are in preview mode and may change without notice in future releases.

```