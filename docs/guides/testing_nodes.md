# Testing nodes

This guide outlines different strategies for testing nodes and pipelines.
Testing an Ordeq project is easy and requires minimal setup.
Because nodes behave like plain Python functions, they can be tested using any Python testing framework.
Let's reconsider the `greet` node from the [node concepts section][concepts-node]:

=== "src/starter_testing/pipeline.py"

    ```python
    from collections.abc import Iterable

    from ordeq import node

    from starter_testing_nodes import catalog


    @node(inputs=catalog.names, outputs=catalog.greetings)
    def greet(rows: Iterable[tuple[str, ...]]) -> list[list[str]]:
        """Returns a greeting for each person."""
        return [[f"Hello, {row[0]}!"] for row in rows]
    ```

=== "src/starter_testing/catalog.py"

    ```python
    from pathlib import Path

    from ordeq_pandas import CSV, Text

    names = CSV(path=Path("names.csv"))
    greetings = Text(path=Path("greetings.txt"))
    ```

This node can be unit-tested as follows:

```python title="tests/unit_test_pipeline.py"
from starter_testing_nodes.pipeline import greet


def test_greet_empty():
    assert greet(()) == []


def test_greet_one_name():
    assert greet(("Alice",)) == ["Hello, Alice!"]


def test_greet_two_names():
    assert greet(("Alice",)("Bob", )) == ["Hello, Alice!", "Hello, Bob!"]


def test_greet_special_chars():
    assert greet(("A$i%*c",)) == ["Hello, A$i%*c!"]
```

These tests only test the _transformations_.
They do not load or save any data, and do not use any hooks.
This is a good practice for unit tests, as it keeps them fast and isolated.

### Running nodes in tests

Alternatively, you can test nodes by running them.
This will load the data from the node inputs, and save the returned data to the node outputs.
It will also invoke any [hooks][concepts-hooks] that are set on the IO or runner.

```python title="tests/test_pipeline_run.py"
from ordeq import run
from starter_testing_nodes.catalog import greetings
from starter_testing_nodes.pipeline import greet


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

### Running nodes with alternative IO

Many times we do not want to connect to a real file system or database when testing.
This can be because connecting to the real data is slow, or because we do not want the tests to change the actual data.
Instead, we want to test the logic with some seed data, often stored locally.

Suppose reading from `greetings` is very expensive, because it is a large file.
We can use a local file with the same structure to test the node:

```python title="test_pipeline_catalog.py"
from pathlib import Path

from starter_testing_nodes.catalog import greetings, names
from starter_testing_nodes.pipeline import greet
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

### Running with an alternative catalog

An alternative way to test your node using test data is by running it with a dedicated test [catalog][concepts-catalog].
The catalog can be defined in the source folder, as explained in [the guide][concepts-catalog], or in a separate package.
Here is a simple overview of your test package with a test catalog:

=== "tests/test_catalog.py"

    from pathlib import Path

    from ordeq_files import CSV, Text

    TEST_RESOURCES_DIR = Path(__file__).resolve().parent.parent / "tests-resources"
    names = CSV(path=TEST_RESOURCES_DIR / "test-names.csv")
    greetings = Text(path=TEST_RESOURCES_DIR / "test-greetings.txt")

=== "tests/test_pipeline_run.py"

    ```python title=
    import test_catalog
    import starter_testing
    from ordeq import run
    from starter_testing.pipeline import greet

    def test_run_greet_catalog():
        run(greet, io={starter_testing.catalog: test_catalog})
        assert test_catalog.greetings.load() == [
            "Hello, Abraham!",
            "Hello, Adam!",
            "Hello, Azul!",
            ...,
        ]
    ```

The test catalog defines the same entries as the source catalog, but points to different data.
In this case, the test data is stored in a `tests-resources` folder, but you can store it anywhere.
The test catalog is imported in the tests, and passed to the runner.
Because `starter_testing.catalog` is mapped to `test_catalog`, Ordeq will replace all entries of the source catalog with those of test catalog.

[concepts-catalog]: ../getting-started/concepts/catalogs.md
[concepts-hooks]: ../getting-started/concepts/hooks.md
[concepts-node]: ../getting-started/concepts/nodes.md
