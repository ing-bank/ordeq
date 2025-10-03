# Welcome to Ordeq!

[![Release](https://github.com/ing-bank/ordeq/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/ing-bank/ordeq/actions/workflows/release.yml)
[![Docs](https://github.com/ing-bank/ordeq/actions/workflows/docs.yml/badge.svg)](https://github.com/ing-bank/ordeq/actions/workflows/docs.yml)
![PyPI](https://img.shields.io/pypi/v/ordeq?label=ordeq)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ordeq?label=downloads)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ordeq is a framework for developing data pipelines.
It simplifies IO and modularizes pipeline logic.
Ordeq elevates your proof-of-concept to a production-grade pipelines.
See the [introduction][intro] for an easy-to-follow example of how Ordeq can help.

## Installation

Ordeq is available under MIT license.
Please refer to the [license] and [notice] for more details.

To install Ordeq, run:

```shell
uv pip install ordeq
```

## Integrations

Ordeq integrates seamlessly with existing tooling.
It provides many integrations out of the box.
You can install them as needed.
For example, for reading and writing data with Pandas, install the `ordeq-pandas` package:

```shell
uv pip install ordeq-pandas
```

Some of the available integrations are listed below.

#### Data processing

<table>
  <tr>
    <td width="80" height="60" align="center"><img src="https://raw.githubusercontent.com/pandas-dev/pandas/main/web/pandas/static/img/pandas_mark.svg" alt="Pandas" height="40"/>Pandas</td>
    <td width="80" height="60" align="center"><img src="https://icon.icepanel.io/Technology/svg/Apache-Spark.svg" alt="Spark" height="40"/>Spark</td>
    <td width="80" height="60" align="center"><img src="https://numpy.org/images/logo.svg" alt="NumPy" height="40"/>Numpy</td>
    <td width="80" height="60" align="center"><img src="https://avatars.githubusercontent.com/u/83768144?s=200&v=4" alt="Polars" height="60"/>Polars</td>
    <td width="80" height="60" align="center"><img src="https://ibis-project.org/logo.svg" alt="Ibis" height="50"/>Ibis</td>
    <td width="80" height="60" align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Matplotlib" height="40"/>Matplotlib</td>
    <td width="80" height="60" align="center"><img src="https://joblib.readthedocs.io/en/stable/_static/joblib_logo.svg" alt="Joblib" height="40"/>Joblib</td>
  </tr>
  <tr>
<td width="80" height="60" align="center"><img src="https://huggingface.co/front/assets/huggingface_logo.svg" alt="HuggingFace" height="40"/>HuggingFace</td>
    <td width="80" height="60" align="center"><img src="https://pymupdf.readthedocs.io/en/latest/_static/sidebar-logo-light.svg" alt="PyMuPDF" height="40"/>PyMuPDF</td>
    <td width="80" height="60" align="center"><img src="https://www.sbert.net/_static/logo.png" alt="SentenceTransformers" height="40"/>st</td>
    <td width="80" height="60" align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" alt="Requests" height="50"/>Requests</td>
    <td width="80" height="60" align="center"><img src="https://avatars.githubusercontent.com/u/110818415?v=4" alt="Pydantic" height="40"/>Pydantic</td>
    <td width="80" height="60" align="center"><img src="https://raw.githubusercontent.com/apache/parquet-format/25f05e73d8cd7f5c83532ce51cb4f4de8ba5f2a2/logo/parquet-logos_1.svg" alt="Parquet" height="50"/>Parquet</td>
    <td width="80" height="60" align="center">
        <img src="https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/duckdb-umoj5fxu8w5pzg7d0js9.png/duckdb-kz05ottxukbgvmp8c3bpi.png?_a=DATAg1AAZAA0" alt="DuckDB" height="40"/><br/>DuckDB
    </td>
  </tr>
  <tr>
    <td width="80" height="60" align="center">
      <img src="https://avatars.githubusercontent.com/u/22396732?s=200&v=4" alt="Altair" height="40"/><br/>Altair
    </td>
    <td width="80" height="60" align="center">
        <img src="https://avatars.githubusercontent.com/u/388785?s=200&v=4" alt="Networkx" height="40"/><br/>NetworkX
    </td>
    <td width="80" height="60" align="center">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/TOML_Logo.svg" alt="TOML" height="40"/><br/>TOML
    </td>
  </tr>
</table>

#### Cloud storage

<table>
    <tr>
        <td height="60"><img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/Amazon-S3-Logo.svg" alt="Azure" height="40"/>Amazon S3</td>
        <td height="60"><img src="https://funnel.io/hubfs/Google_Storage-Logo-1.png" alt="Azure" height="40"/>Google Cloud Storage</td>
        <td height="60"><img src="https://logos-world.net/wp-content/uploads/2021/02/Microsoft-Azure-Emblem.png" alt="Azure" height="40"/>Azure Blob Storage</td>
    </tr>
</table>

Have a look at the [API reference][api-ref] for a list of available packages.

## Documentation

Documentation is available at https://ing-bank.github.io/ordeq/.

## Why consider Ordeq?

- Ordeq is **the GenAI companion**: it gives your project structure and consistency, such that GenAI can thrive
- It offers **seamless integrations** with existing data & ML tooling, such as Spark, Pandas, Pydantic and PyMuPDF, and
    adding new integrations is trivial
- It's **actively developed** and **trusted** by data scientists, engineers, analysts and machine learning engineers at ING

## Learning Ordeq

To learn more about Ordeq, check out the following resources:

- See how Ordeq can help your project in the [introduction][intro]
- Check out the [core concepts][core-concepts] to learn how to use Ordeq
- Explore the [example project][example-project] to see how Ordeq is used

## Acknowledgements

Ordeq builds upon design choices and ideas from [Kedro] and other frameworks.
It has been developed at ING, with contributions from various individuals.
Please refer to the [acknowledgements] section in the documentation for more details.

[acknowledgements]: https://ing-bank.github.io/ordeq/contributing/acknowledgements/
[api-ref]: https://ing-bank.github.io/ordeq/api/ordeq/framework/io/
[core-concepts]: https://ing-bank.github.io/ordeq/getting-started/concepts/io/
[example-project]: docs/guides/examples/example-project/README.md
[intro]: https://ing-bank.github.io/ordeq/getting-started/introduction/
[kedro]: https://github.com/kedro-org/kedro
[license]: https://github.com/ing-bank/ordeq/blob/main/LICENSE
[notice]: https://github.com/ing-bank/ordeq/blob/main/NOTICE
