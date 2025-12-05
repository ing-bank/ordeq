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
    viz(example_1.nodes, example_2.nodes, fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    print(output_file_content)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "Input"}
		io_type_1@{shape: rect, label: "Output"}
		io_type_2@{shape: rect, label: "StringBuffer"}
	end

	example_2.nodes:TestInput2 --> example_2.nodes:transform_input_2
	example_2.nodes:transform_input_2 --> example_2.nodes:TestOutput2
	example_1.nodes:x --> example_1.nodes:world
	example_1.nodes:world --> example_1.nodes:y

	example_2.nodes:transform_input_2@{shape: rounded, label: "transform_input_2"}
	example_1.nodes:world@{shape: rounded, label: "world"}
	example_1.nodes:x@{shape: rect, label: "x"}
	example_1.nodes:y@{shape: rect, label: "y"}
	example_2.nodes:TestInput2@{shape: rect, label: "TestInput2"}
	example_2.nodes:TestOutput2@{shape: rect, label: "TestOutput2"}

	class node_type,example_2.nodes:transform_input_2,example_1.nodes:world node
	class io_type_0,example_2.nodes:TestInput2 io0
	class io_type_1,example_2.nodes:TestOutput2 io1
	class io_type_2,example_1.nodes:x,example_1.nodes:y io2
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb


```