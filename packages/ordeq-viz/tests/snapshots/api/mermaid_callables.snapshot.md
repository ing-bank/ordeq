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
TypeError: All vizzables must be modules or references to modules.
  File "/packages/ordeq-viz/src/ordeq_viz/api.py", line LINO, in viz
    raise TypeError(
        "All vizzables must be modules or references to modules."
    )

  File "/packages/ordeq-viz/tests/resources/api/mermaid_callables.py", line LINO, in <module>
    viz(
    ~~~^
        example_1.nodes.world,
        ^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
        output=output_file,
        ^^^^^^^^^^^^^^^^^^^
    )
    ^

  File "<frozen runpy>", line LINO, in _run_code

  File "<frozen runpy>", line LINO, in _run_module_code

  File "<frozen runpy>", line LINO, in run_path

  File "/packages/ordeq-test-utils/src/ordeq_test_utils/snapshot.py", line LINO, in run_module
    run_path(str(file_path), run_name="__main__")
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```