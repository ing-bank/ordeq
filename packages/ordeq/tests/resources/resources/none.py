# Captures behaviour when setting None as resource
from pathlib import Path

from ordeq_files import CSV

csv = CSV(path=Path("my/path")) @ None
