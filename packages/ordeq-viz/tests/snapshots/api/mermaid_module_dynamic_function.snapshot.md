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
		L00@{shape: rect, label: "IO"}
	end

	example_3.func_defs:hello --> IO0
	example_3.func_defs:hello --> IO1

	example_3.func_defs:hello@{shape: rounded, label: "hello"}
	example_3.func_defs:hello@{shape: rounded, label: "hello"}
	IO0@{shape: rect, label: "&lt;anonymous&gt;"}
	IO1@{shape: rect, label: "&lt;anonymous&gt;"}

	class L0,example_3.func_defs:hello,example_3.func_defs:hello node
	class L00,IO0,IO1 io0
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

Hello, world!
Hello, world!

```

## Logging

```text
INFO	ordeq.runner	Running view "hello" in module "example_3.func_defs"
INFO	ordeq.runner	Running view "hello" in module "example_3.func_defs"

```