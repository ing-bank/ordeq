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
		subgraph objects["Objects"]
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph io_types["IO Types"]
			ordeq._io:IO[("IO")]:::io0
			ordeq._io:Input[("Input")]:::io1
			ordeq._io:Output[("Output")]:::io2
			ordeq_common.io.string_buffer:StringBuffer[("StringBuffer")]:::io3
		end
	end

	example.nodes:<anonymous0> --> example.nodes:node_with_inline_io
	example.nodes:node_with_inline_io --> example.nodes:<anonymous1>
	example.nodes:x --> example.nodes:world
	example.nodes:world --> example.nodes:y
	example2.nodes:TestInput2 --> example2.nodes:transform_input_2
	example2.nodes:transform_input_2 --> example2.nodes:TestOutput2

	subgraph pipeline["Pipeline"]
		direction TB
		example.nodes:node_with_inline_io(["node_with_inline_io"]):::node
		example.nodes:world(["world"]):::node
		example2.nodes:transform_input_2(["transform_input_2"]):::node
		example.nodes:x[("x")]:::io3
		example.nodes:y[("y")]:::io3
		example2.nodes:TestInput2[("TestInput2")]:::io1
		example2.nodes:TestOutput2[("TestOutput2")]:::io2
		example.nodes:<anonymous0>[("&lt;anonymous0&gt;")]:::io0
		example.nodes:<anonymous1>[("&lt;anonymous1&gt;")]:::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb
	classDef io3 fill:#e78ac3


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