## Resource

```python
import tempfile
from collections.abc import Generator
from pathlib import Path

from ordeq import node, run
from ordeq_files import TextLinesStream

example_file_path = Path(
    "/var/folders/cf/zpng87w50mz4ty3cy8xrm3hm0000gp/T/example.txt"
)
example_line_stream = (
    TextLinesStream(path=example_file_path)
    .with_save_options(mode="w")
    .with_load_options(mode="r")
)


@node(outputs=[example_line_stream])
def write_to_line_stream() -> Generator[str]:
    print("Writing to example line stream...")
    yield "First line/n"
    yield "Second line/n"
    yield "Third line/n"


@node(inputs=[example_line_stream])
def show_lines(file_lines: Generator[str]) -> None:
    for line in file_lines:
        print(line.strip())


@node(inputs=[example_line_stream])
def count_lines(file_lines: Generator[str]) -> None:
    print(f"Total lines: {len(list(file_lines))}")


run(write_to_line_stream, show_lines, count_lines)

```

## Output

```text
Writing to example line stream...
First line
Second line
Third line
Total lines: 3

```

## Logging

```text
WARNING	ordeq_files.text_lines_stream	TextLinesStream is in pre-release, functionality may break in future releases 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'comsume_line_stream:show_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node 'comsume_line_stream:count_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "write_to_line_stream" in module "comsume_line_stream"
INFO	ordeq.io	Saving TextLinesStream(path=Path('/var/folders/cf/zpng87w50mz4ty3cy8xrm3hm0000gp/T/example.txt'))
INFO	ordeq.io	Loading TextLinesStream(path=Path('/var/folders/cf/zpng87w50mz4ty3cy8xrm3hm0000gp/T/example.txt'))
INFO	ordeq.runner	Running view "show_lines" in module "comsume_line_stream"
INFO	ordeq.io	Loading TextLinesStream(path=Path('/var/folders/cf/zpng87w50mz4ty3cy8xrm3hm0000gp/T/example.txt'))
INFO	ordeq.runner	Running view "count_lines" in module "comsume_line_stream"

```