# Starting a new project

This guide is meant to help users set up a new project with Ordeq.
It assumes you are familiar with Ordeq's [core concepts][core-concepts], such as IO and nodes.
We will discuss several common setups for projects that use Ordeq, and their pro's and cons.

We use uv for package and project management throughout this guide.
Check out the [uv documentation][uv] for installation and usage instructions.

## Single-file projects

Single-file projects are a great option if you want to run a quick test or experiment.
As the name implies, a single-file project contains only one Python module.

!!! tip "Using notebooks"

    For users interested in using Ordeq with notebooks, we will create a dedicated guide.

To create a single-file project, navigate to the desired project directory and run:

```bash
uv init
```

This will create the following project structure:

```text
project
├── README.md
├── main.py
└── pyproject.toml
```

The `README.md` contains documentation on the project, while the `pyproject.toml` defines the project's dependencies.

Next, install Ordeq from the PyPi registry:

```bash
uv add ordeq
```

This will add the `ordeq` package to the `pyproject.toml` , so that you can use Ordeq in your code.

!!! info "Running scripts with uv"

    uv also supports running scripts with without `pyproject.toml`.
    More info can be found [here][uv-scripts].

### Defining the pipeline

Now you can start editing `main.py` and create your pipeline.
The following example pipeline loads data from an API endpoint, parses it, and saves the result to a YAML:

!!! info "Install `ordeq-yaml` and `ordeq-requests`"

    To run the example below yourself, make sure to install `ordeq-yaml` and `ordeq-packages`.

```python title="project/main.py"
from ordeq import node, run
from ordeq_requests import ResponseJSON
from ordeq_yaml import YAML
from pathlib import Path

user = ResponseJSON(url="https://jsonplaceholder.typicode.com/users/1")
yaml = YAML(path=Path("users.yml"))


@node(inputs=user, outputs=yaml)
def parse_users(user: dict) -> dict:
    return {
        "id": user["id"],
        "address": f"{user["address"]["street"]} {user["address"]["zipcode"]}"
    }

if __name__ == "__main__":
    run(parse_users)
```

The nodes and IOs are defined in the same file, together with the run script.
When you're ready to run this pipeline, use:

```bash
uv run main.py
```

!!! tip "No need to activate the virtual environment"

    uv automatically activates the virtual environment when running commands like `uv run`.
    You do not need to manually activate the virtual environment.

The single file starter project can be downloaded [here][starter-single-file].

## Multiple files: packaging

Single files are convenient for simple pipelines.
Most pipelines are more complex, and therefore it's better to divide your project into multiple files.
This allows you to maintain, test, document, and (re)use parts individually.
For instance, we recommend defining your IOs in a [catalog][catalogs], separately from the nodes.

In Python, a collection of files is called a _package_.
A packaged project may look as follows:

```text
project
├── README.md
├── pyproject.toml
└── src
    └── package
        ├── __init__.py
        ├── __main__.py
        ├── catalog.py
        └── pipeline.py
```

As before, we have the `README.md` and `pyproject.toml`.
In addition:

- the pipeline has been moved to the `pipeline` module
- we've added a [catalog][catalogs]
- `__main__.py` will be used to run the project

!!! note "src-layout vs flat-layout"

    There are two common setups for multi-file projects: the src-layout and the flat layout.
    The example above uses a src-layout.
    There are pro's and cons to both options.
    See [this discussion][src-vs-flat] for more details.
    We will use a src-layout in the remainder of this guide.

Click on the tabs below to see how the example pipeline looks in the package layout:

=== "src/package/\_\_main\_\_.py"

    ```python
    import pipeline
    from ordeq import run

    if __name__ == "__main__":
        run(pipeline)
    ```

=== "src/package/catalog.py"

    ```python
    from pathlib import Path

    from ordeq_requests import ResponseJSON
    from ordeq_yaml import YAML

    user = ResponseJSON(url="https://jsonplaceholder.typicode.com/users/1")
    yaml = YAML(path=Path("users.yml"))
    ```

=== "src/package/pipeline.py"

    ```python
    import catalog
    from ordeq import node


    @node(inputs=catalog.user, outputs=catalog.yaml)
    def parse_users(user: dict) -> dict:
        return {
            "id": user["id"],
            "address": f"{user['address']['street']} {user['address']['zipcode']}",
        }
    ```

=== "src/package/\_\_init\_\_.py"

    ```python
    # This file can be empty: it's only needed to allow imports of this package
    ```

The package can be downloaded [here][starter-package].

#### Sub-pipelines

As your project grows, it's a good idea to modularize even further.
A common way to do this is to break up the pipeline into sub-pipelines.
Each sub-pipeline is represented by its own module or package.

Suppose you are working on a machine learning pipeline that consists of pre-processing, actual processing, and post-processing.
Your project structure may look as follows:

```text
project
├── README.md
├── pyproject.toml
└── src
    └── package
        ├── __init__.py
        ├── __main__.py
        ├── catalog.py
        └── ml
            ├── __init__.py
            ├── inference.py
            ├── postprocessing.py
            └── preprocessing.py
```

The `ml` package contains all nodes of the pipeline, but the nodes are now distributed across modules.
This makes your project easier to maintain.
Each module represents a sub-pipeline, which you can run and visualize individually.
More info can be found [here][run-and-viz].

For more complex projects, it makes sense to bring even more structure.
For instance, you might work on a project with _two_ pipelines: one which processes data for The Netherlands, and another for data for the UK.
Suppose these pipelines share the same source data, but require different transformations.

This project can be structured with one package for `nl` and one for `usa`:

```text
project
├── README.md
├── pyproject.toml
└── src
    └── package
        ├── __init__.py
        ├── __main__.py
        ├── catalog.py
        ├── nl
        │   ├── __init__.py
        │   ├── inference.py
        │   ├── postprocessing.py
        │   └── preprocessing.py
        └── usa
            ├── __init__.py
            ├── inference.py
            ├── postprocessing.py
            └── preprocessing.py
```

You can download the example package above [here][starter-subpipelines].

!!! note "Catalogs and multi-package projects"

    One reason to use catalogs is to ease reuse of IOs across your project.
    If the IOs are shared by multiple packages, it makes sense to create one `catalog.py` under `src` directly.
    You can also create a catalog in the packages themselves, but this has the downside that it's less easy to import.

#### Nested pipelines

You can also nest packages to reflect nested sub-pipelines:

```text
project/
├── README.md
├── pyproject.toml
└── src
    └── package
        ├── __init__.py
        ├── __main__.py
        ├── catalog.py
        └── nl                          # pipeline (package)
            ├── __init__.py
            ├── inference.py            # sub-pipeline (module)
            ├── postprocessing.py       # sub-pipeline (module)
            └── preprocessing           # sub-pipeline (package)
                ├── __init__.py
                ├── cleaning.py         # sub-sub-pipeline (module)
                └── standardization.py  # sub-sub-pipeline (module)
```

The complete example can be downloaded [here][starter-nested-subpipelines].

!!! warning "Pipelines in the same source folder should have shared dependencies"

    Pipelines that reside in the same source folder should have shared dependencies, like the catalog and libraries.
    If the dependencies do not overlap, it makes more sense to create a separate project.
    Projects with different dependencies can still share the same codebase.
    More info [here][uv-monorepo].

## Best practices

Here are some tips to get you started:

- Start simple, with a single file, or a package with just a catalog and a pipeline
- Incrementally add nodes to the pipeline
- Identify the (sub-)pipelines in your project, and create a module or package for each

If you're unsure how to set up your project with Ordeq, feel free to create an [issue on GitHub][issues].

## Developing libraries

The examples above concern executable projects that can run one or more pipelines.
A type of project that we have not covered yet is a library.
Library projects are typically not directly executed, but are meant to be installed and reused in another project.

Consider, for example:

- a machine learning framework that runs an Ordeq pipeline under the hood
- a catalog library, containing IOs for reuse across different projects and codebases
- an extension of Ordeq, like `ordeq-pandas` or `ordeq-viz`

!!! question "Interested in extending Ordeq?"

    If you would like to extend Ordeq, have a look at the [contribution guide][contribution-guide].

Suppose you want to create a library that uses Ordeq.
To initialize your library project, run:

```bash
uv init --lib
```

The layout of the created project is similar to the package layout, but:

- the project does not contain a `__main__.py` entrypoint
- the `pyproject.toml` contains dependencies needed to build and distribute your library

[catalogs]: ../getting-started/concepts/catalogs.md
[contribution-guide]: ../CONTRIBUTING.md
[core-concepts]: ../getting-started/concepts/io.md
[issues]: https://github.com/ing-bank/ordeq/issues
[run-and-viz]: ./run_and_viz.md
[src-vs-flat]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[starter-nested-subpipelines]: https://github.com/ing-bank/ordeq/tree/main/examples/starter_nested_subpipelines
[starter-package]: https://github.com/ing-bank/ordeq/tree/main/examples/starter_package
[starter-single-file]: https://github.com/ing-bank/ordeq/tree/main/examples/starter_single_file
[starter-subpipelines]: https://github.com/ing-bank/ordeq/tree/main/examples/starter_subpipelines
[uv]: https://docs.astral.sh/uv/
[uv-monorepo]: https://docs.astral.sh/uv/concepts/projects/workspaces/
[uv-scripts]: https://docs.astral.sh/uv/guides/scripts/
