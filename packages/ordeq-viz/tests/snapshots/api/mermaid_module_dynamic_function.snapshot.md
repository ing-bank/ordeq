## Resource

```python
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
		end
	end


	subgraph pipeline["Pipeline"]
		direction TB
		example3.nodes:<anonymous0>[("&lt;anonymous0&gt;")]:::io0
		example3.nodes:<anonymous1>[("&lt;anonymous1&gt;")]:::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5

Hello, world!
Hello, world!
{View(name=example3.func_defs:hello): None, View(name=example3.func_defs:hello): None}

```

## Logging

```text
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'example3.func_defs:hello'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running view "f2" in module "example3.nodes"
INFO	ordeq.runner	Running view "f1" in module "example3.nodes"

```

## Typing

```text
packages/ordeq-viz/tests/resources/api/mermaid_module_dynamic_function.py:4: error: Skipping analyzing "example3.nodes": module is installed, but missing library stubs or py.typed marker  [import-untyped]
packages/ordeq-viz/tests/resources/api/mermaid_module_dynamic_function.py:4: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
packages/ordeq-viz/tests/resources/api/mermaid_module_dynamic_function.py:4: error: Skipping analyzing "example3": module is installed, but missing library stubs or py.typed marker  [import-untyped]
Found 2 errors in 1 file (checked 1 source file)

```