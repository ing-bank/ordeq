from pathlib import Path
from tempfile import NamedTemporaryFile

from example_project import inner
from ordeq_manifest import create_manifest_json

with NamedTemporaryFile() as file:
    path = Path(file.name)
    create_manifest_json(inner, output=path)
    print(path.read_text(encoding="utf8"))
