# Shows sugarcoated syntax to add a resource
from pathlib import Path

from ordeq._io import get_resource
from ordeq_files import CSV, Text

resource = 1234
csv = CSV(path=Path("my_path")) @ resource
csv_text = Text(path=Path("my_path")) @ resource
print(get_resource(csv))
print(get_resource(csv_text))
