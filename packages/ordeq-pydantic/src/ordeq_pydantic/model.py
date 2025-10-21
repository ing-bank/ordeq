from dataclasses import dataclass
from typing import Any

import pydantic
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class PydanticModel(IO[pydantic.BaseModel]):
    """IO to load and save Pydantic models from/to any IO that handles
        dictionaries.

    Example usage:

    ```pycon
    >>> from pathlib import Path
    >>> from ordeq_pydantic import PydanticModel
    >>> from pydantic import BaseModel
    >>> from ordeq_yaml import YAML

    >>> class MyModel(BaseModel):
    ...     hello: str
    ...     world: str

    >>> dataset = PydanticModel(
    ...     io=YAML(path=Path("path/to.yaml")),
    ...     model_type=MyModel
    ... )

    ```

    Instead of using:

    ```python
    from pathlib import Path
    from ordeq_pydantic import PydanticModel
    from ordeq_json import JSON

    my_model = PydanticModel(io=JSON(path=Path(...)), model_type=MyModel)
    ```

    you can also use:

    ```python
    from pathlib import Path
    from ordeq_pydantic import PydanticJSON

    PydanticJSON(path=Path(...), model_type=MyModel)
    ```

    This uses the Pydantic JSON implementation which is more efficient for JSON
    files.

    """

    io: IO[dict[str, Any]]
    model_type: type[pydantic.BaseModel]

    def load(self, **load_options: Any) -> pydantic.BaseModel:
        """Load the Pydantic model from the underlying IO.

        Args:
            **load_options: Options to pass to the Pydantic model validation.

        Returns:
            The loaded Pydantic model.
        """
        data = self.io.load()
        return self.model_type.model_validate(data, **load_options)

    def save(self, model: pydantic.BaseModel, **save_options: Any) -> None:
        """Save the Pydantic model to the underlying IO.

        Args:
            model: The Pydantic model to save.
            **save_options: Options to pass to the Pydantic model dump.
        """
        data = model.model_dump(**save_options)
        self.io.save(data)
