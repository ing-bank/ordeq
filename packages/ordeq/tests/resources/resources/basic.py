# Captures basic behaviour of resources
from pathlib import Path

from ordeq._io import get_resource
from ordeq_files import CSV, Text

resource = 0.1244
csv = CSV(path=Path("my/path")).with_resource(resource)
csv_text = Text(path=Path("my/path")).with_resource(resource)
print(get_resource(csv))
print(get_resource(csv_text))
