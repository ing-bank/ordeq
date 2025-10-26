# Checks the behaviour when running an identity node with IO that has a
# read-write lock of some sorts. We expect this to raise an error when
# saving to the locked IO (not when building the graph).
from tempfile import NamedTemporaryFile

from ordeq import node, run, IO
from pathlib import Path


class File(IO):
    def __init__(self, p: Path):
        self.path = p
        super().__init__()

    def save(self, value: str) -> None:
        if self.lock:
            raise RuntimeError("Cannot write to a locked file.")
        self.path.write_text(value)

    def load(self) -> str:
        self.lock = True  # Simulate a read-write lock
        return self.path.read_text()


with NamedTemporaryFile(mode='wt') as tmp:
    path = Path(tmp.name)
    tmp.write("Hello, Ordeq!")
    tmp.flush()
    file = File(path)


    @node(inputs=file, outputs=file)
    def identity(value: str) -> str:
        return value


    run(identity, verbose=True)
