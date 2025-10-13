from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

import joblib
from ordeq import IO

T = TypeVar("T")


@dataclass(frozen=True, kw_only=True)
class Joblib(IO[T]):
    """IO for joblib objects.

    Example of stand-alone use:

    ```pycon
    >>> from ordeq_joblib import Joblib
    >>> from pathlib import Path
    >>> Model = Joblib(path=Path("model.pkl"))
    >>> model = Model.load()  # doctest: +SKIP
    >>> Model.save(model)  # doctest: +SKIP
    ```

    Example in a node:

    ```pycon
    >>> from ordeq_joblib import Joblib
    >>> from ordeq_pandas import PandasExcel
    >>> import pandas as pd
    >>> from pathlib import Path
    >>> from ordeq import node
    >>> @node(
    ...     inputs=[
    ...         Joblib(path=Path("model.pkl")),
    ...         PandasExcel(path=Path("iris.xlsx"))
    ...     ],
    ...     outputs=Joblib(path=Path("model-trained.pkl"))
    ... )
    ... def train(model, df):
    ...     X, y = df.drop('label'), df['label']
    ...     model.fit(X, y)
    ...     return model

    ```
    """

    path: Path

    def load(self, **load_options) -> T:
        return joblib.load(self.path, **load_options)

    def save(self, data: T, **save_options) -> None:
        joblib.dump(data, self.path, **save_options)
