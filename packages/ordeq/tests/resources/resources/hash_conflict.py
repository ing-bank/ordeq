from pathlib import Path

from ordeq_files import CSV, Text

io1 = CSV(path=Path("to.csv"))
resource = hash(io1)
io2 = Text(path=Path("to/other.txt")) @ resource

print(io1._resource)
print(io2._resource)  # expect different resource
