import tempfile
from pathlib import Path
from ordeq import run
import example3.nodes  # ty: ignore[unresolved-import]

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    output_file = tmp_path / "output.mermaid"
    viz(example3.nodes, fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    # we would prefer to see f1 and f2, but since they are dynamically created
    # with the same name, mermaid shows them both as "hello" for now.
    print(output_file_content)
    print(run(example3.nodes))
