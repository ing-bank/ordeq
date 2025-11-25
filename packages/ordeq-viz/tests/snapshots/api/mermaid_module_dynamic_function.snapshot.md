## Resource

```python
import tempfile
from pathlib import Path

import example_3.nodes
from ordeq import run

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    output_file = tmp_path / "output.mermaid"
    viz(example_3.nodes, fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    # we would prefer to see f1 and f2, but since they are dynamically created
    # with the same name, mermaid shows them both as "hello" for now.
    print(output_file_content)
    run(example_3.nodes)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		view_type@{shape: subroutine, label: "View"}
	end


	example_3.nodes:f1@{shape: subroutine, label: "f1"}
	example_3.nodes:f2@{shape: subroutine, label: "f2"}

	class node_type node
	class view_type,example_3.nodes:f1,example_3.nodes:f2 view
	classDef view fill:#00C853,color:#FFF

Hello, world!
Hello, world!

```

## Logging

```text
INFO	ordeq.runner	Running view 'f1' in module 'example_3.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID1)
INFO	ordeq.runner	Running view 'f2' in module 'example_3.nodes'
DEBUG	ordeq.io	Persisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID2)
DEBUG	ordeq.io	Unpersisting data for IO(id=ID1)

```