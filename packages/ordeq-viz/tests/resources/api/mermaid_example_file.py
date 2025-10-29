import tempfile
from pathlib import Path

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    temp_dir = Path(tmpdirname)
    output_file = temp_dir / "output.mermaid"
    viz("example", fmt="mermaid", output=output_file)
    output_file_content = output_file.read_text("utf8")
    print(output_file_content)
