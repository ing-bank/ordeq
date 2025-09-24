# Welcome to Ordeq!

Ordeq is a framework for developing data pipelines.
It simplifies IO and modularizes pipeline logic.
Ordeq elevates your proof-of-concept to a production-grade pipelines.
See the [introduction][intro] for an easy-to-follow example of how Ordeq can help.

## Installation

Ordeq is available under MIT license.
Please refer to the [license][license] and [notice][notice] for more details.

To install Ordeq, run:

```shell
uv pip install ordeq
```

### Extensions

Ordeq integrates seamlessly with existing tooling.
It provides integrations with many popular libraries out of the box.
You can install them as needed.
For example, for reading and writing data with Pandas, install the `ordeq-pandas` package:

```shell
uv pip install ordeq-pandas
```

The following table lists all available packages:

| Package                                                                                                                                              | Description                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <img src="https://raw.githubusercontent.com/pandas-dev/pandas/main/web/pandas/static/img/pandas_mark.svg" alt="drawing" height="50"/> `ordeq-pandas` | IOs for reading and writing data with Pandas                    |
| ![spark](https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg) `ordeq-spark`                                                    | IOs for reading and writing data with PySpark                   |
| ![numpy](https://numpy.org/images/logo.svg) `ordeq-numpy`                                                                                            | IOs for reading and writing data with NumPy                     |
| ![polars](https://www.pola.rs/assets/img/logo.svg) `ordeq-polars`                                                                                    | IOs for reading and writing data with Polars                    |
| ![ibis](https://ibis-project.org/_static/ibis-logo.svg) `ordeq-ibis`                                                                                 | IOs for reading and writing data with Ibis (SQL-like analytics) |
| ![matplotlib](https://matplotlib.org/_static/images/logo2.svg) `ordeq-matplotlib`                                                                    | IOs for visualizing data with Matplotlib                        |
| ![faiss](https://raw.githubusercontent.com/facebookresearch/faiss/main/resources/faiss_logo.png) `ordeq-faiss`                                       | IOs for reading and writing data with Faiss (vector search)     |
| ![joblib](https://joblib.readthedocs.io/en/latest/_static/joblib-logo-light.svg) `ordeq-joblib`                                                      | IOs for reading and writing data with Joblib (serialization)    |
| ![huggingface](https://huggingface.co/front/assets/huggingface_logo.svg) `ordeq-huggingface`                                                         | IOs for HuggingFace models                                      |
| ![pymupdf](https://pymupdf.readthedocs.io/en/latest/_static/logo.png) `ordeq-pymupdf`                                                                | IOs for reading and writing PDF files with PyMuPDF              |
| ![sentence-transformers](https://www.sbert.net/_static/logo.png) `ordeq-sentence-transformers`                                                       | IOs for reading and writing data with SentenceTransformers      |
| ![boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/_static/boto3.png) `ordeq-boto3`                                                    | IOs for reading and writing data with AWS boto3                 |
| ![requests](https://requests.readthedocs.io/en/latest/_static/requests-logo.png) `ordeq-requests`                                                    | IOs for reading and writing data via HTTP requests              |
| `ordeq`                                                                                                                                              | Core framework for Ordeq data pipelines                         |
| `ordeq-args`                                                                                                                                         | Utilities for parsing and handling command-line arguments       |
| `ordeq-cli-runner`                                                                                                                                   | Command-line interface for running Ordeq pipelines              |
| `ordeq-common`                                                                                                                                       | Common utilities and shared logic for Ordeq packages            |
| `ordeq-files`                                                                                                                                        | IOs for reading and writing files (CSV, JSON, Parquet, ...)     |
| `ordeq-project`                                                                                                                                      | Project scaffolding and management for Ordeq pipelines          |
| `ordeq-pydantic`                                                                                                                                     | IOs for reading and writing data with Pydantic models           |
| `ordeq-viz`                                                                                                                                          | Visualization of Ordeq pipelines                                |
| `ordeq-viz-cli`                                                                                                                                      | Command-line interface for pipeline visualization               |

Have a look at the [API reference][api-ref] for the documentation of each package.

## Why consider Ordeq?

- Ordeq is **the GenAI companion**: it gives your project structure and consistency, such that GenAI can thrive
- It offers **seamless integrations** with existing data & ML tooling, such as Spark, Pandas, Pydantic and PyMuPDF, and
  adding new integrations is trivial
- It's **actively developed** and **trusted** by data scientists, engineers, analysts and machine learning engineers at
  ING

## Learning Ordeq

To learn more about Ordeq, check out the following resources:

- See how Ordeq can help your project in the [introduction][intro]
- Check out the [core concepts][core-concepts] to learn how to use Ordeq
- Explore the [example project][example-project] to see how Ordeq is used

[core-concepts]: docs/getting-started/concepts/io.md

[api-ref]: docs/api/ordeq/types.md

[intro]: docs/getting-started/introduction.md

[example-project]: docs/guides/examples/example-project/README.md

[license]: ./LICENSE

[notice]: ./NOTICE
