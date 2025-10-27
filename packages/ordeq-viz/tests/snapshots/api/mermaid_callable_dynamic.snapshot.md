## Resource

```python
import tempfile
from pathlib import Path

import example3.nodes  # ty: ignore[unresolved-import]

from ordeq_viz import viz

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = Path(tmpdirname)
    output_file = tmp_path / "output.mermaid"
    viz(
        example3.nodes.f1, example3.nodes.f2, fmt="mermaid", output=output_file
    )
    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    # we would prefer to see f1 and f2, but since they are dynamically created
    # with the same name, mermaid shows them both as "hello" for now.
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
			L00[("IO")]:::io0
		end
	end

	example3.func_defs.hello --> IO0

	subgraph pipeline["Pipeline"]
		direction TB
		example3.func_defs.hello(["hello"]):::node
		IO0[("&lt;anonymous&gt;")]:::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5


```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 

```

## Typing

```text
packages/ordeq-viz/tests/resources/api/mermaid_callable_dynamic.py:4: error: Skipping analyzing "example3.nodes": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/api/mermaid_callable_dynamic.py:4: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
packages/ordeq-viz/tests/resources/api/mermaid_callable_dynamic.py:4: error: Skipping analyzing "example3": module is installed, but missing library stubs or py.typed marker  [import-untyped]
Found 2 errors in 1 file (checked 1 source file)

```