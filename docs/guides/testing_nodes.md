# Testing nodes

Because nodes behave like plain Python functions, they can be tested using any Python testing framework.
Let's reconsider the `greet` node from the [node concepts section][concepts-node]:

=== "nodes.py"

    ```python
    import catalog
    from ordeq import node


    @node(inputs=catalog.names, outputs=catalog.greetings)
    def greet(names: tuple[str, ...]) -> list[str]:
        """Returns a greeting for each person."""
        greetings = []
        for name in names:
            greetings.append(f"Hello, {name}!")
        return greetings
    ```

=== "catalog.py"

    ```python
    from pathlib import Path

    from ordeq_files import CSV, Text

    names = CSV(path=Path("names.csv"))
    greetings = Text(path=Path("greetings.txt"))
    ```

This node can be unit-tested as follows:

```python
from nodes import greet


def test_greet_empty():
    assert greet() == []


def test_greet_one_name():
    assert greet(["Alice"]) == ["Hello, Alice!"]


def test_greet_two_names():
    assert greet(["Alice", "Bob"]) == ["Hello, Alice!", "Hello, Bob!"]


def test_greet_special_chars():
    assert greet(["A$i%*c"]) == ["Hello, A$i%*c!"]
```

These tests only test the _transformations_.
They do not load or save any data, and do not use any hooks.
This is a good practice for unit tests, as it keeps them fast and isolated.

### Running nodes in tests

Alternatively, you can test nodes by running them.
This will load the data from the node inputs, and save the returned data to the node outputs:

```python
from catalog import greetings
from nodes import greet
from ordeq import run


def test_run_greet():
    run(greet)
    assert greetings.load() == [
        "Hello, Abraham!",
        "Hello, Adam!",
        "Hello, Azul!",
        ...,
    ]
```

In contrast to the unit tests, this test depends on the content of the CSV file used as input to `greet`.
As shown above, the result of `greet` can be retrieved by accessing the `result` dictionary with the `Output` of `greet` as the key:

### Running nodes with alternative IO

Many times we do not want to connect to a real file system or database when testing.
This can be because connecting to the real data is slow, or because we do not want the tests to change the actual data.
Instead, we want to test the logic with some seed data, often stored locally.

Suppose reading from `greetings` is very expensive, because it is a large file.
We can use a local file with the same structure to test the node:

```python
from pathlib import Path

from catalog import greetings, names
from nodes import greet
from ordeq import run
from ordeq_files import CSV, Text


def test_run_greet():
    local_names = CSV(path=Path("to/local/names.csv"))
    local_greetings = Text(path=Path("to/local/greetings.txt"))
    run(greet, io={names: local_names, greetings: local_greetings})
    assert local_greetings.load() == [
        "Hello, Abraham!",
        "Hello, Adam!",
        "Hello, Azul!",
        ...,
    ]
```

When `greet` is run, Ordeq will use the `local_names` and `local_greetings` IOs as replacements of the `names` and `greetings` defined in the catalog.

### IO fixtures

You can also use the `io` argument to `run` as a fixture in your tests.
This allows you to define the IOs once and reuse them multiple times.

```python
from pathlib import Path

import pytest
from catalog import greetings, names
from ordeq import IO, Input, Output
from ordeq_files import CSV, Text


@pytest.fixture(scope="session")
def io() -> dict[IO | Input | Output, IO | Input | Output]:
    """Mapping of node inputs and outputs to the inputs and outputs used throughout tests."""
    return {
        names: CSV(path=Path("to/local/names.csv")),
        greetings: Text(path=Path("to/local/greetings.txt")),
    }
```

Now we can use the `io` fixture in our tests:

```python
import catalog
from nodes import greet
from ordeq import run


def test_run_greet(io):
    run(greet, io=io)
    assert io[catalog.greetings].load() == [
        "Hello, Abraham!",
        "Hello, Adam!",
        "Hello, Azul!",
        ...,
    ]
```

For more information on the fixture scope, refer to the `pytest` [documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes).

[concepts-node]: ../getting-started/concepts/nodes.md
