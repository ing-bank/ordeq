from pathlib import Path

from ordeq import Resource
from ordeq._resource import get_resources
from ordeq_files import CSV

resource = Resource()
csv = resource.add_io(CSV(path=Path("my/path")))

csv_twice = resource.add_io(csv)
print(get_resources(csv))
