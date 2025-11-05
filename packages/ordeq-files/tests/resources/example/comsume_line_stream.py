import tempfile
from collections.abc import Generator
from pathlib import Path

from ordeq import node, run
from ordeq_files import TextLinesStream

example_file_path = Path(tempfile.gettempdir()) / "example.txt"
example_line_stream = (
    TextLinesStream(path=example_file_path)
    .with_save_options(mode="w")
    .with_load_options(mode="r")
)


@node(outputs=[example_line_stream])
def write_to_line_stream() -> Generator[str]:
    print("Writing to example line stream...")
    yield "First line\n"
    yield "Second line\n"
    yield "Third line\n"


@node(inputs=[example_line_stream])
def show_lines(file_lines: Generator[str]) -> None:
    for line in file_lines:
        print(line.strip())


@node(inputs=[example_line_stream])
def count_lines(file_lines: Generator[str]) -> None:
    print(f"Total lines: {len(list(file_lines))}")


run(write_to_line_stream, show_lines, count_lines)
