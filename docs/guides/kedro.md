# Coming from Kedro

This guide is for users familiar with Kedro who want to get started with Ordeq.
Because the frameworks are conceptually close, it's easy to transition and leverage your existing knowledge.
If you are new to Kedro, start with the Ordeq [introduction][intro].

## Conceptual similarities

Ordeq and Kedro share several core abstractions:

- Nodes for modular data pipelines
- Catalogs for defining and managing IO

## Advantages of Ordeq

Ordeq offers several advantages over Kedro:

- Lighter weight and Python-first (no YAML required)
- Integrates easily with Airflow and other Python tools
- Adding new IOs requires a fraction of the code
- Suitable for heavy data engineering and resource management
- User IOs are first-class citizens; built-in IOs are 'Reference IOs' you can extend

## Example project

Below is the directory structure of the Kedro starter project and the Ordeq equivalent.

=== "Kedro"

    ```text
    conf/
    └── base
        └── catalog.yml
    src/
    └── spaceflights_pandas
        ├── pipelines
        │   └── data_processing
        │       ├── __init__.py
        │       ├── nodes.py
        │       └── pipeline.py
        ├── pipeline_registry.py
        ├── settings.py
        └── __main__.py
    ```

=== "Ordeq"

    ```text
    src/
    ├── nodes.py
    ├── pipeline.py
    ├── catalog.py
    └── __main__.py
    ```

!!! tip

    If you would like to follow this tutorial step-by-step:

    - clone the [spaceflights-pandas starter project][kedro-starter]
    - create another, empty project, with the Ordeq layout described above

    You can also download the completed Ordeq project [here][completed-repo].

## Migrating the catalog

Ordeq defines a catalog in code, while Kedro's catalog is YAML-based.
In Kedro, catalogs entries are called _datasets_, while Ordeq uses _IO_.
This section will show how to migrate each dataset in the Kedro catalog to an IO in Ordeq catalog.

!!! info

    For simplicity, we assume the Kedro catalog consists of only one YAML file.
    The guide applies to multiple, layered, catalogs too.
    For more information, see [catalogs].

Switch the tabs to see the Kedro catalog and its Ordeq equivalent:

=== "conf/base/catalog.yml (Kedro)"

    ```yaml
    companies:
        type: pandas.CSVDataset
        filepath: data/01_raw/companies.csv

    shuttles:
        type: pandas.ExcelDataset
        filepath: data/01_raw/shuttles.xlsx
        load_args:
            engine: openpyxl

    preprocessed_companies:
        type: pandas.ParquetDataset
        filepath: data/02_intermediate/preprocessed_companies.parquet

    preprocessed_shuttles:
        type: pandas.ParquetDataset
        filepath: data/02_intermediate/preprocessed_shuttles.parquet
    ```

=== "src/catalog.py (Ordeq)"

    ```python
    from pathlib import Path

    from ordeq_pandas import PandasCSV, PandasExcel, PandasParquet

    companies = PandasCSV(path=Path("data/01_raw/companies.csv"))

    shuttles = PandasExcel(
        path=Path("data/01_raw/shuttles.xlsx")
    ).with_load_options(engine="openpyxl")

    preprocessed_companies = PandasParquet(
        path=Path("data/02_intermediate/preprocessed_companies.parquet")
    )

    preprocessed_shuttles = PandasParquet(
        path=Path("data/02_intermediate/preprocessed_shuttles.parquet")
    )
    ```

For each dataset in the Kedro catalog, we have defined an equivalent Ordeq IO.

- `companies` is a `pandas.CSVDataset` dataset,, so we use the `ordeq_pandas.PandasCSV` IO.
- `shuttles` is a `pandas.ExcelDataset` dataset, so we use the `ordeq_pandas.PandasExcel` IO.
    - The `load_args` in Kedro are translated to `with_load_options` in Ordeq.
- `preprocessed_companies` and `preprocessed_shuttles` are `pandas.ParquetDataset` datasets, so we use the `ordeq_pandas.PandasParquet` IO.

!!! warning "Install the ordeq-pandas package"

    Make sure you have the `ordeq-pandas` package installed to use the Pandas IOs.

## Parameters and node parametrization

Kedro projects often use a `parameters.yml` file to provide runtime parameters to nodes. Ordeq supports node parametrization natively in Python, making it easy to pass parameters directly or via configuration files.

=== "conf/base/parameters.yml (Kedro)"

    ```yaml
    max_shuttles: 10
    company_filter: "SpaceX"
    ```

=== "src/parameters.py (Ordeq)"

    ```python
    max_shuttles = 10
    company_filter = "SpaceX"
    ```

See the [node parametrization guide][node-parameters] for more details on how to use parameters in Ordeq pipelines.

### User IOs and Reference IOs

The IOs provided out-of-the-box by Ordeq (such as PandasCSV, PandasParquet) are "Reference IOs"—examples you can use directly or extend. Creating your own IOs ("User IOs") is a first-class feature in Ordeq, designed to be simple and flexible. You are always in control of how data is loaded and saved.

For more information, see the [guide on creating user IOs][custom-ios].

## Migrating the pipeline

Next we are going to migrate the pipeline.
First, let's cover a couple of differences between Kedro and Ordeq pipelines:

- The Kedro pipeline is defined in a `spaceflights/pipeline.py` file, while Ordeq pipelines can be defined anywhere.
- Kedro pipelines are defined in a `create_pipeline` function, while Ordeq pipelines are defined as plain sets.
- Kedro uses a string to reference the IO, whereas Ordeq uses the actual IO object.

=== "src/spaceflights/pipeline.py (Kedro)"

    ```python
    from kedro.pipeline import Pipeline, node, pipeline
    from nodes import preprocess_companies, preprocess_shuttles


    def create_pipeline(**kwargs) -> Pipeline:
        return pipeline([
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            ...,
        ])
    ```

=== "src/pipeline.py (Ordeq)"

    ```python
    from catalog import (
        companies,
        preprocessed_companies,
        preprocessed_shuttles,
        shuttles,
    )
    from nodes import preprocess_companies, preprocess_shuttles
    from ordeq import node

    spaceflights = {
        node(
            preprocess_companies, inputs=companies, outputs=preprocessed_companies
        ),
        node(preprocess_shuttles, inputs=shuttles, outputs=preprocessed_shuttles),
    }
    ```

=== "src/pipeline.py (Ordeq, Pythonic style)"

    ```python
    from catalog import (
        companies,
        preprocessed_companies,
        preprocessed_shuttles,
        shuttles,
    )
    from nodes import preprocess_companies, preprocess_shuttles
    from ordeq import node

    spaceflights = set()
    spaceflights.add(
        node(
            preprocess_companies, inputs=companies, outputs=preprocessed_companies
        )
    )
    spaceflights.add(
        node(preprocess_shuttles, inputs=shuttles, outputs=preprocessed_shuttles)
    )
    # You can also use a list or any Python collection
    ```

Note that name of the pipeline object in the Ordeq project is `spaceflights`.
In Kedro, the name of the pipeline was implicitly assigned based on the folder name.

## Migrating `__main__.py`

Running a Kedro project is done through the `kedro` CLI.
Ordeq provides two ways to run a project: through the CLI runner, or programmatically.
This section will show how to migrate the `__main__.py` file to use the CLI runner.

!!! warning "Install the ordeq-cli-runner package"

    To run your Ordeq project through the CLI, make sure to install the `ordeq-cli-runner` package.

=== "src/__main__.py (Kedro)"

    ```python
    import sys
    from pathlib import Path
    from typing import Any

    from kedro.framework.cli.utils import find_run_command
    from kedro.framework.project import configure_project


    def main(*args, **kwargs) -> Any:
        package_name = Path(__file__).parent.name
        configure_project(package_name)

        interactive = hasattr(sys, "ps1")
        kwargs["standalone_mode"] = not interactive

        run = find_run_command(package_name)
        return run(*args, **kwargs)


    if __name__ == "__main__":
        main()
    ```

=== "src/__main__.py (Ordeq)"

    ```python
    from ordeq_cli_runner import main

    if __name__ == "__main__":
        main()
    ```

To run your Ordeq project through the CLI, you can now run:

```bash
python -m src run --pipeline pipeline:spaceflights
```

!!! tip

    You can easily manage dependencies by creating a minimal `pyproject.toml` in your project and installing packages with [uv](https://github.com/astral-sh/uv):

    ```bash
    uv add ordeq-pandas ordeq-cli-runner
    ```

    This ensures your environment is reproducible and ready to run Ordeq pipelines.

!!! warning "Activate the virtual environment"

    To run the command above, make sure to activate the virtual environment where you installed Ordeq and its dependencies.
    Alternatively, use `uv` to run the command in an isolated environment.

## Conclusion

That's it!
Because Ordeq builds on the design choices of Kedro, migrating a Kedro project to Ordeq is straightforward.
Let's wrap up with a couple of notes.

### Nodes

You might have noticed that there is no need to migrate the nodes.
Because they are just plain Python functions, they can be reused as-is.
The IOs are bound to the nodes in the pipeline definition, just like in Kedro.
You can also bind the IO to the nodes using decorators, as shown in the [introduction][intro].

### Settings and pipeline registry

Kedro projects have a settings file and a pipeline registry.
Ordeq does not have these concepts, so there is no need to migrate them:

- Ordeq pipelines are referred to by their variable names, so there is no need for a registry.
- The settings file typically contains settings specific to the YAML-based catalog, which is not used by Ordeq.

### More complex projects

Real-world Kedro projects can be more complex than the example shown here.
You might use Kedro's more advanced features, such as parameters or hooks.
Ordeq supports these features too, although the implementation might differ.
If you have any questions or run into any issues, please open an issue on [GitHub][issues].

For more information about catalogs and their power in Ordeq, see the [Catalogs documentation][catalogs].

[catalogs]: ../getting-started/concepts/catalogs.md
[completed-repo]: ./kedro-starter-to-ordeq.zip
[custom-ios]: ./custom_io.md
[intro]: ../getting-started/introduction.md
[issues]: https://github.com/ing-bank/ordeq/issues
[kedro-starter]: https://github.com/kedro-org/kedro-starters/tree/main/spaceflights-pandas
[node-parameters]: ./node_parameters.md
