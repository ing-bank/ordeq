import sys
from dataclasses import dataclass
from typing import Any

import tomli_w
from ordeq import Input, Output
from ordeq._io import _IOMeta  # noqa: PLC2701
from ordeq.types import PathLike

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib  # ty: ignore[unresolved-import]


@dataclass(frozen=True, kw_only=True)
class TOMLInput(Input[dict[str, Any]]):
    """IO class for reading TOML files.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_toml import TOMLInput
    >>> toml_path = Path("config.toml")
    >>> io = TOMLInput(path=toml_path)
    >>> io.load()  # doctest: +SKIP

    ```
    """

    path: PathLike

    def load(self, **load_options: Any) -> dict[str, Any]:
        """Load and parse the TOML file specified by the path attribute.

        Args:
            **load_options: Additional options to pass to the TOML loader.

        Returns:
            A dictionary representing the contents of the TOML file.
        """
        with self.path.open("rb") as file:
            return tomllib.load(file, **load_options)


@dataclass(frozen=True, kw_only=True)
class TOML(TOMLInput, Output[dict[str, Any]], metaclass=_IOMeta):
    """IO class for reading and writing TOML files.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_toml import TOML
    >>> toml_path = Path("config.toml")
    >>> io = TOML(path=toml_path)
    >>> data = {"key": "value", "number": 42}
    >>> io.save(data)  # doctest: +SKIP

    ```
    """

    path: PathLike

    def load(self, **load_options: Any) -> dict[str, Any]:
        """Load and parse the TOML file specified by the path attribute.

        Args:
            **load_options: Additional options to pass to the TOML loader.

        Returns:
            A dictionary representing the contents of the TOML file.
        """
        with self.path.open("rb") as file:
            return tomllib.load(file, **load_options)

    def save(self, data: dict[str, Any], **save_options: Any) -> None:
        """Serialize the given data to a TOML file at the path attribute.

        Args:
            data: A dictionary to be serialized and saved as a TOML file.
            **save_options: Additional options to pass to the TOML dumper.
        """
        with self.path.open("wb") as file:
            tomli_w.dump(data, file, **save_options)
