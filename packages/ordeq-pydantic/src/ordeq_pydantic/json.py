from dataclasses import dataclass
from pathlib import Path

import pydantic
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class PydanticJSON(IO[pydantic.BaseModel]):
    """IO to load and save Pydantic models to JSON

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_pydantic import PydanticJSON
    >>> from pydantic import BaseModel

    >>> class MyModel(BaseModel):
    ...     hello: str
    ...     world: str

    >>> dataset = PydanticJSON(
    ...     path=Path("path/to.json"),
    ...     model_type=MyModel
    ... )

    ```

    """

    path: Path
    model_type: type[pydantic.BaseModel]

    def load(self) -> pydantic.BaseModel:
        """Load the Pydantic model from the JSON file.

        Returns:
            The loaded Pydantic model.
        """
        data = self.path.read_text()
        return self.model_type.model_validate_json(data)

    def save(self, model: pydantic.BaseModel) -> None:
        """Save the Pydantic model to a JSON file.

        Args:
            model: The Pydantic model to save.

        """
        data = model.model_dump_json()
        self.path.write_text(data)
