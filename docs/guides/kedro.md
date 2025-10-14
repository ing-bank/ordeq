# Coming from Kedro

This guide is for users familiar with Kedro who want to get started with Ordeq.
Because the frameworks are conceptually close, it's easy to transition and leverage your existing knowledge.
If you are new to Ordeq, start with the [introduction][intro].

Ordeq and Kedro share several core abstractions:

- [Nodes] for modular data pipelines
- [Catalogs] for defining and managing [IO]

Ordeq offers several advantages over Kedro:

- Lighter weight and Python-first (no YAML required)
- Adding new IOs requires a fraction of the code
- Suitable for heavy data engineering and resource configuration
- Custom IOs are first-class citizens

In this guide, we will compare a starter Kedro project with its Ordeq equivalent.
You may use this as a reference when transitioning from Kedro to Ordeq.

## Spaceflight starter project

We will use the [spaceflights-pandas starter project][kedro-starter] as an example.
Below is the directory structure of the Kedro project, and the Ordeq equivalent.

!!! tip "How to try it out yourself"

    If you would like to follow this guide step-by-step:

    - clone the [spaceflights-pandas starter project][kedro-starter]
    - create another, empty project, with the Ordeq layout described below

    You can also download the completed Ordeq project [here][completed-repo].

=== "Kedro"

    ```text
    conf/
    └── base
        └── catalog.yml
    src/
    ├── pipeline_registry.py
    ├── settings.py
    ├── __main__.py
    └── spaceflights
        ├── __init__.py
        ├── pipeline.py
        ├── catalog.py
        └── nodes.py

    ```

=== "Ordeq"

    ```text
    src/
    ├── __main__.py
    ├── catalog.py
    └── spaceflights
        ├── __init__.py
        └── pipeline.py

    ```

## Migrating the catalog

Ordeq defines a catalog in code, while Kedro's catalog is YAML-based.
In Kedro, catalogs entries are called _datasets_, while Ordeq uses _IO_.
This section will show how to migrate each dataset in the Kedro catalog to an IO in Ordeq catalog.

!!! info "Ordeq also supports layered catalogs"

    For simplicity, we assume the Kedro catalog consists of only one YAML file.
    Ordeq supports multiple, layered, catalogs too.
    For more information, see [catalogs].

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

Switch the tabs above to see the Kedro catalog and its Ordeq equivalent.
For each dataset in the Kedro catalog, we have defined an equivalent Ordeq IO:

- `companies` is a `pandas.CSVDataset`, so we use the `ordeq_pandas.PandasCSV` IO
- `shuttles` is a `pandas.ExcelDataset`, so we use the `ordeq_pandas.PandasExcel` IO
    - The `load_args` in Kedro are translated to `with_load_options` in Ordeq
- `preprocessed_companies` and `preprocessed_shuttles` are `pandas.ParquetDataset`, so we use the
    `ordeq_pandas.PandasParquet` IO

!!! tip "User IOs"

    Ordeq provides many IOs for popular data processing libraries out-of-the-box, such as `PandasCSV` and `PandasParquet`.
    You can use or extend these IOs directly.
    Creating your own IOs is a first-class feature of Ordeq, designed to be simple and flexible.
    You are always in control of how data is loaded and saved.
    For more information, see the [guide on creating user IOs][custom-ios].

## Migrating the nodes and pipeline

Next we are going to migrate the nodes and the pipeline.
First, let's cover a couple of differences between Kedro and Ordeq pipelines:

- Each Kedro pipeline needs to be defined in a `pipeline.py` file
- Kedro pipelines are created using a `create_pipeline` function
- Kedro uses a string to reference the data

In contrast:

- Ordeq pipelines can be defined anywhere
- Ordeq pipelines are Python files (or, modules)
- Ordeq uses the actual IO object to reference the data

Below is the nodes and pipeline definition for the Kedro spaceflights project:

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
        ])
    ```

=== "src/spaceflights/nodes.py (Kedro)"

    ```python
    import pandas as pd

    # ... utility methods omitted for brevity


    def preprocess_companies(companies: pd.DataFrame) -> pd.DataFrame:
        companies["iata_approved"] = _is_true(companies["iata_approved"])
        companies["company_rating"] = _parse_percentage(
            companies["company_rating"]
        )
        return companies


    def preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame:
        shuttles["d_check_complete"] = _is_true(shuttles["d_check_complete"])
        shuttles["moon_clearance_complete"] = _is_true(
            shuttles["moon_clearance_complete"]
        )
        shuttles["price"] = _parse_money(shuttles["price"])
        return shuttles
    ```

In Kedro, the name of the pipeline is implicitly assigned based on the folder name.
In this case, the pipeline is called `spaceflights`.
The datasets are bound to the nodes in the pipeline definition, using strings.

Next, let's have a look at the Ordeq equivalent:

=== "src/spaceflights/pipeline.py (Ordeq)"

    ```python
    import catalog
    import pandas as pd
    from ordeq import node

    # ... utility methods omitted for brevity


    @node(inputs=catalog.companies, outputs=catalog.preprocessed_companies)
    def preprocess_companies(companies: pd.DataFrame) -> pd.DataFrame:
        companies["iata_approved"] = _is_true(companies["iata_approved"])
        companies["company_rating"] = _parse_percentage(
            companies["company_rating"]
        )
        return companies


    @node(inputs=catalog.shuttles, outputs=catalog.preprocessed_shuttles)
    def preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame:
        shuttles["d_check_complete"] = _is_true(shuttles["d_check_complete"])
        shuttles["moon_clearance_complete"] = _is_true(
            shuttles["moon_clearance_complete"]
        )
        shuttles["price"] = _parse_money(shuttles["price"])
        return shuttles
    ```

In Ordeq, the pipeline is defined by the module itself, so there is no need for an additional file.
The IOs are bound to the nodes in the node definition, using the actual IO objects instead of strings.
Note that the node functions themselves are identical in both frameworks.

## Migrating the runner

Running a Kedro project is done through the Kedro CLI.
Ordeq projects can be run both programmatically, or using a CLI.
We will first show how to set up a CLI entry point similar to Kedro's.
Here's the `src/__main__.py` file for both Kedro and Ordeq:

=== "src/\_\_main\_\_.py (Kedro)"

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

=== "src/\_\_main\_\_.py (Ordeq CLI)"

    ```python
    from ordeq_cli_runner import main

    if __name__ == "__main__":
        main()
    ```

!!! info "Install the `ordeq-cli-runner` package"

    To run your Ordeq project through the CLI, make sure to install the `ordeq-cli-runner` package.

To run the Ordeq project through the CLI, you can now run:

```bash
python src/__main__.py run spaceflights.pipeline
```

Alternatively, you can run the pipeline programmatically, as follows:

```python title="src/__main__.py (Ordeq programmatic)"
from ordeq import run
from spaceflights import pipeline

run(pipeline)
```

More info about running Ordeq projects can be found in the [guide][run-and-viz].

## Other components

Kedro projects also have a settings file and a pipeline registry.
Ordeq does not have these concepts, so there is no need to migrate them:

- Ordeq pipelines are referred to by the name of the module, so there is no need for a registry
- The settings file typically contains settings specific to the YAML-based catalog, which is not used by Ordeq

!!! tip "Need help?"

    You might use Kedro's more advanced features, such as parameters or hooks.
    Ordeq supports these features too, although the implementation might differ.
    If you have any questions or run into any issues, please open an issue on [GitHub][issues].

[catalogs]: ../getting-started/concepts/catalogs.md
[completed-repo]: ./kedro-starter-to-ordeq.zip
[custom-ios]: ./custom_io.md
[intro]: ../getting-started/introduction.md
[io]: ../getting-started/concepts/io.md
[issues]: https://github.com/ing-bank/ordeq/issues
[kedro-starter]: https://github.com/kedro-org/kedro-starters/tree/main/spaceflights-pandas
[nodes]: ../getting-started/concepts/nodes.md
[run-and-viz]: ./run_and_viz.md
