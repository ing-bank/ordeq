from pathlib import Path
from tempfile import NamedTemporaryFile

from ordeq_manifest import create_manifest_json
from project import inner

with NamedTemporaryFile() as file:
    path = Path(file.name)
    create_manifest_json(inner, output=path)
    print(path.read_text(encoding="utf8"))
