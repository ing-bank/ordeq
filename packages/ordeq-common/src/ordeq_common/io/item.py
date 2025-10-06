from typing import Any

from ordeq import Input

_MISSING = object()


class Item(Input[Any]):
    """IO for extracting a value from a (possibly nested) dictionary.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_common import Item
    >>> from ordeq_toml import TOML
    >>> item = Item(TOML(path=Path("pyproject.toml")), key=("tool", "my_tool"))
    >>> item.load()  # doctest: +SKIP

    ```

    """

    def __init__(
        self,
        io: Input[dict[str, Any]],
        /,
        *,
        key: tuple[str, ...],
        default: Any = _MISSING,
    ):
        super().__init__()
        self.io = io
        self.key = key
        self.default = default

    def load(self) -> Any:
        """Load the value from the nested dictionary using the specified key.

        Returns:
            The value corresponding to the specified key path.

        """  # noqa: DOC501
        data = self.io.load()
        try:
            for k in self.key:
                data = data[k]
            return data
        except KeyError:
            if self.default is not _MISSING:
                return self.default
            raise
