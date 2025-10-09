from collections.abc import Generator
from dataclasses import dataclass

from ordeq import Input
from ordeq.types import GlobPath, PathLike


@dataclass(frozen=True, kw_only=True)
class Glob(Input[Generator[PathLike, None, None]]):
    """IO class that loads all paths provided a pattern.
    Although this class can be used as dataset in your nodes,
    for most cases it would be more suitable to inherit from
    this class and extend the `load` method, for example:

    ```pycon
    >>> class LoadPartitions(Glob):
    ...     def load(self):
    ...         paths = super().load()
    ...         for path in paths:
    ...             yield my_load_func(path)

    ```
    """

    path: GlobPath
    pattern: str

    def load(self) -> Generator[PathLike, None, None]:
        return self.path.glob(self.pattern)
