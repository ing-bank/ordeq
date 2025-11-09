from pathlib import Path

from ordeq import node
from ordeq_files import CSV, Text

path = Path("to.file")
csv_raw = CSV(path=path) @ path
csv_text = Text(path=path) @ path


@node(outputs=csv_raw)
def generate_raw():
    return


@node(outputs=csv_text)
def generate_text():
    return
