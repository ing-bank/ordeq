import tempfile
from pathlib import Path

import example_1.nodes
import example_2.nodes

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    temp_dir = Path(tmpdirname)
    output_file = temp_dir / "output.mermaid"
    viz(
        example_1.nodes.world,
        example_2.nodes.transform_input_2,
        fmt="mermaid",
        output=output_file,
    )
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    print(output_file_content)
