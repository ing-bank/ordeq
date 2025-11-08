# Captures basic behaviour of resources
from pathlib import Path

from ordeq import Resource
from ordeq._resource import get_resources
from ordeq_files import CSV, Text

resource = Resource()
csv = resource.add_io(CSV(path=Path("my/path")))
csv_text = resource.add_io(Text(path=Path("my/path")))
print(get_resources(csv))
print(get_resources(csv_text))
