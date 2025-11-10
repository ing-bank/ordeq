# Shows potential options to sugarcoat the syntax that adds an IO to a resource.
from pathlib import Path

from ordeq_files import CSV, Text

resource = 1234
csv = CSV(path=Path("my_path")) @ resource
csv_text = Text(path=Path("my_path")) @ resource
print(csv._resource)
print(csv_text._resource)
