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
    tmp.write("Hello, world!")
    tmp.flush()

    path = Path(tmp.name)
    first_file = File(path=path)
    second_file = File(path=path)

    @node(inputs=first_file, outputs=second_file)
    def reverse(value: str) -> str:
        return "".join(reversed(value))

    run(reverse)
    # This is allowed: one node can read and write the same resource.
    print(second_file.load())
