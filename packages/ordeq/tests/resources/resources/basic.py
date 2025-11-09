# Captures basic behaviour of resources
from pathlib import Path

from ordeq_files import CSV, Text

resource = 0.1244
csv = CSV(path=Path("my/path")).with_resource(resource)
csv_text = Text(path=Path("my/path")).with_resource(resource)
print(csv.resources)
print(csv_text.resources)
