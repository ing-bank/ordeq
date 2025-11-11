## Resource

```python
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

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		L0@{shape: rounded, label: "Node"}
		L00@{shape: rect, label: "Input"}
		L01@{shape: rect, label: "Output"}
		L02@{shape: rect, label: "StringBuffer"}
	end

	IO0 --> example_1.nodes:world
	example_1.nodes:world --> IO1
	IO2 --> example_2.nodes:transform_input_2
	example_2.nodes:transform_input_2 --> IO3

	example_1.nodes:world@{shape: rounded, label: "world"}
	example_2.nodes:transform_input_2@{shape: rounded, label: "transform_input_2"}
	IO0@{shape: rect, label: "x"}
	IO1@{shape: rect, label: "y"}
	IO2@{shape: rect, label: "TestInput2"}
	IO3@{shape: rect, label: "TestOutput2"}

	class L0,example_1.nodes:world,example_2.nodes:transform_input_2 node
	class L00,IO2 io0
	class L01,IO3 io1
	class L02,IO0,IO1 io2
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B,color:#000
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb


```