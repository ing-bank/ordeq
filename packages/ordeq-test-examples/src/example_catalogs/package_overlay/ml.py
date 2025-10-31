from ordeq import IO
from typing import Any
from ordeq_files import JSON
from pathlib import Path

model = IO[Any]()
predictions = JSON(path=Path("predictions.json"))
metrics = IO[Any]()
plot = IO[Any]()
