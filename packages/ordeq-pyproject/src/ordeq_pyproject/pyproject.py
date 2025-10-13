from dataclasses import dataclass
from typing import Any

from ordeq_toml import TOMLInput


@dataclass(frozen=True, kw_only=True)
class Pyproject(TOMLInput):
    """IO for loading a pyproject.toml section.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_pyproject import Pyproject
    >>> pyproject = Pyproject(
    ...     path=Path("pyproject.toml"), section="tool.my_tool"
    ... )
    >>> data = pyproject.load() # doctest: +SKIP

    ```
    """

    section: str

    def load(self, **load_options: Any) -> Any:
        """Load the specified section from the pyproject.toml file.

        Args:
            **load_options: Additional options to pass to the TOML loader.

        Returns:
            A dictionary representing the contents of the specified section
                in the pyproject.toml file.
        """
        data = super().load(**load_options)
        section_keys = self.section.split(".")
        for key in section_keys:
            data = data[key]
        return data
