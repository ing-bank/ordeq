## Resource

```python
from collections.abc import Generator
from pathlib import Path
from tempfile import gettempdir

from ordeq import node, run
from ordeq_files import TextLinesStream

example_file_path = Path(gettempdir()) / "with_end_save_option.txt"
example_line_stream = TextLinesStream(
    path=example_file_path
).with_save_options(end="")


@node(outputs=[example_line_stream])
def write_to_line_stream() -> Generator[str]:
    print("Writing to example line stream...")
    yield "First line"
    yield " Continues here/n"
    yield "Second line"


@node(inputs=[example_line_stream])
def show_lines(file_lines: Generator[str]) -> None:
    for line in file_lines:
        print(line.strip())


@node(inputs=[example_line_stream])
def count_lines(file_lines: Generator[str]) -> None:
    print(f"Total lines: {len(list(file_lines))}")


run(write_to_line_stream, show_lines, count_lines)

example_file_path.unlink(missing_ok=True)

```

## Output

```text
Writing to example line stream...
Total lines: 2
First line Continues here
Second line

```

## Logging

```text
WARNING	ordeq_files.text_lines_stream	TextLinesStream is in pre-release, functionality may break in future releases without it being considered a breaking change.
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:show_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
WARNING	ordeq.nodes	Creating a view, as no outputs were provided for node '__main__:count_lines'. Views are in pre-release, functionality may break without notice. Use @node(outputs=...) to create a regular node. 
INFO	ordeq.runner	Running node "write_to_line_stream" in module "__main__"
INFO	ordeq.io	Saving TextLinesStream(path=Path('<TEMP_DIR>/with_end_save_option.txt'))
INFO	ordeq.io	Loading TextLinesStream(path=Path('<TEMP_DIR>/with_end_save_option.txt'))
INFO	ordeq.runner	Running view "count_lines" in module "__main__"
INFO	ordeq.io	Loading TextLinesStream(path=Path('<TEMP_DIR>/with_end_save_option.txt'))
INFO	ordeq.runner	Running view "show_lines" in module "__main__"

```