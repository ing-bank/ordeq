from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import DataclassInstance
from dataclasses import dataclass

from ordeq import IO, Input


@dataclass(frozen=True)
class Dataclass(Input["DataclassInstance"]):
    """IO that parses data as Python dataclass on load.

    Example:

    ```pycon
    >>> from ordeq_common import Dataclass
    >>> from ordeq_files import JSON
    >>> from pathlib import Path
    >>> ValidJSON = JSON(path=Path("to/valid.json"))
    >>> ValidJSON.load()  # doctest: +SKIP
    {"name": "banana", "colour": "yellow"}

    >>> @dataclass
    ... class Fruit:
    ...     name: str
    ...     colour: str
    >>> Dataclass(ValidJSON, Fruit).load()  # doctest: +SKIP
    Fruit(name="banana", colour="yellow")

    >>> InvalidJSON = JSON(path=Path("to/invalid.json"))
    >>> InvalidJSON.load()  # doctest: +SKIP
    {"name": "banana", "weight_gr": "100"}
    >>> Dataclass(InvalidJSON, Fruit).load()  # doctest: +SKIP
    TypeError: Fruit.__init__() got an unexpected keyword argument 'weight_gr'
    ```

    For nested models, or other more sophisticated parsing requirements
    consider using `ordeq-pydantic` instead.

    """

    io: IO[dict]
    dataclass: type[DataclassInstance]

    def load(self) -> DataclassInstance:
        data = self.io.load()
        # noinspection PyArgumentList
        return self.dataclass(**data)
