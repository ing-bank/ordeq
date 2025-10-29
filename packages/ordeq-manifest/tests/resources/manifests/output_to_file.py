from tempfile import NamedTemporaryFile

from ordeq_manifest import create_manifest_json
from project import inner
from pathlib import Path

with NamedTemporaryFile() as file:
    path = Path(file.name)
    create_manifest_json(inner, output=path)
    print('JSON:\n', path.read_text())
