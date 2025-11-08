# Shows potential options to sugarcoat the syntax that adds an IO to a resource.
from pathlib import Path

from ordeq import Resource
from ordeq._resource import get_resources
from ordeq_files import CSV, Text

resource = Resource()
csv_fd = resource // CSV(path=Path("my/path"))
csv_text_fd = resource // Text(path=Path("my/path"))
print(get_resources(csv_fd))
print(get_resources(csv_text_fd))

csv_rshift = resource >> CSV(path=Path("my/path"))
csv_text_rshift = resource >> Text(path=Path("my/path"))

csv_gt = resource > CSV(path=Path("my/path"))
csv_text_gt = resource > Text(path=Path("my/path"))

csv_or = resource | CSV(path=Path("my/path"))
csv_text_or = resource | Text(path=Path("my/path"))

csv_and = resource @ CSV(path=Path("my/path"))
csv_text_and = resource @ Text(path=Path("my/path"))
