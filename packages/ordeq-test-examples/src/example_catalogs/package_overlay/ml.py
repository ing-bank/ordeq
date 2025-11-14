from pathlib import Path
from typing import Any

from ordeq import IO
from ordeq_files import JSON

model = IO[Any]()
predictions = JSON(path=Path("predictions-overlay.json"))
metrics = IO[Any]()
plot = IO[Any]()
