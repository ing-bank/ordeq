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
		L0@{shape: rounded, label: "Node"}
		L2@{shape: subroutine, label: "View"}
	end


	example_3.func_defs:hello@{shape: subroutine, label: "hello"}
	example_3.func_defs:hello@{shape: subroutine, label: "hello"}

	class L0 node
	class L2,example_3.func_defs:hello,example_3.func_defs:hello view
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef view fill:#00C853,color:#FFF

Hello, world!
Hello, world!

```

## Logging

```text
INFO	ordeq.runner	Running view "hello" in module "example_3.func_defs"
INFO	ordeq.runner	Running view "hello" in module "example_3.func_defs"

```