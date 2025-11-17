# Captures behaviour when one IO is added twice to the same resource
from pathlib import Path

from ordeq_files import CSV

resource = "resource!"
csv = CSV(path=Path("my/path")).with_resource(resource)
csv_twice = csv.with_resource(resource)
print(csv._resource)
print(csv_twice._resource)
assert csv is not csv_twice
