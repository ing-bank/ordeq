# Migrating from Kedro

This guide shows how to migrate a Kedro project to Ordeq.
It is intended for users familiar with Kedro and interested in adopting Ordeq.
Users that are not familiar with Kedro, should start from the Ordeq [introduction][intro].

## Example project
The guide will show how to migrate Kedro's [spaceflights-pandas starter project][kedro-starter] to Ordeq.
Below is the directory structure of the Kedro starter project, and the Ordeq equivalent.
Switch the tabs to see the differences:

=== "Kedro"

    ```text
    conf/
    |-- base/
    |-- |-- catalog.yml
    src/
    |-- spaceflights_pandas/
    |-- |-- pipelines/
    |-- |-- |-- data_processing/
    |-- |-- |-- |-- __init__.py
    |-- |-- |-- |-- nodes.py
    |-- |-- |-- |-- pipeline.py
    |-- |-- |-- ...
    |-- |-- pipeline_registry.py
    |-- |-- settings.py
    |-- __main__.py
    ```

=== "Ordeq"

    ```text
    src/
    |-- nodes.py
    |-- pipeline.py
    |-- catalog.py
    |-- __main__.py
    ```

!!!tip
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

    from ordeq_pandas import PandasCSV, PandasParquet, PandasExcel

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
- `shuttles` `pandas.ExcelDataset` dataset, so we use the `ordeq_pandas.PandasExcel` IO.
    - The `load_args` in Kedro are translated to `with_load_options` in Ordeq.
- `preprocessed_companies` and `preprocessed_shuttles` are `pandas.ParquetDataset` datasets, so we use the `ordeq_pandas.PandasParquet` IO.

!!!warning "Install the ordeq-pandas package"
    Make sure you have the `ordeq-pandas` package installed to use the Pandas IOs.

### Custom datasets

The datasets in the example above are all supported by Ordeq.
If you have custom datasets in Kedro, you can create equivalent custom IOs in Ordeq.
The same applies if you have datasets that are not yet supported by Ordeq.
For more information, please refer to the [guide on creating custom IOs][custom-ios].

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
        return pipeline(
            [
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
            ]
        )
    ```

=== "src/pipeline.py (Ordeq)"

    ```python
    from ordeq import node

    from nodes import preprocess_companies, preprocess_shuttles
    from catalog import companies, preprocessed_companies, shuttles, preprocessed_shuttles

    spaceflights = {
        node(
            preprocess_companies,
            inputs=companies,
            outputs=preprocessed_companies,
        ),
        node(
            preprocess_shuttles,
            inputs=shuttles,
            outputs=preprocessed_shuttles,
        )
    }

    ```

Note that name of the pipeline object in the Ordeq project is `spaceflights`.
In Kedro, the name of the pipeline was implicitly assigned based on the folder name.

## Migrating `__main__.py`
Running a Kedro project is done through the `kedro` CLI.
Ordeq provides two ways to run a project: through the CLI runner, or programmatically.
This section will show how to migrate the `__main__.py` file to use the CLI runner.

!!!warning "Install the ordeq-cli-runner package"
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

        interactive = hasattr(sys, 'ps1')
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

To run Ordeq project through the CLI, you can now run:

```bash
python src/__main__.py run --pipeline pipeline:spaceflights
```

!!!warning "Activate the virtual environment"
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

[kedro-starter]: https://github.com/kedro-org/kedro-starters/tree/main/spaceflights-pandas

[catalogs]: ../../getting-started/concepts/catalogs.md

[custom-ios]: ../../guides/custom_io.md

[completed-repo]: ../kedro-starter-to-ordeq.zip

[intro]: ../../getting-started/introduction.md

[issues]: https://github.com/ing-bank/ordeq/issues
