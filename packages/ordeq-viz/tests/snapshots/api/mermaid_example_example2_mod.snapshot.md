## Resource

```python
import tempfile
from pathlib import Path

import example.nodes  # ty: ignore[unresolved-import]
import example2.nodes  # ty: ignore[unresolved-import]

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    temp_dir = Path(tmpdirname)
    output_file = temp_dir / "output.mermaid"
    viz(example.nodes, example2.nodes, fmt="mermaid", output=output_file)
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    print(output_file_content)

```

## Output

```text
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph Objects
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph IO Types
			L00[("Input")]:::io0
			L01[("Output")]:::io1
			L02[("StringBuffer")]:::io2
		end
	end

	IO0 --> transform_input_2
	transform_input_2 --> IO1
	IO2 --> world
	world --> IO3

	subgraph pipeline["Pipeline"]
		direction TB
		transform_input_2(["transform_input_2"]):::node
		world(["world"]):::node
		IO0[("TestInput2")]:::io0
		IO1[("TestOutput2")]:::io1
		IO2[("x")]:::io2
		IO3[("y")]:::io2
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb


```

## Typing

```text
packages/ordeq-viz/tests/resources/api/mermaid_example_example2_mod.py:4: error: Skipping analyzing "example.nodes": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/api/mermaid_example_example2_mod.py:4: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
packages/ordeq-viz/tests/resources/api/mermaid_example_example2_mod.py:4: error: Skipping analyzing "example": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/api/mermaid_example_example2_mod.py:5: error: Skipping analyzing "example2.nodes": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/api/mermaid_example_example2_mod.py:5: error: Skipping analyzing "example2": module is installed, but missing library stubs or py.typed marker  [import-untyped]
Found 4 errors in 1 file (checked 1 source file)

```