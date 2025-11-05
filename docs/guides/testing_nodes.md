# Testing nodes

This guide outlines different strategies for testing nodes and pipelines.
Testing an Ordeq project is easy and requires minimal setup.
Because nodes behave like plain Python functions, they can be tested using any Python testing framework.

## Testing a single node

Let's start by reconsidering the `greet` node from the [node concepts section][concepts-node]:

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

Next, let's create some unit test for this node.
We will use [`pytest`][pytest] to test our project, but the principles also apply to other testing framework like
`unittest`.
First, we will create a `tests` package and a test module `test_pipeline.py`.
This module contains the unit tests for our node:

```python title="tests/test_pipeline.py"
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

Unit-testing the node like can be done in the same way as unit-testing any Python method.
Calling the node doesn't incur any overhead compared to a regular method.
It does not load or save IOs, and does not call hooks.
This is a good practice for unit tests, as it keeps them fast and isolated.

### Running a node in tests

Alternatively, you can test nodes by running them.
This will load the data from the node inputs, and save the returned data to the node outputs.
It will also invoke [hooks][concepts-hooks] that are set on the IO or runner.

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

In contrast to the tests above, this test does depend on the content of the CSV file used as input to `greet`.

### Running with different IO

Many times we do not want to connect to a real file system or database when testing.
This can be because connecting to the real data is slow, or because we do not want the tests to change the actual data.
Instead, we want to test the logic with some seed data, often stored locally.

For example, suppose reading from `greetings` is very expensive, because it is a large file.
We can then use a local file, with the same structure, to test the node.
To run the node with different IO, simply set the `io` argument of the runner:

```python title="tests/test_pipeline.py"
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

When `greet` is run, Ordeq will use the `local_names` and `local_greetings` IOs as replacements of the `names` and
`greetings` defined in the catalog.

!!!info "More on running nodes"
    Running a node from a test works exactly the same as running the node from a production system.
    This improves testability of your project.
    To learn more about how to configure the run of your nodes, for instance how to set alternative hooks during testing, please refer to the [guide][run-and-viz].

### Running with a different catalog

Another way to test your node using alternative data is by running it with a dedicated test [catalog][concepts-catalog].
The catalog can be defined in the source folder, as explained in [the guide][concepts-catalog], or in a separate package.
Here is a simple overview of your test package with a test catalog:

=== "tests/test_catalog.py"

    from pathlib import Path

    from ordeq_files import CSV, Text

    TEST_RESOURCES_DIR = Path(__file__).resolve().parent.parent / "tests-resources"
    names = CSV(path=TEST_RESOURCES_DIR / "test-names.csv")
    greetings = Text(path=TEST_RESOURCES_DIR / "test-greetings.txt")

=== "tests/test_pipeline.py"

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
The test catalog module is imported in the tests, and passed to the runner.
Because `starter_testing.catalog` is mapped to `test_catalog`, Ordeq will replace all entries of the source catalog with those of test catalog.

## Testing more nodes

So far we have covered examples on how to test a single node.
A next step in testing your project would be to test your node in integration with other nodes.
For instance, you might want to run an entire (sub)pipeline and verify the outputs.
To do this, we will again leverage the runner.

Let's take a RAG pipeline as an example.
The RAG pipeline consists of 6 nodes and defines a catalog for the IOs.
The source code for this project can be found [here][rag-pipeline].
Here is a complete example of testing the entire RAG pipeline:

=== "tests/test_pipeline.py"
    ```python
    from rag_pipeline import rag, catalog
    import test_catalog

    def test_pipeline():
        run(rag, io={catalog: test_catalog})
        # do your assertions ...
    ```

=== "tests/test_catalog.py"
    ```python
    from pathlib import Path
    from typing import Any

    from ordeq import IO
    from ordeq_faiss import FaissIndex
    from ordeq_files import Pickle
    from ordeq_pandas import PandasExcel
    from ordeq_pymupdf import PymupdfFile
    from ordeq_sentence_transformers import SentenceTransformer

    policies = PandasExcel(path=Path("policies.xlsx"))
    llm_model = SentenceTransformer(model="llm-model")
    llm_vision_retrieval_model = SentenceTransformer(model="vision-model")
    pdf_documents = PymupdfFile(path=Path("file1.pdf"))
    retrieved_pages = IO[Any]()
    relevant_pages = IO[Any]()
    index = FaissIndex(path=Path("documents.index"))
    questions = IO[Any]()
    metrics = Pickle[Any](path=Path("metrics.pkl"))
    pdfs_documents_annotated = PymupdfFile(path=Path("file1_annotated.pdf"))
    llm_answers = IO[Any]()
    ```

Because `run` runs the (sub)pipeline under test in exactly the same way as it would in a production setting, you can test the actual pipeline behaviour.
For more information on how to set up the run, please see the [guide][run-and-viz] or check out the [API reference][run-api].

[concepts-catalog]: ../getting-started/concepts/catalogs.md

[concepts-hooks]: ../getting-started/concepts/hooks.md

[concepts-node]: ../getting-started/concepts/nodes.md

[pytest]: https://docs.pytest.org/en/stable/

[run-and-viz]: ./run_and_viz.md

[run-api]: ../api/ordeq/_runner.md

[rag-pipeline]: https://github.com/ing-bank/ordeq/tree/main/examples/rag-pipeline-scaffold
