from collections.abc import Generator
from pathlib import Path
from tempfile import gettempdir

from ordeq import node, run
from ordeq_files import TextLinesStream

example_file_path = Path(gettempdir()) / "consume_line_stream.txt"
example_line_stream = TextLinesStream(path=example_file_path)


@node(outputs=[example_line_stream])
def write_to_line_stream() -> Generator[str]:
    print("Writing to example line stream...")
    yield "First line"
    yield "Second line"
    yield "Third line"


@node(inputs=[example_line_stream])
def show_lines(file_lines: Generator[str]) -> None:
    for line in file_lines:
        print(line.strip())


@node(inputs=[example_line_stream])
def count_lines(file_lines: Generator[str]) -> None:
    print(f"Total lines: {len(list(file_lines))}")


run(write_to_line_stream, show_lines, count_lines)

example_file_path.unlink(missing_ok=True)
