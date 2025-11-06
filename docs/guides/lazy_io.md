# Lazily dataset processing

Loading multiple files in memory for processing at the same time can be problematic.
When processing batches of files, such as partitioned parquet files in Polars
or a directory of PDF files, we may run out of memory, and generally consume more resources than required.

The [`Iterate`](../api/ordeq_common/io/iterate.md) dataset can help executing the same logic to multiple datasets,
without the need to load them all in memory first.

Instead, `Iterate` makes use of Python generators to process the datasets one by one.

```python
from collections.abc import Iterable
from pathlib import Path

from ordeq import node
from ordeq_common import Iterate
from ordeq_files import JSON, Text

paths = [Path("hello.txt"), Path("world.txt")]
text_dataset = Iterate(*(Text(path=path) for path in paths))
json_dataset = Iterate(
    *(JSON(path=path.with_suffix(".json")) for path in paths)
)


@node(inputs=text_dataset, outputs=json_dataset)
def generate_json_contents(
    contents: Iterable[str],
) -> Iterable[dict[str, str]]:
    """Wrap the text-contents in a JSON structure."""
    for content in contents:
        yield {"content": content}
```

The [`TextLinesStream`](../api/ordeq_files/text_lines_stream.md) dataset from `ordeq-files` also supports lazy processing of text files line-by-line using a generator. This is particularly useful for processing large text files that may not fit into memory all at once.

It can also be used to write lines to a text file in a memory-efficient manner.

```python
from collections.abc import Generator
from pathlib import Path

from ordeq import node
from ordeq_files import TextLinesStream

example_file_path = Path("example.txt")
example_line_stream = TextLinesStream(path=example_file_path)

@node(outputs=[example_line_stream])
def write_to_line_stream() -> Generator[str]:
    yield "First line"
    yield "Second line"
    yield "Third line"


@node(inputs=[example_line_stream])
def show_lines(file_lines: Generator[str]) -> None:
    for line in file_lines:
        print(line)
```
